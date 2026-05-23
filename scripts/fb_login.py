"""One-time login flow for Facebook via Playwright.

Run this ONCE to capture an authenticated session:
    python scripts/fb_login.py

It opens a headed Chromium window. You log in to Facebook manually.
After login, press ENTER in the terminal — the script saves storage_state
to data/.fb_state.json (gitignored).

Subsequent fb_collect.py runs use that state automatically (no re-login).
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "data" / ".fb_state.json"


def main():
    from playwright.sync_api import sync_playwright
    print("Launching headed Chromium...", file=sys.stderr)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ctx = browser.new_context()
        page = ctx.new_page()
        page.goto("https://www.facebook.com/login")
        print("\n>>> Loghează-te în Facebook în fereastra deschisă.")
        print(">>> După ce ai intrat în cont și vezi feed-ul, apasă ENTER aici.\n")
        input()
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        ctx.storage_state(path=str(STATE_FILE))
        print(f"Saved session to {STATE_FILE.relative_to(ROOT)}")
        browser.close()


if __name__ == "__main__":
    main()
