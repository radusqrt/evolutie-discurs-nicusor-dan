"""Aplicație Streamlit — Evoluția discursului Nicușor Dan.

Pagina Home cu TL;DR + navigare către celelalte pagini.

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
    "Corpus: 1.062 documente / ~650.000 cuvinte / 9 surse media | "
    "28 concluzii | Urmărire promisiuni pe 131 angajamente | 26 topice BERTopic | "
    "3.755 entități NER"
)

st.markdown("---")

# Statistici rapide
stats = corpus_stats()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Toate sursele", f"{stats['overall']['n_docs']} docs",
              f"{stats['overall']['n_words']:,} cuvinte")
with col2:
    st.metric("Scris (Facebook)", f"{stats['scris']['n_docs']} docs",
              f"{stats['scris']['n_words']:,} cuvinte")
with col3:
    st.metric("Vorbit (Video)", f"{stats['vorbit']['n_docs']} docs",
              f"{stats['vorbit']['n_words']:,} cuvinte")

st.markdown("---")

# Concluzii principale
st.header("Concluzii principale")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Despre discurs")
    st.markdown(
        """
        - **Două registre**: scris (FB) = instituțional/branding vs vorbit (video) = deliberativ/reflexiv (cauza neclară — vezi limitări metodologice)
        - Vocabular dominant **abstract** (`vrea, sine, trebui, putea`), nu enumerare de politică publică
        - **Volum prăbușit post-mandat** — scădere de 3,6× față de campanie
        - **Pivot tematic abrupt** trimestru la trimestru
        - **Renunțare la brandul "România onestă"** după investitură (TF-IDF 0,6 → 0)
        - Facebook ultra-disciplinat — **76% într-un singur mega-topic instituțional**
        """
    )

    st.subheader("Diferențe cantitative scris vs vorbit (4 metrici)")
    st.markdown(
        """
        Patru metrici independente arată diferențe radicale între FB și video:

        1. **Hedging (ezitare)** — Facebook 0,13-0,23 vs video 0,51-1,06 (**diferență de 4-5×**)
        2. **Diversitate lexicală (MTLD)** — Facebook creștere dramatică 34→87 post-mandat
        3. **Polarizare sentiment** — Facebook 70% pro/contra vs video 36%
        4. **BERTopic** — Facebook 76% într-un singur mega-topic; video are 8 topice + 25% outliers

        **Cauza e neclară**: diferențe naturale de gen, audiență diferită, sau colaborare cu echipă PR pentru FB. Stylometry formală ar putea distinge — neefectuată în acest proiect.
        """
    )

with col_b:
    st.subheader("Despre promisiuni")

    promises = load_promises()
    n_kept = (promises["status"] == "KEPT").sum()
    n_inprog = (promises["status"] == "IN_PROGRESS").sum()
    n_nom = (promises["status"] == "NO_MENTION").sum()
    n_contr = (promises["status"] == "CONTRADICTED").sum()

    st.markdown(
        f"""
        Din **{len(promises)} promisiuni canonice** clasificate cu LLM:

        - ✅ Ținute: {n_kept} ({100*n_kept/len(promises):.0f}%)
        - 🔄 În curs: {n_inprog} ({100*n_inprog/len(promises):.0f}%)
        - ❓ Nemenționate: {n_nom} ({100*n_nom/len(promises):.0f}%)
        - ⚠️ Contrazise: {n_contr} ({100*n_contr/len(promises):.0f}%)
        - Abandonate: 0 (Nicușor Dan nu rupe vizibil promisiuni)
        """
    )

    st.subheader("Răsturnare prin fact-check (10 promisiuni verificate web)")
    st.markdown(
        """
        - **Rata reală de promisiuni ținute = 60%** vs clasificator 20% — **subestimare cu factor 3×**
        - Nicușor Dan **livrează prin ACȚIUNE, nu prin DISCURS**:
          - Pensii magistrați promulgată (CCR 6-3)
          - Numire DNA/DIICOT (aprilie 2026)
          - Deficit -1,4 puncte procentuale (cea mai mare corecție din UE)
          - OCDE 22/25 opinii primite (pe traiectorie 2026)
          - 50 km tramvai contracte semnate
          - 8 șantiere consolidare active (din 5 promise)
        """
    )

st.markdown("---")

st.header("Navigare")

col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1:
    st.markdown(
        """
        **Explorare Corpus** → caută cuvinte cheie, filtrează dată/proiecție/sursă, citește documente.

        **Topice** → topice descoperite cu BERTopic, harți temporale, drift semantic.
        """
    )
with col_nav2:
    st.markdown(
        """
        **Entități** → cine apare în discurs (Trump, Putin, Bolojan, ...), când, cu ce ton.

        **Promisiuni** → toate 131 promisiunile cu status, filter pe temă și ținute/în curs.
        """
    )
with col_nav3:
    st.markdown(
        """
        **Concluzii** → cele 28 concluzii detaliate cu link-uri către surse.

        **Relația cu Premierul** → raportul ND-Bolojan pe 6 perioade + fact-check independent.

        Navighează din meniul lateral →
        """
    )

st.markdown("---")
st.markdown(
    "**Repo**: [github.com/radusqrt/evolutie-discurs-nicusor-dan]"
    "(https://github.com/radusqrt/evolutie-discurs-nicusor-dan) | "
    "**Autor**: Radu Stochitoiu"
)
