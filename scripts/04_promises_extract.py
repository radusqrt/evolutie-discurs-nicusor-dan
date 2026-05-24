"""Pasul 4a: Extract promisiuni explicite din corpus de campanie (date <= 2025-05-25).

Folosește Gemini 2.5 Flash cu prompt focused pe definiția strictă de promisiune
(angajament la acțiune viitoare specifică). Output JSONL per promisiune.

Run:
    python scripts/04_promises_extract.py [--limit N] [--workers W]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

import frontmatter
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
SRC = ROOT / "data" / "3_nd_overall"
OUT_DIR = ROOT / "results" / "04_promises"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "promises_raw.jsonl"

CAMPAIGN_END = date(2025, 5, 25)  # data învestirii — 26 mai 2025
MODEL_NAME = "gemini-2.5-flash"

PROMPT = """Ești un analist politic care extrage **promisiuni de campanie** din discursul lui Nicușor Dan (candidat la Președinția României, alegeri 2025).

DEFINIȚIE STRICTĂ — promisiune = angajament EXPLICIT la o ACȚIUNE viitoare specifică, făcut de ND.

INCLUDE:
- "Voi face X", "Vom face X" (când ND e clar subiectul)
- "Mă angajez să..."
- "Primul lucru pe care îl voi face este..."
- "Dacă voi fi președinte, voi..."
- "Promit că..."
- Angajament condiționat: "Dacă X, atunci voi face Y"

EXCLUDE:
- Opinii sau evaluări ("cred că X e important", "X e o problemă")
- Diagnoze de probleme fără soluție-acțiune ("avem deficit mare")
- Acțiuni trecute ("am făcut X")
- Comentarii despre alții ("Y trebuie să facă X")
- Aspirații vagi fără acțiune ("România merită mai bine")
- Statement-uri generale despre rolul președintelui fără angajament personal

FORMAT OUTPUT — JSON array. Fiecare promisiune:
{
  "promise_text": "rezumat clar al promisiunii la persoana I (1-2 propoziții)",
  "verbatim_quote": "citatul exact din text",
  "topic": "una din: justiție, NATO/apărare, energie/UE, măsuri fiscale, legi/reformă instituțională, Ucraina/Rusia, diplomație, R. Moldova, diaspora, București/local, anti-corupție, educație, sănătate, social, economie, mediu, justiție electorală, alt",
  "specificity": "high | medium | low (cât de concretă e acțiunea)"
}

Dacă NU sunt promisiuni explicite în text, returnează []. Nu inventa.

TEXT:
=============
{text}
=============

Returnează DOAR JSON array. Niciun preambul, comentariu, sau cod block."""


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or "your-" in api_key:
        print("ERROR: GEMINI_API_KEY missing in .env", file=sys.stderr)
        sys.exit(1)
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=180_000))
    return client, types


def parse_date(date_str: str) -> date | None:
    try:
        return date.fromisoformat(date_str[:10])
    except (ValueError, TypeError):
        return None


def load_campaign_docs(limit: int | None = None) -> list[dict]:
    docs = []
    for path in sorted(SRC.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        d = parse_date(str(post.get("data", "")))
        if not d or d > CAMPAIGN_END:
            continue
        content = post.content.strip()
        if not content or len(content.split()) < 30:
            continue
        docs.append({
            "id": path.stem,
            "date": str(d),
            "tip": str(post.get("tip", "")),
            "sursa": str(post.get("sursa", "")),
            "text": content,
            "word_count": len(content.split()),
        })
    if limit:
        docs = docs[:limit]
    return docs


def extract_promises(doc: dict, client, types) -> list[dict]:
    """LLM call to extract promises from one doc."""
    text = doc["text"]
    # Truncate very long docs to avoid token limits (rare for campaign)
    if len(text) > 30_000:
        text = text[:30_000]

    prompt = PROMPT.replace("{text}", text)
    try:
        resp = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                response_mime_type="application/json",
            ),
        )
        raw = resp.text.strip()
        promises = json.loads(raw)
        if not isinstance(promises, list):
            return []
        # Enrich each promise with source doc metadata
        for p in promises:
            p["source_doc_id"] = doc["id"]
            p["source_date"] = doc["date"]
            p["source_tip"] = doc["tip"]
            p["source_sursa"] = doc["sursa"]
        return promises
    except json.JSONDecodeError as e:
        print(f"  [JSON parse error] {doc['id']}: {str(e)[:100]}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"  [API error] {doc['id']}: {type(e).__name__}: {str(e)[:100]}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None, help="Process only first N docs")
    parser.add_argument("--workers", type=int, default=4, help="Parallel workers")
    parser.add_argument("--resume", action="store_true", help="Skip docs already in output")
    args = parser.parse_args()

    docs = load_campaign_docs(limit=args.limit)
    print(f"Loaded {len(docs)} campaign docs (≤ {CAMPAIGN_END}).")

    done_ids = set()
    if args.resume and OUT.exists():
        with OUT.open() as f:
            for line in f:
                try:
                    done_ids.add(json.loads(line)["source_doc_id"])
                except (json.JSONDecodeError, KeyError):
                    pass
        print(f"Resume mode: skipping {len(done_ids)} already-processed docs.")
        docs = [d for d in docs if d["id"] not in done_ids]
        print(f"Remaining: {len(docs)} docs.")

    client, types = get_client()

    t0 = time.time()
    n_promises = 0
    n_done = 0
    mode = "a" if args.resume else "w"

    with OUT.open(mode) as out_f:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futures = {ex.submit(extract_promises, d, client, types): d for d in docs}
            for fut in as_completed(futures):
                d = futures[fut]
                try:
                    promises = fut.result(timeout=240)
                except Exception as e:
                    print(f"  [timeout/exception] {d['id']}: {e}", file=sys.stderr)
                    promises = []
                for p in promises:
                    out_f.write(json.dumps(p, ensure_ascii=False) + "\n")
                out_f.flush()
                n_promises += len(promises)
                n_done += 1
                elapsed = time.time() - t0
                rate = n_done / max(elapsed, 0.1)
                print(f"[{n_done}/{len(docs)}] {d['id'][:60]:<60} → {len(promises)} promises "
                      f"({n_promises} total | {rate:.1f} docs/s)")

    print(f"\nDone. {n_promises} promises extracted from {n_done} docs in {time.time()-t0:.1f}s.")
    print(f"Output: {OUT}")


if __name__ == "__main__":
    main()
