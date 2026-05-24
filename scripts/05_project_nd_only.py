"""Materialize default ND-only projection: input data/2_diarized/, output data/3_nd_only/.

Strips all non-[ND] lines. Files that have no speaker tags (monologue files)
are copied as-is. Output is the corpus that analyses actually "see" by default —
useful for sharing, quick browsing, sanity checks.

Re-derivable deterministically from 2_diarized at any time.

Run:
    python scripts/05_project_nd_only.py
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "2_diarized"
DST = ROOT / "data" / "3_nd_only"

TAG_RE = re.compile(r"^\[(ND|JURNALIST[^\]]*|ANCHOR|MODERATOR|OFICIAL[^\]]*|UNKNOWN|RUTTE|SIMION)\]\s*")


def project_nd_only(content: str) -> tuple[str, int, int]:
    """Extract only [ND] segments. Returns (text, n_nd, n_other)."""
    # Detect if file has any speaker tags
    has_tags = any(line.lstrip().startswith("[") and TAG_RE.match(line.lstrip())
                   for line in content.splitlines() if line.strip())
    if not has_tags:
        # Monologue file — no projection needed
        return content, 0, 0

    # Split by paragraphs (double newlines), keep only those starting with [ND]
    paras = re.split(r"\n\n+", content)
    nd_paras = []
    n_nd = 0
    n_other = 0
    for p in paras:
        p_stripped = p.lstrip()
        m = TAG_RE.match(p_stripped)
        if not m:
            continue
        tag = m.group(1)
        if tag == "ND":
            # Strip the [ND] tag from the kept paragraph
            cleaned = TAG_RE.sub("", p_stripped).strip()
            if cleaned:
                nd_paras.append(cleaned)
                n_nd += 1
        else:
            n_other += 1
    return "\n\n".join(nd_paras), n_nd, n_other


def main():
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)

    stats = {"copied (monologue)": 0, "projected": 0, "empty after projection": 0}
    total_nd = 0
    total_other = 0
    empty_files = []

    for src in sorted(SRC.rglob("*.md")):
        rel = src.relative_to(SRC)
        dst = DST / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        post = frontmatter.load(src)
        projected, n_nd, n_other = project_nd_only(post.content)

        if n_nd == 0 and n_other == 0:
            # Monologue file — copy as-is
            shutil.copy2(src, dst)
            stats["copied (monologue)"] += 1
        elif n_nd == 0:
            # Multi-voice but no ND segments (e.g., pure anchor news clip about him)
            post.content = ""  # empty content
            post["nota"] = (str(post.get("nota", "")) +
                            " | PROJECT: file e pure anchor/journalist, 0 segmente ND")
            dst.write_text(frontmatter.dumps(post))
            stats["empty after projection"] += 1
            empty_files.append(rel)
            total_other += n_other
        else:
            post.content = projected
            existing_method = str(post.get("metoda", ""))
            post["metoda"] = existing_method + " + ND-only projection"
            post["nota"] = (str(post.get("nota", "")) +
                            f" | PROJECT: {n_nd} ND segments kept, {n_other} other dropped")
            dst.write_text(frontmatter.dumps(post))
            stats["projected"] += 1
            total_nd += n_nd
            total_other += n_other

    print(f"=== ND-only projection ===")
    for k, v in stats.items():
        print(f"  {k:<30} {v}")
    print(f"  Total ND segments kept: {total_nd:,}")
    print(f"  Total non-ND dropped: {total_other:,}")
    print(f"\nOutput: {DST.relative_to(ROOT)}/")
    if empty_files:
        print(f"\nFișiere fără conținut ND (pure anchor/journalist): {len(empty_files)}")
        for f in empty_files[:5]:
            print(f"  {f}")


if __name__ == "__main__":
    main()
