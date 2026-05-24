"""Dedup pipeline: cluster near-duplicates and pick canonical version per cluster.

Input:  data/0_raw/  (immutable snapshot)
Output: data/1_canonical/  (deduplicated corpus)

Strategy:
  1. Group documents by upload date.
  2. Within each date, compute pairwise Jaccard similarity on token sets.
  3. Cluster docs with similarity ≥ THRESHOLD.
  4. Pick canonical per cluster (priority order):
     a. From Administrația Prezidențială (official)
     b. From Privesc.Eu România (event coverage, full streams)
     c. Longest content (most complete)
     d. Highest view count (most popular = likely best edit)
  5. Copy canonical files to data/1_canonical/ preserving folder structure.
  6. Write dedupe_report.md with cluster details.

Run as:
    python scripts/03_dedupe.py [--threshold 0.85] [--dry-run]
"""
from __future__ import annotations

import argparse
import shutil
from collections import defaultdict
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "raw"
DST = ROOT / "data" / "1_canonical"
REPORT = ROOT / "data" / "dedupe_report.md"

THRESHOLD_DEFAULT = 0.85

# Channel priority (lower = better/more authoritative)
CHANNEL_PRIORITY = [
    "Administrația Prezidențială",
    "Privesc.Eu",
    "Nicușor Dan",
    "manual",
    "Digi24",
    "Euronews",
    "Antena 3",
    "B1",
    "Kanal D",
]


def channel_score(ch: str) -> int:
    ch_low = ch.lower()
    for i, prio in enumerate(CHANNEL_PRIORITY):
        if prio.lower() in ch_low:
            return i
    return len(CHANNEL_PRIORITY)


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def cluster_by_similarity(docs: list[dict], threshold: float) -> list[list[int]]:
    """Greedy connected-component clustering on Jaccard graph."""
    n = len(docs)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    token_sets = [set(d["content"].split()) for d in docs]
    for i in range(n):
        for j in range(i + 1, n):
            if jaccard(token_sets[i], token_sets[j]) >= threshold:
                union(i, j)

    groups: dict[int, list[int]] = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return list(groups.values())


def pick_canonical(docs: list[dict], indices: list[int]) -> int:
    """Return index of canonical doc in cluster, using priority rules."""
    candidates = [(idx, docs[idx]) for idx in indices]
    candidates.sort(
        key=lambda x: (
            channel_score(x[1]["channel"]),
            -x[1]["words"],
            -(x[1].get("views") or 0),
        )
    )
    return candidates[0][0]


def load_corpus(src_dir: Path) -> list[dict]:
    docs = []
    for f in sorted(src_dir.rglob("*.md")):
        if "/excluded/" in str(f):
            continue
        post = frontmatter.load(f)
        docs.append({
            "path": f,
            "rel": f.relative_to(src_dir),
            "date": str(post.get("data", "")),
            "channel": str(post.get("sursa_canal", post.get("canal", "manual"))),
            "title": str(post.get("sursa_titlu", post.get("titlu_video", f.name))),
            "words": len(post.content.split()),
            "views": post.get("sursa_vizionari"),
            "content": post.content,
        })
    return docs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, default=THRESHOLD_DEFAULT)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"Loading from {SRC}...")
    docs = load_corpus(SRC)
    print(f"  {len(docs)} docs loaded")

    by_date = defaultdict(list)
    for i, d in enumerate(docs):
        by_date[d["date"]].append(i)

    canonical_ids: list[int] = []
    duplicates_dropped: list[tuple[int, int]] = []  # (drop_idx, kept_idx)
    cluster_info: list[dict] = []

    for date, indices in by_date.items():
        if len(indices) == 1:
            canonical_ids.append(indices[0])
            continue

        sub_docs = [docs[i] for i in indices]
        clusters = cluster_by_similarity(sub_docs, args.threshold)

        for cluster_local in clusters:
            cluster_global = [indices[ci] for ci in cluster_local]
            canon = pick_canonical(docs, cluster_global)
            canonical_ids.append(canon)
            for idx in cluster_global:
                if idx != canon:
                    duplicates_dropped.append((idx, canon))

            if len(cluster_global) > 1:
                cluster_info.append({
                    "date": date,
                    "kept": docs[canon],
                    "dropped": [docs[i] for i in cluster_global if i != canon],
                })

    print(f"\n=== Dedup result ===")
    print(f"  Original: {len(docs)} docs")
    print(f"  Canonical: {len(canonical_ids)}")
    print(f"  Dropped: {len(duplicates_dropped)}")
    print(f"  Clusters with dupes: {len(cluster_info)}")

    if not args.dry_run:
        # Copy canonical files to data/1_canonical/
        if DST.exists():
            shutil.rmtree(DST)
        DST.mkdir(parents=True)
        for idx in sorted(canonical_ids):
            src = docs[idx]["path"]
            rel = docs[idx]["rel"]
            dst = DST / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        print(f"\nCanonical corpus written to {DST.relative_to(ROOT)}/")

        # Write dedup report
        lines = [
            "# Dedup report\n",
            f"- Original: **{len(docs)}** docs",
            f"- Canonical: **{len(canonical_ids)}**",
            f"- Dropped near-duplicates: **{len(duplicates_dropped)}**",
            f"- Threshold: Jaccard ≥ {args.threshold}",
            "",
            "## Clusters with dropped duplicates\n",
        ]
        for c in sorted(cluster_info, key=lambda x: x["date"]):
            lines.append(f"### {c['date']}\n")
            lines.append(f"**Kept canonical:** `{c['kept']['rel']}`")
            lines.append(f"  - channel: {c['kept']['channel']}")
            lines.append(f"  - words: {c['kept']['words']}")
            lines.append(f"  - title: {c['kept']['title'][:80]}\n")
            lines.append(f"**Dropped:**")
            for d in c["dropped"]:
                lines.append(f"  - `{d['rel']}` ({d['channel']}, {d['words']}w): {d['title'][:80]}")
            lines.append("")
        REPORT.write_text("\n".join(lines))
        print(f"Dedup report: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
