"""Fetch transcripts for the strict-filtered candidate list (data/index/youtube_candidates.json).

Uses Webshare proxy. Saves to data/raw/youtube/.
Skips already-collected videos.

Run as:
    python scripts/fetch_from_candidates.py [--limit N] [--start IDX]
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from proxy import get_proxy_for_yt_dlp, get_proxy_for_transcript_api

ROOT = Path(__file__).resolve().parent.parent
INDEX_FILE = ROOT / "data" / "index" / "youtube_candidates.json"
OUT_DIR = ROOT / "data" / "raw" / "youtube"


def slugify(text: str, max_len: int = 60) -> str:
    text = text.lower()
    text = re.sub(r"[Șș]", "s", text)
    text = re.sub(r"[Țț]", "t", text)
    text = re.sub(r"[ăâ]", "a", text)
    text = re.sub(r"[î]", "i", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:max_len].rstrip("-")


def _yaml_escape(s: str | None) -> str:
    if s is None:
        return '""'
    s = str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()
    return f'"{s}"'


def get_video_meta(vid: str) -> dict | None:
    cmd = ["yt-dlp", "--dump-json", "--skip-download"]
    proxy = get_proxy_for_yt_dlp()
    if proxy:
        cmd += ["--proxy", proxy]
    cmd.append(f"https://www.youtube.com/watch?v={vid}")
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if proc.returncode != 0:
            return None
        return json.loads(proc.stdout)
    except Exception:
        return None


def fetch_transcript(vid: str) -> str | None:
    proxy_cfg = get_proxy_for_transcript_api()
    api = YouTubeTranscriptApi(proxy_config=proxy_cfg) if proxy_cfg else YouTubeTranscriptApi()
    try:
        transcript = api.fetch(vid, languages=["ro", "ro-RO"])
        text = " ".join(s.text for s in transcript)
        text = re.sub(r"\b(Yeah|um|uh|ah)\b", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s+", " ", text).strip()
        text = re.sub(r"(?<=[.!?])\s+(?=[A-ZĂÂÎȘȚ])", "\n\n", text)
        return text
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable):
        return None
    except Exception as e:
        msg = str(e)[:120]
        print(f"  fetch_transcript({vid}) error: {msg}", file=sys.stderr)
        return None


def process_one(candidate: dict) -> str:
    vid = candidate["video_id"]
    title = candidate["title"]
    source = candidate["channel"]

    if candidate.get("already_collected"):
        return "ALREADY"

    meta = get_video_meta(vid)
    if not meta:
        return "META-FAIL"
    upload_date_raw = meta.get("upload_date", "")
    if not upload_date_raw or len(upload_date_raw) != 8:
        return "BAD-DATE"
    date = f"{upload_date_raw[:4]}-{upload_date_raw[4:6]}-{upload_date_raw[6:8]}"
    if date < "2024-12-01":
        return "TOO-OLD"

    text = fetch_transcript(vid)
    if not text or len(text) < 200:
        return "NO-TRANSCRIPT"

    slug = slugify(title)
    out_path = OUT_DIR / f"{date}_{slug}.md"
    if out_path.exists():
        out_path = OUT_DIR / f"{date}_{slug}_{vid[:6]}.md"
        if out_path.exists():
            return "DUPLICATE-NAME"

    duration = meta.get("duration")
    view_count = meta.get("view_count")
    like_count = meta.get("like_count")
    description = (meta.get("description") or "")[:500]
    uploader = meta.get("uploader") or source
    upload_timestamp = meta.get("timestamp")

    frontmatter = f"""---
data: {date}
tip: video-transcript
sursa: https://www.youtube.com/watch?v={vid}
sursa_video_id: {vid}
sursa_canal: {_yaml_escape(uploader)}
sursa_canal_filter: {_yaml_escape(source)}
sursa_titlu: {_yaml_escape(title)}
sursa_durata_secunde: {duration if duration is not None else 'null'}
sursa_vizionari: {view_count if view_count is not None else 'null'}
sursa_aprecieri: {like_count if like_count is not None else 'null'}
sursa_descriere: {_yaml_escape(description)}
sursa_upload_timestamp: {upload_timestamp if upload_timestamp is not None else 'null'}
vorbitor: nicusor_dan
verificat: false
metoda: youtube_transcript_api (captions automate RO via Webshare proxy)
nota: Transcript auto-generat din YouTube. Conține doar vocea lui ND DACĂ video-ul e monolog; pentru conferințe/dezbateri trebuie diarizat.
---

{text}
"""
    out_path.write_text(frontmatter)
    return f"SAVED:{out_path.name}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="Max NEW videos to fetch")
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    candidates = json.loads(INDEX_FILE.read_text())
    todo = [c for c in candidates if not c.get("already_collected")]
    todo = todo[args.start:]
    if args.limit:
        todo = todo[: args.limit]

    print(f"Processing {len(todo)} candidates with {args.workers} workers...", file=sys.stderr)
    stats: dict[str, int] = {}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(process_one, c): c for c in todo}
        for i, fut in enumerate(as_completed(futures), 1):
            c = futures[fut]
            try:
                result = fut.result()
            except Exception as e:
                result = f"EXCEPTION:{type(e).__name__}"
            tag = result.split(":")[0]
            stats[tag] = stats.get(tag, 0) + 1
            if result.startswith("SAVED"):
                print(f"  [{i}/{len(todo)}] {result}", file=sys.stderr)
            if i % 25 == 0:
                rate = i / (time.time() - t0)
                print(f"  [{i}/{len(todo)}] {rate:.1f} req/s | stats: {stats}", file=sys.stderr)

    print(f"\n=== Summary ===", file=sys.stderr)
    for tag, n in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {tag:<20} {n}", file=sys.stderr)


if __name__ == "__main__":
    main()
