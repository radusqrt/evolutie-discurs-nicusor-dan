"""LLM-based diarization (Gemini 2.5 Flash) — alternative to heuristic v3.

Pipeline: input data/1_canonical/ → output data/2_diarized/ (overwrites per-file).

Strategy: TRIMITEM LA LLM doar fișierele care arată multi-voce.
Detectăm asta euristic — orice fișier > 200 cuvinte care nu e tip facebook-post
sau monologue.

Prompt:
  - Cere etichete [ND], [JURNALIST], [ANCHOR], [MODERATOR], [OFICIAL: ROL]
  - Insistă pe distincția persoana I (ND) vs persoana III (anchor narrând)
  - Verbatim — fără re-formulare

Strategy iterativă (per user request):
  --limit 1   → 1 fișier (smoke test)
  --limit 10  → 10 fișiere (validare statistică)
  --limit 100 → 100 fișiere
  fără limit  → tot corpus-ul

Run:
    python scripts/04b_diarize_llm.py --limit 1 --file FILENAME
    python scripts/04b_diarize_llm.py --limit 10
    python scripts/04b_diarize_llm.py  # all multi-voice
"""
from __future__ import annotations

import argparse
import os
import random
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

MODEL_NAME = "gemini-2.5-flash"  # cheap, fast, multilingual

PROMPT_TEMPLATE = """Acest text este un transcript auto-generat YouTube cu mai mulți vorbitori. Sarcina ta: ETICHETEAZĂ FIECARE PARAGRAF cu cine vorbește.

Vorbitorul principal e **Nicușor Dan** (NĂSCUT 1969, Președintele României din mai 2025, anterior primar al Bucureștiului 2020-2025, fondator USR și Salvați Bucureștiul).

Etichete posibile:
- `[ND]` — Nicușor Dan vorbește el însuși (persoana I: "am spus", "consider", "voi face", "împreună")
- `[ANCHOR]` — prezentator TV sau anchor narrează DESPRE el (persoana III: "Președintele a declarat", "Nicușor Dan a spus că...")
- `[JURNALIST]` — pune o întrebare sau se prezintă cu nume+canal ("Bună ziua, Maria Popescu, Pro TV", "Domnule președinte, ...")
- `[MODERATOR]` — moderator de eveniment / protocol
- `[OFICIAL: ROL]` — alt oficial (ex. `[OFICIAL: Maia Sandu]`, `[OFICIAL: Mark Rutte]`)
- `[UNKNOWN]` — dacă nu poți decide

CRITERII CHEIE:
1. Distinge **persoana I** (ND însuși) vs **persoana III** (anchor narrând despre el)
2. Întrebări = JURNALIST/ANCHOR, NICIODATĂ ND (el răspunde, nu întreabă)
3. Citate pe care anchor le citește dintr-o declarație ND nu sunt vorbire ND — sunt [ANCHOR] citind
4. Verbatim — păstrează textul EXACT, nu re-formula, nu corecta gramatica, doar adaugă eticheta la început

Format output: fiecare paragraf începe cu eticheta, apoi un space, apoi textul original. Paragrafele se separă prin un singur newline gol.

Exemplu:
```
[ND] Am spus de mai multe ori că reforma e o prioritate.

[JURNALIST] Bună ziua, Maria Popescu, Antena 3. Domnule președinte, când se va face reforma?

[ND] În 6 luni vom avea primele rezultate.

[ANCHOR] Președintele a declarat că reforma justiției e prioritatea sa centrală.
```

NU adăuga comentarii, nu rezuma, nu adăuga preambul. Doar transcriptul etichetat, paragraf cu paragraf.

TRANSCRIPT DE ETICHETAT:
=============
{text}
=============

Returnează doar textul etichetat (fără triplebackticks, fără "Output:")."""


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or "your-" in api_key:
        print("ERROR: GEMINI_API_KEY missing in .env", file=sys.stderr)
        print("  Get key: https://aistudio.google.com/apikey", file=sys.stderr)
        sys.exit(1)
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)


def needs_llm_diarize(post, content: str) -> bool:
    """Decide if a file should go through LLM (vs already-handled by v3)."""
    tip = str(post.get("tip", ""))
    if tip in ("facebook-post", "anunt-candidatura", "lansare-campanie",
               "discurs-victorie", "discurs-investitura", "mesaj-anul-nou",
               "mesaj-ziua-europei"):
        return False  # already monologue
    # Already manually diarized (debate, joint conference)
    if "[SIMION]" in content or "[RUTTE]" in content or "[OFICIAL" in content:
        return False
    word_count = len(content.split())
    if word_count < 100:
        return False  # too short to bother
    return True


def diarize_with_llm(client, text: str, retries: int = 4) -> str | None:
    prompt = PROMPT_TEMPLATE.format(text=text)
    for attempt in range(retries + 1):
        try:
            response = client.generate_content(
                prompt,
                generation_config={"temperature": 0.1, "max_output_tokens": 65536},
                request_options={"timeout": 180},  # 3 min hard cap per call
            )
            return response.text.strip()
        except Exception as e:
            err_class = type(e).__name__
            err = f"{err_class}: {str(e)[:160]}"
            if attempt < retries:
                # Longer backoff for rate limit errors
                delay = 30 if "ResourceExhausted" in err_class or "429" in str(e) else 2 ** attempt
                print(f"    retry in {delay}s after error: {err}", file=sys.stderr)
                time.sleep(delay)
            else:
                print(f"    FINAL ERROR: {err}", file=sys.stderr)
                return None
    return None


def process_one(src: Path, client, dry_run: bool = False, force: bool = False) -> dict:
    rel = src.relative_to(SRC)
    dst = DST / rel
    post = frontmatter.load(src)
    content = post.content

    # Skip if already LLM-diarized (idempotent re-runs)
    if not force and dst.exists():
        dst_post = frontmatter.load(dst)
        if "LLM diarize" in str(dst_post.get("metoda", "")):
            return {"status": "skipped", "reason": "already LLM-diarized"}

    if not needs_llm_diarize(post, content):
        return {"status": "skipped", "reason": "monologue or short or already-tagged"}

    if dry_run:
        return {"status": "would-process", "words": len(content.split())}

    print(f"  → LLM: {rel} ({len(content.split())} words)", file=sys.stderr)
    t0 = time.time()
    diarized = diarize_with_llm(client, content)
    elapsed = time.time() - t0
    if not diarized:
        return {"status": "llm-error", "elapsed": elapsed}

    if len(diarized) < 0.5 * len(content):
        print(f"    ⚠️  output too short ({len(diarized)} vs input {len(content)})", file=sys.stderr)
        return {"status": "too-short", "elapsed": elapsed}

    post.content = diarized
    post["verificat"] = True
    post["metoda"] = f"LLM diarize ({MODEL_NAME})"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(frontmatter.dumps(post))
    return {"status": "diarized", "elapsed": elapsed, "out_words": len(diarized.split())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="Max files to process")
    ap.add_argument("--file", type=str, default=None, help="Specific file name (relative to data/1_canonical)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--workers", type=int, default=8,
                    help="Parallel workers (Gemini Flash paid tier allows 1000+ RPM)")
    args = ap.parse_args()

    client = get_client() if not args.dry_run else None

    if args.file:
        src = SRC / args.file if (SRC / args.file).exists() else None
        if not src:
            candidates = list(SRC.rglob(f"*{args.file}*"))
            if not candidates:
                print(f"File not found: {args.file}", file=sys.stderr)
                sys.exit(1)
            src = candidates[0]
        print(f"Processing single file: {src.relative_to(ROOT)}", file=sys.stderr)
        result = process_one(src, client, dry_run=args.dry_run)
        print(f"  status: {result['status']}", file=sys.stderr)
        return

    # All candidate files
    files = list(SRC.rglob("*.md"))
    # Filter to those that need LLM
    candidates = []
    for f in files:
        post = frontmatter.load(f)
        if needs_llm_diarize(post, post.content):
            candidates.append(f)

    print(f"Total candidates for LLM diarize: {len(candidates)}", file=sys.stderr)
    random.seed(args.seed)
    random.shuffle(candidates)
    if args.limit:
        candidates = candidates[: args.limit]
        print(f"Limited to first {args.limit} (random sample)", file=sys.stderr)

    stats = {"diarized": 0, "llm-error": 0, "too-short": 0, "skipped": 0, "would-process": 0}
    total_time = 0.0
    wall_t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(process_one, src, client, args.dry_run): src for src in candidates}
        for i, fut in enumerate(as_completed(futures), 1):
            try:
                result = fut.result()
            except Exception as e:
                result = {"status": "llm-error", "elapsed": 0}
                print(f"  [{i}] EXCEPTION: {e}", file=sys.stderr)
            stats[result["status"]] = stats.get(result["status"], 0) + 1
            if "elapsed" in result:
                total_time += result["elapsed"]
            if i % 10 == 0 and len(candidates) > 10:
                wall = time.time() - wall_t0
                rate = i / max(wall, 0.1)
                print(f"  [{i}/{len(candidates)}] stats: {stats}, ~{rate:.1f} req/s (wall)", file=sys.stderr)

    print(f"\n=== Summary ===", file=sys.stderr)
    for k, v in stats.items():
        print(f"  {k:<20} {v}", file=sys.stderr)
    if total_time > 0:
        print(f"  Total time: {total_time:.1f}s ({total_time/60:.1f} min)", file=sys.stderr)


if __name__ == "__main__":
    main()
