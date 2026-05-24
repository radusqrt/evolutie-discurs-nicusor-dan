"""Pasul 7: Semantic drift per topic — cum se mută poziția ND pe fiecare topic peste timp?

Folosește output BERTopic (topics.csv per proiecție): doc → topic_id. Pentru top-N
topice, grupează docs by period, embed cu paraphrase-multilingual-mpnet, calculează
centroid per (topic, period), apoi cosine drift față de prima perioadă.

Output: heatmap topic × perioadă cu cât de mult s-a deplasat centroidul + linie de
drift cumulat per topic.

Run:
    PROJECTION=overall python scripts/07_semantic_drift.py
"""
from __future__ import annotations

import os
from pathlib import Path

import frontmatter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from corpus import _normalize_diacritics, strip_speaker_tags_to_nd

PROJECTION = os.getenv("PROJECTION", "overall")
ROOT = Path(__file__).resolve().parent.parent
SRC_TOPICS = ROOT / "results" / f"03_bertopic_{PROJECTION}" / "topics.csv"
SRC_CORPUS = ROOT / "data" / f"3_nd_{PROJECTION}"
OUT = ROOT / "results" / f"07_semantic_drift_{PROJECTION}"
OUT.mkdir(parents=True, exist_ok=True)

MODEL = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
TOP_N_TOPICS = 10
MIN_DOCS_PER_BUCKET = 3


def main():
    if not SRC_TOPICS.exists():
        print(f"ERROR: {SRC_TOPICS} not found. Rulează BERTopic întâi.")
        return

    topics_df = pd.read_csv(SRC_TOPICS)
    topics_df = topics_df[topics_df["topic_id"] != -1].copy()  # drop outliers
    topics_df["period_short"] = topics_df["period"].str.split(" ").str[0]

    # Load doc texts
    print("Loading doc texts...")
    id_to_text: dict[str, str] = {}
    for path in sorted(SRC_CORPUS.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        text = post.content.strip()
        if text:
            id_to_text[path.stem] = strip_speaker_tags_to_nd(_normalize_diacritics(text))

    topics_df["text"] = topics_df["id"].map(id_to_text)
    topics_df = topics_df.dropna(subset=["text"])
    print(f"Joined: {len(topics_df)} docs with topic + text.")

    # Pick top-N topics by total docs
    topic_sizes = topics_df.groupby("topic_id").size().sort_values(ascending=False)
    top_topics = topic_sizes.head(TOP_N_TOPICS).index.tolist()
    print(f"Top {len(top_topics)} topics: {top_topics}")

    # Embed all relevant texts
    print(f"Embedding with {MODEL}...")
    model = SentenceTransformer(MODEL)
    relevant = topics_df[topics_df["topic_id"].isin(top_topics)].copy()
    relevant["text_truncated"] = relevant["text"].str[:2500]  # cap pentru viteză
    embeddings = model.encode(relevant["text_truncated"].tolist(),
                                show_progress_bar=True, normalize_embeddings=True,
                                batch_size=32)
    relevant = relevant.reset_index(drop=True)
    relevant["emb_idx"] = relevant.index

    # Compute centroid per (topic, period)
    centroids: dict[tuple[int, str], np.ndarray] = {}
    bucket_sizes: dict[tuple[int, str], int] = {}
    for (topic_id, period), grp in relevant.groupby(["topic_id", "period"]):
        if len(grp) < MIN_DOCS_PER_BUCKET:
            continue
        idx = grp["emb_idx"].tolist()
        c = embeddings[idx].mean(axis=0)
        c = c / np.linalg.norm(c)
        centroids[(int(topic_id), period)] = c
        bucket_sizes[(int(topic_id), period)] = len(grp)

    # For each topic, compute drift from earliest period
    period_order = sorted(set(p for _, p in centroids.keys()))
    print(f"\nPeriods: {len(period_order)}")
    for p in period_order:
        print(f"  {p}")

    # Get topic labels from BERTopic output (parse topic_label col)
    topic_labels = relevant.drop_duplicates("topic_id").set_index("topic_id")["topic_label"].to_dict()

    drift_rows = []
    for topic_id in top_topics:
        # Find earliest period with this topic
        topic_periods = [p for p in period_order if (topic_id, p) in centroids]
        if len(topic_periods) < 2:
            continue
        base_p = topic_periods[0]
        base_c = centroids[(topic_id, base_p)]
        for p in topic_periods:
            c = centroids[(topic_id, p)]
            sim = float(cosine_similarity(base_c.reshape(1, -1), c.reshape(1, -1))[0, 0])
            drift = 1 - sim
            drift_rows.append({
                "topic_id": topic_id,
                "topic_label": topic_labels.get(topic_id, "?")[:80],
                "period": p,
                "n_docs": bucket_sizes[(topic_id, p)],
                "cosine_sim_to_base": round(sim, 4),
                "drift": round(drift, 4),
            })

    drift_df = pd.DataFrame(drift_rows)
    drift_df.to_csv(OUT / "drift_per_topic_period.csv", index=False)

    # Aggregate: max drift per topic
    max_drift = drift_df.groupby(["topic_id", "topic_label"])["drift"].max().reset_index()
    max_drift = max_drift.sort_values("drift", ascending=False)
    max_drift.to_csv(OUT / "max_drift_per_topic.csv", index=False)

    # Heatmap
    pivot = drift_df.pivot_table(index="topic_label", columns="period",
                                    values="drift", fill_value=np.nan)
    pivot = pivot.reindex(columns=period_order)
    # Sort rows by max drift descending
    pivot["_max"] = pivot.max(axis=1)
    pivot = pivot.sort_values("_max", ascending=False).drop(columns=["_max"])

    fig, ax = plt.subplots(figsize=(14, max(6, 0.5 * len(pivot))))
    im = ax.imshow(pivot.values, aspect="auto", cmap="YlOrRd")
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels([p.split(" ", 1)[0] for p in pivot.columns], rotation=30, ha="right")
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels([str(s)[:60] for s in pivot.index], fontsize=9)
    plt.colorbar(im, ax=ax, label="Semantic drift (1 - cos sim)")
    ax.set_title(f"Semantic drift per topic vs perioada de start ({PROJECTION})")

    # Annotate values
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            v = pivot.values[i, j]
            if not np.isnan(v):
                ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                        color="white" if v > 0.2 else "black", fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "semantic_drift_heatmap.png", dpi=120, bbox_inches="tight")
    plt.close(fig)

    # Markdown summary
    md = [f"# Pasul 7 — Semantic drift per topic ({PROJECTION})\n"]
    md.append(f"**Setup**: Pentru fiecare topic BERTopic (top {len(top_topics)} ca dimensiune), "
              f"calculez centroidul embeddings al docurilor grupate per perioadă, apoi cosine "
              f"distance față de prima perioadă cu ≥{MIN_DOCS_PER_BUCKET} docs.\n")
    md.append("**Interpretare**: drift mare (>0.15) = ND a schimbat substanțial *cum vorbește* "
              "despre topic (lexicon, context, framing). Drift mic = poziție stabilă.\n")
    md.append("## Max drift per topic (sortat)\n")
    md.append(max_drift.to_markdown(index=False))
    md.append("\n## Full drift heatmap\n")
    md.append("Vezi `semantic_drift_heatmap.png`.")
    md.append("\n## Tabel complet\n")
    md.append(drift_df.to_markdown(index=False))

    (OUT / "summary.md").write_text("\n".join(md))
    print(f"\nOutput: {OUT}/")
    print(f"  - drift_per_topic_period.csv")
    print(f"  - max_drift_per_topic.csv")
    print(f"  - semantic_drift_heatmap.png")
    print(f"  - summary.md")


if __name__ == "__main__":
    main()
