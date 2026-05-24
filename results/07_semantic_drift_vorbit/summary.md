# Pasul 7 — Semantic drift per topic (vorbit)

**Setup**: Pentru fiecare topic BERTopic (top 8 ca dimensiune), calculez centroidul embeddings al docurilor grupate per perioadă, apoi cosine distance față de prima perioadă cu ≥3 docs.

**Interpretare**: drift mare (>0.15) = ND a schimbat substanțial *cum vorbește* despre topic (lexicon, context, framing). Drift mic = poziție stabilă.

## Max drift per topic (sortat)

|   topic_id | topic_label                            |   drift |
|-----------:|:---------------------------------------|--------:|
|          2 | 2_trebuie_cred_momentul_spus           |  0.2279 |
|          6 | 6_europa_energie_piață_competitivitate |  0.2116 |
|          4 | 4_momentul_campania_trebuie_există     |  0.1842 |
|          0 | 0_românia_parte_trebuie_spus           |  0.1732 |
|          5 | 5_românia_național_privește_statului   |  0.1352 |
|          1 | 1_există_cred_spus_momentul            |  0.1288 |
|          3 | 3_cred_trebuie_oamenii_făcut           |  0.0798 |

## Full drift heatmap

Vezi `semantic_drift_heatmap.png`.

## Tabel complet

|   topic_id | topic_label                            | period                                |   n_docs |   cosine_sim_to_base |   drift |
|-----------:|:---------------------------------------|:--------------------------------------|---------:|---------------------:|--------:|
|          0 | 0_românia_parte_trebuie_spus           | 2025Q2 campanie + investitură         |        4 |               1      | -0      |
|          0 | 0_românia_parte_trebuie_spus           | 2025Q3 deficit + reforma economică    |       10 |               0.8396 |  0.1604 |
|          0 | 0_românia_parte_trebuie_spus           | 2025Q4 stabilizare + diplomație       |       19 |               0.8268 |  0.1732 |
|          0 | 0_românia_parte_trebuie_spus           | 2025Q4-2026Q1 reformă judiciară       |       17 |               0.8656 |  0.1344 |
|          0 | 0_românia_parte_trebuie_spus           | 2026Q2 cotitură UE + criză guvern     |       22 |               0.8834 |  0.1166 |
|          1 | 1_există_cred_spus_momentul            | 2025Q2 campanie + investitură         |       10 |               1      | -0      |
|          1 | 1_există_cred_spus_momentul            | 2025Q3 deficit + reforma economică    |       11 |               0.9212 |  0.0788 |
|          1 | 1_există_cred_spus_momentul            | 2025Q4 stabilizare + diplomație       |        5 |               0.8936 |  0.1064 |
|          1 | 1_există_cred_spus_momentul            | 2025Q4-2026Q1 reformă judiciară       |       12 |               0.8712 |  0.1288 |
|          1 | 1_există_cred_spus_momentul            | 2026Q2 cotitură UE + criză guvern     |       20 |               0.9027 |  0.0973 |
|          2 | 2_trebuie_cred_momentul_spus           | 2025Q3 deficit + reforma economică    |        8 |               1      |  0      |
|          2 | 2_trebuie_cred_momentul_spus           | 2025Q4 stabilizare + diplomație       |        5 |               0.8372 |  0.1628 |
|          2 | 2_trebuie_cred_momentul_spus           | 2025Q4-2026Q1 reformă judiciară       |       19 |               0.8049 |  0.1951 |
|          2 | 2_trebuie_cred_momentul_spus           | 2026Q2 cotitură UE + criză guvern     |        8 |               0.7721 |  0.2279 |
|          3 | 3_cred_trebuie_oamenii_făcut           | 2024Q4-2025Q1 candidatură-precampanie |       13 |               1      |  0      |
|          3 | 3_cred_trebuie_oamenii_făcut           | 2025Q2 campanie + investitură         |        8 |               0.9202 |  0.0798 |
|          4 | 4_momentul_campania_trebuie_există     | 2024Q4-2025Q1 candidatură-precampanie |        5 |               1      |  0      |
|          4 | 4_momentul_campania_trebuie_există     | 2025Q4 stabilizare + diplomație       |        9 |               0.8158 |  0.1842 |
|          5 | 5_românia_național_privește_statului   | 2025Q2 campanie + investitură         |        7 |               1      |  0      |
|          5 | 5_românia_național_privește_statului   | 2025Q4-2026Q1 reformă judiciară       |        7 |               0.8648 |  0.1352 |
|          6 | 6_europa_energie_piață_competitivitate | 2025Q4-2026Q1 reformă judiciară       |        6 |               1      |  0      |
|          6 | 6_europa_energie_piață_competitivitate | 2026Q2 cotitură UE + criză guvern     |        5 |               0.7884 |  0.2116 |