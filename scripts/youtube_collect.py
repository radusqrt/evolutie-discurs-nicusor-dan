"""Collect Nicușor Dan transcripts from MULTIPLE YouTube channels.

Sources:
  1. Nicușor Dan personal/official channel (@NicusorDanRO)
  2. Administrația Prezidențială (official)
  3. Privesc.Eu România (event coverage)

Pipeline per video:
  - Get metadata (upload_date, title)
  - Skip if before 2024-12-01 (out of scope)
  - Skip if matches exclusion patterns (mayor era, USR era, Klaus Iohannis etc.)
  - Skip if already saved (dedupe by video_id)
  - Pull transcript via YouTubeTranscriptApi
  - Save as data/raw/youtube/<date>_<slug>.md with frontmatter

Run as:
    python scripts/youtube_collect.py [--limit N] [--source X]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
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

# Source channels
SOURCES = {
    "nicusor": {
        "name": "Nicușor Dan",
        "url": "https://www.youtube.com/channel/UCWro8GYVQD34hCLQjA_yz9w/videos",
        "page_limit": 500,
    },
    "prezident": {
        "name": "Administrația Prezidențială",
        "url": "https://www.youtube.com/channel/UC2pG2gHcDa2oaLOpxpmL07g/videos",
        "page_limit": 500,
    },
    "privesc": {
        "name": "Privesc.Eu România",
        "url": "https://www.youtube.com/channel/UCz8tvsWJxsuexe9_rU65ngQ/search?query=Nicușor+Dan",
        "page_limit": 300,
    },
}

# Title patterns we want (presidential + candidate)
KEEP_PATTERNS = [
    r"Nicu[șs]or Dan",
    r"Pre[sș]edintele Rom[âa]niei",
    r"pre[sș]edinte ales",
    r"candidatul .* la pre[sș]eden[țt]ie",
]
# Title patterns we want to EXCLUDE
SKIP_PATTERNS = [
    r"primarul (general |municipiului )?(municipiului Bucure[șs]ti|Capitalei|Bucure[șs]ti)",
    r"liderul Grupului parlamentar USR",
    r"pre[sș]edintele USR",
    r"pre[sș]edintele Uniunii Salva[țt]i Bucure[șs]tiul",
    r"Klaus Iohannis",
    r"Ilie Bolojan",  # PM, not ND
    r"Ion Iliescu",
    r"Traian Băsescu",
    r"Emil Constantinescu",
]


def slugify(text: str, max_len: int = 60) -> str:
    text = text.lower()
    text = re.sub(r"[Șș]", "s", text)
    text = re.sub(r"[Țț]", "t", text)
    text = re.sub(r"[ăâ]", "a", text)
    text = re.sub(r"[î]", "i", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:max_len].rstrip("-")


def list_videos(url: str, page_limit: int) -> list[tuple[str, str]]:
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--print", "%(id)s|%(title)s",
        "--playlist-end", str(page_limit),
        url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    items: list[tuple[str, str]] = []
    for line in proc.stdout.splitlines():
        if "|" not in line:
            continue
        vid, title = line.split("|", 1)
        items.append((vid.strip(), title.strip()))
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
    return out


def already_collected(video_id: str) -> bool:
    """Check if any existing .md file references this video_id."""
    pattern = video_id
    for f in OUT_DIR.glob("*.md"):
        if pattern in f.read_text(errors="ignore")[:500]:  # check just frontmatter
            return True
    return False


def get_video_meta(vid: str) -> dict | None:
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
        text = re.sub(r"\b(Yeah|um|uh|ah)\b", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s+", " ", text).strip()
        text = re.sub(r"(?<=[.!?])\s+(?=[A-ZĂÂÎȘȚ])", "\n\n", text)
        return text
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable):
        return None
    except Exception as e:
        print(f"  fetch_transcript({vid}) error: {e}", file=sys.stderr)
        return None


def _yaml_escape(s: str | None) -> str:
    if s is None:
        return '""'
    s = str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()
    return f'"{s}"'


def process_one(vid: str, title: str, source: str) -> str | None:
    if already_collected(vid):
        return None  # silent skip

    meta = get_video_meta(vid)
    if not meta:
        return None
    upload_date_raw = meta.get("upload_date", "")
    if not upload_date_raw or len(upload_date_raw) != 8:
        return None
    date = f"{upload_date_raw[:4]}-{upload_date_raw[4:6]}-{upload_date_raw[6:8]}"
    if date < "2024-12-01":
        return None

    text = fetch_transcript(vid)
    if not text or len(text) < 200:
        return None

    slug = slugify(title)
    out_path = OUT_DIR / f"{date}_{slug}.md"
    if out_path.exists():
        out_path = OUT_DIR / f"{date}_{slug}_{vid[:6]}.md"
        if out_path.exists():
            return None

    duration = meta.get("duration")
    view_count = meta.get("view_count")
    like_count = meta.get("like_count")
    description = (meta.get("description") or "")[:500]  # truncate long descriptions
    uploader = meta.get("uploader") or source
    upload_timestamp = meta.get("timestamp")  # Unix ts of exact upload time

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
metoda: youtube_transcript_api (captions automate RO)
nota: Transcript auto-generat din YouTube. Pot exista erori de transcriere. Conține doar vocea lui ND DACĂ video-ul e monolog; pentru conferințe/dezbateri trebuie diarizat.
---

{text}
"""
    out_path.write_text(frontmatter)
    return str(out_path.relative_to(ROOT))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="Max NEW videos to process")
    ap.add_argument("--source", choices=list(SOURCES.keys()) + ["all"], default="all")
    args = ap.parse_args()

    sources_to_run = list(SOURCES.keys()) if args.source == "all" else [args.source]

    all_filtered: list[tuple[str, str, str]] = []  # (vid, title, source)
    for src_key in sources_to_run:
        src = SOURCES[src_key]
        print(f"\n=== Source: {src['name']} ===", file=sys.stderr)
        raw = list_videos(src["url"], src["page_limit"])
        print(f"  raw: {len(raw)} videos", file=sys.stderr)
        filtered = filter_videos(raw)
        print(f"  filtered: {len(filtered)} match patterns", file=sys.stderr)
        for vid, title in filtered:
            all_filtered.append((vid, title, src["name"]))

    # Dedupe by video_id (some videos may appear in multiple sources)
    seen_ids = set()
    unique: list[tuple[str, str, str]] = []
    for vid, title, src in all_filtered:
        if vid in seen_ids:
            continue
        seen_ids.add(vid)
        unique.append((vid, title, src))
    print(f"\nUnique: {len(unique)} videos across all sources", file=sys.stderr)

    if args.limit:
        unique = unique[: args.limit]

    print(f"Processing {len(unique)} videos...\n", file=sys.stderr)
    saved = []
    skipped = 0
    failed = 0
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(process_one, vid, title, src): (vid, title, src)
                   for vid, title, src in unique}
        for i, fut in enumerate(as_completed(futures), 1):
            vid, title, src = futures[fut]
            try:
                result = fut.result()
            except Exception as e:
                result = None
                print(f"  [{i}/{len(unique)}] ERROR {vid}: {e}", file=sys.stderr)
            if result is None:
                skipped += 1
                if i % 20 == 0:
                    print(f"  [{i}/{len(unique)}] skipped (dup/old/no-transcript)", file=sys.stderr)
            else:
                saved.append(result)
                print(f"  [{i}/{len(unique)}] saved: {result}", file=sys.stderr)

    print(f"\n=== Summary ===", file=sys.stderr)
    print(f"  Saved (new): {len(saved)}", file=sys.stderr)
    print(f"  Skipped (already collected / before Dec 2024 / no transcript): {skipped}", file=sys.stderr)
    print(f"  Failed: {failed}", file=sys.stderr)


if __name__ == "__main__":
    main()
