# Pasul 1 — Statistici de bază + word clouds

## Sumar corpus

| id                             | data       | tip                 |   n_words_raw |   n_lemmas_clean |   n_unique_lemmas |   ttr_lemma |   n_sentences |
|:-------------------------------|:-----------|:--------------------|--------------:|-----------------:|------------------:|------------:|--------------:|
| 2024-12-16_anunt-candidatura   | 2024-12-16 | anunt-candidatura   |           113 |               55 |                44 |       0.8   |             9 |
| 2025-05-19_discurs-victorie    | 2025-05-19 | discurs-victorie    |           255 |              102 |                70 |       0.686 |            17 |
| 2025-05-26_discurs-investitura | 2025-05-26 | discurs-investitura |           992 |              528 |               325 |       0.616 |            26 |

## Top 20 cuvinte per discurs

### 2024-12-16 — anunt-candidatura

| cuvânt       |   frecvență |
|:-------------|------------:|
| românia      |           5 |
| problemă     |           4 |
| întru        |           2 |
| moment       |           2 |
| apăra        |           2 |
| interes      |           2 |
| cumpănă      |           1 |
| dificil      |           1 |
| revoluție    |           1 |
| anunța       |           1 |
| intenționez  |           1 |
| candidez     |           1 |
| alegere      |           1 |
| prezidențial |           1 |
| rol          |           1 |
| președinte   |           1 |
| important    |           1 |
| corupție     |           1 |
| funcționare  |           1 |
| instituție   |           1 |

### 2025-05-19 — discurs-victorie

| cuvânt    |   frecvență |
|:----------|------------:|
| românia   |           8 |
| împreună  |           5 |
| victorie  |           3 |
| om        |           3 |
| campanie  |           3 |
| opțiune   |           3 |
| construi  |           3 |
| român     |           3 |
| crede     |           2 |
| putea     |           2 |
| sine      |           2 |
| săptămână |           2 |
| societate |           2 |
| politică  |           2 |
| românie   |           2 |
| diasporă  |           2 |
| basarabia |           2 |
| schimba   |           1 |
| direcție  |           1 |
| corect    |           1 |

### 2025-05-26 — discurs-investitura

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |          19 |
| sistem     |          12 |
| român      |          11 |
| privi      |          11 |
| sine       |           9 |
| național   |           9 |
| stat       |           7 |
| interes    |           6 |
| reformă    |           6 |
| om         |           5 |
| european   |           5 |
| diaspora   |           4 |
| republică  |           4 |
| moldova    |           4 |
| societate  |           4 |
| social     |           4 |
| dovedi     |           4 |
| instituție |           4 |
| acces      |           4 |
| dezvoltare |           4 |


## Top 30 cuvinte — corpus integral

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |          32 |
| român       |          14 |
| sistem      |          12 |
| sine        |          11 |
| privi       |          11 |
| național    |           9 |
| interes     |           8 |
| om          |           8 |
| împreună    |           7 |
| stat        |           7 |
| problemă    |           6 |
| putea       |           6 |
| societate   |           6 |
| european    |           6 |
| reformă     |           6 |
| instituție  |           5 |
| vrea        |           5 |
| dovedi      |           5 |
| republică   |           5 |
| moldova     |           5 |
| politică    |           4 |
| diaspora    |           4 |
| social      |           4 |
| acces       |           4 |
| dezvoltare  |           4 |
| extindere   |           4 |
| cultură     |           4 |
| participare |           4 |
| întru       |           3 |
| public      |           3 |

## Stopwords folosite

Listă **stopwordsiso RO** (438 cuvinte) + domain extras (cardinali, câteva auxiliare nestockate).


## Note metodologice

- **Tokenizare + lemmatizare**: spaCy `ro_core_news_sm`. Token-ele sunt reduse la lemma (formă canonică): `românia/româniei/român/români` → `românia`/`român`, `anunț/anunțul` → `anunța`, `săptămânile` → `săptămână`.
- **Stopwords**: `stopwordsiso` (RO) + extensii pentru cardinali și conjuncții scurte.
- **Numerele și punctuația** sunt eliminate; diacriticele cedilă (ş, ţ) sunt normalizate la virgulă-below (ș, ț).
- **TTR** (type-token ratio) e biased de lungime — discursurile scurte au TTR mai mare. Util doar comparativ pe lungimi similare.