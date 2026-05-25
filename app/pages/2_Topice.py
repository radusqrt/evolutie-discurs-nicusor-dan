"""Pagină: Topice — descoperiri BERTopic + drift semantic."""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent.parent))
from data_loaders import load_topic_info, load_topics

ROOT = Path(__file__).resolve().parent.parent.parent

st.set_page_config(page_title="Topice — BERTopic", page_icon="🎯", layout="wide")

st.title("Topice — descoperiri BERTopic")
st.markdown(
    "Topice latente descoperite cu **BERTopic + multilingual-e5-large + UMAP + HDBSCAN**. "
    "Nu sunt categorii predefinite — sunt descoperite automat din date."
)

projection = st.sidebar.selectbox(
    "Proiecție",
    ["overall", "scris", "vorbit"],
    index=0,
    format_func=lambda x: {"overall": "Toate sursele", "scris": "Scris (Facebook)",
                            "vorbit": "Vorbit (Video)"}.get(x, x),
)

info = load_topic_info(projection)
topics_df = load_topics(projection)

if info.empty:
    st.error(f"Lipsesc rezultatele BERTopic pentru proiecția '{projection}'.")
    st.stop()

non_outlier = info[info["topic_id"] != -1]
outliers = info[info["topic_id"] == -1]
total_docs = info["count"].sum()
n_topics = len(non_outlier)
n_outliers = outliers["count"].iloc[0] if not outliers.empty else 0

col1, col2, col3 = st.columns(3)
col1.metric("Topice descoperite", n_topics)
col2.metric("Documente clusterizate", f"{total_docs - n_outliers}",
              f"{100*(total_docs-n_outliers)/total_docs:.0f}%")
col3.metric("Documente neclasificate", n_outliers, f"{100*n_outliers/total_docs:.0f}%")

st.markdown("---")

st.subheader(f"Toate cele {n_topics} topice (sortate după număr de docs)")
display_info = non_outlier.copy()
display_info["label_clean"] = display_info["topic_label"].str.replace(r"^\d+_", "", regex=True)
display_info = display_info[["topic_id", "count", "label_clean"]]
display_info.columns = ["ID", "Docs", "Etichetă topic (cuvinte cheie c-TF-IDF)"]
st.dataframe(display_info, use_container_width=True, hide_index=True)

st.markdown("---")

st.subheader("Hartă topice × perioadă")
heatmap_path = ROOT / "results" / f"03_bertopic_{projection}" / "topics_over_time.png"
if heatmap_path.exists():
    st.image(str(heatmap_path), use_container_width=True)
else:
    st.warning("Imagine harta lipsă.")

st.markdown("---")

st.subheader("Drift semantic per topic")
st.markdown(
    "Distanța cosinus între centroidul embedding-urilor din prima perioadă vs perioadele ulterioare. "
    "Drift mare = Nicușor Dan a schimbat substanțial *cum vorbește* despre topic."
)

drift_path = ROOT / "results" / f"07_semantic_drift_{projection}" / "max_drift_per_topic.csv"
drift_heatmap = ROOT / "results" / f"07_semantic_drift_{projection}" / "semantic_drift_heatmap.png"

if drift_path.exists():
    drift_df = pd.read_csv(drift_path)
    drift_df.columns = ["ID topic", "Etichetă topic", "Drift maxim"]
    st.dataframe(drift_df, use_container_width=True, hide_index=True)
if drift_heatmap.exists():
    st.image(str(drift_heatmap), use_container_width=True)
