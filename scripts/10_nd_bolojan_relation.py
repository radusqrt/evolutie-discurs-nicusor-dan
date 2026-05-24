"""Pasul 10: Raportul ND - Bolojan din corpusul ND.

Extract toate paragrafele unde ND îl menționează pe Bolojan (sau "premier"),
le grupează pe perioadă, le trimite la Gemini pentru characterizare relațională,
și produce raport markdown comparativ vs Ciolacu (predecesor).

Output: results/10_nd_bolojan/
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from collections import defaultdict
from datetime import date
from pathlib import Path

import frontmatter
from dotenv import load_dotenv

from corpus import _normalize_diacritics, strip_speaker_tags_to_nd

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
SRC = ROOT / "data" / "3_nd_overall"
OUT = ROOT / "results" / "10_nd_bolojan"
OUT.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "gemini-2.5-flash"

# Bolojan a devenit premier pe 23 iunie 2025
BOLOJAN_PM_START = date(2025, 6, 23)

# Patterns to find Bolojan mentions
BOLOJAN_PATTERNS = [
    r"\bbolojan\b",
    r"\bilie bolojan\b",
    r"\bpremier(ul|ului)?\b",
    r"\bprim[- ]ministru(l|lui)?\b",
]

CIOLACU_PATTERNS = [
    r"\bciolacu\b",
    r"\bmarcel ciolacu\b",
]

RELATIONSHIP_PROMPT = """Ești un analist politic. Mai jos sunt extrase din discursul lui Nicușor Dan (Președintele României) din perioada {period}, unde face referire la **Ilie Bolojan** (Premierul României, din 23 iunie 2025) sau la funcția de Premier.

Analizează **raportul lui Nicușor Dan cu Bolojan** în această perioadă, pe baza acestor extrase:

EXTRASE:
{passages}

OUTPUT — JSON object:
{{
  "relationship_tone": "colaborativ | deferent | critic | tensionat | distant | mixt",
  "confidence": "high | medium | low",
  "key_themes": ["max 3 teme cheie de care vorbesc împreună"],
  "power_dynamic": "ND domină | Bolojan domină | balansat | n/a",
  "tensions_visible": "da | nu | parțial",
  "rationale": "3-5 propoziții cu citate scurte care justifică",
  "notable_quotes": ["citat scurt 1 (max 250 caractere)", "citat 2", "citat 3"]
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
    return "outside"


def extract_mentions(text: str, patterns: list[str], context_chars: int = 350) -> list[dict]:
    """Extract paragraphs/spans mentioning entity. Returns list of {span, raw_match}."""
    text_norm = _normalize_diacritics(text)
    spans: list[tuple[int, int, str]] = []
    for pat in patterns:
        for m in re.finditer(pat, text_norm, re.IGNORECASE):
            start = max(0, m.start() - context_chars)
            end = min(len(text), m.end() + context_chars)
            spans.append((start, end, m.group()))

    if not spans:
        return []

    # Merge overlapping
    spans.sort()
    merged: list[tuple[int, int, list[str]]] = []
    for s, e, raw in spans:
        if merged and s < merged[-1][1]:
            old_s, old_e, raws = merged[-1]
            new_e = max(old_e, e)
            raws.append(raw)
            merged[-1] = (old_s, new_e, raws)
        else:
            merged.append((s, e, [raw]))

    return [
        {"start": s, "end": e, "span": text[s:e].strip(), "matches": list(set(raws))}
        for s, e, raws in merged
    ]


def parse_date(s: str) -> date | None:
    try:
        return date.fromisoformat(s[:10])
    except (ValueError, TypeError):
        return None


def main():
    print(f"Loading corpus from {SRC}...")
    bolojan_rows = []
    ciolacu_rows = []

    for path in sorted(SRC.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        d_str = str(post.get("data", ""))
        d = parse_date(d_str)
        if not d:
            continue

        text = strip_speaker_tags_to_nd(post.content.strip())
        if not text:
            continue

        # Bolojan mentions
        b_mentions = extract_mentions(text, BOLOJAN_PATTERNS)
        for m in b_mentions:
            bolojan_rows.append({
                "doc_id": path.stem,
                "date": str(d),
                "period": period_for(str(d)),
                "tip": str(post.get("tip", "")),
                "match": " | ".join(m["matches"]),
                "context": m["span"],
            })

        # Ciolacu mentions
        c_mentions = extract_mentions(text, CIOLACU_PATTERNS)
        for m in c_mentions:
            ciolacu_rows.append({
                "doc_id": path.stem,
                "date": str(d),
                "period": period_for(str(d)),
                "tip": str(post.get("tip", "")),
                "match": " | ".join(m["matches"]),
                "context": m["span"],
            })

    print(f"Bolojan/premier mentions: {len(bolojan_rows)} spans")
    print(f"Ciolacu mentions: {len(ciolacu_rows)} spans")

    # Save raw extracted
    with (OUT / "bolojan_mentions.jsonl").open("w") as f:
        for r in bolojan_rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with (OUT / "ciolacu_mentions.jsonl").open("w") as f:
        for r in ciolacu_rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # Distribute Bolojan mentions per period
    by_period: dict[str, list[dict]] = defaultdict(list)
    for r in bolojan_rows:
        by_period[r["period"]].append(r)

    print(f"\nBolojan mentions per perioadă:")
    for p in sorted(by_period.keys()):
        print(f"  {p}: {len(by_period[p])} spans, {len(set(r['doc_id'] for r in by_period[p]))} docs unice")

    # Per period: send to LLM
    client, types = get_client()
    period_analyses: list[dict] = []

    for period, rows in sorted(by_period.items()):
        if len(rows) < 2:
            continue
        passages = "\n===\n".join(r["context"][:600] for r in rows[:25])  # cap
        passages = passages[:10000]
        prompt = RELATIONSHIP_PROMPT.format(period=period, passages=passages)

        print(f"\nClasificare per perioadă: {period} ({len(rows)} spans)...")
        try:
            resp = client.models.generate_content(
                model=MODEL_NAME, contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.1,
                    thinking_config=types.ThinkingConfig(thinking_budget=0),
                    response_mime_type="application/json",
                ),
            )
            result = json.loads(resp.text.strip())
            result["period"] = period
            result["n_mentions"] = len(rows)
            result["n_docs"] = len(set(r["doc_id"] for r in rows))
            period_analyses.append(result)
            print(f"  → {result.get('relationship_tone')} (confidence: {result.get('confidence')})")
        except Exception as e:
            print(f"  ERROR: {e}")

    with (OUT / "period_analyses.jsonl").open("w") as f:
        for a in period_analyses:
            f.write(json.dumps(a, ensure_ascii=False) + "\n")

    # Overall comparative LLM
    print("\nOverall relationship synthesis...")
    all_passages = "\n===\n".join(
        r["context"][:600] for r in sorted(bolojan_rows, key=lambda r: r["date"])[:60]
    )[:15000]

    overall_prompt = f"""Pe baza tuturor mențiunilor lui Nicușor Dan (Președinte) despre Ilie Bolojan (Premier din 23 iunie 2025) sau funcția de Premier, fă o ANALIZĂ DE ANSAMBLU a relației.

EXTRASE (cronologice, primele 60):
{all_passages}

OUTPUT — JSON:
{{
  "overall_tone": "scurt descriptor",
  "evolution": "cum s-a evoluat în timp",
  "key_observations": ["3-5 observații numerotate"],
  "power_dynamic": "descriere",
  "tensions": "descriere tensiuni (dacă există)",
  "agreement_areas": ["zone de acord/colaborare"],
  "headline_quote": "citatul cel mai relevant pentru relație"
}}

Returnează DOAR JSON."""

    try:
        resp = client.models.generate_content(
            model=MODEL_NAME, contents=overall_prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                response_mime_type="application/json",
            ),
        )
        overall = json.loads(resp.text.strip())
        (OUT / "overall_synthesis.json").write_text(
            json.dumps(overall, ensure_ascii=False, indent=2)
        )
        print(f"Overall tone: {overall.get('overall_tone')}")
    except Exception as e:
        print(f"Overall error: {e}")
        overall = {"overall_tone": "ERROR", "evolution": str(e)}

    # Markdown report
    md = [f"# Pasul 10 — Raport relația ND-Bolojan\n"]
    md.append(f"**Sursă date**: corpus ND (1062 docs overall, decembrie 2024 → mai 2026)")
    md.append(f"**Context**: Bolojan = premier de la 23 iunie 2025\n")

    md.append("## Sumar mențiuni\n")
    md.append(f"- **Bolojan / premier**: {len(bolojan_rows)} spans, {len(set(r['doc_id'] for r in bolojan_rows))} docs unice")
    md.append(f"- **Ciolacu (comparativ)**: {len(ciolacu_rows)} spans, {len(set(r['doc_id'] for r in ciolacu_rows))} docs unice")

    md.append("\n## Mențiuni per perioadă\n")
    md.append("| Perioadă | Bolojan / premier | Ciolacu |")
    md.append("|---|---:|---:|")
    all_periods = sorted(set([r["period"] for r in bolojan_rows] +
                              [r["period"] for r in ciolacu_rows]))
    for p in all_periods:
        b = len([r for r in bolojan_rows if r["period"] == p])
        c = len([r for r in ciolacu_rows if r["period"] == p])
        md.append(f"| {p} | {b} | {c} |")

    md.append("\n## Analiza per perioadă (Gemini LLM)\n")
    for a in period_analyses:
        md.append(f"\n### {a['period']}")
        md.append(f"**Spans**: {a['n_mentions']} | **Docs unice**: {a['n_docs']}")
        md.append(f"\n**Ton relațional**: `{a.get('relationship_tone')}` (confidence: {a.get('confidence')})")
        md.append(f"\n**Power dynamic**: {a.get('power_dynamic')}")
        md.append(f"\n**Tensiuni vizibile**: {a.get('tensions_visible')}")
        if a.get("key_themes"):
            md.append(f"\n**Teme cheie**: {', '.join(a['key_themes'])}")
        md.append(f"\n**Raționament**: {a.get('rationale', '')}")
        if a.get("notable_quotes"):
            md.append(f"\n**Citate notabile**:")
            for q in a["notable_quotes"][:3]:
                md.append(f"- *\"{q}\"*")

    md.append("\n---\n## Sinteză generală\n")
    md.append(f"**Tone overall**: `{overall.get('overall_tone', '?')}`")
    md.append(f"\n**Evolution**: {overall.get('evolution', '')}")
    md.append(f"\n**Power dynamic**: {overall.get('power_dynamic', '')}")
    md.append(f"\n**Tensiuni**: {overall.get('tensions', '')}")
    if overall.get("key_observations"):
        md.append("\n**Observații cheie**:")
        for i, obs in enumerate(overall["key_observations"], 1):
            md.append(f"{i}. {obs}")
    if overall.get("agreement_areas"):
        md.append("\n**Zone de acord**:")
        for a_area in overall["agreement_areas"]:
            md.append(f"- {a_area}")
    if overall.get("headline_quote"):
        md.append(f"\n**Headline quote**:\n> *\"{overall['headline_quote']}\"*")

    md.append("\n---\n## Mențiuni Ciolacu (comparativ) per perioadă\n")
    md.append("Ciolacu a fost Premier până în iunie 2025; după, doar context istoric.\n")
    cio_by_period: dict[str, list[dict]] = defaultdict(list)
    for r in ciolacu_rows:
        cio_by_period[r["period"]].append(r)
    md.append("| Perioadă | Mențiuni | Docs |")
    md.append("|---|---:|---:|")
    for p in sorted(cio_by_period.keys()):
        rs = cio_by_period[p]
        md.append(f"| {p} | {len(rs)} | {len(set(r['doc_id'] for r in rs))} |")

    (OUT / "RAPORT.md").write_text("\n".join(md))

    print(f"\nOutputs in: {OUT}/")
    print(f"  - RAPORT.md")
    print(f"  - bolojan_mentions.jsonl ({len(bolojan_rows)} spans)")
    print(f"  - ciolacu_mentions.jsonl ({len(ciolacu_rows)} spans)")
    print(f"  - period_analyses.jsonl ({len(period_analyses)} perioade analizate)")
    print(f"  - overall_synthesis.json")


if __name__ == "__main__":
    main()
