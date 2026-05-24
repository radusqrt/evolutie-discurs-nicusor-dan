# Pasul 7 — Semantic drift per topic (scris)

**Setup**: Pentru fiecare topic BERTopic (top 7 ca dimensiune), calculez centroidul embeddings al docurilor grupate per perioadă, apoi cosine distance față de prima perioadă cu ≥3 docs.

**Interpretare**: drift mare (>0.15) = ND a schimbat substanțial *cum vorbește* despre topic (lexicon, context, framing). Drift mic = poziție stabilă.

## Max drift per topic (sortat)

|   topic_id | topic_label                                 |   drift |
|-----------:|:--------------------------------------------|--------:|
|          1 | 1_bucurești_str_oraș_fonduri                |  0.1872 |
|          0 | 0_românia_romaniaonesta_româniei_trebuie    |  0.1603 |
|          2 | 2_legea_privind_publice_statului            |  0.1377 |
|          6 | 6_voluntari_onestă_românia onestă_campaniei |  0.0931 |

## Full drift heatmap

Vezi `semantic_drift_heatmap.png`.

## Tabel complet

|   topic_id | topic_label                                 | period                                |   n_docs |   cosine_sim_to_base |   drift |
|-----------:|:--------------------------------------------|:--------------------------------------|---------:|---------------------:|--------:|
|          0 | 0_românia_romaniaonesta_româniei_trebuie    | 2024Q4-2025Q1 candidatură-precampanie |       23 |               1      |  0      |
|          0 | 0_românia_romaniaonesta_româniei_trebuie    | 2025Q2 campanie + investitură         |      313 |               0.9786 |  0.0214 |
|          0 | 0_românia_romaniaonesta_româniei_trebuie    | 2025Q3 deficit + reforma economică    |       50 |               0.9031 |  0.0969 |
|          0 | 0_românia_romaniaonesta_româniei_trebuie    | 2025Q4 stabilizare + diplomație       |       65 |               0.8794 |  0.1206 |
|          0 | 0_românia_romaniaonesta_româniei_trebuie    | 2025Q4-2026Q1 reformă judiciară       |       45 |               0.8614 |  0.1386 |
|          0 | 0_românia_romaniaonesta_româniei_trebuie    | 2026Q2 cotitură UE + criză guvern     |       58 |               0.8397 |  0.1603 |
|          1 | 1_bucurești_str_oraș_fonduri                | 2024Q4-2025Q1 candidatură-precampanie |        4 |               1      |  0      |
|          1 | 1_bucurești_str_oraș_fonduri                | 2025Q2 campanie + investitură         |       43 |               0.8128 |  0.1872 |
|          2 | 2_legea_privind_publice_statului            | 2025Q4 stabilizare + diplomație       |       11 |               1      |  0      |
|          2 | 2_legea_privind_publice_statului            | 2025Q4-2026Q1 reformă judiciară       |       14 |               0.8623 |  0.1377 |
|          6 | 6_voluntari_onestă_românia onestă_campaniei | 2024Q4-2025Q1 candidatură-precampanie |        3 |               1      | -0      |
|          6 | 6_voluntari_onestă_românia onestă_campaniei | 2025Q2 campanie + investitură         |        8 |               0.9069 |  0.0931 |