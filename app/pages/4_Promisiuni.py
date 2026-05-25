"""Pagină: Promisiuni — explorator Promise Tracker cu filtre."""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent.parent))
from data_loaders import load_promises

ROOT = Path(__file__).resolve().parent.parent.parent

st.set_page_config(page_title="Urmărire promisiuni", page_icon="✅", layout="wide")

st.title("Urmărire promisiuni")
st.markdown(
    "**131 promisiuni canonice** extrase din corpusul de campanie (≤ 25 mai 2025) cu **Gemini 2.5 Flash**, "
    "deduplicate cu embedding cosinus (prag 0,85), apoi clasificate ca ținute / în curs / "
    "redefinite / abandonate / contrazise / nemenționate în raport cu corpusul de mandat."
)

st.warning(
    "⚠️ **Important**: clasificatorul măsoară *discursul* lui Nicușor Dan, nu *acțiunile reale*. "
    "Fact-check independent (10 promisiuni verificate web) arată **60% ținute în realitate vs 20% în clasificator**. "
    "Nicușor Dan livrează semnificativ prin acțiune (decrete, legi, numiri), dar nu vorbește explicit despre realizările sale."
)

promises = load_promises()

STATUS_RO = {
    "KEPT": "Ținută",
    "IN_PROGRESS": "În curs",
    "NO_MENTION": "Nemenționată",
    "CONTRADICTED": "Contrazisă",
    "REFRAMED": "Redefinită",
    "ABANDONED": "Abandonată",
}

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total promisiuni", len(promises))
col2.metric("Ținute", (promises["status"] == "KEPT").sum(),
            f"{100*(promises['status']=='KEPT').sum()/len(promises):.0f}%")
col3.metric("În curs", (promises["status"] == "IN_PROGRESS").sum(),
            f"{100*(promises['status']=='IN_PROGRESS').sum()/len(promises):.0f}%")
col4.metric("Nemenționate + contrazise",
            ((promises["status"]=="NO_MENTION") | (promises["status"]=="CONTRADICTED")).sum())

st.subheader("Distribuție per temă")
per_topic = promises.groupby(["topic", "status"]).size().unstack(fill_value=0)
per_topic["total"] = per_topic.sum(axis=1)
per_topic["Ținute %"] = (per_topic.get("KEPT", 0) / per_topic["total"] * 100).round(0)
per_topic = per_topic.sort_values("total", ascending=False)
per_topic = per_topic.rename(columns={
    "KEPT": "Ținute",
    "IN_PROGRESS": "În curs",
    "NO_MENTION": "Nemenționate",
    "CONTRADICTED": "Contrazise",
    "REFRAMED": "Redefinite",
    "ABANDONED": "Abandonate",
})
st.dataframe(per_topic, use_container_width=True)

st.markdown("---")

st.subheader("Filtre promisiuni")

c1, c2, c3 = st.columns(3)
with c1:
    topic_filter = st.multiselect("Temă", options=sorted(promises["topic"].unique()))
with c2:
    status_options = sorted(promises["status"].unique())
    status_filter = st.multiselect(
        "Status",
        options=status_options,
        format_func=lambda x: f"{STATUS_RO.get(x, x)} ({x})",
    )
with c3:
    spec_options = ["high", "medium", "low"]
    spec_filter = st.multiselect(
        "Specificitate",
        options=spec_options,
        format_func=lambda x: {"high": "Mare", "medium": "Medie", "low": "Mică"}.get(x, x),
    )

filtered = promises.copy()
if topic_filter:
    filtered = filtered[filtered["topic"].isin(topic_filter)]
if status_filter:
    filtered = filtered[filtered["status"].isin(status_filter)]
if spec_filter:
    filtered = filtered[filtered["specificity"].isin(spec_filter)]

st.markdown(f"**{len(filtered)} promisiuni** după filtre")

for _, p in filtered.iterrows():
    emoji = {"KEPT": "✅", "IN_PROGRESS": "🔄", "NO_MENTION": "❓",
              "CONTRADICTED": "⚠️", "REFRAMED": "🔀", "ABANDONED": "❌"}.get(p["status"], "•")
    status_ro = STATUS_RO.get(p["status"], p["status"])
    with st.expander(
        f"{emoji} **{status_ro}** [{p['topic']} / {p['specificity']}] — {p['promise_text'][:120]}",
        expanded=False
    ):
        st.markdown(f"**Promisiune**: {p['promise_text']}")
        st.markdown(f"**Citat verbatim**: *\"{p['verbatim_quote']}\"*")
        st.markdown(f"**Sursa**: {p['source_date']} — `{p['source_doc_id']}`")
        if p["cluster_size"] > 1:
            st.markdown(f"**Repetată în**: {p['cluster_size']} docs (același mesaj reluat)")
        st.markdown(f"**Status: {emoji} {status_ro}** (încredere: {p['confidence']})")
        st.markdown(f"**Raționament LLM**: {p['reasoning']}")

st.markdown("---")
st.markdown(
    "Audituri complete: [`AUDIT_seed42.md`](https://github.com/radusqrt/evolutie-discurs-nicusor-dan/blob/main/results/04_promises/AUDIT_seed42.md), "
    "[`AUDIT_seed1337.md`](https://github.com/radusqrt/evolutie-discurs-nicusor-dan/blob/main/results/04_promises/AUDIT_seed1337.md). "
    "Fact-check: [`FACT_CHECK_realworld.md`](https://github.com/radusqrt/evolutie-discurs-nicusor-dan/blob/main/results/04_promises/FACT_CHECK_realworld.md), "
    "[`FACT_CHECK_policy.md`](https://github.com/radusqrt/evolutie-discurs-nicusor-dan/blob/main/results/04_promises/FACT_CHECK_policy.md)."
)
