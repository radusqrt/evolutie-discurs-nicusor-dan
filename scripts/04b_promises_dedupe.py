"""Pasul 4b: Dedup promisiuni cu embedding cosinus.

Cluster near-duplicates (e.g. același message repetat în mai multe interviuri),
alege canonical per cluster, salvează cu cluster metadata.

Strategie:
1. Embed promise_text cu paraphrase-multilingual-mpnet (cap-de-clasă pentru
   sentence similarity, 278M params, fast CPU).
2. Cosine similarity matrix, single-link cluster cu threshold 0.85.
3. Canonical pick per cluster:
   a. specificity: high > medium > low
   b. apoi longest verbatim_quote
   c. apoi earliest date

Output: results/04_promises/promises_canonical.jsonl
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "results" / "04_promises" / "promises_raw.jsonl"
DST = ROOT / "results" / "04_promises" / "promises_canonical.jsonl"

MODEL = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
THRESHOLD = 0.85

SPEC_RANK = {"high": 3, "medium": 2, "low": 1}


def union_find_cluster(sim_matrix: np.ndarray, threshold: float) -> list[int]:
    """Returns cluster_id per item using single-link."""
    n = sim_matrix.shape[0]
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    for i in range(n):
        for j in range(i + 1, n):
            if sim_matrix[i, j] >= threshold:
                union(i, j)
    return [find(i) for i in range(n)]


def pick_canonical(promises: list[dict]) -> dict:
    """From a cluster, pick the best canonical representative."""
    def rank_key(p):
        return (
            -SPEC_RANK.get(p.get("specificity", "low"), 0),
            -len(p.get("verbatim_quote", "")),
            p.get("source_date", "9999-12-31"),
        )
    return sorted(promises, key=rank_key)[0]


def main():
    promises = []
    with SRC.open() as f:
        for line in f:
            promises.append(json.loads(line))
    print(f"Loaded {len(promises)} raw promises.")

    print(f"Embedding with {MODEL}...")
    model = SentenceTransformer(MODEL)
    texts = [p["promise_text"] for p in promises]
    embeddings = model.encode(texts, show_progress_bar=True, normalize_embeddings=True)

    sim = cosine_similarity(embeddings)
    cluster_ids = union_find_cluster(sim, THRESHOLD)

    # Group by cluster
    clusters: dict[int, list[dict]] = defaultdict(list)
    for promise, cid in zip(promises, cluster_ids):
        clusters[cid].append(promise)

    # Sort clusters by size descending
    sorted_clusters = sorted(clusters.items(), key=lambda kv: -len(kv[1]))

    print(f"\n{len(clusters)} unique promises after dedup (from {len(promises)} raw).")
    print(f"Clusters with >1 member: {sum(1 for _, v in clusters.items() if len(v) > 1)}")

    print("\nLARGEST CLUSTERS (top 10):")
    for cid, members in sorted_clusters[:10]:
        canon = pick_canonical(members)
        print(f"  [{len(members):>2}x | {canon['topic']:<25}] {canon['promise_text'][:90]}")

    # Write canonical
    with DST.open("w") as f:
        for new_cid, (_, members) in enumerate(sorted_clusters):
            canon = pick_canonical(members)
            canon["cluster_id"] = new_cid
            canon["cluster_size"] = len(members)
            canon["cluster_member_doc_ids"] = sorted({m["source_doc_id"] for m in members})
            canon["cluster_member_dates"] = sorted({m["source_date"] for m in members})
            f.write(json.dumps(canon, ensure_ascii=False) + "\n")

    print(f"\nOutput: {DST}")
    print(f"  {len(sorted_clusters)} canonical promises")


if __name__ == "__main__":
    main()
