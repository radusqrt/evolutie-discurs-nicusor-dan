"""Heuristic diarization for YouTube auto-caption transcripts.

Two formats encountered in Privesc.Eu captions:

1. **>> marker format** (most files from July 2025 onwards):
   Speaker change explicitly marked with `>>`. The Press Conference starts with ND
   speaking, then alternates ND ↔ journalist at each `>>`.

2. **Journalist-intro format** (older June 2025 files):
   No `>>` markers. Journalists self-introduce with patterns like
   "Bună ziua, domnule președinte", "Domnule președinte, ...", etc.

Output: rewrites the .md file with `[ND] / [JURNALIST]` labels on each paragraph,
sets `verificat: true`, records `metoda: heuristic diarization`.

Limitations (documented in file note):
  - Heuristic, not perfect. May misattribute when:
    * ND interrupts a journalist (>> may not be present)
    * Multiple journalists chain questions without separator
    * Joint statements with another head-of-state (Sandu, Zelensky, Rutte) —
      these may benefit from manual review
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
YT_DIR = ROOT / "data" / "raw" / "youtube"

# Patterns that indicate a journalist is starting to speak (case-insensitive)
JOURNALIST_INTRO_PATTERNS = [
    r"^bună (ziua|seara|dimineața)[,]?\s+domnule? (preș|presed)",
    r"^domnule? (preș|presed)edint",
    r"^stimate? domn",
    r"^întreb(are|area)\s*:",
    r"o întrebare,\s*domnule? (preș|presed)",
    r"dacă (îmi |i )?permite",
    r"^revin(.{0,30})cu o întrebare",
]
JOURNALIST_RE = re.compile("|".join(JOURNALIST_INTRO_PATTERNS), re.IGNORECASE)

# Patterns where ND opens his speech / signals taking over
ND_RESUMPTION = [
    r"^(da|nu|ăă|deci|așa(?:dar)?|în primul rând|deci|bun)\b",
    r"^o întrebare\s+l(a|e)?\s*",  # unlikely as ND but rare
]


def split_at_markers(text: str) -> list[str]:
    """Split text on '>>' markers. Each segment is a contiguous speaker turn."""
    return [s.strip() for s in re.split(r">>", text) if s.strip()]


def split_at_journalist_intros(text: str) -> list[str]:
    """Split text on journalist intro patterns (used when no '>>' markers)."""
    paras = re.split(r"\n\n+", text)
    out: list[str] = []
    current: list[str] = []
    for p in paras:
        if JOURNALIST_RE.match(p.strip()):
            if current:
                out.append("\n\n".join(current).strip())
                current = []
            current.append(p)
        else:
            current.append(p)
    if current:
        out.append("\n\n".join(current).strip())
    return [s for s in out if s]


QA_TRIGGER_PATTERNS = [
    r"sunt(em)? gata( pentru| la)? întreb",
    r"răspund.{0,40}întreb",
    r"sunt disponibil.{0,40}întreb",
    r"aștept(ăm)? întreb",
]
QA_TRIGGER_RE = re.compile("|".join(QA_TRIGGER_PATTERNS), re.IGNORECASE)


def label_segments(segments: list[str], format_kind: str) -> list[tuple[str, str]]:
    """Assign speaker label to each segment using two-phase logic.

    Phase 1 (opening): All segments before the Q&A trigger ("sunt gata pentru întrebări"
    or similar) are ND. This captures ND's opening statement which can span many
    >>-separated chunks.

    Phase 2 (Q&A): After the trigger, alternate JOURNALIST → ND. Override to JOURNALIST
    when a segment matches journalist intro pattern.
    """
    labeled: list[tuple[str, str]] = []
    if format_kind == "markers":
        # Find Q&A trigger position
        trigger_idx = None
        for i, seg in enumerate(segments):
            if QA_TRIGGER_RE.search(seg):
                trigger_idx = i
                break

        if trigger_idx is None:
            # No clear trigger — fall back to: first segment ND, then alternate at journalist intros
            speaker = "ND"
            for seg in segments:
                if JOURNALIST_RE.match(seg):
                    speaker = "JURNALIST"
                labeled.append((speaker, seg))
                # Only flip on journalist intro or if seg ends with "?"
                if speaker == "JURNALIST":
                    speaker = "ND"  # journalist usually one chunk, then ND responds
        else:
            # Phase 1: all segments up to and including trigger = ND
            for i in range(trigger_idx + 1):
                labeled.append(("ND", segments[i]))
            # Phase 2: alternate JOURNALIST → ND, with override on intro pattern
            speaker = "JURNALIST"
            for seg in segments[trigger_idx + 1:]:
                if JOURNALIST_RE.match(seg):
                    speaker = "JURNALIST"
                labeled.append((speaker, seg))
                speaker = "ND" if speaker == "JURNALIST" else "JURNALIST"
    else:  # intros (no >> markers)
        for seg in segments:
            if JOURNALIST_RE.match(seg):
                labeled.append(("JURNALIST", seg))
            else:
                labeled.append(("ND", seg))
    return labeled


def format_diarized(labeled: list[tuple[str, str]]) -> str:
    out = []
    for speaker, text in labeled:
        out.append(f"[{speaker}] {text}")
    return "\n\n".join(out)


JOINT_CONFERENCE_KEYWORDS = [
    "maia sandu", "zelensky", "zelenskyy", "zelenschi",
    "secretarul general al nato", "mark rutte",
    "cancelarul german", "premierul",
    "comunitatea românească",  # diaspora meetings
]


def is_joint_conference(post) -> bool:
    title = (post.get("titlu_video") or "").lower()
    return any(kw in title for kw in JOINT_CONFERENCE_KEYWORDS)


def diarize_file(md_path: Path, dry_run: bool = False) -> dict:
    post = frontmatter.load(md_path)
    if post.get("verificat"):
        return {"status": "already-verified", "file": md_path.name}

    if is_joint_conference(post):
        return {"status": "skipped-joint", "file": md_path.name,
                "format": "joint", "segments": 0, "nd_segments": 0,
                "journalist_segments": 0, "nd_ratio": 0.0}

    text = post.content
    has_markers = ">>" in text

    if has_markers:
        segments = split_at_markers(text)
        format_kind = "markers"
    else:
        segments = split_at_journalist_intros(text)
        format_kind = "intros"

    labeled = label_segments(segments, format_kind)
    diarized = format_diarized(labeled)

    nd_chars = sum(len(t) for s, t in labeled if s == "ND")
    j_chars = sum(len(t) for s, t in labeled if s == "JURNALIST")

    stats = {
        "status": "diarized",
        "file": md_path.name,
        "format": format_kind,
        "segments": len(segments),
        "nd_segments": sum(1 for s, _ in labeled if s == "ND"),
        "journalist_segments": sum(1 for s, _ in labeled if s == "JURNALIST"),
        "nd_ratio": round(nd_chars / max(nd_chars + j_chars, 1), 2),
    }

    if dry_run:
        return stats

    post.content = diarized
    post["verificat"] = True
    post["metoda"] = (f"heuristic diarization (format={format_kind}, "
                      f"{stats['nd_segments']} ND segments, "
                      f"{stats['journalist_segments']} JURNALIST segments)")
    post["nota"] = (
        "Transcript YouTube auto-generat, diarizat euristic. "
        "Format-uri detectate: '>>' marker (canalul Privesc.Eu, post iul 2025) "
        "sau pattern jurnalist 'Bună ziua, domnule președinte' (iun 2025). "
        "Pentru analize pe vocea pură ND, filtrează doar liniile [ND]. "
        "Pot exista erori la edge-cases (interpreting interrupții, joint statements). "
        "Pentru precizie audio-based, e nevoie de pyannote sau LLM diarizare audio."
    )
    md_path.write_text(frontmatter.dumps(post))
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", type=str, help="Filename substring filter")
    args = ap.parse_args()

    files = sorted(YT_DIR.glob("*.md"))
    if args.only:
        files = [f for f in files if args.only in f.name]

    print(f"{'fmt':<8} {'seg':>4} {'ND':>4} {'J':>4} {'ND%':>5}  file")
    print("-" * 110)
    for f in files:
        stats = diarize_file(f, dry_run=args.dry_run)
        if stats["status"] == "already-verified":
            continue
        pct = f"{int(stats['nd_ratio']*100)}%"
        print(f"{stats['format']:<8} {stats['segments']:>4} {stats['nd_segments']:>4} "
              f"{stats['journalist_segments']:>4} {pct:>5}  {stats['file']}")


if __name__ == "__main__":
    main()
