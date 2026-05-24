"""Pasul 9: Sentiment per entitate × perioadă.

Folosește output NER (Pasul 8). Pentru top-N entități × perioadă cu suficiente
mențiuni, extrage paragrafele care le menționează și clasifică sentimentul lui
ND față de entitate cu Gemini 2.5 Flash (pozitiv / neutru / negativ / mixt).

Output: heatmap entitate × perioadă cu sentiment colorat + tabel detaliat.

Run:
    PROJECTION=overall python scripts/09_sentiment_per_entity.py
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import frontmatter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dotenv import load_dotenv

from corpus import _normalize_diacritics, strip_speaker_tags_to_nd

PROJECTION = os.getenv("PROJECTION", "overall")
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
SRC_NER = ROOT / "results" / f"08_ner_{PROJECTION}" / "entities_per_doc.jsonl"
SRC_CORPUS = ROOT / "data" / f"3_nd_{PROJECTION}"
OUT = ROOT / "results" / f"09_sentiment_per_entity_{PROJECTION}"
OUT.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "gemini-2.5-flash"
MIN_MENTIONS_PER_BUCKET = 3
TOP_N_ENTITIES = 25

SENTIMENT_PROMPT = """Ești un analist de discurs politic. Mai jos sunt extrase din discursurile lui Nicușor Dan (Președintele României) unde menționează entitatea **{entity}**.

Analizează DOAR atitudinea lui Nicușor Dan față de acea entitate, în aceste extrase. Ignoră atitudinea ta sau a altor surse.

ETICHETE:
- "pozitiv" — ND vorbește favorabil, apreciază, susține, colaborează
- "negativ" — ND critică, dezaprobă, se opune, atacă
- "neutru" — menționare neutrală, informațională, fără polaritate
- "mixt" — are atât elemente pozitive cât și negative
- "n/a" — extrasele nu permit evaluarea (entitate menționată tehnic, sub formă de hashtag, link, etc.)

EXTRASE (separate prin ===):
{passages}

OUTPUT — JSON object:
{{
  "sentiment": "pozitiv | negativ | neutru | mixt | n/a",
  "confidence": "high | medium | low",
  "rationale": "1-2 propoziții de justificare cu citat scurt din extrase",
  "key_phrases": ["citat scurt 1", "citat scurt 2"]
}}

Returnează DOAR JSON. Niciun preambul."""


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        print("ERROR: GEMINI_API_KEY missing", file=sys.stderr)
        sys.exit(1)
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=120_000))
    return client, types


def period_for(date_str: str) -> str:
    y, m = int(date_str[:4]), int(date_str[5:7])
    if y == 2024 or (y == 2025 and m <= 2):
        return "2024Q4-2025Q1 candidatură-precampanie"
    if y == 2025 and m <= 5:
        return "2025Q2 campanie + investitură"
    if y == 2025 and m <= 8:
        return "2025Q3 deficit + reforma economică"
    if y == 2025 and m <= 11:
        return "2025Q4 stabilizare + diplomație"
    if y == 2025 and m == 12 or (y == 2026 and m <= 2):
        return "2025Q4-2026Q1 reformă judiciară"
    if y == 2026 and m <= 5:
        return "2026Q2 cotitură UE + criză guvern"
    return "outside-scope"


def extract_passages(doc_id: str, entity_raw_forms: list[str],
                       text: str, context_chars: int = 250) -> list[str]:
    """Find sentences/snippets mentioning the entity (any raw form) in text."""
    text_norm = _normalize_diacritics(text)
    found_spans: list[tuple[int, int, str]] = []
    for form in entity_raw_forms:
        form_norm = _normalize_diacritics(form)
        # Case-insensitive search
        for m in re.finditer(re.escape(form_norm), text_norm, re.IGNORECASE):
            start = max(0, m.start() - context_chars)
            end = min(len(text_norm), m.end() + context_chars)
            found_spans.append((start, end, text[start:end]))
    # Dedup overlapping spans
    if not found_spans:
        return []
    found_spans.sort(key=lambda x: (x[0], -x[1]))
    merged: list[tuple[int, int, str]] = []
    for s, e, snip in found_spans:
        if merged and s < merged[-1][1]:
            # Extend
            old_s, old_e, _ = merged[-1]
            new_e = max(old_e, e)
            merged[-1] = (old_s, new_e, text[old_s:new_e])
        else:
            merged.append((s, e, snip))
    return [snip.strip() for _, _, snip in merged]


def classify_one(entity: str, passages: list[str], client, types) -> dict:
    if not passages:
        return {"sentiment": "n/a", "confidence": "low", "rationale": "no passages", "key_phrases": []}
    # Cap total passage length
    total = "\n===\n".join(passages)[:8000]
    prompt = SENTIMENT_PROMPT.format(entity=entity, passages=total)
    try:
        resp = client.models.generate_content(
            model=MODEL_NAME, contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                response_mime_type="application/json",
            ),
        )
        return json.loads(resp.text.strip())
    except json.JSONDecodeError as e:
        return {"sentiment": "n/a", "confidence": "low",
                "rationale": f"json error: {e}", "key_phrases": []}
    except Exception as e:
        return {"sentiment": "n/a", "confidence": "low",
                "rationale": f"{type(e).__name__}: {str(e)[:80]}",
                "key_phrases": []}


def main():
    # Load NER per-doc
    docs_entities: list[dict] = []
    with SRC_NER.open() as f:
        for line in f:
            docs_entities.append(json.loads(line))
    print(f"Loaded NER for {len(docs_entities)} docs.")

    # Load doc texts
    id_to_text: dict[str, str] = {}
    for path in sorted(SRC_CORPUS.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        text = post.content.strip()
        if text:
            id_to_text[path.stem] = strip_speaker_tags_to_nd(text)

    # Build: (canonical, period) -> list of (doc_id, raw_forms, passages)
    entity_period_passages: dict[tuple[str, str], list[dict]] = defaultdict(list)
    total_mentions = defaultdict(int)
    for d in docs_entities:
        period = period_for(d["date"])
        text = id_to_text.get(d["id"], "")
        for ent in d.get("entities", []):
            canon = ent["canonical"]
            total_mentions[canon] += ent["count"]
            raw_forms = ent.get("raw_forms", [canon])
            passages = extract_passages(d["id"], raw_forms, text)
            if passages:
                entity_period_passages[(canon, period)].append({
                    "doc_id": d["id"], "passages": passages,
                })

    # Top entities by total mentions
    top_entities = sorted(total_mentions, key=lambda k: -total_mentions[k])[:TOP_N_ENTITIES]
    print(f"\nTop {len(top_entities)} entities:")
    for e in top_entities:
        print(f"  {total_mentions[e]:>5} — {e}")

    # Build tasks
    tasks = []
    for canon in top_entities:
        for period in sorted(set(p for _, p in entity_period_passages.keys())):
            docs = entity_period_passages.get((canon, period), [])
            all_passages = [p for d in docs for p in d["passages"]]
            if len(all_passages) >= MIN_MENTIONS_PER_BUCKET:
                tasks.append({"entity": canon, "period": period,
                              "n_passages": len(all_passages),
                              "passages": all_passages[:15],  # cap at 15 per bucket
                              "n_docs": len(docs)})

    print(f"\n{len(tasks)} (entity × period) buckets to classify.")

    # Classify with parallel workers
    client, types = get_client()
    t0 = time.time()
    results: list[dict] = []

    def process(task):
        r = classify_one(task["entity"], task["passages"], client, types)
        return {**task, **r}

    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(process, t): t for t in tasks}
        for i, fut in enumerate(as_completed(futs), 1):
            try:
                res = fut.result(timeout=120)
            except Exception as e:
                t = futs[fut]
                res = {**t, "sentiment": "n/a", "rationale": f"timeout: {e}"}
            results.append(res)
            elapsed = time.time() - t0
            print(f"[{i}/{len(tasks)}] {res['entity']:<20} {res['period'][:25]:<25} "
                  f"→ {res.get('sentiment','?'):<8} ({elapsed:.0f}s)")

    # Save full results
    with (OUT / "sentiment_per_entity_period.jsonl").open("w") as f:
        for r in results:
            # Slim down: drop bulky passages from saved version
            r_save = {k: v for k, v in r.items() if k != "passages"}
            f.write(json.dumps(r_save, ensure_ascii=False) + "\n")

    df = pd.DataFrame([{
        "entity": r["entity"], "period": r["period"],
        "n_passages": r["n_passages"], "n_docs": r["n_docs"],
        "sentiment": r.get("sentiment", "?"),
        "confidence": r.get("confidence", "?"),
        "rationale": r.get("rationale", "")[:300],
    } for r in results])
    df.to_csv(OUT / "sentiment_summary.csv", index=False)

    # Heatmap
    period_order = sorted(df["period"].unique())
    sentiment_to_val = {"pozitiv": 1.0, "neutru": 0.0, "negativ": -1.0,
                         "mixt": -0.3, "n/a": np.nan}
    df["sent_val"] = df["sentiment"].map(sentiment_to_val)
    pivot = df.pivot_table(index="entity", columns="period",
                              values="sent_val", aggfunc="mean")
    pivot = pivot.reindex(columns=period_order)
    # Order rows by total mentions
    pivot = pivot.reindex([e for e in top_entities if e in pivot.index])

    fig, ax = plt.subplots(figsize=(14, max(6, 0.4 * len(pivot))))
    cmap = plt.get_cmap("RdYlGn")
    im = ax.imshow(pivot.values, aspect="auto", cmap=cmap, vmin=-1, vmax=1)
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels([p.split(" ", 1)[0] for p in pivot.columns],
                       rotation=30, ha="right")
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index, fontsize=10)
    plt.colorbar(im, ax=ax, label="Sentiment (-1=neg, 0=neu, +1=poz)")
    # Cells with n/a left empty
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            v = pivot.values[i, j]
            label = "—" if np.isnan(v) else (
                "+" if v > 0.3 else ("-" if v < -0.3 else "·")
            )
            ax.text(j, i, label, ha="center", va="center", fontsize=10,
                    color="white" if abs(v) > 0.5 else "black",
                    fontweight="bold" if not np.isnan(v) else "normal")
    ax.set_title(f"Sentiment ND × entitate × perioadă ({PROJECTION})")
    fig.tight_layout()
    fig.savefig(OUT / "sentiment_heatmap.png", dpi=120, bbox_inches="tight")
    plt.close(fig)

    # Markdown
    md = [f"# Pasul 9 — Sentiment per entitate × perioadă ({PROJECTION})\n"]
    md.append(f"**Setup**: Top {len(top_entities)} entități din NER × perioade cu ≥{MIN_MENTIONS_PER_BUCKET} mențiuni.")
    md.append(f"Sentiment clasificat cu Gemini 2.5 Flash pe paragrafele care menționează entitatea.\n")
    md.append(f"**Buckets clasificate**: {len(results)}\n")
    md.append("## Sumar (tabel)\n")
    md.append(df.to_markdown(index=False))

    (OUT / "summary.md").write_text("\n".join(md))
    print(f"\nOutput: {OUT}/")


if __name__ == "__main__":
    main()
