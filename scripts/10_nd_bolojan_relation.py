"""Pasul 10: Raportul ND - Bolojan din corpusul ND.

V2 — folosește utils_entity_disambiguation pentru a evita false positives pe
match-uri generice ("premier", "prim ministru") care pot fi despre Ciolacu,
Ponta (istoric), sau context generic.

Pipeline:
1. Pentru fiecare document din corpus, extrage candidați (regex pe aliases +
   generic_terms).
2. Aliases (Bolojan, Ilie) → auto-acceptate.
3. Generic terms (premier, prim ministru):
   - dacă alias e în ±150 chars → auto-acceptat
   - altfel → trimise la Gemini cu întrebare disambiguare
4. Doar spans cu is_about_entity=True intră în classification per perioadă.

Output: results/10_nd_bolojan/
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import frontmatter
from dotenv import load_dotenv

from corpus import strip_speaker_tags_to_nd
from utils_entity_disambiguation import extract_disambiguated_mentions

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
SRC = ROOT / "data" / "3_nd_overall"
OUT = ROOT / "results" / "10_nd_bolojan"
OUT.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "gemini-2.5-flash"

# Bolojan a devenit premier pe 23 iunie 2025
BOLOJAN_PM_START = date(2025, 6, 23)

BOLOJAN_ALIASES = ["Bolojan", "Ilie Bolojan"]
BOLOJAN_GENERIC_TERMS = ["premier", "premierul", "premierului",
                         "prim ministru", "prim-ministru",
                         "prim ministrul", "prim-ministrul",
                         "prim ministrului", "prim-ministrului"]

CIOLACU_ALIASES = ["Ciolacu", "Marcel Ciolacu"]
# Pentru Ciolacu nu adăugăm "premier" generic — vrem doar mențiunile explicite

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


def parse_date(s: str) -> date | None:
    try:
        return date.fromisoformat(s[:10])
    except (ValueError, TypeError):
        return None


def main():
    print(f"Loading corpus from {SRC}...")
    client, types = get_client()

    bolojan_rows = []
    ciolacu_rows = []
    # Audit counters
    audit_counts = {
        "strict_alias": 0,
        "generic_with_name_nearby": 0,
        "llm_kept": 0,
        "llm_rejected": 0,
        "llm_unknown": 0,
    }
    rejected_examples: list[dict] = []

    md_files = sorted(SRC.rglob("*.md"))
    md_files = [p for p in md_files if "/excluded/" not in str(p)]
    print(f"Found {len(md_files)} documents.")

    for i, path in enumerate(md_files):
        if i % 50 == 0:
            print(f"  [{i}/{len(md_files)}] {path.name}")
        post = frontmatter.load(path)
        d_str = str(post.get("data", ""))
        d = parse_date(d_str)
        if not d:
            continue

        text = strip_speaker_tags_to_nd(post.content.strip())
        if not text:
            continue

        # Bolojan: cu disambiguare LLM pentru match-uri generice
        b_spans = extract_disambiguated_mentions(
            text=text,
            entity_name="Ilie Bolojan",
            aliases=BOLOJAN_ALIASES,
            generic_terms=BOLOJAN_GENERIC_TERMS,
            client=client, types=types,
        )
        for s in b_spans:
            mt = s["match_type"]
            if mt == "strict_alias":
                audit_counts["strict_alias"] += 1
            elif mt == "generic_with_name_nearby":
                audit_counts["generic_with_name_nearby"] += 1
            elif mt == "llm_disambiguated":
                if s["is_about_entity"] is True:
                    audit_counts["llm_kept"] += 1
                elif s["is_about_entity"] is False:
                    audit_counts["llm_rejected"] += 1
                    if len(rejected_examples) < 30:
                        rejected_examples.append({
                            "doc_id": path.stem,
                            "date": str(d),
                            "match": s["match_term"],
                            "reasoning": s.get("reasoning", ""),
                            "actual_subject": s.get("actual_subject", ""),
                            "span": s["span_text"][:400],
                        })
                else:
                    audit_counts["llm_unknown"] += 1

            if s["is_about_entity"] is True:
                bolojan_rows.append({
                    "doc_id": path.stem,
                    "date": str(d),
                    "period": period_for(str(d)),
                    "tip": str(post.get("tip", "")),
                    "match": s["match_term"],
                    "match_type": s["match_type"],
                    "confidence": s.get("confidence", "?"),
                    "context": s["span_text"],
                })

        # Ciolacu: doar nume strict
        c_spans = extract_disambiguated_mentions(
            text=text,
            entity_name="Marcel Ciolacu",
            aliases=CIOLACU_ALIASES,
            generic_terms=[],
            skip_llm=True,
        )
        for s in c_spans:
            if s["is_about_entity"]:
                ciolacu_rows.append({
                    "doc_id": path.stem,
                    "date": str(d),
                    "period": period_for(str(d)),
                    "tip": str(post.get("tip", "")),
                    "match": s["match_term"],
                    "match_type": s["match_type"],
                    "context": s["span_text"],
                })

    print(f"\n=== Audit ===")
    total_accepted = audit_counts["strict_alias"] + audit_counts["generic_with_name_nearby"] + audit_counts["llm_kept"]
    total_seen = total_accepted + audit_counts["llm_rejected"] + audit_counts["llm_unknown"]
    print(f"Strict alias match: {audit_counts['strict_alias']}")
    print(f"Generic + name nearby: {audit_counts['generic_with_name_nearby']}")
    print(f"LLM disambiguated → KEPT: {audit_counts['llm_kept']}")
    print(f"LLM disambiguated → REJECTED: {audit_counts['llm_rejected']}")
    print(f"LLM unknown: {audit_counts['llm_unknown']}")
    print(f"Total accepted: {total_accepted} / seen {total_seen} ({100*total_accepted/max(total_seen,1):.0f}%)")

    print(f"\nBolojan accepted spans: {len(bolojan_rows)}")
    print(f"Ciolacu mentions: {len(ciolacu_rows)}")

    (OUT / "audit_counts.json").write_text(json.dumps(audit_counts, indent=2))
    with (OUT / "rejected_examples.jsonl").open("w") as f:
        for r in rejected_examples:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

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

    print(f"\nBolojan mentions per perioadă (după disambiguare):")
    for p in sorted(by_period.keys()):
        print(f"  {p}: {len(by_period[p])} spans, {len(set(r['doc_id'] for r in by_period[p]))} docs unice")

    # Per period: send to LLM
    period_analyses: list[dict] = []

    for period, rows in sorted(by_period.items()):
        if len(rows) < 2:
            continue
        passages = "\n===\n".join(r["context"][:600] for r in rows[:25])
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
            if isinstance(result, list) and result:
                result = result[0]
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

    overall_prompt = f"""Pe baza tuturor mențiunilor lui Nicușor Dan (Președinte) despre Ilie Bolojan (Premier din 23 iunie 2025), fă o ANALIZĂ DE ANSAMBLU a relației.

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
        if isinstance(overall, list) and overall:
            overall = overall[0]
        (OUT / "overall_synthesis.json").write_text(
            json.dumps(overall, ensure_ascii=False, indent=2)
        )
        print(f"Overall tone: {overall.get('overall_tone')}")
    except Exception as e:
        print(f"Overall error: {e}")
        overall = {"overall_tone": "ERROR", "evolution": str(e)}

    # Markdown report
    md = [f"# Pasul 10 — Raport relația ND-Bolojan (v2, cu disambiguare LLM)\n"]
    md.append(f"**Sursă date**: corpus ND (decembrie 2024 → mai 2026)")
    md.append(f"**Context**: Bolojan = premier de la 23 iunie 2025\n")

    md.append("## Disambiguare entitate — audit\n")
    md.append("Pentru a evita false positives pe match-uri generice ('premier', 'prim-ministru'), folosim un pas de verificare:")
    md.append("- Match-uri **strict alias** (Bolojan/Ilie Bolojan) → auto-acceptate")
    md.append("- Match-uri **generice cu nume în vecinătate** (±150 chars) → auto-acceptate")
    md.append("- Match-uri **generice ambigue** → trimise la Gemini: 'este acest paragraf despre Bolojan?'\n")
    md.append("| Tip match | Număr |")
    md.append("|---|---:|")
    md.append(f"| Strict alias | {audit_counts['strict_alias']} |")
    md.append(f"| Generic + nume în vecinătate | {audit_counts['generic_with_name_nearby']} |")
    md.append(f"| LLM disambiguated → KEPT | {audit_counts['llm_kept']} |")
    md.append(f"| LLM disambiguated → REJECTED | {audit_counts['llm_rejected']} |")
    md.append(f"| LLM unknown | {audit_counts['llm_unknown']} |")
    rejection_rate = 100 * audit_counts['llm_rejected'] / max(audit_counts['llm_kept'] + audit_counts['llm_rejected'], 1)
    md.append(f"\n**Rejection rate pe match-uri ambigue: {rejection_rate:.0f}%** — adică {audit_counts['llm_rejected']} din {audit_counts['llm_kept']+audit_counts['llm_rejected']} erau false positives.\n")

    md.append("## Sumar mențiuni acceptate\n")
    md.append(f"- **Bolojan / premier (validat)**: {len(bolojan_rows)} spans, {len(set(r['doc_id'] for r in bolojan_rows))} docs unice")
    md.append(f"- **Ciolacu (comparativ, nume strict)**: {len(ciolacu_rows)} spans, {len(set(r['doc_id'] for r in ciolacu_rows))} docs unice")

    md.append("\n## Mențiuni per perioadă\n")
    md.append("| Perioadă | Bolojan (validat) | Ciolacu |")
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
        md.append(f"**Spans validate**: {a['n_mentions']} | **Docs unice**: {a['n_docs']}")
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

    if rejected_examples:
        md.append("\n---\n## Exemple de false positives rejected\n")
        md.append("(Primele 10 cazuri unde LLM a confirmat că paragraful NU e despre Bolojan)\n")
        for r in rejected_examples[:10]:
            md.append(f"\n**{r['date']} ({r['doc_id']})** — match: *'{r['match']}'*")
            md.append(f"- Subject real: **{r.get('actual_subject', '?')}**")
            md.append(f"- Motiv: {r.get('reasoning', '')}")

    (OUT / "RAPORT.md").write_text("\n".join(md))

    print(f"\nOutputs in: {OUT}/")
    print(f"  - RAPORT.md")
    print(f"  - bolojan_mentions.jsonl ({len(bolojan_rows)} spans)")
    print(f"  - ciolacu_mentions.jsonl ({len(ciolacu_rows)} spans)")
    print(f"  - period_analyses.jsonl ({len(period_analyses)} perioade analizate)")
    print(f"  - overall_synthesis.json")
    print(f"  - audit_counts.json")
    print(f"  - rejected_examples.jsonl ({len(rejected_examples)} cazuri)")


if __name__ == "__main__":
    main()
