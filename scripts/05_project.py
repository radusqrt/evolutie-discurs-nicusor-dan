"""Materialize ND-voice projections — multiple branches for different analyses.

Projections:
  overall  → data/3_nd_overall/  — toate sursele (FB + video), doar [ND]
  scris    → data/3_nd_scris/    — doar FB posts (text scris direct)
  vorbit   → data/3_nd_vorbit/   — doar transcripturi video/discursuri (rostit oral)

Toate trei sunt regenerable determinist din data/2_diarized/. Rulează ori
de câte ori se schimbă 2_diarized.

Categorization rules (pe `tip` din frontmatter):
  - scris: tip == 'facebook-post'
  - vorbit: orice altceva (video-transcript, discurs-*, conferinta-presa,
            dezbatere-*, interviu-*, mesaj-*, alocuțiune, anunt-*, lansare-*)
  - overall: TOATE (union scris + vorbit)

Run:
    python scripts/05_project.py  # generates all 3 projections
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "2_diarized"

PROJECTIONS = {
    "overall": ROOT / "data" / "3_nd_overall",
    "scris":   ROOT / "data" / "3_nd_scris",
    "vorbit":  ROOT / "data" / "3_nd_vorbit",
}

TAG_RE = re.compile(r"^\[(ND|JURNALIST[^\]]*|ANCHOR|MODERATOR|OFICIAL[^\]]*|UNKNOWN|RUTTE|SIMION)\]\s*")
WRITTEN_TIPS = {"facebook-post"}


def is_written(tip: str) -> bool:
    return tip in WRITTEN_TIPS


def project_nd_only(content: str) -> tuple[str, int, int]:
    """Extract only [ND] segments. Returns (text, n_nd, n_other).

    Splits on ANY newline (not just \n\n) so consecutive [ND] segments without
    blank line between are handled correctly. Then groups consecutive ND chunks
    into paragraphs in output."""
    has_tags = any(line.lstrip().startswith("[") and TAG_RE.match(line.lstrip())
                   for line in content.splitlines() if line.strip())
    if not has_tags:
        return content, 0, 0

    # Split on single newlines to catch every tagged segment
    segments = re.split(r"\n+", content)
    nd_paras = []
    n_nd = n_other = 0
    for seg in segments:
        seg_stripped = seg.lstrip()
        if not seg_stripped:
            continue
        m = TAG_RE.match(seg_stripped)
        if not m:
            # Untagged line — could be continuation of previous; we skip to be safe
            continue
        if m.group(1) == "ND":
            cleaned = TAG_RE.sub("", seg_stripped).strip()
            if cleaned:
                nd_paras.append(cleaned)
                n_nd += 1
        else:
            n_other += 1
    return "\n\n".join(nd_paras), n_nd, n_other


def materialize_projection(dst: Path, filter_fn) -> dict:
    """filter_fn(post) -> True if file should be included in this projection."""
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    stats = {"included_monologue": 0, "included_projected": 0,
             "excluded_filter": 0, "excluded_empty": 0}
    total_nd = total_other = 0
    for src in sorted(SRC.rglob("*.md")):
        rel = src.relative_to(SRC)
        post = frontmatter.load(src)
        if not filter_fn(post):
            stats["excluded_filter"] += 1
            continue
        projected, n_nd, n_other = project_nd_only(post.content)
        if n_nd == 0 and n_other == 0:
            (dst / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst / rel)
            stats["included_monologue"] += 1
        elif n_nd == 0:
            stats["excluded_empty"] += 1
            total_other += n_other
        else:
            post.content = projected
            post["metoda"] = str(post.get("metoda", "")) + " + ND-only projection"
            (dst / rel).parent.mkdir(parents=True, exist_ok=True)
            (dst / rel).write_text(frontmatter.dumps(post))
            stats["included_projected"] += 1
            total_nd += n_nd
            total_other += n_other
    return {**stats, "nd_segments": total_nd, "other_segments_dropped": total_other}


def main():
    print(f"{'projection':<10} {'monolog':>7} {'projected':>10} {'excl_filter':>12} {'excl_empty':>11} {'ND segs':>10}")
    print("-" * 80)
    for name, dst in PROJECTIONS.items():
        if name == "overall":
            fn = lambda p: True
        elif name == "scris":
            fn = lambda p: is_written(str(p.get("tip", "")))
        elif name == "vorbit":
            fn = lambda p: not is_written(str(p.get("tip", "")))
        else:
            continue
        stats = materialize_projection(dst, fn)
        print(f"{name:<10} {stats['included_monologue']:>7} {stats['included_projected']:>10} "
              f"{stats['excluded_filter']:>12} {stats['excluded_empty']:>11} "
              f"{stats['nd_segments']:>10}")

    print(f"\nOutput folders:")
    for name, dst in PROJECTIONS.items():
        n = sum(1 for _ in dst.rglob("*.md"))
        print(f"  data/{dst.name}/  → {n} docs")


if __name__ == "__main__":
    main()
