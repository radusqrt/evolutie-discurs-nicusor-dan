"""Backfill rich source metadata on existing YouTube .md files.

For each .md in data/raw/youtube/ with a youtube.com URL in `sursa`, fetches
yt-dlp metadata and adds: sursa_video_id, sursa_canal, sursa_durata_secunde,
sursa_vizionari, sursa_aprecieri, sursa_descriere, sursa_upload_timestamp.

Preserves existing content and other frontmatter fields. Idempotent.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
YT_DIR = ROOT / "data" / "raw" / "youtube"


def video_id_from_url(url: str) -> str | None:
    m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", str(url))
    return m.group(1) if m else None


sys.path.insert(0, str(Path(__file__).resolve().parent))
from proxy import get_proxy_for_yt_dlp


def get_meta(vid: str) -> dict | None:
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


def enrich(md_path: Path) -> str:
    post = frontmatter.load(md_path)
    sursa = str(post.get("sursa", ""))
    vid = video_id_from_url(sursa)
    if not vid:
        return "no-video-id"

    # Skip if already enriched
    if post.get("sursa_video_id"):
        return "already-enriched"

    meta = get_meta(vid)
    if not meta:
        return "yt-dlp-failed"

    post["sursa_video_id"] = vid
    post["sursa_canal"] = meta.get("uploader") or post.get("canal", "")
    post["sursa_titlu"] = meta.get("title") or post.get("titlu_video", "")
    if meta.get("duration") is not None:
        post["sursa_durata_secunde"] = int(meta["duration"])
    if meta.get("view_count") is not None:
        post["sursa_vizionari"] = int(meta["view_count"])
    if meta.get("like_count") is not None:
        post["sursa_aprecieri"] = int(meta["like_count"])
    descr = (meta.get("description") or "")[:500]
    if descr:
        post["sursa_descriere"] = descr.replace("\n", " ").strip()
    if meta.get("timestamp") is not None:
        post["sursa_upload_timestamp"] = int(meta["timestamp"])

    md_path.write_text(frontmatter.dumps(post))
    return "enriched"


def main():
    files = sorted(YT_DIR.glob("*.md"))
    print(f"Enriching {len(files)} files...\n", file=sys.stderr)
    stats = {"enriched": 0, "already-enriched": 0, "yt-dlp-failed": 0, "no-video-id": 0}
    for f in files:
        result = enrich(f)
        stats[result] += 1
        if result == "enriched":
            print(f"  + {f.name}", file=sys.stderr)
        elif result == "yt-dlp-failed":
            print(f"  X {f.name}", file=sys.stderr)
    print(f"\nDone: {stats}", file=sys.stderr)


if __name__ == "__main__":
    main()
