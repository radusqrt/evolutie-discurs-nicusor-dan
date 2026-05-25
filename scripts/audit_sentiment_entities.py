"""Audit spot-check pe sentiment per entity — verifică dacă passagele extrase
chiar sunt despre entitatea țintă (false positive check pe co-occurrence).

Sample: TRUMP, PSD, SIMION, TĂRICEANU pe perioadele cele mai populate.
Pentru fiecare bucket: re-extrag passagele, trimit fiecare la Gemini cu
întrebarea "este paragraful efectiv despre {entitate}?".

Raport: % din passages care nu sunt despre entitate (= co-occurrence FP).
"""
from __future__ import annotations

import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

import frontmatter
from dotenv import load_dotenv

from corpus import strip_speaker_tags_to_nd
from utils_entity_disambiguation import _classify_with_llm

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
SRC_NER = ROOT / "results" / "08_ner_overall" / "entities_per_doc_clean.jsonl"
SRC_CORPUS = ROOT / "data" / "3_nd_overall"
OUT = ROOT / "results" / "audit_sentiment_entities.md"

TARGET_ENTITIES = ["TRUMP", "PSD", "SIMION", "TĂRICEANU", "ORBÁN"]
SAMPLE_PER_BUCKET = 5  # how many passages to verify per bucket


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
    """Same logic as scripts/09_sentiment_per_entity.py."""
    import re
    from corpus import _normalize_diacritics
    text_norm = _normalize_diacritics(text)
    found = []
    for form in entity_raw_forms:
        form_norm = _normalize_diacritics(form)
        for m in re.finditer(re.escape(form_norm), text_norm, re.IGNORECASE):
            start = max(0, m.start() - context_chars)
            end = min(len(text_norm), m.end() + context_chars)
            found.append((start, end, text[start:end]))
    if not found:
        return []
    found.sort(key=lambda x: (x[0], -x[1]))
    merged = []
    for s, e, snip in found:
        if merged and s < merged[-1][1]:
            old_s, _, _ = merged[-1]
            merged[-1] = (old_s, max(merged[-1][1], e), text[old_s:max(merged[-1][1], e)])
        else:
            merged.append((s, e, snip))
    return [snip.strip() for _, _, snip in merged]


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=120_000))
    return client, types


def main():
    docs_entities = []
    with SRC_NER.open() as f:
        for line in f:
            docs_entities.append(json.loads(line))

    id_to_text = {}
    for path in sorted(SRC_CORPUS.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        text = post.content.strip()
        if text:
            id_to_text[path.stem] = strip_speaker_tags_to_nd(text)

    # Build entity -> period -> [(doc_id, passages)]
    entity_period: dict[tuple[str, str], list[tuple[str, list[str]]]] = defaultdict(list)
    for d in docs_entities:
        period = period_for(d["date"])
        text = id_to_text.get(d["id"], "")
        for ent in d.get("entities", []):
            canon = ent["canonical"]
            if canon not in TARGET_ENTITIES:
                continue
            raw_forms = ent.get("raw_forms", [canon])
            passages = extract_passages(raw_forms, text)
            if passages:
                entity_period[(canon, period)].append((d["id"], passages))

    client, types = get_client()

    rows = []
    print("Audit pe sentiment per entitate...")
    for (entity, period), docs in sorted(entity_period.items()):
        all_passages = [(doc_id, p) for doc_id, ps in docs for p in ps]
        if len(all_passages) < 3:
            continue
        sample = all_passages[:SAMPLE_PER_BUCKET]
        kept = 0
        rejected = 0
        reject_examples = []
        for doc_id, passage in sample:
            res = _classify_with_llm(passage, entity, entity, client, types)
            if res.get("is_about_entity") is True:
                kept += 1
            elif res.get("is_about_entity") is False:
                rejected += 1
                reject_examples.append({
                    "doc_id": doc_id,
                    "passage": passage[:300],
                    "actual_subject": res.get("actual_subject", "?"),
                    "reasoning": res.get("reasoning", "?")[:200],
                })
        row = {
            "entity": entity, "period": period,
            "total": len(all_passages), "sampled": len(sample),
            "kept": kept, "rejected": rejected,
            "fp_rate_pct": round(100*rejected/max(kept+rejected,1)),
            "examples": reject_examples,
        }
        rows.append(row)
        print(f"  {entity:<10} | {period[:25]:<25} | total={len(all_passages):>3} | "
              f"sampled={len(sample)} | kept={kept} | rejected={rejected} | FP={row['fp_rate_pct']}%")

    # Report
    md = ["# Audit sentiment per entitate — false positive check\n"]
    md.append(f"**Sample**: max {SAMPLE_PER_BUCKET} passages/bucket pentru entitățile {', '.join(TARGET_ENTITIES)}.\n")
    md.append("**Întrebare LLM**: pentru fiecare passage, e despre entitate sau alt subject?\n")
    md.append("## Sumar\n")
    md.append("| Entitate | Perioadă | Total passages | Sampled | Kept | Rejected | FP rate |")
    md.append("|---|---|---:|---:|---:|---:|---:|")
    for r in rows:
        md.append(f"| {r['entity']} | {r['period']} | {r['total']} | {r['sampled']} | "
                  f"{r['kept']} | {r['rejected']} | **{r['fp_rate_pct']}%** |")

    total_kept = sum(r['kept'] for r in rows)
    total_rejected = sum(r['rejected'] for r in rows)
    total_overall = total_kept + total_rejected
    fp_overall = round(100 * total_rejected / max(total_overall, 1))
    md.append(f"\n**Overall FP rate**: {total_rejected}/{total_overall} ({fp_overall}%)\n")

    md.append("## Exemple false positives\n")
    for r in rows:
        if r["examples"]:
            md.append(f"\n### {r['entity']} / {r['period']}")
            for ex in r["examples"]:
                md.append(f"\n**doc**: `{ex['doc_id']}`")
                md.append(f"- Actual subject: **{ex['actual_subject']}**")
                md.append(f"- Motiv: {ex['reasoning']}")
                md.append(f"- Passage: *\"{ex['passage']}\"*")

    OUT.write_text("\n".join(md))
    print(f"\nReport: {OUT}")
    print(f"Overall FP rate: {fp_overall}% ({total_rejected}/{total_overall})")


if __name__ == "__main__":
    main()
