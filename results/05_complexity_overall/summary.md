# Pasul 5 — Discourse complexity (overall)

**Docs analizate**: 1062 | total words: 289,684 | total sentences: 13,125

## Aggregate per perioadă

| period                                |   n_words_sum |   n_sentences_sum |   sent_len_mean_mean |   sent_len_mean_std |   tree_depth_mean_mean |   tree_depth_mean_std |   ttr_lemma_mean |   mtld_mean |   func_ratio_mean |   word_len_mean_mean |   docs |
|:--------------------------------------|--------------:|------------------:|---------------------:|--------------------:|-----------------------:|----------------------:|-----------------:|------------:|------------------:|---------------------:|-------:|
| 2024Q4-2025Q1 candidatură-precampanie |         22653 |               198 |              143.94  |             271.483 |                  7.117 |                 5.709 |            0.667 |      49.855 |             0.447 |                5.517 |     55 |
| 2025Q2 campanie + investitură         |         54539 |              2910 |               17.761 |              35.423 |                  3.736 |                 1.703 |            0.797 |      35.866 |             0.429 |                5.57  |    468 |
| 2025Q3 deficit + reforma economică    |         51127 |              2482 |               20.984 |               8.332 |                  4.502 |                 1.344 |            0.633 |      61.322 |             0.46  |                5.279 |     96 |
| 2025Q4 stabilizare + diplomație       |         46106 |              2202 |               21.523 |               6.554 |                  4.921 |                 1.115 |            0.624 |      70.304 |             0.475 |                5.252 |    136 |
| 2025Q4-2026Q1 reformă judiciară       |         66728 |              3038 |               22.741 |               7.388 |                  4.942 |                 1.211 |            0.603 |      62.792 |             0.488 |                5.086 |    157 |
| 2026Q2 cotitură UE + criză guvern     |         48531 |              2295 |               21.132 |               6.972 |                  4.826 |                 1.085 |            0.639 |      59.069 |             0.446 |                5.326 |    150 |

## Métrici explicate

- **sent_len_mean**: lungime medie a propoziției (token-uri non-punctuație)
- **tree_depth_mean**: adâncimea medie a arborelui de dependență (proxy de complexitate sintactică)
- **ttr_lemma**: type-token ratio pe leme (0-1, mai mare = vocabular mai divers)
- **mtld**: Measure of Textual Lexical Diversity (robust la length, valori tipice 50-150)
- **func_ratio**: proporție de cuvinte funcționale (proxy pentru stil simplu — mai sus = mai simplu)
- **word_len_mean**: lungime medie cuvânt (caractere)