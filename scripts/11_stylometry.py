"""Pasul 11: Stylometry formală — Burrows' Delta + PCA + classifier pe function words.

Testează ipoteza că FB și video sunt produse de același sau registre diferite,
folosind metode stilometrice consacrate.

Output:
  results/11_stylometry/
    - pca_scatter.png         — PCA 2D, color by projection (FB vs video)
    - burrows_delta.csv       — distanță Delta între perechi de docs
    - top_features.csv        — function words care discriminează cel mai mult
    - classifier_results.md   — Random Forest accuracy + confusion matrix
    - SUMMARY.md              — interpretare integrată

Metodologie:
1. Tokenize toate docs cu spaCy, păstrăm doar POS function (ADP, AUX, CCONJ, DET,
   PART, PRON, SCONJ)
2. Vector frecvențe relative top 100 function words
3. Z-score normalizare
4. PCA 2D + scatter colored
5. Burrows' Delta = mean |z-difference| între doc și centroide
6. Random Forest: poate distinge FB de video doar din aceste 100 features?
"""
from __future__ import annotations

import os
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import spacy
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split

from corpus import _normalize_diacritics, load_corpus

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "results" / "11_stylometry"
OUT.mkdir(parents=True, exist_ok=True)

FUNCTION_POS = {"ADP", "AUX", "CCONJ", "DET", "PART", "PRON", "SCONJ"}
N_TOP_FEATURES = 100
MIN_DOC_LEN = 50  # cuvinte minim pentru a fi inclus


def extract_function_words(text: str, nlp) -> list[str]:
    """Return list of function-word lemmas from text."""
    text = _normalize_diacritics(text)
    doc = nlp(text)
    out = []
    for tok in doc:
        if tok.is_punct or tok.is_space or tok.like_num:
            continue
        if tok.pos_ in FUNCTION_POS:
            out.append(_normalize_diacritics(tok.lemma_.lower()))
    return out


def main():
    print("Loading corpus from all 3 projections...")
    # Use OVERALL projection to get all docs, then label by tip
    os.environ["PROJECTION"] = "overall"
    # Need to reload corpus module path
    speeches = load_corpus()
    print(f"  {len(speeches)} docs in overall.")

    # Filter docs by length and assign label
    docs_data = []
    for s in speeches:
        wc = len(s.nd_only_text.split())
        if wc < MIN_DOC_LEN:
            continue
        label = "scris" if s.tip == "facebook-post" else "vorbit"
        docs_data.append({"id": s.id, "label": label, "text": s.nd_only_text,
                          "tip": s.tip, "date": s.date, "wc": wc})

    df_docs = pd.DataFrame(docs_data)
    print(f"  Filtered (≥{MIN_DOC_LEN} words): {len(df_docs)} docs")
    print(f"  Distribution: {df_docs['label'].value_counts().to_dict()}")

    # Load spaCy with full pipeline
    print("\nLoading spaCy ro_core_news_sm...")
    nlp = spacy.load("ro_core_news_sm", disable=["parser", "ner"])

    # Tokenize all docs to function words
    print(f"\nExtracting function words from {len(df_docs)} docs...")
    function_words_per_doc: list[list[str]] = []
    for i, row in df_docs.iterrows():
        if i % 100 == 0 and i > 0:
            print(f"  [{i}/{len(df_docs)}]")
        fw = extract_function_words(row["text"], nlp)
        function_words_per_doc.append(fw)
    df_docs = df_docs.reset_index(drop=True)
    df_docs["fw_count"] = [len(fw) for fw in function_words_per_doc]
    df_docs = df_docs[df_docs["fw_count"] >= 20].reset_index(drop=True)
    function_words_per_doc = [function_words_per_doc[i] for i in df_docs.index
                                  if i < len(function_words_per_doc)]
    # Recompute after filter:
    valid_idx = df_docs.index.tolist()
    function_words_per_doc = [extract_function_words(t, nlp)
                                  for t in df_docs["text"].tolist()]

    # Identify top N function words across corpus
    print(f"\nIdentifying top {N_TOP_FEATURES} function words...")
    all_fw = Counter()
    for fw_list in function_words_per_doc:
        all_fw.update(fw_list)
    top_features = [w for w, _ in all_fw.most_common(N_TOP_FEATURES)]
    print(f"  Top 10: {top_features[:10]}")

    # Build feature matrix — relative frequency per doc
    X = np.zeros((len(df_docs), N_TOP_FEATURES))
    for i, fw_list in enumerate(function_words_per_doc):
        c = Counter(fw_list)
        total = max(sum(c.values()), 1)
        for j, w in enumerate(top_features):
            X[i, j] = c.get(w, 0) / total

    # Z-score normalize (Burrows-style)
    means = X.mean(axis=0)
    stds = X.std(axis=0)
    stds[stds == 0] = 1.0
    Z = (X - means) / stds
    print(f"  Feature matrix: {Z.shape}")

    # PCA 2D
    print("\nPCA 2D...")
    pca = PCA(n_components=2, random_state=42)
    Z2 = pca.fit_transform(Z)
    explained = pca.explained_variance_ratio_
    print(f"  Explained variance: PC1={explained[0]:.1%}, PC2={explained[1]:.1%}")

    df_docs["pc1"] = Z2[:, 0]
    df_docs["pc2"] = Z2[:, 1]

    # PCA scatter plot
    fig, ax = plt.subplots(figsize=(10, 7))
    colors = {"scris": "#003049", "vorbit": "#d62828"}
    for label, color in colors.items():
        sub = df_docs[df_docs["label"] == label]
        ax.scatter(sub["pc1"], sub["pc2"], c=color, label=f"{label} (n={len(sub)})",
                   alpha=0.4, s=18, edgecolors="white", linewidths=0.3)
    ax.set_xlabel(f"PC1 ({explained[0]:.1%} var)")
    ax.set_ylabel(f"PC2 ({explained[1]:.1%} var)")
    ax.set_title(f"PCA — {N_TOP_FEATURES} function words (z-normalizate)\n"
                  f"Scatter pe {len(df_docs)} documente, color by canal")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "pca_scatter.png", dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  Plot saved.")

    # Centroids
    scris_centroid = Z[df_docs["label"] == "scris"].mean(axis=0)
    vorbit_centroid = Z[df_docs["label"] == "vorbit"].mean(axis=0)

    # Burrows' Delta = mean |z-difference| between centroid and each doc
    delta_to_scris = np.abs(Z - scris_centroid).mean(axis=1)
    delta_to_vorbit = np.abs(Z - vorbit_centroid).mean(axis=1)
    centroid_distance = np.abs(scris_centroid - vorbit_centroid).mean()
    print(f"\nBurrows' Delta centroid distance scris↔vorbit: {centroid_distance:.3f}")

    df_docs["delta_to_scris_centroid"] = delta_to_scris
    df_docs["delta_to_vorbit_centroid"] = delta_to_vorbit
    df_docs["closer_to"] = np.where(delta_to_scris < delta_to_vorbit, "scris", "vorbit")

    # Confusion: how often does Burrows' Delta correctly classify?
    correct = (df_docs["closer_to"] == df_docs["label"]).sum()
    delta_acc = correct / len(df_docs)
    print(f"Burrows' Delta nearest-centroid accuracy: {delta_acc:.1%}")

    # Random Forest classifier (5-fold CV)
    print("\nRandom Forest classifier (5-fold CV)...")
    y = df_docs["label"].values
    rf = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)
    cv_scores = cross_val_score(rf, Z, y, cv=5, scoring="accuracy")
    print(f"  CV accuracy: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

    # Train on full set + confusion matrix on held-out
    X_train, X_test, y_train, y_test = train_test_split(
        Z, y, test_size=0.3, random_state=42, stratify=y)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred, labels=["scris", "vorbit"])
    print(f"  Confusion matrix on held-out 30%:")
    print(f"    {cm}")

    # Top discriminating features
    importances = rf.feature_importances_
    feat_df = pd.DataFrame({
        "word": top_features,
        "importance": importances,
        "mean_scris": X[df_docs["label"] == "scris"].mean(axis=0),
        "mean_vorbit": X[df_docs["label"] == "vorbit"].mean(axis=0),
    })
    feat_df["ratio_vorbit_over_scris"] = (feat_df["mean_vorbit"] /
                                                feat_df["mean_scris"].replace(0, 0.0001))
    feat_df = feat_df.sort_values("importance", ascending=False)
    feat_df.to_csv(OUT / "top_features.csv", index=False)

    # Save Burrows results
    burrows_df = df_docs[["id", "label", "wc", "delta_to_scris_centroid",
                            "delta_to_vorbit_centroid", "closer_to",
                            "pc1", "pc2"]].copy()
    burrows_df.to_csv(OUT / "burrows_delta.csv", index=False)

    # Markdown summary
    md = [f"# Stylometry formală — Burrows' Delta + PCA + RF\n"]
    md.append(f"**Corpus**: {len(df_docs)} documente (≥{MIN_DOC_LEN} cuvinte fiecare)")
    md.append(f"- Scris (Facebook): {(df_docs['label']=='scris').sum()}")
    md.append(f"- Vorbit (video): {(df_docs['label']=='vorbit').sum()}")
    md.append(f"\n**Metodă**: top {N_TOP_FEATURES} function words (POS: ADP/AUX/CCONJ/DET/PART/PRON/SCONJ), frecvențe relative z-normalizate.\n")

    md.append("## Rezultat 1 — Burrows' Delta")
    md.append(f"\n**Distanță centroidă scris ↔ vorbit**: `{centroid_distance:.3f}`\n")
    md.append(f"**Accuracy nearest-centroid clasificare** (la care centroid e mai aproape fiecare doc): **{delta_acc:.1%}**\n")
    md.append("Dacă FB și video ar fi indistinguibile stilometric, accuracy ar fi ~50% (random). Cu cât mai mare, cu atât mai distincte sunt cele 2 register-uri.")

    md.append("\n## Rezultat 2 — PCA")
    md.append(f"\n**Variance explicată**: PC1 = {explained[0]:.1%}, PC2 = {explained[1]:.1%}\n")
    md.append("Vezi `pca_scatter.png`. Dacă cele 2 grupuri se separă clar pe PC1-PC2, sunt registre stilometrice distincte.")

    md.append("\n## Rezultat 3 — Random Forest")
    md.append(f"\n**5-fold CV accuracy**: **{cv_scores.mean():.1%} ± {cv_scores.std():.1%}**\n")
    md.append(f"**Held-out 30% test confusion matrix**:")
    md.append(f"```")
    md.append(f"             pred_scris  pred_vorbit")
    md.append(f"true_scris   {cm[0,0]:>10d}  {cm[0,1]:>10d}")
    md.append(f"true_vorbit  {cm[1,0]:>10d}  {cm[1,1]:>10d}")
    md.append(f"```\n")
    md.append("Dacă un model simplu distinge FB de video cu >90% acuratețe **doar din 100 function words** (cuvinte ca: și, sau, în, la, dar, etc.), atunci cele 2 register-uri au amprente stilometrice distincte.")

    md.append("\n## Top 20 function words care discriminează FB vs video\n")
    md.append("Cuvinte unde frecvența diferă cel mai mult între cele 2 canale:\n")
    md.append("| Cuvânt | Importance | Mediu FB | Mediu video | Raport vorbit/scris |")
    md.append("|---|---:|---:|---:|---:|")
    for _, row in feat_df.head(20).iterrows():
        md.append(f"| `{row['word']}` | {row['importance']:.4f} | {row['mean_scris']:.4f} | "
                  f"{row['mean_vorbit']:.4f} | {row['ratio_vorbit_over_scris']:.2f}× |")

    md.append("\n## Interpretare\n")
    if delta_acc >= 0.85 and cv_scores.mean() >= 0.85:
        md.append("**Concluzie**: cele 2 registre sunt **stilometric distincte cu mare confidence**.")
        md.append(f"\nAtât Burrows' Delta cât și Random Forest distinge corect FB de video cu acuratețe ridicată ({delta_acc:.0%} și {cv_scores.mean():.0%}). Asta înseamnă că **amprenta stilometrică** (frecvențele function words) diferă substanțial între cele 2 canale.")
        md.append("\n**Posibile interpretări** (nu putem distinge fără date suplimentare):")
        md.append("- ND adaptează stil conștient pentru fiecare medium")
        md.append("- Conversia natural scris-vs-vorbit (regularitate universală)")
        md.append("- Co-autori PR pentru FB (ghostwriting parțial sau total)")
        md.append("\nFără un **baseline politic** (Iohannis, Băsescu, etc.), nu putem zice dacă această diferență e *normală* pentru un președinte sau *anormal de mare*.")
    elif delta_acc >= 0.7:
        md.append(f"**Concluzie**: cele 2 registre sunt **moderat distincte stilometric** ({delta_acc:.0%} accuracy).")
        md.append("Diferența e clară dar nu dramatică. Ar putea fi diferențe naturale gen scris vs vorbit.")
    else:
        md.append(f"**Concluzie**: cele 2 registre sunt **stilometric similare** ({delta_acc:.0%} accuracy).")
        md.append("Asta sugerează că diferențele de vocabular/sentiment observate anterior se pot datora pur tematicii/audienței, nu stilului fundamental.")

    md.append("\n## Limitări\n")
    md.append(f"- Folosim doar {N_TOP_FEATURES} function words; analize stilometrice profesionale folosesc 200-500.")
    md.append("- spaCy ro_core_news_sm are accuracy POS-tag moderată — pot fi erori sistematice.")
    md.append("- Nu avem **baseline politic comparativ** (Iohannis, etc.) — nu știm dacă pattern-ul observat e specific ND sau general.")
    md.append("- Random Forest tinde să exploateze și features non-stilometrice (lungime, repetiții) — accuracy poate fi inflated.")

    (OUT / "SUMMARY.md").write_text("\n".join(md))
    print(f"\nOutput in: {OUT}/")
    print(f"  - pca_scatter.png")
    print(f"  - burrows_delta.csv ({len(burrows_df)} rows)")
    print(f"  - top_features.csv (top {N_TOP_FEATURES})")
    print(f"  - SUMMARY.md")


if __name__ == "__main__":
    main()
