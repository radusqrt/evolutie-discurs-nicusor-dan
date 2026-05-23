"""Pull existing Apify dataset to local FB posts dir.

Usage:
    python scripts/fb_pull_dataset.py [--run-id RUN_ID]

If --run-id is omitted, uses the latest run on the facebook-posts-scraper actor.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
OUT_DIR = ROOT / "data" / "raw" / "facebook"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def slugify(text: str, max_len: int = 60) -> str:
    text = text.lower()
    text = re.sub(r"[șş]", "s", text)
    text = re.sub(r"[țţ]", "t", text)
    text = re.sub(r"[ăâ]", "a", text)
    text = re.sub(r"[î]", "i", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:max_len].rstrip("-")


def _yaml_escape(s: str | None) -> str:
    if s is None:
        return '""'
    s = str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()
    return f'"{s}"'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", default=None)
    args = ap.parse_args()

    from apify_client import ApifyClient
    client = ApifyClient(os.getenv("APIFY_TOKEN"))

    if args.run_id:
        run = client.run(args.run_id).get()
    else:
        runs = client.actor("apify/facebook-posts-scraper").runs().list(limit=10, desc=True)
        # Pick latest non-aborted run with items
        run = None
        for r in runs.items:
            if r.get("status") in ("SUCCEEDED", "RUNNING") and r.get("defaultDatasetId"):
                info = client.dataset(r["defaultDatasetId"]).get()
                if info.get("itemCount", 0) > 5:
                    run = r
                    break
        if not run:
            print("No suitable run found")
            sys.exit(1)

    print(f"Using run: {run['id']}, status={run['status']}", file=sys.stderr)
    ds = client.dataset(run["defaultDatasetId"])
    info = ds.get()
    print(f"Dataset has {info.get('itemCount', 0)} items", file=sys.stderr)

    saved = 0
    skipped_short = 0
    skipped_nodate = 0
    skipped_error = 0
    saved_dates = []

    for item in ds.iterate_items():
        if item.get("error"):
            skipped_error += 1
            continue
        text = (item.get("text") or "").strip()
        if not text or len(text) < 30:
            skipped_short += 1
            continue

        date = "unknown"
        ts = item.get("timestamp")
        if isinstance(ts, (int, float)) and ts > 1000000000:
            date = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")
        elif isinstance(item.get("time"), str):
            t = item["time"]
            m = re.match(r"(\d{4}-\d{2}-\d{2})", t)
            if m:
                date = m.group(1)
        if date == "unknown":
            skipped_nodate += 1
            continue

        post_url = item.get("url") or item.get("facebookUrl") or "https://www.facebook.com/NicusorDan.ro"
        likes = item.get("likes") or item.get("topReactionsCount")
        comments = item.get("comments")
        shares = item.get("shares")
        post_id = item.get("postId", "")

        title_excerpt = text[:80].replace("\n", " ").strip()
        slug = slugify(title_excerpt)
        out_path = OUT_DIR / f"{date}_{slug}.md"
        if out_path.exists():
            # use postId for disambiguation if available, else counter
            suffix = post_id[-6:] if post_id else str(saved)
            out_path = OUT_DIR / f"{date}_{slug}_{suffix}.md"
            if out_path.exists():
                continue  # truly duplicate

        frontmatter = f"""---
data: {date}
tip: facebook-post
sursa: {_yaml_escape(post_url)}
sursa_canal: "Facebook (NicusorDan.ro)"
sursa_post_id: {_yaml_escape(post_id)}
sursa_titlu: {_yaml_escape(title_excerpt)}
sursa_aprecieri: {likes if likes is not None else 'null'}
sursa_comentarii: {comments if comments is not None else 'null'}
sursa_distribuiri: {shares if shares is not None else 'null'}
vorbitor: nicusor_dan
verificat: true
metoda: apify scrape (apify/facebook-posts-scraper)
nota: Postare Facebook publică, text plain (fără imagini sau reacții individuale).
---

{text}
"""
        out_path.write_text(frontmatter)
        saved += 1
        saved_dates.append(date)

    print(f"\n=== Summary ===")
    print(f"  Saved: {saved}")
    print(f"  Skipped (too short): {skipped_short}")
    print(f"  Skipped (no date): {skipped_nodate}")
    print(f"  Skipped (error): {skipped_error}")
    if saved_dates:
        print(f"  Date range: {min(saved_dates)} → {max(saved_dates)}")


if __name__ == "__main__":
    main()
