"""Scrape Facebook public page posts via Apify's facebook-pages-scraper actor.

Pașii:
  1. Sign up gratis la https://apify.com (primesc $5 credit lunar)
  2. Settings → Integrations → API token
  3. APIFY_TOKEN=apify_api_xxxxx în .env

Actor folosit: `apify/facebook-posts-scraper`
  - input: startUrls (list of FB page URLs) + resultsLimit
  - output: JSON cu posturi (text, time, url, reactions, comments_count, etc.)

Run as:
    python scripts/fb_apify_collect.py [--page nicusordan] [--limit 500]
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

OUT_DIR = ROOT / "data" / "raw" / "facebook"
OUT_DIR.mkdir(parents=True, exist_ok=True)

ACTOR_ID = "apify/facebook-posts-scraper"


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
    ap.add_argument("--page", default="nicusordan.bucuresti")
    ap.add_argument("--limit", type=int, default=500, help="Max posts to fetch")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    token = os.getenv("APIFY_TOKEN", "").strip()
    if not token or not token.startswith("apify_api"):
        print("ERROR: APIFY_TOKEN missing in .env")
        print("  1. Sign up: https://apify.com/sign-up")
        print("  2. Get token: https://console.apify.com/settings/integrations")
        print("  3. Add to .env: APIFY_TOKEN=apify_api_xxxxx")
        sys.exit(1)

    from apify_client import ApifyClient
    client = ApifyClient(token)

    print(f"Calling Apify actor {ACTOR_ID}...", file=sys.stderr)
    run_input = {
        "startUrls": [{"url": f"https://www.facebook.com/{args.page}/"}],
        "resultsLimit": args.limit,
    }
    print(f"Input: {run_input}", file=sys.stderr)

    if args.dry_run:
        print("DRY RUN — not calling Apify.", file=sys.stderr)
        return

    run = client.actor(ACTOR_ID).call(run_input=run_input)
    print(f"Run completed. Status: {run['status']}", file=sys.stderr)
    dataset = client.dataset(run["defaultDatasetId"])
    items = list(dataset.iterate_items())
    print(f"Retrieved {len(items)} posts", file=sys.stderr)

    from datetime import datetime
    saved = 0
    skipped_short = 0
    skipped_nodate = 0
    skipped_error = 0
    for item in items:
        if item.get("error"):
            skipped_error += 1
            continue
        text = (item.get("text") or "").strip()
        if not text or len(text) < 30:
            skipped_short += 1
            continue

        # Date — Apify schema returns 'timestamp' (Unix sec) and 'time' (ISO string)
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

        post_url = item.get("url") or item.get("facebookUrl") or f"https://www.facebook.com/{args.page}"
        likes = item.get("likes") or item.get("topReactionsCount")
        comments = item.get("comments")
        shares = item.get("shares")

        title_excerpt = text[:80].replace("\n", " ").strip()
        slug = slugify(title_excerpt)
        out_path = OUT_DIR / f"{date}_{slug}.md"
        if out_path.exists():
            out_path = OUT_DIR / f"{date}_{slug}_{saved}.md"

        frontmatter = f"""---
data: {date}
tip: facebook-post
sursa: {_yaml_escape(post_url)}
sursa_canal: "Facebook (pagina {args.page})"
sursa_titlu: {_yaml_escape(title_excerpt)}
sursa_aprecieri: {likes if likes is not None else 'null'}
sursa_comentarii: {comments if comments is not None else 'null'}
sursa_distribuiri: {shares if shares is not None else 'null'}
vorbitor: nicusor_dan
verificat: true
metoda: apify scrape ({ACTOR_ID})
nota: Postare Facebook, text plain (fără imagini sau reacții individuale).
---

{text}
"""
        out_path.write_text(frontmatter)
        saved += 1

    print(f"\n=== Summary ===")
    print(f"  Saved: {saved}")
    print(f"  Skipped (too short): {skipped_short}")
    print(f"  Skipped (no date): {skipped_nodate}")
    print(f"  Skipped (error from Apify): {skipped_error}")
    print(f"  Output: {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
