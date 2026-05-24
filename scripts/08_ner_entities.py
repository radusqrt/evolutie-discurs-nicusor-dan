"""Pasul 8: NER cu GLiNER zero-shot — extrage entități din corpus.

GLiNER (urchade/gliner_multi-v2.1) e SotA pentru zero-shot NER multilingv.
Specifică etichete custom în limba RO, primește entități tipate.

Etichete utilizate:
  - "persoană politică" (Trump, Putin, Bolojan, Ciolacu, Simion, etc.)
  - "țară"
  - "instituție națională" (CCR, CSM, BNR, ANAF, DNA, DIICOT, etc.)
  - "instituție internațională" (UE, NATO, OECD/OCDE, ONU, etc.)
  - "partid politic"

Output: results/08_ner/entities_per_doc.jsonl + entity_timeline.csv

Run:
    PROJECTION=overall python scripts/08_ner_entities.py
"""
from __future__ import annotations

import json
import os
import re
import time
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd
import torch
from gliner import GLiNER

from corpus import _normalize_diacritics, load_corpus

PROJECTION = os.getenv("PROJECTION", "overall")
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "results" / f"08_ner_{PROJECTION}"
OUT.mkdir(parents=True, exist_ok=True)

LABELS = [
    "persoană politică",
    "țară",
    "instituție națională",
    "instituție internațională",
    "partid politic",
]

CHUNK_SIZE = 800  # tokens; GLiNER are limită ~384 by default but we chunk text


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


def chunk_text(text: str, max_chars: int = 1500) -> list[str]:
    """Split text into paragraph chunks respecting paragraph boundaries."""
    paragraphs = re.split(r"\n\n+", text)
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if current_len + len(p) > max_chars and current:
            chunks.append("\n\n".join(current))
            current = [p]
            current_len = len(p)
        else:
            current.append(p)
            current_len += len(p)
    if current:
        chunks.append("\n\n".join(current))
    return chunks


def canonicalize(name: str) -> str:
    """Normalize entity names — lowercase, strip, common variants → canonical."""
    n = name.strip().lower()
    n = re.sub(r"\s+", " ", n)
    n = _normalize_diacritics(n)
    # Common aliases
    aliases = {
        "donald trump": "trump",
        "vladimir putin": "putin", "v. putin": "putin",
        "volodimir zelenski": "zelenski", "volodymyr zelensky": "zelenski",
        "zelensky": "zelenski",
        "ilie bolojan": "bolojan",
        "marcel ciolacu": "ciolacu",
        "george simion": "simion",
        "călin georgescu": "georgescu", "calin georgescu": "georgescu",
        "maia sandu": "maia sandu",
        "viktor orban": "orban", "viktor orbán": "orban",
        "ursula von der leyen": "ursula vdl", "von der leyen": "ursula vdl",
        "klaus iohannis": "iohannis", "k. iohannis": "iohannis",
        "ciprian ciucu": "ciucu",
        "stelian bujduveanu": "bujduveanu",
        "victor ponta": "ponta",
        "sosoaca": "șoșoacă", "diana sosoaca": "șoșoacă", "diana șoșoacă": "șoșoacă",
        "uniunea europeană": "ue", "uniunea europeana": "ue", "comisia europeană": "ce",
        "comisia europeana": "ce",
        "statele unite": "sua", "statele unite ale americii": "sua",
        "federația rusă": "rusia", "federatia rusa": "rusia",
        "republica moldova": "r. moldova", "republica moldovei": "r. moldova",
        "marea britanie": "uk", "regatul unit": "uk",
        "macron": "macron", "emmanuel macron": "macron",
        "kaja kallas": "kallas",
        "mark rutte": "rutte",
    }
    return aliases.get(n, n)


def main():
    speeches = load_corpus()
    print(f"Loaded {len(speeches)} docs (projection={PROJECTION}).")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")
    print("Loading GLiNER...")
    model = GLiNER.from_pretrained("urchade/gliner_multi-v2.1").to(device)

    rows = []  # one row per entity mention
    doc_entities: list[dict] = []

    t0 = time.time()
    for i, s in enumerate(speeches):
        if i and i % 50 == 0:
            elapsed = time.time() - t0
            eta = (elapsed / i) * (len(speeches) - i)
            print(f"  [{i}/{len(speeches)}] elapsed {elapsed:.1f}s, ETA {eta:.0f}s")

        text = _normalize_diacritics(s.nd_only_text)
        if not text.strip() or len(text.split()) < 20:
            continue

        chunks = chunk_text(text, max_chars=1500)
        all_ents: list[dict] = []
        for chunk in chunks:
            try:
                ents = model.predict_entities(chunk, LABELS, threshold=0.45)
                all_ents.extend(ents)
            except Exception as e:
                print(f"  [error] {s.id}: {e}", file=sys.stderr)
                continue

        # Aggregate per canonical name + label
        agg: dict[tuple[str, str], dict] = {}
        for e in all_ents:
            key = (canonicalize(e["text"]), e["label"])
            if key not in agg:
                agg[key] = {"canonical": key[0], "label": key[1],
                             "raw_forms": set(), "count": 0, "max_score": 0.0}
            agg[key]["raw_forms"].add(e["text"].strip())
            agg[key]["count"] += 1
            agg[key]["max_score"] = max(agg[key]["max_score"], e["score"])

        doc_ents = []
        for (canon, label), v in agg.items():
            doc_ents.append({
                "canonical": canon, "label": label,
                "count": v["count"],
                "raw_forms": sorted(v["raw_forms"]),
                "max_score": round(v["max_score"], 3),
            })
            rows.append({
                "doc_id": s.id, "date": s.date, "tip": s.tip,
                "period": period_for(s.date),
                "canonical": canon, "label": label,
                "count": v["count"], "max_score": round(v["max_score"], 3),
            })
        doc_entities.append({"id": s.id, "date": s.date, "tip": s.tip,
                              "entities": doc_ents})

    elapsed = time.time() - t0
    print(f"\nNER done in {elapsed:.1f}s. Total mentions: {len(rows)}.")

    # Save per-doc JSONL
    with (OUT / "entities_per_doc.jsonl").open("w") as f:
        for d in doc_entities:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "mentions.csv", index=False)
    print(f"Mentions CSV: {len(df)} rows.")

    # Top entities by total count
    top_entities = (
        df.groupby(["canonical", "label"])["count"].sum()
          .sort_values(ascending=False)
          .reset_index()
    )
    top_entities.head(50).to_csv(OUT / "top_entities.csv", index=False)
    print("\nTop 30 entities by total mention count:")
    print(top_entities.head(30).to_string())

    # Entity × period timeline (top 25 entities only)
    top_25 = top_entities.head(25)["canonical"].tolist()
    timeline = df[df["canonical"].isin(top_25)].groupby(
        ["canonical", "period"])["count"].sum().unstack(fill_value=0)
    period_order = sorted(df["period"].unique())
    timeline = timeline.reindex(columns=period_order, fill_value=0)
    # Sort rows by total
    timeline["_total"] = timeline.sum(axis=1)
    timeline = timeline.sort_values("_total", ascending=False).drop(columns=["_total"])
    timeline.to_csv(OUT / "entity_timeline.csv")

    # Markdown summary
    md = [f"# Pasul 8 — NER + Entity timeline ({PROJECTION})\n"]
    md.append(f"**Model**: GLiNER multi-v2.1 (zero-shot multilingv, threshold 0.45)")
    md.append(f"**Labels**: {', '.join(LABELS)}")
    md.append(f"**Docs procesate**: {len(doc_entities)} | **Mentions extrase**: {len(rows)}")
    md.append(f"**Entități canonice unice**: {df['canonical'].nunique()}\n")

    md.append("## Top 30 entități (by mention count)\n")
    md.append(top_entities.head(30).to_markdown(index=False))

    md.append("\n## Entity timeline (top 25, count per perioadă)\n")
    md.append(timeline.to_markdown())

    (OUT / "summary.md").write_text("\n".join(md))
    print(f"\nOutput: {OUT}/")


if __name__ == "__main__":
    import sys
    main()
