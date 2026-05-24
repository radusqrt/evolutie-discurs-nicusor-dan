"""Streamlit app — Evoluția discursului Nicușor Dan.

Home page cu TL;DR + navigare către celelalte pagini.

Rulare:
    streamlit run app/app.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Add app/ to path so submodules importable
sys.path.insert(0, str(Path(__file__).parent))
from data_loaders import corpus_stats, load_promises

st.set_page_config(
    page_title="Evoluția discursului — Nicușor Dan",
    page_icon="🇷🇴",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Evoluția discursului — Nicușor Dan")
st.markdown(
    "**Analiză cantitativă a primului an de mandat (decembrie 2024 → mai 2026)**\n\n"
    "Corpus: 1,062 documente / ~650k cuvinte / 9 surse media | "
    "27 findings | Promise Tracker pe 131 promisiuni | 26 topice BERTopic | "
    "3,755 entități NER"
)

st.markdown("---")

# Quick stats
stats = corpus_stats()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Overall (toate sursele)", f"{stats['overall']['n_docs']} docs",
              f"{stats['overall']['n_words']:,} cuvinte")
with col2:
    st.metric("Scris (Facebook)", f"{stats['scris']['n_docs']} docs",
              f"{stats['scris']['n_words']:,} cuvinte")
with col3:
    st.metric("Vorbit (Video)", f"{stats['vorbit']['n_docs']} docs",
              f"{stats['vorbit']['n_words']:,} cuvinte")

st.markdown("---")

# TL;DR findings
st.header("Top findings")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Despre discurs")
    st.markdown(
        """
        - **Doi Nicușor Dan**: registru **scris (FB) = instituțional/branding** vs **vorbit (video) = deliberativ/reflexiv**
        - Vocabular dominant **abstract** (`vrea, sine, trebui, putea`), nu enumerare de policy
        - **Volum prăbușit post-mandat** — drop 3.6× față de campanie
        - **Pivot tematic abrupt** trimestru-la-trimestru
        - **Brand-shedding "România onestă"** după investitură (TF-IDF 0.6 → 0)
        - FB ultra-disciplinat — **76% într-un singur mega-topic instituțional**
        """
    )

    st.subheader("Convergent evidence — IPOTEZA GHOSTWRITING FB")
    st.markdown(
        """
        4 metrici independente arată că FB e *un alt agent comunicativ* decât video:

        1. **Hedging** — FB 0.13-0.23 vs video 0.51-1.06 (**4-5× diferență**)
        2. **Lexical diversity (MTLD)** — FB growth dramatic 34→87 post-mandat
        3. **Sentiment polarization** — FB 70% pro/contra vs video 36%
        4. **BERTopic** — FB 76% într-un singur mega-topic; video are 8 topice + 25% outliers
        """
    )

with col_b:
    st.subheader("Despre promisiuni (Pasul 4)")

    promises = load_promises()
    n_kept = (promises["status"] == "KEPT").sum()
    n_inprog = (promises["status"] == "IN_PROGRESS").sum()
    n_nom = (promises["status"] == "NO_MENTION").sum()
    n_contr = (promises["status"] == "CONTRADICTED").sum()

    st.markdown(
        f"""
        Din **{len(promises)} promisiuni canonice** clasificate cu LLM:

        - ✅ KEPT: {n_kept} ({100*n_kept/len(promises):.0f}%)
        - 🔄 IN_PROGRESS: {n_inprog} ({100*n_inprog/len(promises):.0f}%)
        - ❓ NO_MENTION: {n_nom} ({100*n_nom/len(promises):.0f}%)
        - ⚠️ CONTRADICTED: {n_contr} ({100*n_contr/len(promises):.0f}%)
        - ABANDONED: 0 (ND nu rupe vizibil promisiuni)
        """
    )

    st.subheader("Răsturnare prin fact-check (10 promisiuni verificate web)")
    st.markdown(
        """
        - **Rate KEPT real = 60%** vs classifier 20% — **subestimare factor 3×**
        - ND **livrează prin ACȚIUNE, nu prin DISCURS**:
          - Pensii magistrați promulgată (CCR 6-3)
          - DNA/DIICOT numire (apr 2026)
          - Deficit -1.4pp (cea mai mare corecție UE)
          - OCDE 22/25 opinii (on track 2026)
          - 50km tramvai contracte semnate
          - 8 șantiere consolidare active (vs 5 promise)
        """
    )

st.markdown("---")

st.header("Navigare")

col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1:
    st.markdown(
        """
        **Browse Corpus** → search keyword, filter date/proiecție/sursă, citește documente.

        **Topics** → BERTopic discoveries, heatmaps temporale, drift semantic.
        """
    )
with col_nav2:
    st.markdown(
        """
        **Entities** → cine apare în discurs (Trump, Putin, Bolojan, ...), când, cu ce sentiment.

        **Promises** → toate 131 promisiunile cu status, filter pe topic și KEPT/IN_PROGRESS.
        """
    )
with col_nav3:
    st.markdown(
        """
        **Findings** → cele 27 findings detaliate cu link-uri către artefacte.

        Navighează din sidebar →
        """
    )

st.markdown("---")
st.markdown(
    "**Repo**: [github.com/radusqrt/evolutie-discurs-nicusor-dan]"
    "(https://github.com/radusqrt/evolutie-discurs-nicusor-dan) | "
    "**Autor**: Radu Stochitoiu"
)
