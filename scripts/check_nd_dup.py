"""Quick check: how many near-duplicate pairs exist in 3_nd_overall?

Pairwise Jaccard on token sets (post ND-only extraction). Reports distribution
of similarities at 0.70, 0.80, 0.85, 0.90, 0.95 thresholds.

Decide if a post-projection dedup step is worth implementing.
"""
from __future__ import annotations

import time
from collections import Counter
from itertools import combinations
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "3_nd_overall"


def tokens(text: str) -> set[str]:
    return {w.lower() for w in text.split() if len(w) > 2}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> None:
    docs = []
    for path in sorted(SRC.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        content = post.content.strip()
        if not content:
            continue
        tks = tokens(content)
        if len(tks) < 20:  # ignore very short docs
            continue
        docs.append((path.stem, str(post.get("data", "")),
                     str(post.get("tip", "")), tks, len(content.split())))
    print(f"Loaded {len(docs)} docs (filter: ≥20 unique tokens).")

    # Pairwise Jaccard. 1062 docs → ~563k pairs. Manageable.
    pair_count = len(docs) * (len(docs) - 1) // 2
    print(f"Computing {pair_count:,} pairwise similarities...")
    t0 = time.time()

    thresholds = [0.70, 0.80, 0.85, 0.90, 0.95]
    above = {t: 0 for t in thresholds}
    examples = {t: [] for t in thresholds}

    for i, j in combinations(range(len(docs)), 2):
        sim = jaccard(docs[i][3], docs[j][3])
        for t in thresholds:
            if sim >= t:
                above[t] += 1
                if len(examples[t]) < 5:
                    examples[t].append((sim, docs[i][0], docs[i][1], docs[i][2], docs[i][4],
                                        docs[j][0], docs[j][1], docs[j][2], docs[j][4]))

    elapsed = time.time() - t0
    print(f"Done in {elapsed:.1f}s.\n")

    print("PAIR COUNT BY THRESHOLD:")
    print(f"{'threshold':>10} {'pairs':>8}")
    print("-" * 22)
    for t in thresholds:
        print(f"{t:>10.2f} {above[t]:>8,}")

    print("\nEXAMPLES (5 highest per threshold):")
    for t in thresholds:
        print(f"\n--- Jaccard ≥ {t} ({above[t]} pairs) ---")
        for ex in examples[t][:3]:
            sim, id_a, d_a, tip_a, wc_a, id_b, d_b, tip_b, wc_b = ex
            print(f"  {sim:.3f} | {d_a} {tip_a:20} {wc_a:>4}w  {id_a[:50]}")
            print(f"         | {d_b} {tip_b:20} {wc_b:>4}w  {id_b[:50]}")


if __name__ == "__main__":
    main()
