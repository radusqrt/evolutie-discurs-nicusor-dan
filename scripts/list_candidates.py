"""Just list YouTube video candidates without fetching transcripts.

Saves to data/index/youtube_candidates.json for later batched processing
(when IP rate limit lifts).
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = ROOT / "data" / "index"
INDEX_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = INDEX_DIR / "youtube_candidates.json"

SOURCES = {
    # Official channels (highest priority — uploads of presidential speeches)
    "Nicușor Dan": "https://www.youtube.com/channel/UCWro8GYVQD34hCLQjA_yz9w/videos",
    "Administrația Prezidențială": "https://www.youtube.com/channel/UC2pG2gHcDa2oaLOpxpmL07g/videos",
    # Event coverage (live streams of conferences, declarations)
    "Privesc.Eu (search ND)": "https://www.youtube.com/channel/UCz8tvsWJxsuexe9_rU65ngQ/search?query=Nicușor+Dan",
    # TV station channels (interviews, talk shows, news coverage with ND)
    "Digi24 (search ND)": "https://www.youtube.com/channel/UCbvKamSrJkwT6ed2BMMZXwg/search?query=Nicușor+Dan",
    "Antena 3 CNN (search ND)": "https://www.youtube.com/channel/UCw9Hc3CD8hbqP-Y9XOJS--Q/search?query=Nicușor+Dan",
    "B1 TV (search ND)": "https://www.youtube.com/channel/UCeqNP-Wt7YNjPyH6XhMYPxw/search?query=Nicușor+Dan",
    "Euronews Romania (search ND)": "https://www.youtube.com/channel/UCbATDExtWstHnwWELZnXNZA/search?query=Nicușor+Dan",
    "Kanal D Romania (search ND)": "https://www.youtube.com/channel/UCD_R9fKyrQLxlDJsOwvGKyg/search?query=Nicușor+Dan",
}
PAGE_LIMIT = 500

# STRICT keep: titles where ND clearly speaks himself. We look for patterns
# like "Nicușor Dan: ..." (he says X), "Nicușor Dan, declarație/interviu/mesaj/discurs/...",
# "ND a spus/anunță/a declarat/a transmis", "Mesajul/Discursul/Declarația lui ND", etc.
KEEP_PATTERNS = [
    # Speech act + ND
    r"Nicu[șs]or Dan,?\s*(declar|interviu|mesaj|discurs|aloc|conferin[țt]|cuv[âa]nt|despre|anun[țt]|spus|spune|explică|prim|reac[țt]|afirma|comenteaz|răspund|atac|critică|încep|continu|finaliz|salut|mulțum)",
    r"(declara|interviu|mesaj|discurs|alocu[țt]|conferin[țt]|cuv[âa]nt) [a-zș]+ Nicu[șs]or Dan",
    r"Nicu[șs]or Dan: ",  # direct quote pattern
    # Title role + ND
    r"Pre[sș]edintele Rom[âa]niei,? Nicu[șs]or Dan",
    # Direct from him
    r"Mesajul .{0,30}Nicu[șs]or Dan",
    r"Discursul .{0,30}Nicu[șs]or Dan",
    r"Declara[țt]ia .{0,30}Nicu[șs]or Dan",
    r"Alocu[țt]iunea .{0,30}Nicu[șs]or Dan",
    r"Conferin[țt]a .{0,30}Nicu[șs]or Dan",
    # He announces / says X
    r"Nicu[șs]or Dan\b.*(anun[țt]|aprob|promulg|semneaz|cere|propune|invită|conf)",
    r"Nicu[șs]or Dan,? (după|înainte) (de )?",
]
KEEP = re.compile("|".join(KEEP_PATTERNS), re.IGNORECASE)

# STRICT skip: titles that are clearly about ND but with someone else as speaker
SKIP_PATTERNS = [
    # Previous filters
    r"primarul (general |municipiului )?",
    r"liderul Grupului parlamentar USR",
    r"Klaus Iohannis|Ilie Bolojan|Ion Iliescu|Traian Băsescu|Emil Constantinescu",
    # Commentary BY others ABOUT ND
    r"\b(CTP|Cristoiu|Băsescu|Becali|Piperea|Șoșoacă|Georgescu|Simion|Grindeanu|Caramitru|Naumescu|Ponta|Năstase|Pleșu|Dragnea|Cioran|Reformata|Antena 3 [^c])\b.*Nicu[șs]or Dan",
    r"Nicu[șs]or Dan.*(spune|spune|paraplegic|crede)",  # ?
    # Reactions to ND
    r"\b(reac[țt]ia|răspuns(ul)?|comentari|critică|atac(at|ă)?|haluc|părere)\b.*Nicu[șs]or Dan",
    r"despre .* Nicu[șs]or Dan(,| la| de la)",
    r"către Nicu[șs]or Dan",
    r"\b(replic|răspund)(ă|e|și|i)\s+(lui |către )?Nicu[șs]or Dan",
    # Pure analysis / news without his voice
    r"^(analiz|sondaj|bilan[țt]|bilan)",
    r"editorial.*Nicu[șs]or Dan",
    # General talk show name in title
    r"^(TALK|MARIUS TUCĂ|SINTEZA ZILEI)\s+",
]
SKIP = re.compile("|".join(SKIP_PATTERNS), re.IGNORECASE)


def list_channel(name: str, url: str) -> list[dict]:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from proxy import get_proxy_for_yt_dlp
    cmd = [
        "yt-dlp", "--flat-playlist",
        "--print", "%(id)s||%(title)s||%(duration)s||%(view_count)s",
        "--playlist-end", str(PAGE_LIMIT),
    ]
    proxy = get_proxy_for_yt_dlp()
    if proxy:
        cmd += ["--proxy", proxy]
    cmd.append(url)
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    items = []
    for line in proc.stdout.splitlines():
        parts = line.split("||")
        if len(parts) < 2:
            continue
        vid = parts[0].strip()
        title = parts[1].strip()
        duration = parts[2].strip() if len(parts) > 2 else None
        views = parts[3].strip() if len(parts) > 3 else None
        if not vid or not title:
            continue
        items.append({
            "video_id": vid,
            "title": title,
            "channel": name,
            "duration_seconds": int(duration) if duration and duration.isdigit() else None,
            "view_count": int(views) if views and views.isdigit() else None,
            "url": f"https://www.youtube.com/watch?v={vid}",
        })
    return items


def main():
    all_items: list[dict] = []
    for name, url in SOURCES.items():
        print(f"=== {name} ===", file=sys.stderr)
        items = list_channel(name, url)
        print(f"  raw: {len(items)}", file=sys.stderr)
        kept = [i for i in items if KEEP.search(i["title"]) and not SKIP.search(i["title"])]
        print(f"  kept: {len(kept)}", file=sys.stderr)
        all_items.extend(kept)

    # Dedupe by video_id
    seen = set()
    unique = []
    for i in all_items:
        if i["video_id"] in seen:
            continue
        seen.add(i["video_id"])
        unique.append(i)

    # Mark which are already collected
    yt_dir = ROOT / "data" / "raw" / "youtube"
    existing_ids = set()
    for f in yt_dir.glob("*.md"):
        text = f.read_text(errors="ignore")[:500]
        m = re.search(r"v=([A-Za-z0-9_-]{11})", text)
        if m:
            existing_ids.add(m.group(1))
    for i in unique:
        i["already_collected"] = i["video_id"] in existing_ids

    new_count = sum(1 for i in unique if not i["already_collected"])
    print(f"\nTotal unique candidates: {len(unique)}", file=sys.stderr)
    print(f"  already collected: {len(unique) - new_count}", file=sys.stderr)
    print(f"  TO FETCH: {new_count}", file=sys.stderr)

    OUT_FILE.write_text(json.dumps(unique, indent=2, ensure_ascii=False))
    print(f"\nSaved to {OUT_FILE.relative_to(ROOT)}", file=sys.stderr)


if __name__ == "__main__":
    main()
