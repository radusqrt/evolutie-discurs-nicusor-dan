"""Final diarize attempt — uses google-genai (NEW SDK) with thinking_budget=0 and HttpOptions.timeout.

This bypasses the documented socket-hang bug in google-generativeai
(https://github.com/googleapis/python-genai/issues/1893) which had no
working timeout mechanism.

Run:
    python scripts/04d_diarize_llm_v2.py [--workers N] [--chunk-words N]
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import frontmatter
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
SRC = ROOT / "data" / "1_canonical"
DST = ROOT / "data" / "2_diarized"

MODEL_NAME = "gemini-2.5-flash"

PROMPT_TEMPLATE = """Acest text este o bucată dintr-un transcript (poate continua de unde s-a oprit). Vorbitorul principal e **Nicușor Dan** (Președintele României, anterior primar București).

ETICHETEAZĂ FIECARE PARAGRAF cu cine vorbește:
- `[ND]` — Nicușor Dan vorbește el însuși (persoana I)
- `[ANCHOR]` — prezentator TV narând DESPRE el (persoana III)
- `[JURNALIST]` — pune o întrebare sau se prezintă cu nume+canal
- `[MODERATOR]` — moderator de eveniment / protocol
- `[OFICIAL: ROL]` — alt oficial cu nume/funcție
- `[UNKNOWN]` — fragment foarte scurt sau ambiguu

REGULI:
1. Persoana I (ND) vs persoana III (anchor despre el) — distinge ferm
2. Întrebări = JURNALIST/ANCHOR, NICIODATĂ ND
3. **OFICIAL cu NUME**: Dacă un anchor/jurnalist introduce un invitat prin nume ("Avem pe analistul X", "Bun găsit lui Y, ministrul Z"), folosește `[OFICIAL: Numele Lor]` pentru TOATE replicile lor ulterioare. NU folosi `[UNKNOWN]` dacă numele e disponibil în context.
4. `[UNKNOWN]` doar pentru: fragmente foarte scurte ambigue (1-3 cuvinte, exclamații crowd, sunete tehnice), NU pentru replici lungi unde poți deduce vorbitorul din context
5. Verbatim — păstrează textul EXACT, doar adaugă etichete
6. Format: fiecare paragraf începe cu eticheta + space + text. Separate prin newline gol.

TRANSCRIPT:
=============
{text}
=============

Returnează doar textul etichetat. Niciun preambul, comentariu sau cod block."""


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or "your-" in api_key:
        print("ERROR: GEMINI_API_KEY missing", file=sys.stderr)
        sys.exit(1)
    from google import genai
    from google.genai import types
    # 5 min HTTP timeout
    client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=300_000))
    return client, types


def chunk_text(text: str, chunk_words: int) -> list[str]:
    paras = re.split(r"\n\n+", text)
    chunks: list[str] = []
    current: list[str] = []
    current_words = 0
    for p in paras:
        wc = len(p.split())
        if current and current_words + wc > chunk_words:
            chunks.append("\n\n".join(current))
            current = []
            current_words = 0
        current.append(p)
        current_words += wc
    if current:
        chunks.append("\n\n".join(current))
    return chunks


def diarize_chunk(client, types, chunk: str, retries: int = 2) -> str | None:
    prompt = PROMPT_TEMPLATE.format(text=chunk)
    for attempt in range(retries + 1):
        try:
            # thinking_budget=0 disables Gemini's chain-of-thought entirely
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.1,
                    max_output_tokens=16384,
                    thinking_config=types.ThinkingConfig(thinking_budget=0),
                ),
            )
            return response.text.strip() if response.text else None
        except Exception as e:
            err_class = type(e).__name__
            if attempt < retries:
                delay = 10 if "ResourceExhausted" in err_class else 2 ** attempt
                time.sleep(delay)
            else:
                print(f"    final error: {err_class}: {str(e)[:120]}", file=sys.stderr)
                return None
    return None


def process_one(src: Path, client_pair, chunk_words: int) -> dict:
    client, types = client_pair
    rel = src.relative_to(SRC)
    dst = DST / rel
    post = frontmatter.load(src)
    content = post.content

    if dst.exists():
        dst_post = frontmatter.load(dst)
        if "LLM diarize" in str(dst_post.get("metoda", "")):
            return {"status": "skipped (already done)"}

    tip = str(post.get("tip", ""))
    if tip in ("facebook-post", "anunt-candidatura", "lansare-campanie",
               "discurs-victorie", "discurs-investitura", "mesaj-anul-nou",
               "mesaj-ziua-europei"):
        return {"status": "skipped (monologue)"}
    if "[SIMION]" in content or "[RUTTE]" in content or "[OFICIAL" in content:
        return {"status": "skipped (manual)"}
    if len(content.split()) < 100:
        return {"status": "skipped (too short)"}

    chunks = chunk_text(content, chunk_words)
    print(f"  → {rel.name[:60]} ({len(content.split())} → {len(chunks)} chunks)", file=sys.stderr)

    diarized_chunks: list[str] = []
    for i, chunk in enumerate(chunks, 1):
        t0 = time.time()
        result = diarize_chunk(client, types, chunk)
        elapsed = time.time() - t0
        if result is None:
            print(f"    chunk {i}/{len(chunks)} FAILED", file=sys.stderr)
            return {"status": "chunk-failed", "n_chunks": len(chunks), "failed_at": i}
        diarized_chunks.append(result)
        print(f"    chunk {i}/{len(chunks)} ✓ {elapsed:.1f}s", file=sys.stderr)

    merged = "\n\n".join(diarized_chunks)
    post.content = merged
    post["verificat"] = True
    post["metoda"] = f"LLM diarize v2 (new SDK, {MODEL_NAME}, thinking=0, {len(chunks)} chunks)"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(frontmatter.dumps(post))
    return {"status": "diarized", "n_chunks": len(chunks)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--chunk-words", type=int, default=3000)
    args = ap.parse_args()

    client_pair = get_client()

    candidates = []
    for f in SRC.rglob("*.md"):
        rel = f.relative_to(SRC)
        post = frontmatter.load(f)
        content = post.content
        tip = str(post.get("tip", ""))
        if tip in ("facebook-post", "anunt-candidatura", "lansare-campanie",
                   "discurs-victorie", "discurs-investitura", "mesaj-anul-nou",
                   "mesaj-ziua-europei"):
            continue
        if "[SIMION]" in content or "[RUTTE]" in content or "[OFICIAL" in content:
            continue
        if len(content.split()) < 100:
            continue
        dst = DST / rel
        if dst.exists():
            dpost = frontmatter.load(dst)
            if "LLM diarize" in str(dpost.get("metoda", "")):
                continue
        candidates.append(f)

    print(f"Candidates: {len(candidates)}", file=sys.stderr)
    stats = {}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(process_one, src, client_pair, args.chunk_words): src for src in candidates}
        for fut in as_completed(futures):
            try:
                r = fut.result()
            except Exception as e:
                r = {"status": "exception"}
                print(f"  exception: {e}", file=sys.stderr)
            stats[r["status"]] = stats.get(r["status"], 0) + 1
    wall = time.time() - t0
    print(f"\n=== Summary ({wall:.1f}s) ===", file=sys.stderr)
    for k, v in stats.items():
        print(f"  {k:<30} {v}", file=sys.stderr)


if __name__ == "__main__":
    main()
