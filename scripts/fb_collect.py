"""Scrape Facebook public posts from a logged-in session.

Requires data/.fb_state.json (from fb_login.py).
Loads page, scrolls, extracts visible posts with timestamps, saves each
as data/raw/facebook/<date>_<slug>.md with proper frontmatter.

Run as:
    python scripts/fb_collect.py [--page nicusordan] [--scrolls 20]
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "data" / ".fb_state.json"
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


def parse_relative_date(raw: str, now=None) -> str | None:
    """Parse FB relative date like '3 ore', 'ieri', '15 mai' → YYYY-MM-DD."""
    from datetime import datetime, timedelta
    now = now or datetime.now()
    raw = raw.lower().strip()

    # Already absolute (e.g., "15 ianuarie 2025")
    months = {
        "ianuarie": 1, "februarie": 2, "martie": 3, "aprilie": 4, "mai": 5, "iunie": 6,
        "iulie": 7, "august": 8, "septembrie": 9, "octombrie": 10, "noiembrie": 11, "decembrie": 12,
    }
    m = re.match(r"(\d{1,2})\s+(\w+)\s*(\d{4})?", raw)
    if m and m.group(2) in months:
        day = int(m.group(1))
        month = months[m.group(2)]
        year = int(m.group(3)) if m.group(3) else now.year
        try:
            return f"{year}-{month:02d}-{day:02d}"
        except Exception:
            return None

    # Relative
    if "ieri" in raw or "yesterday" in raw:
        return (now - timedelta(days=1)).strftime("%Y-%m-%d")
    if any(w in raw for w in ["acum câteva minute", "few minutes", "now"]):
        return now.strftime("%Y-%m-%d")
    m = re.match(r"(\d+)\s*(or[ăe]|h|hour|min|day|zi)", raw)
    if m:
        n = int(m.group(1))
        unit = m.group(2)
        if "or" in unit or "h" in unit:
            return (now - timedelta(hours=n)).strftime("%Y-%m-%d")
        if "min" in unit:
            return now.strftime("%Y-%m-%d")
        if "day" in unit or "zi" in unit:
            return (now - timedelta(days=n)).strftime("%Y-%m-%d")

    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", default="nicusordan")
    ap.add_argument("--scrolls", type=int, default=30)
    ap.add_argument("--headless", action="store_true", default=True)
    ap.add_argument("--headed", action="store_true")
    args = ap.parse_args()

    if not STATE_FILE.exists():
        print(f"ERROR: {STATE_FILE.relative_to(ROOT)} doesn't exist.")
        print(f"Run first: python scripts/fb_login.py")
        sys.exit(1)

    from playwright.sync_api import sync_playwright

    headless = not args.headed
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        ctx = browser.new_context(storage_state=str(STATE_FILE))
        page = ctx.new_page()
        url = f"https://www.facebook.com/{args.page}"
        print(f"Navigating to {url}...", file=sys.stderr)
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(5000)

        # Scroll to load more posts
        print(f"Scrolling {args.scrolls} times...", file=sys.stderr)
        for i in range(args.scrolls):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(2000)
            if i % 5 == 4:
                print(f"  scroll {i+1}/{args.scrolls}", file=sys.stderr)

        # Extract posts via JS
        posts = page.evaluate("""
            () => {
                const articles = document.querySelectorAll('div[role="article"]');
                const out = [];
                articles.forEach(a => {
                    const tEl = a.querySelector('[role="link"] > span, a[aria-label]');
                    const time = tEl?.getAttribute('aria-label') || tEl?.innerText || '';
                    // Extract text content
                    const text = a.innerText.substring(0, 5000);
                    // Try to get post URL
                    const link = a.querySelector('a[href*="/posts/"], a[href*="/permalink"]');
                    const url = link?.href || '';
                    out.push({ time, text, url });
                });
                return out;
            }
        """)
        print(f"Extracted {len(posts)} raw posts", file=sys.stderr)
        browser.close()

    # Save each
    saved = 0
    skipped = 0
    for p in posts:
        text = p["text"].strip()
        if len(text) < 50:
            skipped += 1
            continue
        date = parse_relative_date(p["time"]) or "unknown"
        if date == "unknown":
            # Fall back: skip undated posts
            skipped += 1
            continue
        title_excerpt = text[:60].replace("\n", " ")
        slug = slugify(title_excerpt)
        out_path = OUT_DIR / f"{date}_{slug}.md"
        if out_path.exists():
            out_path = OUT_DIR / f"{date}_{slug}_{saved}.md"

        frontmatter = f"""---
data: {date}
tip: facebook-post
sursa: {_yaml_escape(p['url'] or f'https://www.facebook.com/{args.page}')}
sursa_canal: "Facebook (pagina nicusordan)"
sursa_titlu: {_yaml_escape(title_excerpt)}
sursa_data_relativa: {_yaml_escape(p['time'])}
vorbitor: nicusor_dan
verificat: true
metoda: playwright scrape de pe pagina publică FB (sesiune logată)
nota: Postare Facebook scrapată ca text plain (fără imagini sau metadate de reacții).
---

{text}
"""
        out_path.write_text(frontmatter)
        saved += 1

    print(f"\nSaved: {saved} | Skipped: {skipped}", file=sys.stderr)


if __name__ == "__main__":
    main()
