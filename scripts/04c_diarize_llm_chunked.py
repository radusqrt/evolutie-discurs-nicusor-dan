"""Chunked LLM diarize for files too long to process in a single call.

Reads files from data/1_canonical/ that DON'T have LLM diarize tag yet in
data/2_diarized/. Splits each into chunks of ~CHUNK_WORDS, diarizes each
chunk independently, concatenates results.

Run:
    python scripts/04c_diarize_llm_chunked.py [--workers N] [--chunk-words N]
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
CHUNK_WORDS_DEFAULT = 4000

# Same prompt as 04b — but adds note for chunked context
PROMPT_TEMPLATE = """Acest text este o BUCATĂ dintr-un transcript mai mare (continuă de unde s-a oprit segmentul anterior). Vorbitorul principal e **Nicușor Dan** (Președintele României din mai 2025, anterior primar București).

ETICHETEAZĂ FIECARE PARAGRAF cu cine vorbește:
- `[ND]` — Nicușor Dan vorbește el însuși (persoana I: "am spus", "consider")
- `[ANCHOR]` — prezentator TV narând DESPRE el (persoana III)
- `[JURNALIST]` — pune o întrebare sau se prezintă cu nume+canal
- `[MODERATOR]` — moderator de eveniment / protocol
- `[OFICIAL: ROL]` — alt oficial (ex. `[OFICIAL: Maia Sandu]`)
- `[UNKNOWN]` — dacă nu poți decide

REGULI:
1. Persoana I (ND însuși) vs persoana III (anchor narrând despre el) — distinge ferm
2. Întrebări = NICIODATĂ ND (el răspunde, nu întreabă)
3. Citate pe care anchor le citește dintr-o declarație ND = [ANCHOR] citind, NU [ND]
4. Verbatim — păstrează textul EXACT
5. Această bucată poate începe în mijlocul unei replici — etichetează coerent cu contextul aparent

Format: fiecare paragraf începe cu eticheta, apoi space, apoi text. Paragrafele separate de newline gol.

TRANSCRIPT (bucată):
=============
{text}
=============

Returnează doar textul etichetat."""


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or "your-" in api_key:
        print("ERROR: GEMINI_API_KEY missing in .env", file=sys.stderr)
        sys.exit(1)
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)


def chunk_text(text: str, chunk_words: int) -> list[str]:
    """Split text into chunks of ~chunk_words, on paragraph boundaries."""
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


def diarize_chunk(client, chunk: str, retries: int = 3) -> str | None:
    """Wraps Gemini call in an outer ThreadPoolExecutor timeout to bypass
    the documented socket-level hang in google-generativeai SDK
    (https://github.com/googleapis/python-genai/issues/1893)."""
    from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeout
    prompt = PROMPT_TEMPLATE.format(text=chunk)

    def _call():
        return client.generate_content(
            prompt,
            generation_config={
                "temperature": 0.1,
                "max_output_tokens": 16384,
            },
        )

    for attempt in range(retries + 1):
        with ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(_call)
            try:
                response = future.result(timeout=90)
                return response.text.strip()
            except FutureTimeout:
                future.cancel()
                if attempt < retries:
                    time.sleep(2)
                    continue
                print(f"    final timeout after {retries+1} attempts", file=sys.stderr)
                return None
            except Exception as e:
                err_class = type(e).__name__
                if attempt < retries:
                    delay = 15 if "ResourceExhausted" in err_class else 3 ** attempt
                    time.sleep(delay)
                else:
                    print(f"    final error: {err_class}: {str(e)[:120]}", file=sys.stderr)
                    return None
    return None


def process_one(src: Path, client, chunk_words: int) -> dict:
    rel = src.relative_to(SRC)
    dst = DST / rel
    post = frontmatter.load(src)
    content = post.content

    # Skip if already LLM-diarized
    if dst.exists():
        dst_post = frontmatter.load(dst)
        if "LLM diarize" in str(dst_post.get("metoda", "")):
            return {"status": "skipped (already done)"}

    # Skip non-candidates
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
    print(f"  → {rel.name[:60]} ({len(content.split())} words → {len(chunks)} chunks)", file=sys.stderr)

    diarized_chunks: list[str] = []
    for i, chunk in enumerate(chunks, 1):
        t0 = time.time()
        result = diarize_chunk(client, chunk)
        elapsed = time.time() - t0
        if result is None:
            print(f"    chunk {i}/{len(chunks)} FAILED after retries", file=sys.stderr)
            return {"status": "chunk-failed", "n_chunks": len(chunks), "failed_at": i}
        diarized_chunks.append(result)
        print(f"    chunk {i}/{len(chunks)} ✓ ({len(chunk.split())} → {len(result.split())} words, {elapsed:.1f}s)", file=sys.stderr)

    merged = "\n\n".join(diarized_chunks)
    post.content = merged
    post["verificat"] = True
    post["metoda"] = f"LLM diarize chunked ({MODEL_NAME}, {len(chunks)} chunks)"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(frontmatter.dumps(post))
    return {"status": "diarized", "n_chunks": len(chunks)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--chunk-words", type=int, default=CHUNK_WORDS_DEFAULT)
    args = ap.parse_args()

    client = get_client()

    # Find candidate files (those missing from 2_diarized with LLM tag)
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

    print(f"Candidates for chunked LLM diarize: {len(candidates)}", file=sys.stderr)
    if not candidates:
        return

    stats = {}
    wall_t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(process_one, src, client, args.chunk_words): src for src in candidates}
        for fut in as_completed(futures):
            try:
                result = fut.result()
            except Exception as e:
                result = {"status": "exception"}
                print(f"  exception: {e}", file=sys.stderr)
            stats[result["status"]] = stats.get(result["status"], 0) + 1

    wall = time.time() - wall_t0
    print(f"\n=== Summary ({wall:.1f}s wall) ===", file=sys.stderr)
    for k, v in stats.items():
        print(f"  {k:<30} {v}", file=sys.stderr)


if __name__ == "__main__":
    main()
