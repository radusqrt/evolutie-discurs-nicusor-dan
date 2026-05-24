"""Page: Promises — Promise Tracker explorer cu filter."""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent.parent))
from data_loaders import load_promises

ROOT = Path(__file__).resolve().parent.parent.parent

st.set_page_config(page_title="Promises", page_icon="✅", layout="wide")

st.title("Promise Tracker")
st.markdown(
    "**131 promisiuni canonice** extrase din corpusul de campanie (≤ 25 mai 2025) cu **Gemini 2.5 Flash**, "
    "deduplicate cu embedding cosinus (threshold 0.85), apoi clasificate ca KEPT / IN_PROGRESS / "
    "REFRAMED / ABANDONED / CONTRADICTED / NO_MENTION față de corpusul de mandat."
)

st.warning(
    "⚠️ **Important**: clasificator-ul măsoară *discursul* lui ND, nu *acțiunile reale*. "
    "Fact-check independent (10 promisiuni verificate web) arată **60% KEPT real vs 20% classifier**. "
    "ND livrează semnificativ prin acțiune (decrete, legi, numiri), dar nu vorbește explicit despre realizările sale."
)

promises = load_promises()

# Summary
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total promisiuni", len(promises))
col2.metric("KEPT", (promises["status"] == "KEPT").sum(),
            f"{100*(promises['status']=='KEPT').sum()/len(promises):.0f}%")
col3.metric("IN_PROGRESS", (promises["status"] == "IN_PROGRESS").sum(),
            f"{100*(promises['status']=='IN_PROGRESS').sum()/len(promises):.0f}%")
col4.metric("NO_MENTION + CONTRADICTED",
            ((promises["status"]=="NO_MENTION") | (promises["status"]=="CONTRADICTED")).sum())

# Per-topic breakdown
st.subheader("Distribuție per topic")
per_topic = promises.groupby(["topic", "status"]).size().unstack(fill_value=0)
per_topic["total"] = per_topic.sum(axis=1)
per_topic["KEPT %"] = (per_topic.get("KEPT", 0) / per_topic["total"] * 100).round(0)
per_topic = per_topic.sort_values("total", ascending=False)
st.dataframe(per_topic, use_container_width=True)

st.markdown("---")

# Filters
st.subheader("Filter promisiuni")

c1, c2, c3 = st.columns(3)
with c1:
    topic_filter = st.multiselect("Topic", options=sorted(promises["topic"].unique()))
with c2:
    status_filter = st.multiselect("Status", options=sorted(promises["status"].unique()))
with c3:
    spec_filter = st.multiselect("Specificity", options=["high", "medium", "low"])

filtered = promises.copy()
if topic_filter:
    filtered = filtered[filtered["topic"].isin(topic_filter)]
if status_filter:
    filtered = filtered[filtered["status"].isin(status_filter)]
if spec_filter:
    filtered = filtered[filtered["specificity"].isin(spec_filter)]

st.markdown(f"**{len(filtered)} promisiuni** după filtre")

# Display
for _, p in filtered.iterrows():
    emoji = {"KEPT": "✅", "IN_PROGRESS": "🔄", "NO_MENTION": "❓",
              "CONTRADICTED": "⚠️", "REFRAMED": "🔀", "ABANDONED": "❌"}.get(p["status"], "•")
    with st.expander(
        f"{emoji} **{p['status']}** [{p['topic']} / {p['specificity']}] — {p['promise_text'][:120]}",
        expanded=False
    ):
        st.markdown(f"**Promisiune**: {p['promise_text']}")
        st.markdown(f"**Quote verbatim**: *\"{p['verbatim_quote']}\"*")
        st.markdown(f"**Sursa**: {p['source_date']} — `{p['source_doc_id']}`")
        if p["cluster_size"] > 1:
            st.markdown(f"**Cluster size**: {p['cluster_size']} (repetată în alte docs)")
        st.markdown(f"**Status: {emoji} {p['status']}** (confidence: {p['confidence']})")
        st.markdown(f"**Raționament LLM**: {p['reasoning']}")

st.markdown("---")
st.markdown(
    f"Audit complete: [`AUDIT_seed42.md`]({ROOT}/results/04_promises/AUDIT_seed42.md), "
    f"[`AUDIT_seed1337.md`]({ROOT}/results/04_promises/AUDIT_seed1337.md). "
    f"Fact-check: [`FACT_CHECK_realworld.md`]({ROOT}/results/04_promises/FACT_CHECK_realworld.md), "
    f"[`FACT_CHECK_policy.md`]({ROOT}/results/04_promises/FACT_CHECK_policy.md)."
)
