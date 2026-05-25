"""Pasul 9b: Retry sentiment doar pe entry-urile cu n/a (timeout/error).

Recitește output-ul existent, identifică doar buckets cu sentiment=n/a,
le re-rulează cu handling mai robust (acceptă list sau dict ca răspuns LLM).
Apoi merge înapoi în fișier.

Run:
    PROJECTION=vorbit python scripts/09b_sentiment_retry.py
"""
from __future__ import annotations

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import frontmatter
from dotenv import load_dotenv

from corpus import _normalize_diacritics, strip_speaker_tags_to_nd

PROJECTION = os.getenv("PROJECTION", "overall")
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
SRC_NER = ROOT / "results" / f"08_ner_{PROJECTION}" / "entities_per_doc_clean.jsonl"
SRC_CORPUS = ROOT / "data" / f"3_nd_{PROJECTION}"
SRC_SENT = ROOT / "results" / f"09_sentiment_per_entity_{PROJECTION}" / "sentiment_per_entity_period.jsonl"

MODEL_NAME = "gemini-2.5-flash"

SENTIMENT_PROMPT = """Ești un analist de discurs politic. Mai jos sunt extrase din discursurile lui Nicușor Dan (Președintele României) unde menționează entitatea **{entity}**.

Analizează DOAR atitudinea lui Nicușor Dan față de acea entitate, în aceste extrase.

ETICHETE:
- "pozitiv" — ND vorbește favorabil
- "negativ" — ND critică, dezaprobă
- "neutru" — menționare neutrală
- "mixt" — elemente atât pozitive cât și negative
- "n/a" — nu se poate evalua

EXTRASE (separate prin ===):
{passages}

OUTPUT — JSON object (NU array):
{{
  "sentiment": "pozitiv | negativ | neutru | mixt | n/a",
  "confidence": "high | medium | low",
  "rationale": "1-2 propoziții justificare",
  "key_phrases": ["citat scurt 1", "citat scurt 2"]
}}

Returnează DOAR JSON object. NU array. Niciun preambul."""


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=180_000))
    return client, types


def classify_robust(entity: str, passages: list[str], client, types) -> dict:
    """Robust: handle both dict and list response from LLM."""
    if not passages:
        return {"sentiment": "n/a", "confidence": "low", "rationale": "no passages"}
    total = "\n===\n".join(passages)[:8000]
    prompt = SENTIMENT_PROMPT.format(entity=entity, passages=total)

    for attempt in range(3):
        try:
            resp = client.models.generate_content(
                model=MODEL_NAME, contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.1,
                    thinking_config=types.ThinkingConfig(thinking_budget=0),
                    response_mime_type="application/json",
                ),
            )
            raw = resp.text.strip()
            parsed = json.loads(raw)
            # Handle list response (LLM sometimes returns [{...}])
            if isinstance(parsed, list):
                if len(parsed) > 0 and isinstance(parsed[0], dict):
                    parsed = parsed[0]
                else:
                    raise ValueError(f"unexpected list format: {raw[:200]}")
            if not isinstance(parsed, dict):
                raise ValueError(f"not a dict: {type(parsed).__name__}")
            return parsed
        except (json.JSONDecodeError, ValueError) as e:
            if attempt == 2:
                return {"sentiment": "n/a", "confidence": "low",
                        "rationale": f"parse error after 3 attempts: {str(e)[:120]}"}
            time.sleep(2)
        except Exception as e:
            if attempt == 2:
                return {"sentiment": "n/a", "confidence": "low",
                        "rationale": f"{type(e).__name__}: {str(e)[:120]}"}
            time.sleep(2)
    return {"sentiment": "n/a", "confidence": "low", "rationale": "exhausted retries"}


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


def extract_passages(entity_raw_forms: list[str], text: str,
                       context_chars: int = 250) -> list[str]:
    import re
    text_norm = _normalize_diacritics(text)
    found_spans = []
    for form in entity_raw_forms:
        form_norm = _normalize_diacritics(form)
        for m in re.finditer(re.escape(form_norm), text_norm, re.IGNORECASE):
            start = max(0, m.start() - context_chars)
            end = min(len(text_norm), m.end() + context_chars)
            found_spans.append((start, end))
    if not found_spans:
        return []
    found_spans.sort()
    merged = []
    for s, e in found_spans:
        if merged and s < merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    return [text[s:e].strip() for s, e in merged]


def main():
    # Load existing sentiment results
    existing = []
    with SRC_SENT.open() as f:
        for line in f:
            existing.append(json.loads(line))

    # Find n/a entries
    failures = [r for r in existing if r.get("sentiment") == "n/a"
                  and "no passages" not in str(r.get("rationale", ""))]
    print(f"Total entries: {len(existing)}, n/a failures to retry: {len(failures)}")

    if not failures:
        print("Nothing to retry.")
        return

    # Load NER docs + corpus to rebuild passages
    docs_entities = []
    with SRC_NER.open() as f:
        for line in f:
            docs_entities.append(json.loads(line))

    id_to_text = {}
    for path in SRC_CORPUS.rglob("*.md"):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        text = post.content.strip()
        if text:
            id_to_text[path.stem] = strip_speaker_tags_to_nd(text)

    # Rebuild passages per (entity, period)
    from collections import defaultdict
    bucket_passages = defaultdict(list)
    for d in docs_entities:
        period = period_for(d["date"])
        text = id_to_text.get(d["id"], "")
        for ent in d.get("entities", []):
            canon = ent["canonical"]
            raw_forms = ent.get("raw_forms", [canon])
            passages = extract_passages(raw_forms, text)
            for p in passages:
                bucket_passages[(canon, period)].append(p)

    # Re-classify each failure
    client, types = get_client()
    fixed_count = 0
    t0 = time.time()

    def retry_one(r):
        key = (r["entity"], r["period"])
        passages = bucket_passages.get(key, [])[:15]
        if not passages:
            return r  # no data, keep as is
        result = classify_robust(r["entity"], passages, client, types)
        r_new = {**r, **result, "rationale": result.get("rationale", "")}
        return r_new

    results_new = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(retry_one, r): r for r in failures}
        for i, fut in enumerate(as_completed(futs), 1):
            try:
                new_r = fut.result(timeout=200)
            except Exception as e:
                new_r = futs[fut]
                new_r["rationale"] = f"outer timeout: {e}"
            results_new.append(new_r)
            sent = new_r.get("sentiment", "?")
            if sent != "n/a":
                fixed_count += 1
            print(f"[{i}/{len(failures)}] {new_r['entity']:<22} {new_r['period'][:25]:<25} → {sent}")

    # Merge: replace old failures with new results
    keyfn = lambda r: (r["entity"], r["period"])
    new_by_key = {keyfn(r): r for r in results_new}
    merged = []
    for r in existing:
        k = keyfn(r)
        if k in new_by_key:
            merged.append(new_by_key[k])
        else:
            merged.append(r)

    # Save
    with SRC_SENT.open("w") as f:
        for r in merged:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"\nRetried {len(failures)}, fixed {fixed_count}/{len(failures)} "
          f"({100*fixed_count/max(len(failures),1):.0f}%) in {time.time()-t0:.0f}s.")


if __name__ == "__main__":
    main()
