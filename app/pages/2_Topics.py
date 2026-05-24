"""Page: Topics — BERTopic discoveries + drift semantic."""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent.parent))
from data_loaders import load_topic_info, load_topics

ROOT = Path(__file__).resolve().parent.parent.parent

st.set_page_config(page_title="Topics", page_icon="🎯", layout="wide")

st.title("Topics — BERTopic")
st.markdown(
    "Topice latente descoperite cu **BERTopic + multilingual-e5-large + UMAP + HDBSCAN**. "
    "Nu sunt categorii pre-definite — sunt descoperite automat din date."
)

projection = st.sidebar.selectbox(
    "Proiecție", ["overall", "scris", "vorbit"], index=0,
)

info = load_topic_info(projection)
topics_df = load_topics(projection)

if info.empty:
    st.error(f"Lipsesc rezultatele BERTopic pentru proiecția '{projection}'.")
    st.stop()

# Stats
non_outlier = info[info["topic_id"] != -1]
outliers = info[info["topic_id"] == -1]
total_docs = info["count"].sum()
n_topics = len(non_outlier)
n_outliers = outliers["count"].iloc[0] if not outliers.empty else 0

col1, col2, col3 = st.columns(3)
col1.metric("Topice descoperite", n_topics)
col2.metric("Documente clusterizate", f"{total_docs - n_outliers}", f"{100*(total_docs-n_outliers)/total_docs:.0f}%")
col3.metric("Outliers", n_outliers, f"{100*n_outliers/total_docs:.0f}%")

st.markdown("---")

# Topic table
st.subheader(f"Toate {n_topics} topicele (sortate după count)")
display_info = non_outlier.copy()
display_info["label_clean"] = display_info["topic_label"].str.replace(r"^\d+_", "", regex=True)
display_info = display_info[["topic_id", "count", "label_clean"]]
display_info.columns = ["ID", "Docs", "Topic label (keywords c-TF-IDF)"]
st.dataframe(display_info, use_container_width=True, hide_index=True)

st.markdown("---")

# Topic timeline heatmap
st.subheader("Heatmap topice × perioadă")
heatmap_path = ROOT / "results" / f"03_bertopic_{projection}" / "topics_over_time.png"
if heatmap_path.exists():
    st.image(str(heatmap_path), use_container_width=True)
else:
    st.warning("Heatmap PNG missing.")

st.markdown("---")

# Drift section
st.subheader("Semantic drift per topic")
st.markdown(
    "Cosine distance între centroidul embedding-urilor în prima perioadă vs. cele ulterioare. "
    "Drift mare = ND a schimbat substanțial *cum vorbește* despre topic."
)

drift_path = ROOT / "results" / f"07_semantic_drift_{projection}" / "max_drift_per_topic.csv"
drift_heatmap = ROOT / "results" / f"07_semantic_drift_{projection}" / "semantic_drift_heatmap.png"

if drift_path.exists():
    drift_df = pd.read_csv(drift_path)
    st.dataframe(drift_df, use_container_width=True, hide_index=True)
if drift_heatmap.exists():
    st.image(str(drift_heatmap), use_container_width=True)
