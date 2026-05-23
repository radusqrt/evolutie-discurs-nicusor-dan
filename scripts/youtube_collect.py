"""Collect Nicușor Dan speech transcripts from YouTube (via Privesc.Eu channel).

Pipeline:
  1. Search Privesc.Eu channel for "Nicușor Dan" → list of (video_id, title)
  2. Filter to presidential period (titles starting with "Președintele" or campaign keywords)
  3. For each video: pull upload_date + transcript via YouTubeTranscriptApi
  4. Save as data/raw/youtube/<date>_<slug>.md with proper frontmatter

Run as:
    python scripts/youtube_collect.py [--limit N]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "data" / "raw" / "youtube"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PRIVESC_CHANNEL = "UCz8tvsWJxsuexe9_rU65ngQ"
SEARCH_URL = f"https://www.youtube.com/channel/{PRIVESC_CHANNEL}/search?query=Nicu%C8%99or+Dan"

# Title patterns we want (presidential + campaign period)
KEEP_PATTERNS = [
    r"Pre[sș]edintele Rom[âa]niei",
    r"candidatul .* Nicu[șs]or Dan",  # campaign appearances
    r"declara[țt]ia .* Nicu[șs]or Dan",
    r"discurs .* Nicu[șs]or Dan",
    r"conferin[țt][aă] .* Nicu[șs]or Dan",
    r"Mesajul .* Nicu[șs]or Dan",
    r"alocu[țt]iunea .* Nicu[șs]or Dan",
]
# Title patterns we want to EXCLUDE (mayoralty, USR group leader, etc.)
SKIP_PATTERNS = [
    r"primarul general",
    r"liderul Grupului parlamentar USR",
    r"pre[sș]edintele USR",
    r"pre[sș]edintele Uniunii Salva[țt]i Bucure[șs]tiul",
]


def slugify(text: str, max_len: int = 60) -> str:
    text = text.lower()
    text = re.sub(r"[Șș]", "s", text)  # Ș/ș
    text = re.sub(r"[Țț]", "t", text)  # Ț/ț
    text = re.sub(r"[ăâ]", "a", text)
    text = re.sub(r"[î]", "i", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:max_len].rstrip("-")


def list_videos(max_pages: int = 5) -> list[tuple[str, str]]:
    """Use yt-dlp to list videos from Privesc.Eu channel search."""
    print(f"Listing videos from Privesc.Eu search...", file=sys.stderr)
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--print", "%(id)s|%(title)s",
        "--playlist-end", str(max_pages * 30),
        SEARCH_URL,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    items: list[tuple[str, str]] = []
    for line in proc.stdout.splitlines():
        if "|" not in line:
            continue
        vid, title = line.split("|", 1)
        items.append((vid.strip(), title.strip()))
    print(f"  raw: {len(items)} videos", file=sys.stderr)
    return items


def filter_videos(items: list[tuple[str, str]]) -> list[tuple[str, str]]:
    keep_re = re.compile("|".join(KEEP_PATTERNS), re.IGNORECASE)
    skip_re = re.compile("|".join(SKIP_PATTERNS), re.IGNORECASE)
    out: list[tuple[str, str]] = []
    for vid, title in items:
        if skip_re.search(title):
            continue
        if keep_re.search(title):
            out.append((vid, title))
    print(f"  filtered: {len(out)} videos match presidency/campaign patterns", file=sys.stderr)
    return out


def get_video_meta(vid: str) -> dict | None:
    """yt-dlp dump of metadata. Returns dict with id, title, upload_date, channel."""
    cmd = ["yt-dlp", "--dump-json", "--skip-download", f"https://www.youtube.com/watch?v={vid}"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if proc.returncode != 0:
            return None
        return json.loads(proc.stdout)
    except Exception:
        return None


def fetch_transcript(vid: str) -> str | None:
    api = YouTubeTranscriptApi()
    try:
        transcript = api.fetch(vid, languages=["ro", "ro-RO"])
        text = " ".join(s.text for s in transcript)
        # Clean common artifacts
        text = re.sub(r"\b(Yeah|um|uh|ah)\b", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s+", " ", text).strip()
        # Sentence-ish line breaks
        text = re.sub(r"(?<=[.!?])\s+(?=[A-ZĂÂÎȘȚ])", "\n\n", text)
        return text
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable):
        return None
    except Exception as e:
        print(f"  fetch_transcript({vid}) error: {e}", file=sys.stderr)
        return None


def process_one(vid: str, title: str) -> str | None:
    """Get metadata, transcript, save .md. Return relative path or None."""
    meta = get_video_meta(vid)
    if not meta:
        return None
    upload_date_raw = meta.get("upload_date", "")  # YYYYMMDD
    if not upload_date_raw or len(upload_date_raw) != 8:
        return None
    date = f"{upload_date_raw[:4]}-{upload_date_raw[4:6]}-{upload_date_raw[6:8]}"
    # Only keep videos from Dec 2024 onward
    if date < "2024-12-01":
        return None

    text = fetch_transcript(vid)
    if not text or len(text) < 200:
        return None

    slug = slugify(title)
    out_path = OUT_DIR / f"{date}_{slug}.md"
    if out_path.exists():
        return f"SKIP (exists): {out_path.name}"

    frontmatter = f"""---
data: {date}
tip: video-transcript
sursa: https://www.youtube.com/watch?v={vid}
canal: Privesc.Eu România
titlu_video: {title}
vorbitor: nicusor_dan
verificat: false
metoda: youtube_transcript_api (captions automate RO)
nota: Transcript auto-generat din YouTube. Pot exista erori de transcriere; pentru analiză precisă trebuie revizuit manual. Conține doar vocea lui ND DACĂ video-ul e monolog; pentru conferințe de presă cu jurnaliști sau dezbateri, transcriptul include și alte voci (de etichetat ulterior).
---

{text}
"""
    out_path.write_text(frontmatter)
    return str(out_path.relative_to(ROOT))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="Max videos to process")
    ap.add_argument("--max-pages", type=int, default=5, help="yt-dlp pagination depth")
    args = ap.parse_args()

    raw = list_videos(max_pages=args.max_pages)
    filtered = filter_videos(raw)
    if args.limit:
        filtered = filtered[: args.limit]

    print(f"\nProcessing {len(filtered)} videos...", file=sys.stderr)
    saved = []
    skipped = 0
    failed = 0
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(process_one, vid, title): (vid, title) for vid, title in filtered}
        for i, fut in enumerate(as_completed(futures), 1):
            vid, title = futures[fut]
            try:
                result = fut.result()
            except Exception as e:
                result = None
                print(f"  [{i}/{len(filtered)}] ERROR {vid}: {e}", file=sys.stderr)
            if result and result.startswith("SKIP"):
                skipped += 1
                print(f"  [{i}/{len(filtered)}] {result}", file=sys.stderr)
            elif result:
                saved.append(result)
                print(f"  [{i}/{len(filtered)}] saved: {result}", file=sys.stderr)
            else:
                failed += 1
                print(f"  [{i}/{len(filtered)}] FAILED: {vid} | {title[:70]}", file=sys.stderr)

    print(f"\n=== Summary ===", file=sys.stderr)
    print(f"  Saved: {len(saved)}", file=sys.stderr)
    print(f"  Skipped (exists): {skipped}", file=sys.stderr)
    print(f"  Failed (no transcript / no metadata / too short / too old): {failed}", file=sys.stderr)


if __name__ == "__main__":
    main()
