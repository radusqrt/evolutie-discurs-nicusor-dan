"""Pasul 9d: Audit pe toate clasificările NEGATIV — verifică dacă ND e actor critic
sau mediator/apărător.

Pentru fiecare bucket cu sentiment="negativ":
1. Cere Gemini second-opinion cu prompt focused pe "ND ca actor": e ATACATOR
   activ sau MEDIATOR/APĂRĂTOR?
2. Daca a doua opinie diferă, marchează ca "suspect" pentru review manual

Run:
    python scripts/09d_negative_audit.py
"""
from __future__ import annotations

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
OUT = ROOT / "results" / "09_sentiment_audit_negativ.md"
MODEL_NAME = "gemini-2.5-flash"

AUDIT_PROMPT = """Ești un fact-checker rigoros. Mai jos sunt extrase din discursul lui Nicușor Dan (Președintele României) unde menționează entitatea **{entity}** în perioada {period}.

O clasificare automată anterioară a marcat acest set ca **NEGATIV** (ND critică {entity}).
Verifică dacă această clasificare e corectă, sau dacă ND era de fapt:
- MEDIATOR (vorbește despre tensiune fără să atace direct)
- APĂRĂTOR (apără {entity} sau procesul/instituția)
- CONSTATATOR pragmatic (recunoaște dificultăți fără atitudine ostilă)
- IRELEVANT (entitatea apare doar în context, fără sentiment evident față de ea)
- CONFIRMAT NEGATIV (ND chiar critică direct {entity})

EXTRASE:
{passages}

OUTPUT — JSON object:
{{
  "verdict": "CONFIRMAT_NEGATIV | MIXT | MEDIATOR | APARARE | CONSTATATOR | IRELEVANT",
  "confidence": "high | medium | low",
  "is_nd_attacking": "da | nu | partial",
  "rationale": "1-3 propoziții — ce face ND în aceste extrase?",
  "key_red_flags": ["fraze concrete unde ND chiar atacă entitatea, dacă există"]
}}

Returnează DOAR JSON object. NU array. Niciun preambul."""


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=120_000))
    return client, types


def load_negativ_buckets():
    """Find all buckets with sentiment=negativ across 3 projections (with passages)."""
    from collections import defaultdict
    from corpus import strip_speaker_tags_to_nd, _normalize_diacritics
    import re
    import frontmatter

    def period_for(d):
        y, m = int(d[:4]), int(d[5:7])
        if y == 2024 or (y == 2025 and m <= 2): return "2024Q4-2025Q1 candidatură-precampanie"
        if y == 2025 and m <= 5: return "2025Q2 campanie + investitură"
        if y == 2025 and m <= 8: return "2025Q3 deficit + reforma economică"
        if y == 2025 and m <= 11: return "2025Q4 stabilizare + diplomație"
        if y == 2025 and m == 12 or (y == 2026 and m <= 2): return "2025Q4-2026Q1 reformă judiciară"
        if y == 2026 and m <= 5: return "2026Q2 cotitură UE + criză guvern"
        return "outside"

    buckets = []
    for proj in ["overall", "vorbit", "scris"]:
        sent_path = ROOT / "results" / f"09_sentiment_per_entity_{proj}" / "sentiment_per_entity_period.jsonl"
        if not sent_path.exists():
            continue
        # Build passages from corpus + NER
        ner_path = ROOT / "results" / f"08_ner_{proj}" / "entities_per_doc_clean.jsonl"
        corpus_dir = ROOT / "data" / f"3_nd_{proj}"

        docs_ner = []
        with ner_path.open() as f:
            for line in f:
                docs_ner.append(json.loads(line))
        id_to_text = {}
        for p in corpus_dir.rglob("*.md"):
            if "/excluded/" in str(p):
                continue
            post = frontmatter.load(p)
            id_to_text[p.stem] = strip_speaker_tags_to_nd(post.content.strip())

        bucket_passages = defaultdict(list)
        for d in docs_ner:
            period = period_for(d["date"])
            text = id_to_text.get(d["id"], "")
            text_norm = _normalize_diacritics(text)
            for ent in d.get("entities", []):
                canon = ent["canonical"]
                for form in ent.get("raw_forms", [canon]):
                    form_norm = _normalize_diacritics(form)
                    for m in re.finditer(re.escape(form_norm), text_norm, re.IGNORECASE):
                        s = max(0, m.start() - 250)
                        e = min(len(text), m.end() + 250)
                        bucket_passages[(canon, period)].append(text[s:e].strip())

        # Now load negativ buckets
        with sent_path.open() as f:
            for line in f:
                r = json.loads(line)
                if r.get("sentiment") == "negativ":
                    key = (r["entity"], r["period"])
                    r["projection"] = proj
                    r["passages_text"] = bucket_passages.get(key, [])[:10]
                    buckets.append(r)
    return buckets


def audit_one(bucket, client, types) -> dict:
    passages_text = "\n===\n".join(bucket["passages_text"])[:8000]
    prompt = AUDIT_PROMPT.format(
        entity=bucket["entity"],
        period=bucket["period"],
        passages=passages_text or "(no passages)",
    )
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
            p = json.loads(raw)
            if isinstance(p, list) and len(p) > 0:
                p = p[0]
            if isinstance(p, dict):
                return p
            raise ValueError("not dict")
        except Exception as e:
            if attempt == 2:
                return {"verdict": "ERROR", "rationale": str(e)[:200]}
            time.sleep(2)
    return {"verdict": "ERROR"}


def main():
    print("Loading all NEGATIV buckets across projections...")
    buckets = load_negativ_buckets()
    # Dedup overall + vorbit duplicates (same entity, same period)
    # Keep overall as primary
    seen = set()
    unique_buckets = []
    for b in buckets:
        key = (b["entity"], b["period"])
        if key not in seen:
            seen.add(key)
            unique_buckets.append(b)
    print(f"Found {len(unique_buckets)} unique negativ buckets (after dedup).")

    client, types = get_client()
    results = []
    t0 = time.time()

    def process(b):
        audit = audit_one(b, client, types)
        return {**b, "audit": audit}

    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(process, b): b for b in unique_buckets}
        for i, fut in enumerate(as_completed(futs), 1):
            try:
                r = fut.result(timeout=180)
            except Exception as e:
                r = futs[fut]
                r["audit"] = {"verdict": "TIMEOUT", "rationale": str(e)[:100]}
            results.append(r)
            v = r["audit"].get("verdict", "?")
            print(f"[{i}/{len(unique_buckets)}] {r['entity']:<22} {r['period'][:25]:<25} → {v}")

    # Generate report
    md = ["# Audit clasificări NEGATIV — second opinion Gemini\n"]
    md.append(f"**Setup**: pentru fiecare bucket cu sentiment=NEGATIV, am cerut Gemini să verifice dacă ND e *atacator activ* sau *mediator/apărător*. Buckets unde a doua opinie diferă = candidați pentru override manual.\n")
    md.append(f"**Total audited**: {len(results)} buckets\n")

    # Group by verdict
    from collections import Counter
    verdicts = Counter(r["audit"].get("verdict", "?") for r in results)
    md.append("## Distribuție verdicte\n")
    for v, n in verdicts.most_common():
        md.append(f"- **{v}**: {n}")

    md.append("\n## Detalii\n")
    # Sort: CONFIRMAT_NEGATIV last (those are fine), problematic first
    priority = {"MEDIATOR": 0, "APARARE": 1, "CONSTATATOR": 2, "IRELEVANT": 3,
                 "MIXT": 4, "ERROR": 5, "TIMEOUT": 6, "CONFIRMAT_NEGATIV": 99}
    results.sort(key=lambda r: priority.get(r["audit"].get("verdict", "?"), 10))

    for r in results:
        a = r["audit"]
        verdict = a.get("verdict", "?")
        emoji = "⚠️" if verdict not in ["CONFIRMAT_NEGATIV", "ERROR"] else "✅" if verdict == "CONFIRMAT_NEGATIV" else "❓"
        md.append(f"\n### {emoji} {r['entity']} × {r['period']}")
        md.append(f"**Verdict audit**: `{verdict}` (confidence: {a.get('confidence', '?')})")
        md.append(f"**Atacator?**: {a.get('is_nd_attacking', '?')}")
        md.append(f"**Raționament audit**: {a.get('rationale', '')}")
        red = a.get("key_red_flags") or []
        if red:
            md.append(f"**Atacuri concrete**: {', '.join(repr(s) for s in red[:3])}")
        md.append(f"**Raționament original Gemini**: {r.get('rationale', '')[:300]}")
        md.append(f"**Proiecție**: `{r['projection']}` | n_passages: {r.get('n_passages', '?')}")

    OUT.write_text("\n".join(md))
    print(f"\nReport: {OUT}")
    print(f"\nVerdicte:")
    for v, n in verdicts.most_common():
        print(f"  {v:<25} {n}")
    print(f"\nElapsed: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "scripts"))
    main()
