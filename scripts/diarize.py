"""Diarize unverified YouTube transcripts using Gemini on the downloaded audio.

For each .md file in data/raw/youtube/ where verificat=false:
  1. Parse video_id from `sursa` URL
  2. yt-dlp → /tmp/yt_audio/<id>.mp3
  3. gemini-cli on the mp3 → diarized transcript with [ND]/[JURNALIST]/[MODERATOR] labels
  4. Overwrite the .md content with the diarized version, set verificat=true

Run as:
    python scripts/diarize.py [--limit N] [--only <video_id>]
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
YT_DIR = ROOT / "data" / "raw" / "youtube"
AUDIO_DIR = Path("/tmp/yt_audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

GEMINI_MODEL = "gemini-3-flash-preview"

PROMPT_TEMPLATE = """Procesează acest fișier audio. Este {title_descr}.

Sarcina ta: DIARIZARE. Identifică pentru fiecare replică cine vorbește și transcrie verbatim în română.

Etichete strict acestea:
  [ND] = Nicușor Dan (Președintele României)
  [JURNALIST] = orice jurnalist (cu nume dacă se prezintă verbal, ex. [JURNALIST: Ion Popescu])
  [MODERATOR] = moderator / protocol / prezentator de eveniment
  [OFICIAL: rol] = alt oficial (premier, ministru, ambasador, alt președinte etc.) cu rolul lui

Reguli stricte:
  - Returnează DOAR transcriptul diarizat în română.
  - Fiecare replică pe rând nou, începând cu eticheta între paranteze pătrate.
  - Verbatim — exact ce se aude. Nu rezuma, nu parafraza, nu corecta exprimarea.
  - Dacă o replică e scurtă (da/nu/mhm) include-o oricum cu eticheta.
  - Nu adăuga introducere, concluzie, comentarii, header-uri, markdown — doar replicile etichetate.
  - Dacă nu poți identifica vorbitorul, folosește [UNKNOWN].

Începe direct cu prima replică."""


def video_id_from_url(url: str) -> str | None:
    m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else None


def download_audio(video_id: str) -> Path | None:
    out = AUDIO_DIR / f"{video_id}.mp3"
    if out.exists() and out.stat().st_size > 100_000:
        return out
    cmd = [
        "yt-dlp",
        "-x", "--audio-format", "mp3", "--audio-quality", "9",
        "-o", str(AUDIO_DIR / "%(id)s.%(ext)s"),
        f"https://www.youtube.com/watch?v={video_id}",
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if proc.returncode != 0:
            print(f"  yt-dlp fail: {proc.stderr[-200:]}", file=sys.stderr)
            return None
    except subprocess.TimeoutExpired:
        return None
    return out if out.exists() else None


def diarize_with_gemini(audio_path: Path, title: str) -> str | None:
    prompt = PROMPT_TEMPLATE.format(title_descr=title) + f"\n\n@{audio_path}"
    try:
        proc = subprocess.run(
            ["gemini", "-m", GEMINI_MODEL, "-p", prompt],
            capture_output=True, text=True, timeout=600,
        )
        if proc.returncode != 0:
            print(f"  gemini fail: {proc.stderr[-200:]}", file=sys.stderr)
            return None
        # Strip common warnings before content (Gemini sometimes prefixes warnings)
        text = proc.stdout
        # Find the first line that starts with a tag like [ND] or similar
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if re.match(r"^\[(ND|JURNALIST|MODERATOR|OFICIAL|UNKNOWN)", line.strip()):
                text = "\n".join(lines[i:])
                break
        return text.strip()
    except subprocess.TimeoutExpired:
        print(f"  gemini timeout", file=sys.stderr)
        return None


def diarize_file(md_path: Path) -> bool:
    post = frontmatter.load(md_path)
    if post.get("verificat"):
        return False  # already verified, skip

    sursa = str(post.get("sursa", ""))
    vid = video_id_from_url(sursa)
    if not vid:
        print(f"  no video_id in sursa for {md_path.name}", file=sys.stderr)
        return False

    print(f"  -> {md_path.name} | video {vid}", file=sys.stderr)
    audio = download_audio(vid)
    if not audio:
        print(f"     audio download failed", file=sys.stderr)
        return False
    print(f"     audio: {audio.stat().st_size // 1024} KB", file=sys.stderr)

    title = post.get("titlu_video") or post.get("tip") or "discurs"
    diarized = diarize_with_gemini(audio, str(title))
    if not diarized or len(diarized) < 200:
        print(f"     diarization too short / empty ({len(diarized) if diarized else 0} chars)", file=sys.stderr)
        return False

    # Overwrite content, mark verified, add diarization metadata
    post.content = diarized
    post["verificat"] = True
    post["metoda"] = "gemini diarization (audio mp3 via yt-dlp)"
    md_path.write_text(frontmatter.dumps(post))
    print(f"     saved {len(diarized)} chars diarized", file=sys.stderr)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--only", type=str, default=None, help="Process only this video_id")
    args = ap.parse_args()

    files = sorted(YT_DIR.glob("*.md"))
    todo = []
    for f in files:
        post = frontmatter.load(f)
        if post.get("verificat"):
            continue
        vid = video_id_from_url(str(post.get("sursa", "")))
        if args.only and vid != args.only:
            continue
        todo.append(f)

    if args.limit:
        todo = todo[: args.limit]

    print(f"Diarizing {len(todo)} files...\n", file=sys.stderr)
    ok = fail = 0
    for f in todo:
        if diarize_file(f):
            ok += 1
        else:
            fail += 1

    print(f"\n=== Done: {ok} diarized, {fail} failed ===", file=sys.stderr)


if __name__ == "__main__":
    main()
