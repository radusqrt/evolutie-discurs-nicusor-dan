# Pasul 5 — Discourse complexity (scris)

**Docs analizate**: 724 | total words: 64,404 | total sentences: 3,483

## Aggregate per perioadă

| period                                |   n_words_sum |   n_sentences_sum |   sent_len_mean_mean |   sent_len_mean_std |   tree_depth_mean_mean |   tree_depth_mean_std |   ttr_lemma_mean |   mtld_mean |   func_ratio_mean |   word_len_mean_mean |   docs |
|:--------------------------------------|--------------:|------------------:|---------------------:|--------------------:|-----------------------:|----------------------:|-----------------:|------------:|------------------:|---------------------:|-------:|
| 2024Q4-2025Q1 candidatură-precampanie |          1827 |               120 |               12.673 |               7.689 |                  3.381 |                 1.26  |            0.851 |      51.259 |             0.353 |                6.324 |     30 |
| 2025Q2 campanie + investitură         |         24333 |              1594 |               13.776 |               9.147 |                  3.526 |                 1.439 |            0.84  |      34.834 |             0.413 |                5.711 |    406 |
| 2025Q3 deficit + reforma economică    |          5583 |               298 |               19.969 |               9.183 |                  4.484 |                 1.652 |            0.747 |      67.208 |             0.409 |                5.695 |     54 |
| 2025Q4 stabilizare + diplomație       |         11331 |               532 |               21.634 |               6.569 |                  5.2   |                 1.131 |            0.697 |      87.876 |             0.424 |                5.713 |     79 |
| 2025Q4-2026Q1 reformă judiciară       |         11634 |               518 |               23.331 |               6.601 |                  5.326 |                 1.124 |            0.688 |      80.234 |             0.442 |                5.573 |     72 |
| 2026Q2 cotitură UE + criză guvern     |          9696 |               421 |               21.344 |               7.493 |                  5.145 |                 1.203 |            0.752 |      66.718 |             0.369 |                5.845 |     83 |

## Métrici explicate

- **sent_len_mean**: lungime medie a propoziției (token-uri non-punctuație)
- **tree_depth_mean**: adâncimea medie a arborelui de dependență (proxy de complexitate sintactică)
- **ttr_lemma**: type-token ratio pe leme (0-1, mai mare = vocabular mai divers)
- **mtld**: Measure of Textual Lexical Diversity (robust la length, valori tipice 50-150)
- **func_ratio**: proporție de cuvinte funcționale (proxy pentru stil simplu — mai sus = mai simplu)
- **word_len_mean**: lungime medie cuvânt (caractere)