"""Webshare proxy helper — used by collection scripts to bypass YouTube IP bans.

Reads credentials from .env (loaded with python-dotenv).

Usage:
    from proxy import get_proxy_for_yt_dlp, get_proxy_for_transcript_api

    api = YouTubeTranscriptApi(proxy_config=get_proxy_for_transcript_api())
    transcript = api.fetch(video_id)

    subprocess.run(["yt-dlp", "--proxy", get_proxy_for_yt_dlp(), url])
"""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


import random


# Webshare username convention: base-ro-<index>. User has up to 200 IPs.
# Rotate randomly to avoid per-IP YouTube rate-limiting.
WEBSHARE_BASE_USERNAME = "ihirvbtp"
WEBSHARE_USERNAME_RANGE = (1, 200)


def webshare_credentials(rotate: bool = True, suffix: int | None = None) -> tuple[str, str] | None:
    """Get a Webshare proxy username + password.

    If rotate=True (default), randomly pick a suffix between 1 and 200.
    If suffix=N is given, use that specific suffix (overrides rotation).
    If neither, use the .env's WEBSHARE_PROXY_USERNAME as-is.
    """
    pwd = os.getenv("WEBSHARE_PROXY_PASSWORD", "").strip()
    env_user = os.getenv("WEBSHARE_PROXY_USERNAME", "").strip()
    if not pwd or "your-password" in pwd:
        return None

    if suffix is not None:
        user = f"{WEBSHARE_BASE_USERNAME}-ro-{suffix}"
    elif rotate:
        idx = random.randint(*WEBSHARE_USERNAME_RANGE)
        user = f"{WEBSHARE_BASE_USERNAME}-ro-{idx}"
    elif env_user and "your-username" not in env_user:
        user = env_user
    else:
        return None
    return user, pwd


def webshare_host_port() -> tuple[str, str]:
    return (
        os.getenv("WEBSHARE_PROXY_HOST", "p.webshare.io").strip() or "p.webshare.io",
        os.getenv("WEBSHARE_PROXY_PORT", "80").strip() or "80",
    )


def get_proxy_for_yt_dlp(rotate: bool = True) -> str | None:
    """Returns proxy URL for yt-dlp's --proxy flag, or None if not configured.

    By default, a fresh random IP suffix is chosen each call.
    """
    creds = webshare_credentials(rotate=rotate)
    if not creds:
        return None
    user, pwd = creds
    host, port = webshare_host_port()
    return f"http://{user}:{pwd}@{host}:{port}"


def get_proxy_for_transcript_api():
    """Returns GenericProxyConfig for youtube_transcript_api, or None if not configured.

    We use GenericProxyConfig (with our full proxy URL) rather than WebshareProxyConfig
    because the latter constructs a different endpoint that didn't work with our creds.
    """
    proxy_url = get_proxy_for_yt_dlp()
    if not proxy_url:
        return None
    try:
        from youtube_transcript_api.proxies import GenericProxyConfig
        return GenericProxyConfig(http_url=proxy_url, https_url=proxy_url)
    except ImportError:
        return None


if __name__ == "__main__":
    cfg = get_proxy_for_yt_dlp()
    if cfg:
        # Don't print full creds — mask them
        masked = cfg.replace(os.getenv("WEBSHARE_PROXY_PASSWORD", ""), "***")
        print(f"Webshare proxy configured: {masked}")
    else:
        print("No proxy configured. Set WEBSHARE_PROXY_USERNAME/PASSWORD in .env")
