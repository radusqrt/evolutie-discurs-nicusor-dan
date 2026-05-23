# Pasul 1 — Statistici de bază + word clouds

## Sumar corpus

| id                                                                             | data       | tip                       |   n_words_raw |   n_lemmas_clean |   n_unique_lemmas |   ttr_lemma |   n_sentences |
|:-------------------------------------------------------------------------------|:-----------|:--------------------------|--------------:|-----------------:|------------------:|------------:|--------------:|
| 2025-05-08_dezbatere-euronews-simion                                           | 2025-05-08 | dezbatere-electorala      |            63 |               34 |                28 |       0.824 |             5 |
| 2024-12-16_anunt-candidatura                                                   | 2024-12-16 | anunt-candidatura         |           113 |               55 |                44 |       0.8   |             9 |
| 2025-02-03_lansare-campanie-romania-onesta                                     | 2025-02-03 | lansare-campanie          |           184 |               90 |                68 |       0.756 |            13 |
| 2025-05-19_discurs-victorie                                                    | 2025-05-19 | discurs-victorie          |           255 |              102 |                70 |       0.686 |            17 |
| 2025-05-26_discurs-investitura                                                 | 2025-05-26 | discurs-investitura       |           992 |              528 |               325 |       0.616 |            26 |
| 2025-06-04_conferinta-presa-cotroceni                                          | 2025-06-04 | conferinta-presa          |           108 |               50 |                44 |       0.88  |             9 |
| 2025-09-04_autoevaluare-100-zile                                               | 2025-09-04 | interviu-autoevaluare     |           157 |               67 |                59 |       0.881 |            17 |
| 2025-12-31_mesaj-anul-nou                                                      | 2025-12-31 | mesaj-anul-nou            |           277 |              142 |               116 |       0.817 |            16 |
| 2024-12-04_political-studio-nicusor-dan-the-signal-is-good-even-if-it-i        | 2024-12-04 | video-transcript          |          5403 |             2489 |               985 |       0.396 |             0 |
| 2024-12-16_nicusor-dan-despre-calin-georgescu-in-ceea-ce-priveste-conte        | 2024-12-16 | video-transcript          |           106 |               56 |                50 |       0.893 |             0 |
| 2024-12-16_nicusor-dan-intentionez-sa-candidez-ca-independent-la-aleger        | 2024-12-16 | video-transcript          |           675 |              297 |               191 |       0.643 |             0 |
| 2024-12-16_nicusor-dan-reactie-la-decizia-ccr-de-a-anula-alegerile-prez        | 2024-12-16 | video-transcript          |           130 |               64 |                50 |       0.781 |             0 |
| 2024-12-16_nicusor-dan-si-a-anuntat-candidatura-la-alegerile-prezidenti        | 2024-12-16 | video-transcript          |          3354 |             1469 |               589 |       0.401 |             0 |
| 2024-12-16_nicusor-dan-urmeaza-sa-si-anunte-candidatura-ca-independent         | 2024-12-16 | video-transcript          |           368 |              187 |               117 |       0.626 |             0 |
| 2024-12-17_ciprian-ciucu-despre-candidatura-lui-nicusor-dan-nu-a-cerut         | 2024-12-17 | video-transcript          |         12222 |             5839 |              1621 |       0.278 |             0 |
| 2024-12-18_nicusor-dan-iesirea-unui-partid-din-coalitie-ne-ar-lasa-cu-u        | 2024-12-18 | video-transcript          |          5653 |             2408 |               802 |       0.333 |             0 |
| 2024-12-18_studio-politic-ludovic-orban-nicusor-dan-nu-e-ca-basescu-nu         | 2024-12-18 | video-transcript          |          6404 |             3201 |              1096 |       0.342 |             0 |
| 2024-12-19_nicusor-dan-dupa-retragerea-psd-de-la-negocieri-sunt-surprin        | 2024-12-19 | video-transcript          |           799 |              363 |               196 |       0.54  |             0 |
| 2024-12-23_nicusor-dan-despre-candidatura-lui-crin-antonescu-partidele         | 2024-12-23 | video-transcript          |           739 |              348 |               206 |       0.592 |             0 |
| 2024-12-25_mesajul-lui-nicusor-dan-pentru-romani-stiri-b1tv-25-dec-2024        | 2024-12-25 | video-transcript          |           245 |              122 |                90 |       0.738 |             0 |
| 2024-12-30_nicusor-dan-candidez-indiferent-de-ce-va-fi-stiri-b1tv-30-de        | 2024-12-30 | video-transcript          |           317 |              155 |                99 |       0.639 |             0 |
| 2024-12-30_nicusor-dan-despre-calin-georgescu-stiri-b1tv-30-dec-2024           | 2024-12-30 | video-transcript          |          1055 |              446 |               255 |       0.572 |             0 |
| 2025-01-09_nicusor-dan-critica-decizia-coalitiei-privind-data-alegerilo        | 2025-01-09 | video-transcript          |           818 |              389 |               230 |       0.591 |             0 |
| 2025-01-13_nicusor-dan-explicatiile-privind-anularea-prezidentialelor-s        | 2025-01-13 | video-transcript          |           236 |               97 |                72 |       0.742 |             0 |
| 2025-01-18_nicusor-dan-cere-explicatii-pentru-anulare-stiri-b1tv-18-ian        | 2025-01-18 | video-transcript          |           309 |              141 |                91 |       0.645 |             0 |
| 2025-01-30_nicusor-dan-despre-alegerile-prezidentiale-daca-va-castiga-g        | 2025-01-30 | video-transcript          |           238 |              103 |                83 |       0.806 |             0 |
| 2025-02-04_nicusor-dan-declara-iar-ca-nu-se-retrage-din-cursa-in-turul         | 2025-02-04 | video-transcript          |            85 |               34 |                27 |       0.794 |             0 |
| 2025-02-05_nicusor-dan-cand-statul-se-imprumuta-ca-sa-plateasca-deficit        | 2025-02-05 | video-transcript          |           441 |              189 |               132 |       0.698 |             0 |
| 2025-02-05_nicusor-dan-despre-scandalul-nordis-mult-din-ce-se-construie        | 2025-02-05 | video-transcript          |          7246 |             3103 |              1087 |       0.35  |             0 |
| 2025-02-08_nicusor-dan-reactie-in-scandalul-cu-lasconi-stiri-b1tv-8-feb        | 2025-02-08 | video-transcript          |           231 |              128 |                84 |       0.656 |             0 |
| 2025-02-16_nicusor-dan-vrem-sa-cumparam-inca-250-de-tramvaie-si-sa-mode        | 2025-02-16 | video-transcript          |           373 |              180 |               106 |       0.589 |             0 |
| 2025-02-24_nicusor-dan-despre-demisia-lui-ciolacu-stiri-b1tv-24-febr-20        | 2025-02-24 | video-transcript          |           245 |              114 |                82 |       0.719 |             0 |
| 2025-02-26_nicusor-dan-despre-dovezile-pe-care-vrea-sa-le-vada-in-legat        | 2025-02-26 | video-transcript          |           226 |               95 |                72 |       0.758 |             0 |
| 2025-02-27_nicusor-dan-despre-inculparea-lui-calin-georgescu-trebuie-sa        | 2025-02-27 | video-transcript          |           763 |              344 |               189 |       0.549 |             0 |
| 2025-02-27_sume-uriase-si-tehnologie-avansata-nicusor-dan-despre-campan        | 2025-02-27 | video-transcript          |           128 |               57 |                41 |       0.719 |             0 |
| 2025-03-07_nicusor-dan-candidatura-mea-este-candidatura-celor-240-de-mi        | 2025-03-07 | video-transcript          |           186 |               77 |                56 |       0.727 |             0 |
| 2025-03-07_nicusor-dan-fata-de-aceasta-decizie-a-ccr-ne-invartim-in-cee        | 2025-03-07 | video-transcript          |           204 |              102 |                74 |       0.725 |             0 |
| 2025-03-07_nicusor-dan-primul-candidat-care-s-a-inscris-oficial-la-prez        | 2025-03-07 | video-transcript          |           168 |               77 |                60 |       0.779 |             0 |
| 2025-03-14_buna-romania-nicusor-dan-romania-e-un-stat-bolnav-bec-trebui        | 2025-03-14 | video-transcript          |          7186 |             3163 |              1086 |       0.343 |             0 |
| 2025-03-14_nicusor-dan-despre-premierul-ciolacu-este-evident-ca-toata-l        | 2025-03-14 | video-transcript          |           548 |              221 |               147 |       0.665 |             0 |
| 2025-03-19_nicusor-dan-am-discutat-cu-bolojan-la-cotroceni-despre-alege        | 2025-03-19 | video-transcript          |          2412 |             1099 |               423 |       0.385 |             0 |
| 2025-03-27_bugetul-capitalei-retras-de-pe-ordinea-de-zi-nicusor-dan-nu         | 2025-03-27 | video-transcript          |           394 |              191 |               115 |       0.602 |             0 |
| 2025-04-01_nicusor-dan-criticat-dur-dupa-declaratia-despre-introducerea        | 2025-04-01 | video-transcript          |         11409 |             5482 |              1730 |       0.316 |           876 |
| 2025-04-02_nicusor-dan-ar-putea-fi-un-presedinte-care-sa-aduca-prestigi        | 2025-04-02 | video-transcript          |            67 |               41 |                36 |       0.878 |             5 |
| 2025-04-03_nicusor-dan-atacat-de-psd-stiri-b1tv-3-apr-2025                     | 2025-04-03 | video-transcript          |           283 |              170 |               114 |       0.671 |             0 |
| 2025-04-08_crin-antonescu-il-troleaza-pe-nicusor-dan-nu-mananc-medenele        | 2025-04-08 | video-transcript          |           124 |               60 |                48 |       0.8   |            10 |
| 2025-04-08_strategia-lui-nicusor-dan-cum-vrea-sa-o-convinga-pe-lasconi         | 2025-04-08 | video-transcript          |           298 |              153 |                85 |       0.556 |            13 |
| 2025-04-10_usr-decide-daca-il-sprijina-pe-nicusor-dan-la-alegerile-prez        | 2025-04-10 | video-transcript          |           338 |              185 |                95 |       0.514 |            18 |
| 2025-04-11_lasconi-arata-mesajul-de-la-nicusor-dan-cand-ii-cere-sa-se-v        | 2025-04-11 | video-transcript          |           286 |              123 |                85 |       0.691 |            15 |
| 2025-05-02_nicusor-dan-mesaj-pentru-romani-sa-aleaga-pe-cei-care-au-dov        | 2025-05-02 | video-transcript          |           440 |              205 |               133 |       0.649 |            24 |
| 2025-05-04_nicusor-dan-am-votat-pentru-speranta-si-pentru-un-nou-incepu        | 2025-05-04 | video-transcript          |          1171 |              546 |               234 |       0.429 |            74 |
| 2025-05-04_nicusor-dan-o-sa-fie-o-disputa-intre-un-candidat-pro-occiden        | 2025-05-04 | video-transcript          |          1225 |              542 |               288 |       0.531 |            90 |
| 2025-05-04_nicusor-dan-sa-ne-raportam-cu-pruden-a-la-rezultatele-exit-p        | 2025-05-04 | video-transcript          |           278 |              132 |                81 |       0.614 |            15 |
| 2025-05-05_exclusiv-nicusor-dan-dupa-turul-i-al-prezidentialelor-urmeaz        | 2025-05-05 | video-transcript          |           148 |               80 |                56 |       0.7   |             6 |
| 2025-05-05_nicusor-dan-despre-turul-doi-ii-chem-pe-toti-romanii-sa-fie         | 2025-05-05 | video-transcript          |           246 |              108 |                72 |       0.667 |            16 |
| 2025-05-06_apelul-lui-nicusor-dan-dupa-evolutiile-pietei-financiare-din        | 2025-05-06 | video-transcript          |           191 |              101 |                71 |       0.703 |             8 |
| 2025-05-07_editie-speciala-nicusor-dan-anunta-ca-accepta-invitatia-lui         | 2025-05-07 | video-transcript          |         11743 |             5500 |              1571 |       0.286 |           818 |
| 2025-05-07_interviu-nicusor-dan-despre-criza-economica-in-care-poate-in        | 2025-05-07 | video-transcript          |          2857 |             1294 |               527 |       0.407 |           175 |
| 2025-05-07_nicusor-dan-despre-planul-lui-simion-de-concediere-a-bugetar        | 2025-05-07 | video-transcript          |           100 |               43 |                35 |       0.814 |             6 |
| 2025-05-07_nicusor-dan-interviu-exclusiv-pentru-euronews-romania               | 2025-05-07 | video-transcript          |           150 |               61 |                43 |       0.705 |            10 |
| 2025-05-07_nicusor-dan-romania-are-nevoie-de-schimbare-dar-nu-una-care         | 2025-05-07 | video-transcript          |           124 |               55 |                42 |       0.764 |            10 |
| 2025-05-07_nicusor-dan-romania-are-nevoie-de-schimbare-dar-nu-una-care_yMbfqR  | 2025-05-07 | video-transcript          |           189 |               91 |                67 |       0.736 |            13 |
| 2025-05-10_nicusor-dan-nu-poti-sa-dai-afara-500-000-de-oameni-e-imposib        | 2025-05-10 | video-transcript          |           296 |              121 |                82 |       0.678 |            26 |
| 2025-05-14_nicusor-dan-dau-in-scris-ca-tva-nu-va-creste                        | 2025-05-14 | video-transcript          |           259 |              131 |                93 |       0.71  |            17 |
| 2025-05-15_educatia-e-o-problema-de-securitate-nationala-nicusor-dan-ce        | 2025-05-15 | video-transcript          |           356 |              178 |               113 |       0.635 |            18 |
| 2025-05-15_mirabela-gradinaru-partenera-lui-nicusor-dan-despre-momentel        | 2025-05-15 | video-transcript          |           220 |               97 |                68 |       0.701 |            15 |
| 2025-05-15_nicusor-dan-nu-sunt-izolationist-sunt-suveranist-ce-a-spus-c        | 2025-05-15 | video-transcript          |            87 |               43 |                36 |       0.837 |             7 |
| 2025-05-15_nicusor-dan-prima-reactie-dupa-jignirea-lui-simion-n-dan-con        | 2025-05-15 | video-transcript          |           208 |              105 |                79 |       0.752 |            25 |
| 2025-05-15_nicusor-dan-vs-george-simion-cele-mai-importante-momente-din        | 2025-05-15 | video-transcript          |           562 |              257 |               166 |       0.646 |            42 |
| 2025-05-16_fiul-lui-ratiu-mesaj-pentru-nicusor-dan-b1tv-16-mai-2025            | 2025-05-16 | video-transcript          |            54 |               25 |                23 |       0.92  |             8 |
| 2025-05-18_alegeri-prezidentiale-2025-mesajul-lui-nicusor-dan-dupa-apar        | 2025-05-18 | video-transcript          |           380 |              218 |               100 |       0.459 |            23 |
| 2025-05-18_nicusor-dan-am-votat-pentru-o-directie-europeana-nu-pentru-i        | 2025-05-18 | video-transcript          |            47 |               19 |                18 |       0.947 |             2 |
| 2025-05-18_nicusor-dan-dupa-ce-a-castigat-alegerile-prezidentiale-e-vic        | 2025-05-18 | video-transcript          |           216 |               91 |                61 |       0.67  |            16 |
| 2025-05-18_nicusor-dan-dupa-rezultatele-exit-poll-traim-un-moment-de-sp        | 2025-05-18 | video-transcript          |           378 |              205 |               103 |       0.502 |            30 |
| 2025-05-18_nicusor-dan-incepem-o-noua-etapa-de-maine-la-munca-sustinato        | 2025-05-18 | video-transcript          |           567 |              297 |               130 |       0.438 |            67 |
| 2025-05-18_romania-alege-cu-l-chiriac-discursul-presedintelui-nicusor-d        | 2025-05-18 | video-transcript          |          5436 |             2578 |              1015 |       0.394 |           387 |
| 2025-05-19_nicusor-dan-despre-scenariul-unei-victorii-a-lui-george-simi        | 2025-05-19 | video-transcript          |           515 |              227 |               156 |       0.687 |            48 |
| 2025-05-19_nicusor-dan-despre-viitorul-premier-bolojan-ramane-optiunea         | 2025-05-19 | video-transcript          |           463 |              225 |               153 |       0.68  |            34 |
| 2025-05-19_prima-reactie-a-rusiei-dupa-victoria-lui-nicusor-dan-alegeri        | 2025-05-19 | video-transcript          |           868 |              387 |               253 |       0.654 |            41 |
| 2025-05-20_nicusor-dan-despre-planurile-pentru-romania-stiri-b1tv-20-ma        | 2025-05-20 | video-transcript          |           335 |              173 |               108 |       0.624 |            27 |
| 2025-05-21_nicusor-dan-romania-angajament-ferm-fata-de-relatia-cu-sua          | 2025-05-21 | video-transcript          |            97 |               57 |                40 |       0.702 |             4 |
| 2025-05-21_nicusor-dan-toate-informatiile-despre-viitorul-guvern-sunt-s        | 2025-05-21 | video-transcript          |           293 |              157 |               118 |       0.752 |            16 |
| 2025-05-22_ce-spune-nicusor-dan-despre-relatiile-romaniei-cu-sua-si-ue         | 2025-05-22 | video-transcript          |          2378 |             1129 |               536 |       0.475 |           155 |
| 2025-05-22_nicusor-dan-anunta-primele-masuri-dupa-ce-a-fost-validat            | 2025-05-22 | video-transcript          |           217 |              123 |                84 |       0.683 |            19 |
| 2025-05-22_nicusor-dan-daca-sunt-amenintari-institutiile-isi-vor-face-d        | 2025-05-22 | video-transcript          |           130 |               73 |                47 |       0.644 |            11 |
| 2025-05-22_nicusor-dan-despre-cum-va-evita-romania-atacurile-hibride-tr        | 2025-05-22 | video-transcript          |            71 |               36 |                34 |       0.944 |             4 |
| 2025-05-22_nicusor-dan-despre-subventiile-pentru-partide-b1tv-22-mai-20        | 2025-05-22 | video-transcript          |           270 |              117 |                92 |       0.786 |            22 |
| 2025-05-22_nicusor-dan-o-tinta-realista-de-deficit-este-7-5-din-pib            | 2025-05-22 | video-transcript          |           390 |              185 |               115 |       0.622 |            20 |
| 2025-05-22_nicusor-dan-statul-roman-trebuie-sa-rezolve-obstacolele-pe-c        | 2025-05-22 | video-transcript          |           468 |              199 |               123 |       0.618 |            31 |
| 2025-05-22_nicusor-dan-trebuie-sa-lamurim-anularea-alegerilor-de-anul-t        | 2025-05-22 | video-transcript          |           111 |               65 |                50 |       0.769 |             5 |
| 2025-05-22_nicusor-dan-urmeaza-un-nou-capitol-in-istoria-recenta-si-con        | 2025-05-22 | video-transcript          |            97 |               52 |                46 |       0.885 |             7 |
| 2025-05-22_romania-tinta-atacurilor-hibride-rusesti-nicusor-dan-suntem         | 2025-05-22 | video-transcript          |           410 |              221 |               143 |       0.647 |            18 |
| 2025-05-23_nicusor-dan-propune-o-tinta-de-deficit-bugetar-de-7-5-din-pi        | 2025-05-23 | video-transcript          |           557 |              296 |               182 |       0.615 |            26 |
| 2025-05-24_nicusor-dan-e-un-deficit-de-implicare-in-politica-statul-est        | 2025-05-24 | video-transcript          |           219 |               82 |                62 |       0.756 |             9 |
| 2025-05-26_live-investirea-lui-nicusor-dan-juramantul-de-la-parlament-s        | 2025-05-26 | video-transcript          |         12628 |             6082 |              1514 |       0.249 |           802 |
| 2025-05-26_nicusor-dan-depune-azi-juramantul-de-presedinte-al-romaniei         | 2025-05-26 | video-transcript          |           185 |              106 |                87 |       0.821 |            10 |
| 2025-05-26_nicusor-dan-incepe-o-munca-de-cosmar-ca-presedinte-al-romani        | 2025-05-26 | video-transcript          |          1756 |              813 |               428 |       0.526 |           103 |
| 2025-05-26_nicusor-dan-oficial-presedintele-romaniei-ceremonia-de-inves        | 2025-05-26 | video-transcript          |          1789 |              985 |               457 |       0.464 |            74 |
| 2025-05-26_nicusor-dan-reformele-fiscale-sunt-inevitabile-e-obligatoriu        | 2025-05-26 | video-transcript          |           153 |               72 |                61 |       0.847 |            11 |
| 2025-05-26_stirile-kanal-d-exclusiv-nicusor-dan-primul-discurs-ca-prese        | 2025-05-26 | video-transcript          |          4472 |             2273 |              1070 |       0.471 |           273 |
| 2025-05-27_nicusor-dan-despre-fetita-sa-mi-a-zis-ca-m-am-plictisit-la-d        | 2025-05-27 | video-transcript          |            82 |               38 |                35 |       0.921 |            15 |
| 2025-05-28_mesajul-lui-nicusor-dan-inainte-de-consultarile-de-la-cotroc        | 2025-05-28 | video-transcript          |            81 |               34 |                31 |       0.912 |             9 |
| 2025-05-29_nicusor-dan-explica-de-ce-nu-vrea-un-premier-tehnocrat-in-vi        | 2025-05-29 | video-transcript          |           673 |              298 |               180 |       0.604 |            61 |
| 2025-05-29_nicusor-dan-la-ceremonia-de-ziua-eroilor-primul-eveniment-of        | 2025-05-29 | video-transcript          |           124 |               78 |                56 |       0.718 |            11 |
| 2025-05-30_nicusor-dan-dupa-decizia-ccr-privind-declaratiile-de-avere-d        | 2025-05-30 | video-transcript          |            68 |               35 |                27 |       0.771 |             5 |
| 2025-05-30_nicusor-dan-primele-discutii-cu-partidele-privind-formarea-g        | 2025-05-30 | video-transcript          |           163 |               87 |                69 |       0.793 |            10 |
| 2025-05-30_presedintele-nicusor-dan-l-am-invitat-pe-donald-trump-in-rom        | 2025-05-30 | video-transcript          |           122 |               71 |                46 |       0.648 |             8 |
| 2025-06-02_briefing-nicusor-dan-avem-un-stat-disfunctional-si-trebuie-s        | 2025-06-02 | video-transcript          |          3876 |             1762 |               693 |       0.393 |           231 |
| 2025-06-02_conferinta-presa-nicusor-dan-concluzii-summit-si-situatia-di        | 2025-06-02 | video-transcript          |           290 |              138 |                88 |       0.638 |            17 |
| 2025-06-03_nicusor-dan-anunturi-de-ultima-ora-despre-situatia-economica        | 2025-06-03 | video-transcript          |           552 |              261 |               168 |       0.644 |            32 |
| 2025-06-03_nicusor-dan-cere-implicarea-serviciilor-secrete-pentru-a-com        | 2025-06-03 | video-transcript          |           143 |               68 |                56 |       0.824 |             5 |
| 2025-06-03_romania-lui-vitalie-nicusor-dan-cere-implicarea-serviciilor         | 2025-06-03 | video-transcript          |         14253 |             6464 |              1944 |       0.301 |           766 |
| 2025-06-04_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus_74PzSE | 2025-06-04 | video-transcript          |           585 |              272 |               155 |       0.57  |            35 |
| 2025-06-04_nicusor-dan-amenintarea-ruseasca-vizeaza-toata-europa-relati        | 2025-06-04 | video-transcript          |           232 |              118 |                81 |       0.686 |            10 |
| 2025-06-04_nicusor-dan-despre-cheltuielile-statului-platim-o-pizza-medi        | 2025-06-04 | video-transcript          |             6 |                4 |                 4 |       1     |             1 |
| 2025-06-04_nicusor-dan-despre-situatia-bugetului                               | 2025-06-04 | video-transcript          |            17 |                8 |                 8 |       1     |             1 |
| 2025-06-04_nicusor-dan-luni-vom-avea-o-prima-schita-a-programului-de-gu        | 2025-06-04 | video-transcript          |           120 |               58 |                43 |       0.741 |             8 |
| 2025-06-04_zamfir-si-buzaianu-au-comentat-conferinta-de-presa-a-lui-nic        | 2025-06-04 | video-transcript          |           504 |              232 |               135 |       0.582 |            59 |
| 2025-06-05_alocutiunea-presedintelui-romaniei-nicusor-dan-la-forumul-na        | 2025-06-05 | video-transcript          |             0 |                0 |                 0 |       0     |             0 |
| 2025-06-09_nicusor-dan-taxele-pe-tranzactii-bancare-doar-scenarii-guver        | 2025-06-09 | video-transcript          |           195 |               90 |                67 |       0.744 |            18 |
| 2025-06-10_conferinta-sustinuta-de-presedinta-moldovei-maia-sandu-si-pr        | 2025-06-10 | video-transcript          |          2781 |             1390 |               664 |       0.478 |           170 |
| 2025-06-10_nicusor-dan-a-confirmat-continuarea-sprijinului-romaniei-pen        | 2025-06-10 | video-transcript          |           126 |               67 |                56 |       0.836 |             9 |
| 2025-06-10_presedintele-nicusor-dan-este-in-vizita-la-chisinau-unde-va         | 2025-06-10 | video-transcript          |           942 |              494 |               260 |       0.526 |            46 |
| 2025-06-10_studio-politic-nicusor-dan-romania-sprijina-aderarea-republi        | 2025-06-10 | video-transcript          |          4040 |             1807 |               735 |       0.407 |           268 |
| 2025-06-11_editie-speciala-nicusor-dan-prezinta-prioritatile-partidelor        | 2025-06-11 | video-transcript          |          7990 |             3909 |              1362 |       0.348 |           474 |
| 2025-06-11_taxele-ultima-optiune-nicusor-dan-prioritatea-taierea-unor-c        | 2025-06-11 | video-transcript          |           113 |               61 |                52 |       0.852 |             6 |
| 2025-06-20_declaratie-de-presa-sustinuta-de-presedintele-romaniei-nicus        | 2025-06-20 | video-transcript          |           417 |              205 |               138 |       0.673 |            24 |
| 2025-06-25_nicusor-dan-crestem-cheltuielile-de-aparare-pentru-ca-orice         | 2025-06-25 | video-transcript          |            60 |               25 |                23 |       0.92  |             2 |
| 2025-06-26_declaratia-presedintelui-romaniei-nicusor-dan-dupa-participa        | 2025-06-26 | video-transcript          |           753 |              345 |               207 |       0.6   |            54 |
| 2025-06-26_nicusor-dan-declaratie-de-la-summitul-nato-digi24v-stiriledi        | 2025-06-26 | video-transcript          |            62 |               37 |                29 |       0.784 |             4 |
| 2025-07-14_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus_cp-szg | 2025-07-14 | video-transcript          |          5583 |             2533 |               963 |       0.38  |           338 |
| 2025-07-14_nicusor-dan-despre-cresterea-tva-digi24-stiriledigi24               | 2025-07-14 | video-transcript          |            86 |               39 |                29 |       0.744 |             2 |
| 2025-07-14_nicusor-dan-despre-introducerea-femicidului-in-legislatia-ro        | 2025-07-14 | video-transcript          |           188 |               84 |                69 |       0.821 |            12 |
| 2025-07-14_nicusor-dan-despre-primele-de-pensionare-de-la-ccr-si-pensii        | 2025-07-14 | video-transcript          |           195 |               91 |                66 |       0.725 |            11 |
| 2025-07-14_nicusor-dan-nu-ne-dorim-sa-avem-rusia-ca-vecin-vom-ajuta-ucr        | 2025-07-14 | video-transcript          |            81 |               38 |                30 |       0.789 |             5 |
| 2025-07-14_prima-reactie-a-lui-nicusor-dan-dupa-masurile-fiscale-ale-gu        | 2025-07-14 | video-transcript          |           386 |              201 |               120 |       0.597 |            18 |
| 2025-07-15_nicusor-dan-masura-cresterii-tva-putea-sa-nu-fie-luata              | 2025-07-15 | video-transcript          |           383 |              222 |               141 |       0.635 |            22 |
| 2025-07-16_nicusor-dan-despre-femicid-digi24-stiriledigi24                     | 2025-07-16 | video-transcript          |            87 |               45 |                35 |       0.778 |             3 |
| 2025-07-16_nicusor-dan-despre-femicid-trebuie-sa-ajungem-sa-transmitem         | 2025-07-16 | video-transcript          |           439 |              239 |               136 |       0.569 |            21 |
| 2025-07-18_declaratia-presedintelui-romaniei-nicusor-dan-si-cancelarul         | 2025-07-18 | video-transcript          |          2840 |             1392 |               614 |       0.441 |           158 |
| 2025-07-18_nicusor-dan-despre-interferentele-rusesti-in-alegerile-prezi        | 2025-07-18 | video-transcript          |          2113 |              872 |               435 |       0.499 |           123 |
| 2025-07-21_nicusor-dan-despre-influenta-rusiei-in-alegeri-anuntul-impor        | 2025-07-21 | video-transcript          |           614 |              304 |               210 |       0.691 |            28 |
| 2025-07-25_presedintele-nicusor-dan-prima-aparitie-oficiala-cu-familia         | 2025-07-25 | video-transcript          |           553 |              285 |               177 |       0.621 |            37 |
| 2025-07-25_sindicalistii-din-invatamant-ii-cer-lui-nicusor-dan-sa-nu-pr        | 2025-07-25 | video-transcript          |           284 |              137 |               106 |       0.774 |            17 |
| 2025-07-30_nicusor-dan-propune-reguli-noi-privind-cererile-de-pensionar        | 2025-07-30 | video-transcript          |          4879 |             2232 |               847 |       0.379 |           300 |
| 2025-07-30_ora-14-presedintele-nicusor-dan-sustine-o-conferinta-de-pres        | 2025-07-30 | video-transcript          |         11113 |             5117 |              1545 |       0.302 |           712 |
| 2025-07-30_presedintele-nicusor-dan-sustine-o-conferinta-de-presa-la-or        | 2025-07-30 | video-transcript          |           340 |              191 |               133 |       0.696 |            24 |
| 2025-07-31_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus_nGAQ5B | 2025-07-31 | video-transcript          |         11017 |             5061 |              1527 |       0.302 |           705 |
| 2025-07-31_nicusor-dan-despre-valul-de-pensionari-din-justitie-ce-este         | 2025-07-31 | video-transcript          |           114 |               54 |                45 |       0.833 |             8 |
| 2025-08-24_nicusor-dan-mesaj-pentru-ucraina-ucraina-celebreaza-ziua-ind        | 2025-08-24 | video-transcript          |           488 |              324 |               235 |       0.725 |            20 |
| 2025-08-26_discursul-presedintelui-romaniei-nicusor-dan-cu-ocazia-reuni        | 2025-08-26 | video-transcript          |           862 |              428 |               239 |       0.558 |            46 |
| 2025-08-29_editie-speciala-nicusor-dan-reactioneaza-in-cazul-livratorul        | 2025-08-29 | video-transcript          |         10887 |             5239 |              1929 |       0.368 |           713 |
| 2025-08-31_nicusor-dan-sunteti-mai-europeni-decat-europenii-si-locul-du        | 2025-08-31 | video-transcript          |            52 |               23 |                22 |       0.957 |             2 |
| 2025-09-01_nicusor-dan-2025-si-2026-vor-fi-ani-dificili-pentru-romani          | 2025-09-01 | video-transcript          |           214 |               87 |                65 |       0.747 |             9 |
| 2025-09-02_conferinta-presedintele-romaniei-nicusor-dan-si-presedinta-c        | 2025-09-02 | video-transcript          |          1803 |              884 |               467 |       0.528 |           157 |
| 2025-09-03_nicusor-dan-coalitia-de-guvernare-functioneaza-si-va-merge-i        | 2025-09-03 | video-transcript          |           108 |               54 |                40 |       0.741 |             9 |
| 2025-09-03_nicusor-dan-energia-nucleara-reprezinta-20-din-necesarul-de         | 2025-09-03 | video-transcript          |           299 |              142 |               102 |       0.718 |            15 |
| 2025-09-05_nicusor-dan-despre-pensiile-specialilor-au-fost-suprasolicit        | 2025-09-05 | video-transcript          |           203 |              105 |                78 |       0.743 |            11 |
| 2025-09-05_nicusor-dan-romania-nu-va-trimite-trupe-de-mentinere-a-pacii        | 2025-09-05 | video-transcript          |           119 |               57 |                41 |       0.719 |             8 |
| 2025-09-10_alocutiunea-presedintelui-romaniei-nicusor-dan-sustinuta-in         | 2025-09-10 | video-transcript          |             0 |                0 |                 0 |       0     |             0 |
| 2025-09-10_nicusor-dan-daca-se-va-intampla-si-la-noi-vom-reactiona-la-f        | 2025-09-10 | video-transcript          |           131 |               58 |                50 |       0.862 |             8 |
| 2025-09-11_ce-spune-nicusor-dan-despre-vizita-in-sua-sper-sa-fie-o-vizi        | 2025-09-11 | video-transcript          |           164 |               74 |                52 |       0.703 |            15 |
| 2025-09-11_nicusor-dan-daca-ucraina-cedeaza-romania-ar-fi-vecina-direct        | 2025-09-11 | video-transcript          |           748 |              323 |               207 |       0.641 |            49 |
| 2025-09-11_nicusor-dan-de-zece-ani-romania-e-in-razboiul-hibrid-al-fede        | 2025-09-11 | video-transcript          |          1437 |              640 |               313 |       0.489 |           100 |
| 2025-09-11_nicusor-dan-despre-cresterea-aur-in-sondaje-arata-ca-cei-40         | 2025-09-11 | video-transcript          |           672 |              289 |               188 |       0.651 |            39 |
| 2025-09-12_nicusor-dan-romania-de-10-ani-sub-atacul-hibrid-al-rusiei-ab        | 2025-09-12 | video-transcript          |           134 |               63 |                46 |       0.73  |             8 |
| 2025-09-16_nicusor-dan-reactie-dupa-incidentul-din-spatiul-aerian-roman        | 2025-09-16 | video-transcript          |           172 |               80 |                61 |       0.762 |            11 |
| 2025-09-16_nicusor-dan-we-don-t-know-if-the-russian-drone-was-armed            | 2025-09-16 | video-transcript          |           139 |               61 |                41 |       0.672 |            13 |
| 2025-09-23_nicusor-dan-cere-responsabilitate-liderilor-coalitiei-romani        | 2025-09-23 | video-transcript          |           675 |              328 |               208 |       0.634 |            37 |
| 2025-09-25_nicusor-dan-au-fost-80-000-de-atacuri-cibernetice-in-perioad        | 2025-09-25 | video-transcript          |           129 |               51 |                47 |       0.922 |             8 |
| 2025-09-25_nicusor-dan-georgescu-nu-a-fost-un-calaret-singuratic-in-jur        | 2025-09-25 | video-transcript          |           104 |               38 |                28 |       0.737 |             7 |
| 2025-09-25_nicusor-dan-nu-vad-rusia-capabila-sa-atace-nato-dar-provocar        | 2025-09-25 | video-transcript          |           154 |               76 |                60 |       0.789 |             8 |
| 2025-09-25_nicusor-dan-primul-interviu-dupa-sedinta-csat-la-digi24             | 2025-09-25 | video-transcript          |          3836 |             1692 |               709 |       0.419 |           271 |
| 2025-09-25_nicusor-dan-primul-interviu-dupa-sedinta-csat-rusia-ramane-i        | 2025-09-25 | video-transcript          |          5563 |             2449 |               976 |       0.399 |           376 |
| 2025-09-26_nicusor-dan-despre-influenta-sri-in-romania-stiri-b1tv-26-se        | 2025-09-26 | video-transcript          |           186 |               95 |                66 |       0.695 |            10 |
| 2025-09-26_nicusor-dan-sri-a-intervenit-in-viata-politica-si-economica         | 2025-09-26 | video-transcript          |           235 |              111 |                75 |       0.676 |            10 |
| 2025-09-30_nicusor-dan-a-anuntat-cand-va-desecretiza-sedinta-csat-si-ac        | 2025-09-30 | video-transcript          |           170 |               75 |                58 |       0.773 |            10 |
| 2025-09-30_nicusor-dan-avem-dovada-cu-peschir-banuim-ca-au-fost-20-de-m        | 2025-09-30 | video-transcript          |           208 |               69 |                53 |       0.768 |            15 |
| 2025-09-30_nicusor-dan-despre-aderarea-moldovei-la-ue-poate-fi-facuta-c        | 2025-09-30 | video-transcript          |           190 |               90 |                63 |       0.7   |            15 |
| 2025-09-30_nicusor-dan-despre-anularea-alegerilor-avem-dovada-ca-au-fos        | 2025-09-30 | video-transcript          |           397 |              168 |               116 |       0.69  |            19 |
| 2025-09-30_nicusor-dan-despre-stagiul-militar-voluntar-romania-sa-aiba         | 2025-09-30 | video-transcript          |           247 |              110 |                76 |       0.691 |            12 |
| 2025-10-02_nicusor-dan-amenin-area-nu-mai-este-o-chestiune-de-vecinatat        | 2025-10-02 | video-transcript          |            77 |               27 |                23 |       0.852 |             2 |
| 2025-10-02_nicusor-dan-zidul-anti-drone-ar-putea-fi-operational-in-cate        | 2025-10-02 | video-transcript          |           447 |              214 |               140 |       0.654 |            20 |
| 2025-10-14_studio-politic-nicusor-dan-vrea-sa-implice-sri-in-lupta-anti        | 2025-10-14 | video-transcript          |          6227 |             2860 |              1012 |       0.354 |           302 |
| 2025-10-21_nicusor-dan-in-principiu-imi-doresc-un-al-doilea-mandat-la-c        | 2025-10-21 | video-transcript          |            73 |               30 |                26 |       0.867 |             5 |
| 2025-10-23_nicusor-dan-avem-un-razboi-hibrid-de-cel-putin-10-ani               | 2025-10-23 | video-transcript          |           541 |              255 |               156 |       0.612 |            37 |
| 2025-10-23_nicusor-dan-trebuie-sa-ne-echipam-ca-sa-descurajam-rusia-de         | 2025-10-23 | video-transcript          |           108 |               50 |                42 |       0.84  |             7 |
| 2025-10-24_nicusor-dan-a-society-is-defined-by-the-institutions-it-has         | 2025-10-24 | video-transcript          |           295 |              139 |                95 |       0.683 |            14 |
| 2025-10-27_nicusor-dan-catedrala-nationala-simbol-de-speranta-intr-o-pe        | 2025-10-27 | video-transcript          |           213 |              129 |               105 |       0.814 |             7 |
| 2025-11-02_nicusor-dan-reactie-despre-reducerea-numarului-de-militari-a        | 2025-11-02 | video-transcript          |          1083 |              537 |               277 |       0.516 |            69 |
| 2025-11-06_rutte-nato-isi-va-juca-rolul-sau-nicusor-dan-reinarmarea-nu         | 2025-11-06 | video-transcript          |          1720 |              845 |               444 |       0.525 |            95 |
| 2025-11-07_nicusor-dan-despre-intalnirea-lui-bolojan-nu-cred-ca-premier        | 2025-11-07 | video-transcript          |           190 |               94 |                69 |       0.734 |            21 |
| 2025-11-07_nicusor-dan-despre-salariul-minim-sa-inghete                        | 2025-11-07 | video-transcript          |           105 |               57 |                44 |       0.772 |             6 |
| 2025-11-11_nicusor-dan-declaratia-oanei-gheorghiu-e-nefericita-reactia         | 2025-11-11 | video-transcript          |          2085 |             1032 |               509 |       0.493 |           115 |
| 2025-11-11_posibile-fragmente-de-drona-cazute-in-tulcea-nicusor-dan-a-f        | 2025-11-11 | video-transcript          |          1255 |              619 |               324 |       0.523 |            59 |
| 2025-11-11_presedintele-romaniei-nicusor-dan-despre-pensii-si-justitie         | 2025-11-11 | video-transcript          |           106 |               43 |                31 |       0.721 |             6 |
| 2025-11-12_ce-l-a-socat-pe-nicusor-dan-dupa-ce-a-ajuns-presedinte              | 2025-11-12 | video-transcript          |           133 |               58 |                48 |       0.828 |             9 |
| 2025-11-12_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus_6l2Eup | 2025-11-12 | video-transcript          |          6289 |             2811 |              1017 |       0.362 |           377 |
| 2025-11-12_nicusor-dan-conferinta-de-presa-presedintele-prezinta-strate        | 2025-11-12 | video-transcript          |          5699 |             2738 |              1140 |       0.416 |           340 |
| 2025-11-12_nicusor-dan-e-mai-bine-sa-fii-vecin-cu-ucraina-decat-cu-rusi        | 2025-11-12 | video-transcript          |           183 |               71 |                51 |       0.718 |             6 |
| 2025-11-12_nicusor-dan-nu-ne-dorim-sa-fim-vecini-cu-rusia                      | 2025-11-12 | video-transcript          |           389 |              169 |               123 |       0.728 |            18 |
| 2025-11-12_nicusor-dan-nu-vrem-sa-aparam-statul-vrem-sa-aparam-cetateni        | 2025-11-12 | video-transcript          |          1715 |              827 |               402 |       0.486 |            80 |
| 2025-11-12_nicusor-dan-serviciile-de-informatii-vor-fi-implicate-in-lup        | 2025-11-12 | video-transcript          |            89 |               44 |                39 |       0.886 |             7 |
| 2025-11-21_nicusor-dan-despre-aducerea-in-tara-a-mercenarului-horatiu-p        | 2025-11-21 | video-transcript          |            75 |               38 |                32 |       0.842 |             5 |
| 2025-11-21_nicusor-dan-orice-plan-de-pace-trebuie-aprobat-de-ucraina           | 2025-11-21 | video-transcript          |          2115 |             1055 |               491 |       0.465 |           176 |
| 2025-11-21_prima-reactie-a-lui-nicusor-dan-dupa-informatiile-aparute-cu        | 2025-11-21 | video-transcript          |           160 |               73 |                44 |       0.603 |            11 |
| 2025-11-26_nicusor-dan-declaratii-din-parlament-despre-problemele-inter        | 2025-11-26 | video-transcript          |          1001 |              502 |               298 |       0.594 |            48 |
| 2025-11-26_nicusor-dan-declaratii-dupa-sustinerea-discursului-in-parlam        | 2025-11-26 | video-transcript          |           538 |              241 |               166 |       0.689 |            25 |
| 2025-11-26_nicusor-dan-drone-care-din-cand-in-cand-intra-pe-teritoriul         | 2025-11-26 | video-transcript          |           142 |               62 |                49 |       0.79  |            10 |
| 2025-11-26_nicusor-dan-vom-sustine-in-continuare-ucraina-si-republica-m        | 2025-11-26 | video-transcript          |            46 |               27 |                23 |       0.852 |             5 |
| 2025-12-01_a-inceput-parada-militara-la-arcul-de-triumf-nicusor-dan-pre        | 2025-12-01 | video-transcript          |          1362 |              707 |               402 |       0.569 |            83 |
| 2025-12-01_nicusor-dan-mesaj-de-ziua-nationala-e-o-zi-de-sarbatoare-sa         | 2025-12-01 | video-transcript          |           138 |               65 |                52 |       0.8   |            18 |
| 2025-12-01_nicusor-dan-suntem-membri-ai-ue-dar-de-multe-ori-vocea-roman        | 2025-12-01 | video-transcript          |            67 |               34 |                29 |       0.853 |             3 |
| 2025-12-02_nicusor-dan-mesaj-de-1-decembrie-digi24-stiriledigi24               | 2025-12-02 | video-transcript          |           152 |               66 |                46 |       0.697 |             9 |
| 2025-12-02_nicusor-dan-mesaj-de-1-decembrie-totusi-suntem-mai-putin-cor        | 2025-12-02 | video-transcript          |          7337 |             3364 |              1242 |       0.369 |           456 |
| 2025-12-03_nicusor-dan-despre-criza-apei-potabile-din-prahova-vinova-ia        | 2025-12-03 | video-transcript          |          1326 |              610 |               329 |       0.539 |            88 |
| 2025-12-03_nicusor-dan-despre-criza-apei-potabile-din-prahova-vinova-ia_cxJ5Wc | 2025-12-03 | video-transcript          |            84 |               35 |                32 |       0.914 |             6 |
| 2025-12-03_nicusor-dan-dupa-amenintarile-lui-putin-sunt-declaratii-pent        | 2025-12-03 | video-transcript          |            73 |               39 |                28 |       0.718 |             7 |
| 2025-12-03_nicusor-dan-vinovatia-este-la-apele-romane                          | 2025-12-03 | video-transcript          |           401 |              187 |               121 |       0.647 |            24 |
| 2025-12-04_bomba-lui-nicusor-dan-serviciile-au-stiut-cine-este-calin-ge        | 2025-12-04 | video-transcript          |           135 |               59 |                39 |       0.661 |             9 |
| 2025-12-04_nicusor-dan-despre-alegerile-anulate-au-aparut-suficiente-in        | 2025-12-04 | video-transcript          |           208 |               98 |                73 |       0.745 |            14 |
| 2025-12-04_nicusor-dan-despre-demisia-lui-mosteanu-intensitatea-critici        | 2025-12-04 | video-transcript          |           263 |              127 |                82 |       0.646 |            14 |
| 2025-12-04_nicusor-dan-vinovatia-este-la-apele-romane-newsroom-din-3-de        | 2025-12-04 | video-transcript          |          5654 |             2697 |              1023 |       0.379 |           391 |
| 2025-12-07_presedintele-nicusor-dan-de-mult-nu-am-mai-votat-pentru-altc        | 2025-12-07 | video-transcript          |           104 |               34 |                30 |       0.882 |             5 |
| 2025-12-08_l-orban-a-izbucnit-in-ras-dupa-mesajul-transmis-de-nicusor-d        | 2025-12-08 | video-transcript          |           305 |              154 |               110 |       0.714 |            20 |
| 2025-12-09_nicusor-dan-nu-vad-vreun-motiv-pentru-care-un-ministru-trebu        | 2025-12-09 | video-transcript          |           108 |               44 |                37 |       0.841 |             5 |
| 2025-12-10_nicusor-dan-nu-toti-votantii-aur-sunt-extremisti-stiri-b1tv         | 2025-12-10 | video-transcript          |           210 |               94 |                69 |       0.734 |            12 |
| 2025-12-10_romania-lui-vitalie-nicusor-dan-despre-strategia-de-securita        | 2025-12-10 | video-transcript          |         11471 |             5555 |              1846 |       0.332 |           781 |
| 2025-12-11_nicusor-dan-judecatorii-sa-se-implice-in-rezolvarea-probleme        | 2025-12-11 | video-transcript          |           196 |               92 |                66 |       0.717 |            10 |
| 2025-12-12_bolojan-anunta-ca-a-discutat-cu-nicusor-dan-dupa-acuzatiile         | 2025-12-12 | video-transcript          |          3269 |             1474 |               625 |       0.424 |           214 |
| 2025-12-15_nicusor-dan-anunturi-majore-in-scandalurile-momentului              | 2025-12-15 | video-transcript          |           320 |              136 |               104 |       0.765 |            18 |
| 2025-12-15_nicusor-dan-dupa-guta-buna-romania-b1tv-15-dec-2025                 | 2025-12-15 | video-transcript          |          1065 |              441 |               235 |       0.533 |            95 |
| 2025-12-15_nicusor-dan-voi-actiona-pentru-apararea-independentei-justit        | 2025-12-15 | video-transcript          |           286 |              136 |                98 |       0.721 |            12 |
| 2025-12-16_ciucu-spune-ce-a-gasit-la-primarie-dupa-nicusor-dan-lucruril        | 2025-12-16 | video-transcript          |           258 |              127 |                88 |       0.693 |            17 |
| 2025-12-16_nicusor-dan-declara-ca-rusia-va-continua-sa-fie-o-amenintare        | 2025-12-16 | video-transcript          |          1004 |              472 |               277 |       0.587 |            49 |
| 2025-12-16_nicusor-dan-sunt-destul-de-pesimist-cu-privire-la-intentia-r        | 2025-12-16 | video-transcript          |           484 |              288 |               213 |       0.74  |            26 |
| 2025-12-16_nicusor-dan-trebuie-sa-fim-calmi-dar-sa-investim-in-aparare         | 2025-12-16 | video-transcript          |           102 |               56 |                49 |       0.875 |             6 |
| 2025-12-17_declaratia-presedintelui-romaniei-nicusor-dan-in-regatul-mar        | 2025-12-17 | video-transcript          |          1259 |              575 |               324 |       0.563 |            86 |
| 2025-12-17_nicusor-dan-despre-cresterea-impozitelor-nu-e-nici-fericire         | 2025-12-17 | video-transcript          |           100 |               46 |                37 |       0.804 |             7 |
| 2025-12-17_nicusor-dan-sunt-probleme-la-modul-in-care-se-fac-promovaril        | 2025-12-17 | video-transcript          |           866 |              429 |               241 |       0.562 |            59 |
| 2025-12-18_nicusor-dan-avem-atacuri-cibernetice-campanie-de-dezinformar        | 2025-12-18 | video-transcript          |           262 |              100 |                78 |       0.78  |            16 |
| 2025-12-18_nicusor-dan-primit-de-regele-charles-stiri-b1tv-18-dec-2025         | 2025-12-18 | video-transcript          |           110 |               58 |                47 |       0.81  |             5 |
| 2025-12-18_nicusor-dan-problema-fundamentala-este-de-ce-nu-reusim-in-15        | 2025-12-18 | video-transcript          |            47 |               22 |                19 |       0.864 |             3 |
| 2025-12-18_nicusor-dan-problema-fundamentala-este-de-ce-nu-reusim-in-15_wynkjt | 2025-12-18 | video-transcript          |           865 |              455 |               291 |       0.64  |            33 |
| 2025-12-18_nicusor-dan-sustinem-oricare-dintre-variantele-de-ajutor-fin        | 2025-12-18 | video-transcript          |           431 |              205 |               134 |       0.654 |            20 |
| 2025-12-19_nicusor-dan-anunt-inainte-de-intalnirea-cu-magistratii              | 2025-12-19 | video-transcript          |            87 |               49 |                38 |       0.776 |             6 |
| 2025-12-21_declaratia-presedintelui-romaniei-nicusor-dan-pe-tema-proble        | 2025-12-21 | video-transcript          |          1321 |              565 |               288 |       0.51  |            50 |
| 2025-12-21_nicusor-dan-exista-magistrati-care-actioneaza-in-interesul-u        | 2025-12-21 | video-transcript          |           954 |              459 |               255 |       0.556 |            37 |
| 2025-12-21_nicusor-dan-exista-magistrati-care-actioneaza-in-interesul-u_i-HYCW | 2025-12-21 | video-transcript          |           108 |               54 |                44 |       0.815 |             3 |
| 2025-12-21_nicusor-dan-magistratii-intimidati-inainte-de-discutiile-de         | 2025-12-21 | video-transcript          |          2578 |             1141 |               464 |       0.407 |            88 |
| 2025-12-21_nicusor-dan-magistratii-intimidati-inainte-de-discutiile-de__MoX2e  | 2025-12-21 | video-transcript          |           125 |               49 |                45 |       0.918 |             4 |
| 2025-12-21_nicusor-dan-voi-face-un-referendum-daca-csm-nu-actioneaza-in        | 2025-12-21 | video-transcript          |           122 |               69 |                43 |       0.623 |             3 |
| 2025-12-21_nicusor-dan-voi-initia-in-ianuarie-un-referendum-in-cadrul-c        | 2025-12-21 | video-transcript          |           178 |               84 |                55 |       0.655 |             6 |
| 2025-12-22_discutii-publice-la-cotroceni-intre-presedintele-romaniei-ni_7lGgIp | 2025-12-22 | video-transcript          |         23573 |            11107 |              2562 |       0.231 |          1181 |
| 2025-12-22_nicusor-dan-anunta-un-referendum-printre-magistrati-digi24          | 2025-12-22 | video-transcript          |           146 |               81 |                50 |       0.617 |             6 |
| 2025-12-22_nicusor-dan-multe-dintre-cele-semnalate-necesita-verificari         | 2025-12-22 | video-transcript          |            49 |               26 |                20 |       0.769 |             2 |
| 2025-12-22_opozitia-vrea-suspendarea-lui-nicusor-dan-dupa-anuntul-despr        | 2025-12-22 | video-transcript          |           120 |               76 |                62 |       0.816 |             6 |
| 2026-01-01_nicusor-dan-mesaj-de-anul-nou-drumul-nu-va-fi-usor                  | 2026-01-01 | video-transcript          |           230 |              122 |                80 |       0.656 |            12 |
| 2026-01-01_nicusor-dan-mesaj-de-condoleante-dupa-incediul-din-elvetia          | 2026-01-01 | video-transcript          |            72 |               41 |                37 |       0.902 |             4 |
| 2026-01-06_declaratia-presedintelui-romaniei-nicusor-dan-dupa-participa_iZQQF2 | 2026-01-06 | video-transcript          |          2177 |              998 |               488 |       0.489 |           135 |
| 2026-01-06_nicusor-dan-declaratii-la-bordul-avionului-spartan-cu-care-a        | 2026-01-06 | video-transcript          |            46 |               24 |                18 |       0.75  |             2 |
| 2026-01-06_nicusor-dan-suntem-intr-un-context-international-dificil            | 2026-01-06 | video-transcript          |            90 |               48 |                35 |       0.729 |             9 |
| 2026-01-07_garantii-de-securitate-pentru-ucraina-si-mize-interne-nicuso        | 2026-01-07 | video-transcript          |          2920 |             1340 |               604 |       0.451 |           170 |
| 2026-01-07_nicusor-dan-e-nevoie-de-un-avion-prezidential                       | 2026-01-07 | video-transcript          |           270 |              109 |                85 |       0.78  |            26 |
| 2026-01-07_nicusor-dan-mi-ar-fi-placut-mai-degraba-ca-taxele-sa-scada          | 2026-01-07 | video-transcript          |           191 |               83 |                62 |       0.747 |             9 |
| 2026-01-12_sefa-curtii-de-apel-bucuresti-cere-intalnire-cu-nicusor-dan         | 2026-01-12 | video-transcript          |           246 |              132 |                83 |       0.629 |            11 |
| 2026-01-15_nicusor-dan-despre-taierile-pentru-romani-dureroase-dar-obli        | 2026-01-15 | video-transcript          |            91 |               51 |                45 |       0.882 |             6 |
| 2026-01-15_nicusor-dan-ne-asteapta-o-perioada-complicata-si-dificil-de         | 2026-01-15 | video-transcript          |            82 |               47 |                46 |       0.979 |             4 |
| 2026-01-15_nicusor-dan-romania-sustine-pacea-in-ucraina-si-integrarea-r        | 2026-01-15 | video-transcript          |          2033 |             1184 |               623 |       0.526 |            97 |
| 2026-01-20_nicusor-dan-anunta-azi-daca-merge-la-davos-pentru-consiliul         | 2026-01-20 | video-transcript          |           463 |              269 |               148 |       0.55  |            18 |
| 2026-01-22_nicusor-dan-despre-pozitia-romaniei-cu-privire-la-groenlanda        | 2026-01-22 | video-transcript          |           327 |              154 |               106 |       0.688 |            16 |
| 2026-01-23_nicusor-dan-explica-ce-inseamna-ca-nu-a-mers-teleleu-la-davo        | 2026-01-23 | video-transcript          |           115 |               51 |                41 |       0.804 |            13 |
| 2026-01-24_discursul-lui-nicusor-dan-de-la-iasi-bruiat-de-simpatizantii        | 2026-01-24 | video-transcript          |           440 |              176 |               111 |       0.631 |            26 |
| 2026-01-24_huiduieli-si-aplauze-la-focsani-nicusor-dan-este-un-drept-pe        | 2026-01-24 | video-transcript          |           355 |              136 |                88 |       0.647 |            24 |
| 2026-01-24_iasi-nicusor-dan-prezent-la-ceremonia-de-ziua-unirii-princip        | 2026-01-24 | video-transcript          |           648 |              342 |               189 |       0.553 |            47 |
| 2026-01-24_nicusor-dan-e-democratie-e-libertate-sa-spuna-fiecare-ce-vre        | 2026-01-24 | video-transcript          |          1821 |              794 |               400 |       0.504 |           129 |
| 2026-01-24_nicusor-dan-la-multi-ani-dragi-focsaneni-care-huiduiti-autor        | 2026-01-24 | video-transcript          |            91 |               38 |                25 |       0.658 |            10 |
| 2026-01-24_nicusor-dan-mae-analizeaza-participarea-romaniei-la-consiliu        | 2026-01-24 | video-transcript          |            97 |               48 |                38 |       0.792 |             6 |
| 2026-01-24_nicusor-dan-nu-facem-comedii-din-relatia-intre-guvern-si-par        | 2026-01-24 | video-transcript          |           175 |               94 |                56 |       0.596 |            16 |
| 2026-01-24_ziua-unirii-principatelor-umbrita-de-proteste-discursul-lui         | 2026-01-24 | video-transcript          |           659 |              323 |               194 |       0.601 |            44 |
| 2026-01-30_nicusor-dan-despre-numirile-la-sri-si-sie-digi24-stiriledigi        | 2026-01-30 | video-transcript          |           158 |               64 |                49 |       0.766 |            10 |
| 2026-01-30_nicusor-dan-despre-tensiunile-din-coalitie-nu-exista-alterna        | 2026-01-30 | video-transcript          |          3322 |             1488 |               676 |       0.454 |           233 |
| 2026-01-30_nicusor-dan-despre-tensiunile-din-coalitie-nu-exista-alterna_9sksTM | 2026-01-30 | video-transcript          |            80 |               35 |                29 |       0.829 |            10 |
| 2026-01-30_nicusor-dan-despre-vizita-in-sua-digi24-stiriledigi24               | 2026-01-30 | video-transcript          |           102 |               44 |                34 |       0.773 |             6 |
| 2026-01-30_nicusor-dan-nu-exista-risc-de-crestere-de-taxe-in-viitorul-a        | 2026-01-30 | video-transcript          |           112 |               38 |                35 |       0.921 |             6 |
| 2026-01-30_nicusor-dan-un-guvern-minoritar-putin-probabil-bolojan-a-rap        | 2026-01-30 | video-transcript          |           183 |               96 |                70 |       0.729 |            11 |
| 2026-02-09_participa-sau-nu-romania-la-consiliul-pentru-pace-al-lui-tru        | 2026-02-09 | video-transcript          |          6189 |             2903 |              1144 |       0.394 |           409 |
| 2026-02-12_ce-spune-nicusor-dan-despre-participarea-romaniei-la-prima-e        | 2026-02-12 | video-transcript          |           114 |               53 |                39 |       0.736 |             7 |
| 2026-02-12_declaratii-de-presa-sustinute-de-presedintele-romaniei-nicus        | 2026-02-12 | video-transcript          |          1098 |              515 |               263 |       0.511 |            66 |
| 2026-02-12_nicusor-dan-anunt-de-la-consiliul-european-il-refuza-din-nou        | 2026-02-12 | video-transcript          |          2089 |              979 |               442 |       0.451 |           102 |
| 2026-02-12_nicusor-dan-despre-candidatii-la-sefia-parchetelor-sunt-pers        | 2026-02-12 | video-transcript          |           164 |               81 |                55 |       0.679 |            10 |
| 2026-02-12_nicusor-dan-dupa-summitul-din-belgia-comisia-europeana-va-pr        | 2026-02-12 | video-transcript          |          4030 |             1822 |               729 |       0.4   |           216 |
| 2026-02-12_nicusor-dan-este-evidenta-tergiversarea-ccr-imi-doresc-o-asu        | 2026-02-12 | video-transcript          |           150 |               73 |                50 |       0.685 |             9 |
| 2026-02-12_nicusor-dan-pretul-energiei-este-o-chestiune-foarte-importan        | 2026-02-12 | video-transcript          |           113 |               50 |                39 |       0.78  |             4 |
| 2026-02-12_nicusor-dan-romania-poate-fi-cel-mult-observator-in-consiliu        | 2026-02-12 | video-transcript          |           268 |              113 |                74 |       0.655 |            12 |
| 2026-02-13_declaratiile-presedintelui-romaniei-nicusor-dan-dupa-reuniun        | 2026-02-13 | video-transcript          |          3287 |             1462 |               637 |       0.436 |           175 |
| 2026-02-13_nicusor-dan-despre-propunerile-privind-scaderea-pretului-ene        | 2026-02-13 | video-transcript          |            85 |               41 |                33 |       0.805 |             5 |
| 2026-02-13_nicusor-dan-in-ciuda-atacurilor-coalitia-functioneaza-mai-bi        | 2026-02-13 | video-transcript          |           244 |               98 |                63 |       0.643 |            10 |
| 2026-02-17_nicusor-dan-a-anuntat-ca-romania-va-participa-la-consiliul-p        | 2026-02-17 | video-transcript          |           144 |               67 |                54 |       0.806 |             9 |
| 2026-02-17_nicusor-dan-prezenta-la-consiliul-de-pace-necesara-dupa-anul        | 2026-02-17 | video-transcript          |           201 |               98 |                70 |       0.714 |            10 |
| 2026-02-17_nicusor-dan-prezenta-la-consiliul-de-pace-necesara-dupa-anul_yYS5fW | 2026-02-17 | video-transcript          |           160 |               78 |                60 |       0.769 |             7 |
| 2026-02-19_declaratii-de-presa-sustinute-de-presedintele-romaniei-nicus        | 2026-02-19 | video-transcript          |          1237 |              565 |               338 |       0.598 |            78 |
| 2026-02-19_interviu-exclusiv-cu-nicusor-dan-dupa-intalnirea-cu-trump           | 2026-02-19 | video-transcript          |          2007 |              854 |               413 |       0.484 |            97 |
| 2026-02-19_nicusor-dan-discurs-la-consiliul-pentru-pace-in-sua-avem-bur        | 2026-02-19 | video-transcript          |           185 |               88 |                65 |       0.739 |            14 |
| 2026-02-19_prima-reactie-a-lui-nicusor-dan-dupa-ce-donald-trump-l-a-num        | 2026-02-19 | video-transcript          |            27 |               16 |                15 |       0.938 |             7 |
| 2026-02-20_nicusor-dan-nu-alegem-intre-sua-si-ue-romania-trebuie-sa-fie        | 2026-02-20 | video-transcript          |           113 |               55 |                39 |       0.709 |             8 |
| 2026-02-20_presedintele-nicusor-dan-problema-legitimitatii-administrati        | 2026-02-20 | video-transcript          |          1054 |              487 |               264 |       0.542 |            80 |
| 2026-02-24_nicusor-dan-explica-de-ce-nu-a-promulgat-legea-pensiilor-spe        | 2026-02-24 | video-transcript          |            78 |               42 |                38 |       0.905 |             6 |
| 2026-02-24_nicusor-dan-mesaj-de-sustinere-fata-de-ucraina-la-patru-ani         | 2026-02-24 | video-transcript          |           173 |              106 |                83 |       0.783 |            11 |
| 2026-02-27_acum-nicusor-dan-a-promulgat-reforma-pensiilor-magistratilor        | 2026-02-27 | video-transcript          |           248 |              143 |                92 |       0.643 |            13 |
| 2026-02-27_nicusor-dan-a-promulgat-reforma-pensiilor-magistratilor             | 2026-02-27 | video-transcript          |           241 |              126 |                89 |       0.706 |            14 |
| 2026-03-05_acum-nicusor-dan-anunta-daca-romania-va-gazdui-arme-nucleare        | 2026-03-05 | video-transcript          |           442 |              218 |               146 |       0.67  |            24 |
| 2026-03-05_nicusor-dan-conferinta-de-presa-in-polonia-stiri-b1tv-5-mar         | 2026-03-05 | video-transcript          |          2059 |             1056 |               557 |       0.527 |           124 |
| 2026-03-05_nicusor-dan-despre-propunerile-pentru-sefia-parchetelor-stir        | 2026-03-05 | video-transcript          |           206 |               87 |                69 |       0.793 |             7 |
| 2026-03-05_nicusor-dan-despre-scumpirile-la-pompa-nu-putem-umbla-la-acc        | 2026-03-05 | video-transcript          |           273 |              139 |                92 |       0.662 |            15 |
| 2026-03-05_nicusor-dan-despre-situatia-din-orient-nu-o-sa-plangem-iranu        | 2026-03-05 | video-transcript          |            83 |               47 |                40 |       0.851 |             6 |
| 2026-03-05_nicusor-dan-despre-umbrela-nucleara-propusa-de-franta-stiri         | 2026-03-05 | video-transcript          |           213 |              111 |                80 |       0.721 |             8 |
| 2026-03-05_nicusor-dan-dezbaterea-pe-buget-este-o-dezbatere-legitima           | 2026-03-05 | video-transcript          |            69 |               30 |                28 |       0.933 |             2 |
| 2026-03-05_nicusor-dan-nu-o-sa-plangem-republica-islamica-iran                 | 2026-03-05 | video-transcript          |           133 |               67 |                58 |       0.866 |             8 |
| 2026-03-05_nicusor-dan-polonia-participa-la-brigada-multinationala-care        | 2026-03-05 | video-transcript          |           179 |               90 |                61 |       0.678 |             8 |
| 2026-03-05_nicusor-dan-polonia-si-romania-impreuna-au-multe-oportunitat        | 2026-03-05 | video-transcript          |          1933 |              937 |               485 |       0.518 |            95 |
| 2026-03-05_nicusor-dan-romania-este-acoperita-de-o-umbrela-nucleara            | 2026-03-05 | video-transcript          |            63 |               29 |                25 |       0.862 |             4 |
| 2026-03-05_pretul-carburantilor-nicusor-dan-exclude-modificarea-taxelor        | 2026-03-05 | video-transcript          |           146 |               72 |                52 |       0.722 |             7 |
| 2026-03-06_declaratii-de-presa-sustinute-de-presedintele-romaniei-nicus_Ry-ZYl | 2026-03-06 | video-transcript          |          1931 |              935 |               481 |       0.514 |            95 |
| 2026-03-06_nicusor-dan-romania-nu-va-gazdui-focoase-nucleare-in-viitoru        | 2026-03-06 | video-transcript          |           167 |               92 |                63 |       0.685 |             8 |
| 2026-03-07_nicusor-dan-imi-voi-asuma-in-justitie-vin-din-societatea-civ        | 2026-03-07 | video-transcript          |           191 |               92 |                67 |       0.728 |            13 |
| 2026-03-11_ce-trimite-sua-in-tara-noastra-declaratiile-lui-nicusor-dan         | 2026-03-11 | video-transcript          |           139 |               67 |                49 |       0.731 |             8 |
| 2026-03-11_declaratie-sustinuta-de-presedintele-romaniei-nicusor-dan-du        | 2026-03-11 | video-transcript          |           504 |              246 |               159 |       0.646 |            27 |
| 2026-03-12_discursul-lui-nicusor-dan-dupa-intrevederea-cu-zelenski-stir        | 2026-03-12 | video-transcript          |             0 |                0 |                 0 |       0     |             0 |
| 2026-03-12_nicusor-dan-we-will-produce-drones-in-romania-together-with         | 2026-03-12 | video-transcript          |           472 |              240 |               139 |       0.579 |            27 |
| 2026-03-13_conferinta-sustinuta-de-presedintii-romaniei-si-ucrainei-nic        | 2026-03-13 | video-transcript          |          3520 |             1700 |               673 |       0.396 |           210 |
| 2026-03-16_nicusor-dan-resursele-de-petrol-ale-tarii-insuficiente-rafin        | 2026-03-16 | video-transcript          |           368 |              198 |               138 |       0.697 |            15 |
| 2026-03-19_conferinta-presedintelui-romaniei-nicusor-dan-si-a-secretaru        | 2026-03-19 | video-transcript-diarizat |           461 |              194 |               125 |       0.644 |            26 |
| 2026-03-19_nicusor-dan-romania-has-taken-a-clear-position-on-the-transa        | 2026-03-19 | video-transcript          |           151 |               61 |                48 |       0.787 |             7 |
| 2026-03-19_nicusor-dan-romania-has-taken-a-clear-position-on-the-transa_BurJvC | 2026-03-19 | video-transcript          |           309 |              138 |                91 |       0.659 |            16 |
| 2026-03-26_ce-a-spus-nicusor-dan-despre-o-eventuala-rationalizare-a-car        | 2026-03-26 | video-transcript          |             0 |                0 |                 0 |       0     |             0 |
| 2026-03-26_nicusor-dan-a-anuntat-ca-va-promulga-legea-bugetului-asa-cum        | 2026-03-26 | video-transcript          |            58 |               30 |                27 |       0.9   |            10 |
| 2026-03-27_nicusor-dan-if-the-measures-are-not-sufficient-the-governmen        | 2026-03-27 | video-transcript          |           214 |              102 |                77 |       0.755 |            10 |
| 2026-03-30_nicusor-dan-despre-iesirea-psd-de-la-guvernare-un-guvern-min        | 2026-03-30 | video-transcript          |            62 |               27 |                24 |       0.889 |             4 |
| 2026-03-30_o-posibila-iesire-a-psd-de-la-guvernare-nicusor-dan-nu-cred         | 2026-03-30 | video-transcript          |           786 |              373 |               201 |       0.539 |            54 |
| 2026-03-31_carburantii-s-ar-putea-ieftini-nicusor-dan-cred-ca-va-fi-o-s        | 2026-03-31 | video-transcript          |            74 |               34 |                30 |       0.882 |             5 |
| 2026-03-31_carburantii-s-ar-putea-ieftini-nicusor-dan-cred-ca-va-fi-o-s_eIg4Ys | 2026-03-31 | video-transcript          |           159 |               79 |                59 |       0.747 |            10 |
| 2026-04-01_presedintele-nicusor-dan-trecerea-romaniei-la-euro-esentiala        | 2026-04-01 | video-transcript          |            98 |               40 |                32 |       0.8   |             5 |
| 2026-04-07_declaratiile-presedintelui-nicusor-dan-dupa-vizita-la-centru        | 2026-04-07 | video-transcript          |          3901 |             1788 |               784 |       0.438 |           253 |
| 2026-04-07_nicusor-dan-despre-demisia-lui-bolojan-in-ce-calitate-sa-i-o        | 2026-04-07 | video-transcript          |            78 |               34 |                32 |       0.941 |             5 |
| 2026-04-07_nicusor-dan-intrebat-daca-ii-va-cere-demisia-lui-bolojan-eu         | 2026-04-07 | video-transcript          |          1900 |              848 |               482 |       0.568 |           151 |
| 2026-04-07_nicusor-dan-lucescu-was-romania-s-ambassador-on-the-world-s         | 2026-04-07 | video-transcript          |           188 |              108 |                82 |       0.759 |            11 |
| 2026-04-07_nicusor-dan-nu-sunt-riscuri-acum-dar-avem-un-plan-de-criza-p        | 2026-04-07 | video-transcript          |           116 |               52 |                40 |       0.769 |             6 |
| 2026-04-08_nicusor-dan-anunta-numiri-in-fruntea-parchetelor-astept-o-di        | 2026-04-08 | video-transcript          |          4905 |             2300 |               865 |       0.376 |           292 |
| 2026-04-08_nicusor-dan-confirma-sabotajul-in-cazul-pozelor-trucate-foto        | 2026-04-08 | video-transcript          |           235 |              121 |                95 |       0.785 |            11 |
| 2026-04-08_nicusor-dan-i-was-happy-that-the-head-of-the-iasi-dna-is-run        | 2026-04-08 | video-transcript          |          2016 |              891 |               415 |       0.466 |            92 |
| 2026-04-08_nicusor-dan-if-i-make-a-mistake-romanians-will-penalize-me          | 2026-04-08 | video-transcript          |          1461 |              696 |               367 |       0.527 |            93 |
| 2026-04-08_nicusor-dan-respinge-acuzatiile-nu-sunt-propunerile-psd             | 2026-04-08 | video-transcript          |           110 |               56 |                43 |       0.768 |             4 |
| 2026-04-09_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus_yJJ1E7 | 2026-04-09 | video-transcript          |          3971 |             1826 |               745 |       0.408 |           246 |
| 2026-04-17_death-threat-against-president-nicusor-dan-i-am-organizing-a        | 2026-04-17 | video-transcript          |           186 |              102 |                81 |       0.794 |            14 |
| 2026-04-17_nicusor-dan-calin-georgescu-a-fost-sustinut-de-o-infrastruct        | 2026-04-17 | video-transcript          |           150 |               66 |                44 |       0.667 |            16 |
| 2026-04-20_ciprian-ciucu-critics-of-nicusor-dan-he-coordinates-more-wit        | 2026-04-20 | video-transcript          |          4442 |             2000 |               682 |       0.341 |           312 |
| 2026-04-20_nicusor-dan-lack-of-financial-education-led-to-unhealthy-dec        | 2026-04-20 | video-transcript          |           462 |              220 |               144 |       0.655 |            25 |
| 2026-04-20_nicusor-dan-traim-un-razboi-informational-ce-a-anuntat-prese        | 2026-04-20 | video-transcript          |           256 |              114 |                78 |       0.684 |            14 |
| 2026-04-20_we-will-enter-political-turbulence-nicusor-dan-i-do-not-supp        | 2026-04-20 | video-transcript          |          1128 |              566 |               289 |       0.511 |            92 |
| 2026-04-22_declaratie-de-presa-sustinuta-de-presedintele-romaniei-nicus        | 2026-04-22 | video-transcript          |           273 |              130 |                97 |       0.746 |            17 |
| 2026-04-22_kelemen-hunor-at-the-end-of-discussions-with-nicusor-dan-we         | 2026-04-22 | video-transcript          |           160 |               72 |                49 |       0.681 |            11 |
| 2026-04-23_nicusor-dan-despre-situatia-demisiilor-ministrilor-psd-aprec        | 2026-04-23 | video-transcript          |           694 |              310 |               200 |       0.645 |            51 |
| 2026-04-24_nicusor-dan-reacts-to-george-simion-s-new-discriminatory-sta        | 2026-04-24 | video-transcript          |          2304 |             1062 |               514 |       0.484 |           111 |
| 2026-04-24_nicusor-dan-simion-s-statement-to-me-is-below-any-level-of-d        | 2026-04-24 | video-transcript          |           118 |               57 |                48 |       0.842 |             7 |
| 2026-04-25_nicusor-dan-a-semnat-demisiile-ministrilor-psd-anuntul-facut        | 2026-04-25 | video-transcript          |           380 |              206 |               130 |       0.631 |            12 |
| 2026-04-29_nicusor-dan-i-wish-romania-would-be-governed-by-pro-western         | 2026-04-29 | video-transcript          |           160 |               68 |                54 |       0.794 |            13 |
| 2026-05-04_nicusor-dan-europa-isi-consolideaza-apararea-pe-fondul-reori        | 2026-05-04 | video-transcript          |           137 |               69 |                54 |       0.783 |             7 |
| 2026-05-04_nicusor-dan-regardless-of-what-happens-romania-will-continue        | 2026-05-04 | video-transcript          |          1950 |              936 |               463 |       0.495 |           121 |
| 2026-05-04_nicusor-dan-the-state-will-function-regardless-of-the-outcom        | 2026-05-04 | video-transcript          |           123 |               47 |                36 |       0.766 |            15 |
| 2026-05-05_declaratii-de-presa-sustinute-de-presedintele-romaniei-nicus        | 2026-05-05 | video-transcript          |           234 |              133 |                89 |       0.669 |            23 |
| 2026-05-05_nicusor-dan-vom-avea-un-nou-guvern-pro-occidental-in-termen         | 2026-05-05 | video-transcript          |           133 |               72 |                55 |       0.764 |            13 |
| 2026-05-06_nicusor-dan-vrea-refacerea-coalitiei-dar-pnl-si-usr-resping         | 2026-05-06 | video-transcript          |           409 |              188 |               126 |       0.67  |            15 |
| 2026-05-06_usr-attack-on-nicusor-dan-he-was-totally-disinterested-in-th        | 2026-05-06 | video-transcript          |           145 |               69 |                60 |       0.87  |             9 |
| 2026-05-07_ciucu-about-the-possible-suspension-of-nicusor-dan-pnl-would        | 2026-05-07 | video-transcript          |           489 |              221 |               141 |       0.638 |            35 |
| 2026-05-08_pnl-usr-offer-for-nicusor-dan-bolojan-prime-minister-in-mino        | 2026-05-08 | video-transcript          |          1779 |              805 |               362 |       0.45  |           103 |
| 2026-05-09_mesajul-presedintelui-romaniei-nicusor-dan-cu-prilejul-zilei        | 2026-05-09 | video-transcript          |           719 |              357 |               202 |       0.566 |            42 |
| 2026-05-09_nicusor-dan-we-will-continue-discussions-for-a-pro-western-g        | 2026-05-09 | video-transcript          |           128 |               73 |                50 |       0.685 |             7 |
| 2026-05-12_nicusor-dan-daca-ne-referim-la-europa-asa-ca-la-o-icoana-nu         | 2026-05-12 | video-transcript          |           574 |              244 |               145 |       0.594 |            39 |
| 2026-05-12_nicusor-dan-i-will-convene-the-parties-for-formal-consultati        | 2026-05-12 | video-transcript          |           190 |               96 |                64 |       0.667 |            17 |
| 2026-05-12_nicusor-dan-suntem-intr-o-perioada-cu-provocari-statele-care        | 2026-05-12 | video-transcript          |           765 |              385 |               218 |       0.566 |            48 |
| 2026-05-13_nicusor-dan-am-discutat-cu-secretarul-general-al-nato-despre        | 2026-05-13 | video-transcript          |           526 |              263 |               169 |       0.643 |            27 |
| 2026-05-13_nicusor-dan-moldova-e-un-stat-pe-flancul-estic-amenintat-int        | 2026-05-13 | video-transcript          |            87 |               46 |                39 |       0.848 |             3 |
| 2026-05-13_summit-b9-la-bucuresti-nicusor-dan-trebuie-sa-sporim-cheltui        | 2026-05-13 | video-transcript          |           121 |               66 |                54 |       0.818 |            10 |
| 2026-05-13_summit-b9-la-bucuresti-nicusor-dan-trebuie-sa-sporim-cheltui_VSRZ5y | 2026-05-13 | video-transcript          |           245 |              124 |                88 |       0.71  |            16 |
| 2026-05-15_nicusor-dan-i-would-not-like-to-appoint-a-government-that-wo        | 2026-05-15 | video-transcript          |           153 |               69 |                51 |       0.739 |             9 |
| 2026-05-15_nicusor-dan-majoritatea-parlamentara-va-fi-cheia-consultaril        | 2026-05-15 | video-transcript          |          2004 |              925 |               485 |       0.524 |           144 |
| 2026-05-20_nicusor-dan-continues-consultations-a-psd-only-government-is        | 2026-05-20 | video-transcript          |           275 |              164 |               101 |       0.616 |            15 |
| 2026-05-20_the-us-president-s-strategist-impressed-by-nicusor-dan-i-lik        | 2026-05-20 | video-transcript          |           493 |              222 |               145 |       0.653 |            25 |

## Top 20 cuvinte per discurs

### 2025-05-08 — dezbatere-electorala

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| trebui                          |           4 |
| românia                         |           3 |
| membru                          |           2 |
| continua                        |           1 |
| consolida                       |           1 |
| parteneriat                     |           1 |
| stateleunitealeamericii         |           1 |
| rămâne                          |           1 |
| northatlantictreatyorganization |           1 |
| stat                            |           1 |
| cheltuială                      |           1 |
| militar                         |           1 |
| pace                            |           1 |
| sine                            |           1 |
| obține                          |           1 |
| descurajare                     |           1 |
| război                          |           1 |
| activ                           |           1 |
| uniuneaeuropeană                |           1 |
| obiectiv                        |           1 |

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

### 2025-02-03 — lansare-campanie

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           3 |
| stat       |           3 |
| propune    |           3 |
| invi       |           3 |
| instituție |           2 |
| interes    |           2 |
| funcționa  |           2 |
| om         |           2 |
| important  |           2 |
| societate  |           2 |
| președinte |           2 |
| mecanism   |           2 |
| putea      |           2 |
| valoare    |           2 |
| comunitate |           2 |
| campanie   |           2 |
| împreună   |           2 |
| euro       |           2 |
| decembrie  |           1 |
| anunța     |           1 |

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

### 2025-06-04 — conferinta-presa

| cuvânt    |   frecvență |
|:----------|------------:|
| schiță    |           2 |
| guvernare |           2 |
| discuție  |           2 |
| deficit   |           2 |
| vrea      |           2 |
| director  |           2 |
| dori      |           1 |
| lună      |           1 |
| prim      |           1 |
| program   |           1 |
| începe    |           1 |
| privind   |           1 |
| grup      |           1 |
| lucra     |           1 |
| prezenta  |           1 |
| lider     |           1 |
| joi       |           1 |
| menține   |           1 |
| privi     |           1 |
| porni     |           1 |

### 2025-09-04 — interviu-autoevaluare

| cuvânt     |   frecvență |
|:-----------|------------:|
| lucru      |           4 |
| important  |           2 |
| provocare  |           2 |
| sine       |           2 |
| întâmpla   |           2 |
| coaliție   |           2 |
| formare    |           1 |
| guvern     |           1 |
| stabil     |           1 |
| deficit    |           1 |
| fericire   |           1 |
| control    |           1 |
| prezență   |           1 |
| extern     |           1 |
| opinie     |           1 |
| consistent |           1 |
| reuniune   |           1 |
| necesar    |           1 |
| europa     |           1 |
| lume       |           1 |

### 2025-12-31 — mesaj-anul-nou

| cuvânt           |   frecvență |
|:-----------------|------------:|
| an               |           8 |
| român            |           4 |
| drum             |           3 |
| viitor           |           3 |
| putea            |           3 |
| sine             |           3 |
| stat             |           3 |
| responsabilitate |           2 |
| loc              |           2 |
| românia          |           2 |
| rămâne           |           2 |
| eficient         |           2 |
| cetățean         |           2 |
| prag             |           1 |
| opri             |           1 |
| clipă            |           1 |
| privi            |           1 |
| luciditate       |           1 |
| onestita         |           1 |
| atât             |           1 |

### 2024-12-04 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          55 |
| putea      |          43 |
| partid     |          39 |
| sine       |          34 |
| spune      |          31 |
| vedea      |          29 |
| românia    |          25 |
| trebui     |          25 |
| călin      |          24 |
| georgescu  |          24 |
| președinte |          20 |
| elena      |          18 |
| crede      |          17 |
| european   |          16 |
| moment     |          16 |
| scut       |          15 |
| campanie   |          15 |
| discuție   |          15 |
| parlament  |          14 |
| alegere    |          14 |

### 2024-12-16 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| românia      |           2 |
| declarație   |           2 |
| crede        |           2 |
| trebui       |           2 |
| întrebare    |           2 |
| privi        |           2 |
| seara        |           1 |
| rud          |           1 |
| novacovici   |           1 |
| jurnalista   |           1 |
| euronews     |           1 |
| vedere       |           1 |
| controversat |           1 |
| călin        |           1 |
| georgescu    |           1 |
| legionar     |           1 |
| putea        |           1 |
| spune        |           1 |
| valida       |           1 |
| candidatură  |           1 |

### 2024-12-16 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |          12 |
| sine       |           8 |
| vrea       |           7 |
| președinte |           6 |
| putea      |           5 |
| problemă   |           5 |
| rol        |           5 |
| interes    |           5 |
| moment     |           4 |
| public     |           4 |
| direcție   |           4 |
| român      |           3 |
| alegere    |           3 |
| instituție |           3 |
| stat       |           3 |
| valoare    |           3 |
| corupție   |           3 |
| partid     |           3 |
| competență |           3 |
| mecanism   |           3 |

### 2024-12-16 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| alegere        |           3 |
| crede          |           3 |
| curte          |           3 |
| constituțional |           3 |
| trebui         |           2 |
| anulare        |           2 |
| bun            |           2 |
| situație       |           2 |
| instituție     |           2 |
| stat           |           2 |
| seara          |           1 |
| punct          |           1 |
| vedere         |           1 |
| instituțional  |           1 |
| trage          |           1 |
| răspundere     |           1 |
| întrebare      |           1 |
| nuanță         |           1 |
| rând           |           1 |
| decizie        |           1 |

### 2024-12-16 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          34 |
| partid        |          31 |
| sine          |          26 |
| românia       |          23 |
| spune         |          20 |
| crede         |          20 |
| alegere       |          18 |
| parte         |          15 |
| moment        |          13 |
| întrebare     |          13 |
| pro           |          13 |
| bun           |          13 |
| putea         |          12 |
| trebui        |          12 |
| stat          |          12 |
| discuție      |          12 |
| dumneavoastră |          12 |
| societate     |          11 |
| om            |          11 |
| public        |          10 |

### 2024-12-16 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| candidatură  |           8 |
| sine         |           5 |
| informație   |           4 |
| general      |           4 |
| prezidențial |           3 |
| anunța       |           3 |
| independent  |           3 |
| elena        |           3 |
| bun          |           3 |
| găsi         |           3 |
| nicușor      |           3 |
| dan          |           3 |
| primărie     |           3 |
| vot          |           3 |
| întreba      |           3 |
| spune        |           3 |
| intra        |           3 |
| nicuș        |           3 |
| ordan        |           3 |
| candidat     |           3 |

### 2024-12-17 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| vrea     |         128 |
| partid   |         122 |
| sine     |         112 |
| domn     |          91 |
| spune    |          84 |
| putea    |          75 |
| românia  |          62 |
| vedea    |          62 |
| nicușor  |          58 |
| usr      |          55 |
| dan      |          53 |
| candidat |          52 |
| ști      |          45 |
| om       |          45 |
| trebui   |          44 |
| moment   |          42 |
| crede    |          37 |
| bun      |          35 |
| vorbi    |          32 |
| veni     |          30 |

### 2024-12-18 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          72 |
| sine          |          46 |
| trebui        |          44 |
| spune         |          43 |
| om            |          35 |
| moment        |          33 |
| alegere       |          33 |
| putea         |          29 |
| crede         |          29 |
| partid        |          22 |
| dumneavoastră |          21 |
| parte         |          20 |
| românia       |          19 |
| an            |          19 |
| bun           |          18 |
| instituție    |          18 |
| vedea         |          17 |
| important     |          17 |
| candidat      |          16 |
| chestiune     |          16 |

### 2024-12-18 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          85 |
| sine       |          60 |
| trebui     |          43 |
| românia    |          36 |
| spune      |          33 |
| putea      |          31 |
| informație |          28 |
| partid     |          28 |
| exista     |          28 |
| psd        |          24 |
| guvern     |          24 |
| decizie    |          23 |
| ști        |          21 |
| parte      |          20 |
| politic    |          19 |
| alegere    |          19 |
| rusia      |          18 |
| stat       |          18 |
| usr        |          18 |
| președinte |          18 |

### 2024-12-19 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |          16 |
| guvern       |          13 |
| crede        |          12 |
| partid       |          10 |
| politic      |           9 |
| om           |           9 |
| alegere      |           8 |
| sine         |           7 |
| prezidențial |           6 |
| trebui       |           6 |
| spune        |           5 |
| întâmpla     |           4 |
| dialog       |           4 |
| vorbi        |           4 |
| parlament    |           4 |
| putea        |           3 |
| economic     |           3 |
| nicușor      |           3 |
| dan          |           3 |
| vedea        |           3 |

### 2024-12-23 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| partid        |           8 |
| vrea          |           7 |
| om            |           7 |
| alegere       |           6 |
| candidat      |           6 |
| bun           |           5 |
| spune         |           5 |
| lucru         |           5 |
| situație      |           5 |
| pro           |           5 |
| trebui        |           5 |
| domn          |           4 |
| vedea         |           4 |
| exista        |           4 |
| crede         |           4 |
| merge         |           4 |
| dumneavoastră |           4 |
| moment        |           4 |
| bucurești     |           4 |
| nivel         |           4 |

### 2024-12-25 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |           5 |
| an          |           5 |
| crăciun     |           4 |
| român       |           4 |
| trebui      |           4 |
| stat        |           3 |
| bun         |           3 |
| alături     |           3 |
| om          |           2 |
| fericit     |           2 |
| drag        |           2 |
| complicat   |           2 |
| alegere     |           2 |
| față        |           2 |
| lucru       |           2 |
| forță       |           2 |
| situație    |           2 |
| viitor      |           1 |
| candidat    |           1 |
| președinție |           1 |

### 2024-12-30 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           7 |
| sine         |           4 |
| an           |           4 |
| românia      |           4 |
| om           |           4 |
| investiție   |           4 |
| primar       |           3 |
| capitală     |           3 |
| ultim        |           3 |
| adică        |           3 |
| nemulțumire  |           3 |
| pune         |           3 |
| trebui       |           3 |
| veni         |           3 |
| spune        |           2 |
| retrage      |           2 |
| cursă        |           2 |
| prezidențial |           2 |
| precizare    |           2 |
| privi        |           2 |

### 2024-12-30 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| sine        |          15 |
| om          |          14 |
| spune       |           9 |
| bineînțeles |           7 |
| alegere     |           6 |
| georgescu   |           6 |
| campanie    |           6 |
| tiktok      |           6 |
| proces      |           5 |
| trebui      |           5 |
| vrea        |           5 |
| exista      |           5 |
| plăti       |           5 |
| nemulțumire |           5 |
| uita        |           4 |
| anulare     |           4 |
| clar        |           4 |
| bun         |           4 |
| niciun      |           4 |
| punct       |           4 |

### 2025-01-09 — video-transcript

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| alegere                 |          11 |
| românia                 |           9 |
| candidat                |           9 |
| vedea                   |           7 |
| om                      |           6 |
| nicu                    |           5 |
| dumneavoastră           |           5 |
| bun                     |           5 |
| imagine                 |           5 |
| sine                    |           5 |
| partid                  |           5 |
| domn                    |           4 |
| ordan                   |           4 |
| merge                   |           4 |
| guvern                  |           4 |
| putea                   |           4 |
| important               |           4 |
| partidulnaționalliberal |           4 |
| situație                |           4 |
| general                 |           3 |

### 2025-01-13 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| veni      |           5 |
| răspuns   |           4 |
| parte     |           3 |
| bun       |           2 |
| sine      |           2 |
| crede     |           2 |
| începe    |           2 |
| alegere   |           2 |
| domn      |           2 |
| aștepta   |           2 |
| moment    |           2 |
| vrea      |           2 |
| întreba   |           2 |
| necesar   |           2 |
| trebui    |           2 |
| lămurire  |           2 |
| încredere |           2 |
| ști       |           2 |
| sper      |           2 |
| lege      |           1 |

### 2025-01-18 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| alegere      |           8 |
| iohannis     |           7 |
| anulare      |           5 |
| crede        |           5 |
| lucru        |           4 |
| klaus        |           4 |
| trebui       |           3 |
| mandat       |           3 |
| rămâne       |           3 |
| stat         |           3 |
| lămuri       |           3 |
| lună         |           3 |
| român        |           2 |
| final        |           2 |
| atât         |           2 |
| exista       |           2 |
| singur       |           2 |
| scor         |           2 |
| însemna      |           2 |
| extraordinar |           2 |

### 2025-01-30 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| primar      |           4 |
| sine        |           4 |
| mandat      |           3 |
| politic     |           3 |
| candidatură |           2 |
| imediat     |           2 |
| câștiga     |           2 |
| om          |           2 |
| bun         |           2 |
| parte       |           2 |
| obține      |           2 |
| adică       |           2 |
| situație    |           2 |
| schimbare   |           2 |
| lega        |           1 |
| cră         |           1 |
| susține     |           1 |
| primărie    |           1 |
| ruga        |           1 |
| celălalt    |           1 |

### 2025-02-04 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| public    |           3 |
| sine      |           2 |
| vot       |           2 |
| tur       |           2 |
| candidat  |           2 |
| adresez   |           2 |
| pune      |           1 |
| problemă  |           1 |
| retrage   |           1 |
| discuție  |           1 |
| lum       |           1 |
| lucru     |           1 |
| moment    |           1 |
| intra     |           1 |
| comenta   |           1 |
| cin       |           1 |
| antonescu |           1 |
| crede     |           1 |
| schimba   |           1 |
| campanie  |           1 |

### 2025-02-05 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| spune     |           7 |
| sine      |           7 |
| vrea      |           6 |
| nordis    |           3 |
| capitală  |           3 |
| buget     |           3 |
| an        |           3 |
| încredere |           3 |
| românia   |           3 |
| împrumuta |           3 |
| duce      |           3 |
| ban       |           3 |
| decizie   |           2 |
| rămâne    |           2 |
| hai       |           2 |
| față      |           2 |
| înțelege  |           2 |
| același   |           2 |
| deficit   |           2 |
| putea     |           2 |

### 2025-02-05 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |          65 |
| spune         |          60 |
| vrea          |          59 |
| putea         |          48 |
| vedea         |          40 |
| om            |          40 |
| moment        |          38 |
| trebui        |          36 |
| exista        |          30 |
| crede         |          29 |
| românia       |          26 |
| președinte    |          25 |
| dumneavoastră |          24 |
| duce          |          24 |
| alegere       |          22 |
| an            |          22 |
| bucurești     |          22 |
| sector        |          22 |
| bun           |          21 |
| ști           |          20 |

### 2025-02-08 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| partid    |           5 |
| nicu      |           4 |
| jordan    |           4 |
| românia   |           4 |
| politic   |           4 |
| georgescu |           3 |
| vrea      |           3 |
| trece     |           3 |
| interior  |           3 |
| usr       |           3 |
| situație  |           3 |
| crede     |           3 |
| spune     |           3 |
| lascon    |           2 |
| compara   |           2 |
| călin     |           2 |
| pune      |           2 |
| gaz       |           2 |
| foc       |           2 |
| printr    |           2 |

### 2025-02-16 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| vrea      |          11 |
| tramvai   |           9 |
| bucurești |           6 |
| ilfov     |           5 |
| transport |           5 |
| linie     |           4 |
| exista    |           4 |
| an        |           4 |
| centru    |           4 |
| lega      |           4 |
| program   |           3 |
| comercial |           3 |
| public    |           3 |
| probabil  |           3 |
| aștepta   |           3 |
| lansare   |           3 |
| contract  |           3 |
| întrebare |           2 |
| ajunge    |           2 |
| însemna   |           2 |

### 2025-02-24 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| premier   |           5 |
| românia   |           5 |
| ciolacu   |           4 |
| guvern    |           4 |
| coaliție  |           3 |
| perioadă  |           3 |
| lung      |           3 |
| partid    |           2 |
| trebui    |           2 |
| alegere   |           2 |
| fan       |           2 |
| legitim   |           2 |
| crede     |           2 |
| clar      |           2 |
| guvernare |           2 |
| bucurești |           2 |
| interimar |           2 |
| încredere |           2 |
| printr    |           2 |
| opoziție  |           1 |

### 2025-02-26 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| vedea    |           6 |
| sine     |           3 |
| lucru    |           3 |
| plăti    |           3 |
| ști      |           3 |
| cont     |           3 |
| parte    |           3 |
| aștepta  |           2 |
| fapt     |           2 |
| plată    |           2 |
| trebui   |           2 |
| adică    |           2 |
| cumpere  |           2 |
| domn     |           1 |
| nicuș    |           1 |
| jordan   |           1 |
| auzi     |           1 |
| oară     |           1 |
| spune    |           1 |
| lămuri   |           1 |

### 2025-02-27 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| trebui        |          10 |
| alegere       |           9 |
| campanie      |           8 |
| exista        |           8 |
| sine          |           6 |
| parchet       |           6 |
| indiciu       |           6 |
| călin         |           6 |
| georgescu     |           6 |
| vedea         |           5 |
| apărea        |           5 |
| domn          |           5 |
| dumneavoastră |           4 |
| moment        |           4 |
| parte         |           4 |
| anulare       |           4 |
| om            |           4 |
| probă         |           4 |
| lucru         |           4 |
| românia       |           4 |

### 2025-02-27 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| campanie    |           5 |
| om          |           3 |
| spune       |           2 |
| trebui      |           2 |
| milion      |           2 |
| călin       |           2 |
| georgescu   |           2 |
| vorbim      |           2 |
| vedea       |           2 |
| plăti       |           2 |
| ban         |           2 |
| companie    |           2 |
| consulta    |           1 |
| consultanță |           1 |
| politic     |           1 |
| amplitudine |           1 |
| costa       |           1 |
| euro        |           1 |
| tehnologie  |           1 |
| folosit     |           1 |

### 2025-03-07 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| vrea           |           4 |
| candida        |           4 |
| candidatură    |           4 |
| dumneavoastră  |           3 |
| laon           |           2 |
| fapt           |           2 |
| spune          |           2 |
| om             |           2 |
| retrage        |           2 |
| crede          |           2 |
| stat           |           2 |
| curte          |           2 |
| constituțional |           2 |
| principiu      |           2 |
| lansa          |           1 |
| spațiu         |           1 |
| public         |           1 |
| ofertă         |           1 |
| tr             |           1 |
| prezidențială  |           1 |

### 2025-03-07 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| constituțional |           5 |
| trebui         |           3 |
| candida        |           3 |
| vedere         |           3 |
| curte          |           3 |
| principiu      |           3 |
| alegere        |           3 |
| opinie         |           2 |
| călin          |           2 |
| georgescu      |           2 |
| sine           |           2 |
| vedea          |           2 |
| decizie        |           2 |
| juridic        |           2 |
| curții         |           2 |
| noiembrie      |           2 |
| șoșoacă        |           2 |
| lege           |           2 |
| față           |           2 |
| context        |           1 |

### 2025-03-07 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| vrea           |           5 |
| candidatură    |           4 |
| candida        |           3 |
| cursă          |           2 |
| depune         |           2 |
| spune          |           2 |
| crede          |           2 |
| stat           |           2 |
| curte          |           2 |
| constituțional |           2 |
| principiu      |           2 |
| nicu           |           1 |
| jordan         |           1 |
| candidat       |           1 |
| înscrie        |           1 |
| oficial        |           1 |
| prezidențial   |           1 |
| actual         |           1 |
| primar         |           1 |
| general        |           1 |

### 2025-03-14 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          69 |
| sine       |          68 |
| domn       |          67 |
| putea      |          45 |
| georgescu  |          44 |
| om         |          43 |
| vedea      |          39 |
| spune      |          37 |
| românia    |          36 |
| partid     |          35 |
| președinte |          34 |
| trebui     |          30 |
| alegere    |          28 |
| ști        |          25 |
| veni       |          22 |
| situație   |          22 |
| lucru      |          22 |
| român      |          21 |
| parte      |          21 |
| întâmpla   |          20 |

### 2025-03-14 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| guvern     |          14 |
| președinte |           6 |
| veni       |           5 |
| spune      |           5 |
| putea      |           3 |
| guvernare  |           3 |
| situație   |           3 |
| vrea       |           3 |
| evident    |           3 |
| alegere    |           3 |
| public     |           3 |
| sine       |           3 |
| românia    |           3 |
| problemă   |           3 |
| ști        |           3 |
| trebui     |           3 |
| schimba    |           3 |
| partid     |           2 |
| pericol    |           2 |
| extremist  |           2 |

### 2025-03-19 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| dumneavoastră |          32 |
| domn          |          30 |
| alegere       |          23 |
| vrea          |          21 |
| spune         |          17 |
| susține       |          17 |
| bolojan       |          16 |
| prezidențial  |          15 |
| întâlnire     |          14 |
| crede         |          13 |
| antonescu     |          12 |
| tur           |          12 |
| sine          |          12 |
| nicușor       |          11 |
| bun           |          11 |
| ilie          |          11 |
| dan           |          10 |
| discuție      |          10 |
| cotroceni     |          10 |
| exista        |           9 |

### 2025-03-27 — video-transcript

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| buget                   |          11 |
| vrea                    |           8 |
| spune                   |           7 |
| trece                   |           6 |
| vota                    |           5 |
| proiect                 |           5 |
| sine                    |           4 |
| capitală                |           3 |
| an                      |           3 |
| ordine                  |           3 |
| majoritate              |           3 |
| consiliu                |           3 |
| psd                     |           3 |
| partidulnaționalliberal |           3 |
| usl                     |           3 |
| ședință                 |           3 |
| veni                    |           3 |
| viitor                  |           3 |
| rămâne                  |           3 |
| vedea                   |           3 |

### 2025-04-01 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| domn       |         144 |
| sine       |         114 |
| vrea       |          99 |
| spune      |          84 |
| ști        |          72 |
| putea      |          67 |
| vedea      |          63 |
| om         |          62 |
| românia    |          38 |
| președinte |          38 |
| bun        |          37 |
| doamnă     |          35 |
| antonescu  |          33 |
| trump      |          33 |
| ponta      |          32 |
| vorbi      |          31 |
| crede      |          30 |
| nicușor    |          30 |
| trebui     |          28 |
| dan        |          28 |

### 2025-04-02 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| țară         |           3 |
| absolvent    |           2 |
| sorbona      |           2 |
| prestigiu    |           2 |
| bogdan       |           1 |
| suditu       |           1 |
| conferențiar |           1 |
| universitar  |           1 |
| doctor       |           1 |
| universitate |           1 |
| bucurești    |           1 |
| specialist   |           1 |
| planificare  |           1 |
| urban        |           1 |
| teritorial   |           1 |
| carol        |           1 |
| spune        |           1 |
| domn         |           1 |
| prim         |           1 |
| ministru     |           1 |

### 2025-04-03 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| campanie     |           9 |
| psd          |           5 |
| nicușor      |           4 |
| dan          |           4 |
| primărie     |           4 |
| prezidențial |           3 |
| dona         |           3 |
| finanța      |           3 |
| capitală     |           3 |
| nicuș        |           3 |
| jordan       |           3 |
| vrea         |           3 |
| ron          |           3 |
| milion       |           3 |
| atac         |           2 |
| primar       |           2 |
| general      |           2 |
| veni         |           2 |
| daniel       |           2 |
| zamfir       |           2 |

### 2025-04-08 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| merden     |           4 |
| crin       |           2 |
| antonescu  |           2 |
| social     |           2 |
| vrea       |           2 |
| filma      |           2 |
| plăcea     |           2 |
| spune      |           2 |
| om         |           2 |
| inteligent |           2 |
| xenia      |           1 |
| trola      |           1 |
| rețea      |           1 |
| nicușordan |           1 |
| citez      |           1 |
| mănânc     |           1 |
| îm         |           1 |
| încheia    |           1 |
| citat      |           1 |
| platformă  |           1 |

### 2025-04-08 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           7 |
| alegere      |           7 |
| prezidențial |           7 |
| elena        |           6 |
| lasconi      |           6 |
| nicușor      |           5 |
| dan          |           5 |
| sine         |           4 |
| putea        |           4 |
| vot          |           4 |
| spune        |           3 |
| loc          |           3 |
| electoral    |           3 |
| retrage      |           2 |
| usr          |           2 |
| oară         |           2 |
| renunța      |           2 |
| cursă        |           2 |
| negociere    |           2 |
| xenia        |           2 |

### 2025-04-10 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| vrea      |          11 |
| usr       |           9 |
| sine      |           8 |
| partid    |           7 |
| campanie  |           6 |
| putea     |           6 |
| politic   |           5 |
| nicușor   |           5 |
| dan       |           5 |
| candidat  |           5 |
| susținere |           4 |
| elena     |           4 |
| lasconi   |           4 |
| comitet   |           3 |
| lider     |           3 |
| parte     |           3 |
| decide    |           2 |
| lucru     |           2 |
| vota      |           2 |
| situație  |           2 |

### 2025-04-11 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| mesaj        |           4 |
| dan          |           4 |
| cere         |           4 |
| întâlni      |           4 |
| ciucă        |           3 |
| retrage      |           3 |
| răspunde     |           3 |
| elena        |           2 |
| nicușor      |           2 |
| trimite      |           2 |
| trece        |           2 |
| nicolae      |           2 |
| sine         |           2 |
| prezidențial |           2 |
| urmă         |           2 |
| însă         |           2 |
| lasconi      |           2 |
| vedea        |           2 |
| usr          |           2 |
| noiembrie    |           2 |

### 2025-05-02 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| alegere      |          11 |
| vrea         |           6 |
| românia      |           5 |
| vedea        |           5 |
| delegație    |           4 |
| stat         |           4 |
| exista       |           4 |
| spune        |           4 |
| rând         |           4 |
| alege        |           4 |
| vot          |           4 |
| unit         |           3 |
| electoral    |           3 |
| lupta        |           3 |
| discuție     |           2 |
| monitoriza   |           2 |
| interferență |           2 |
| extern       |           2 |
| proces       |           2 |
| duminică     |           2 |

### 2025-05-04 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| vota         |          16 |
| alegere      |          15 |
| românia      |          14 |
| vot          |          12 |
| oră          |          12 |
| vrea         |          11 |
| prezidențial |          10 |
| primar       |          10 |
| român        |          10 |
| candidat     |           9 |
| capitală     |           9 |
| iată         |           8 |
| candida      |           8 |
| declarație   |           8 |
| urnă         |           8 |
| independent  |           7 |
| sine         |           7 |
| om           |           7 |
| direct       |           6 |
| nicușor      |           6 |

### 2025-05-04 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          21 |
| spune         |          12 |
| dumneavoastră |          11 |
| intra         |          11 |
| campanie      |          10 |
| moment        |          10 |
| usr           |          10 |
| tur           |           9 |
| trebui        |           8 |
| susține       |           8 |
| candidat      |           7 |
| guvern        |           7 |
| putea         |           6 |
| om            |           6 |
| discuție      |           6 |
| majoritate    |           6 |
| vedea         |           5 |
| caz           |           5 |
| încredere     |           5 |
| guvernare     |           5 |

### 2025-05-04 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| nicușor        |          30 |
| vrea           |           6 |
| mulțumi        |           4 |
| vreau          |           3 |
| campanie       |           3 |
| democrație     |           2 |
| comunitate     |           2 |
| aspirație      |           2 |
| dezbatere      |           2 |
| opinie         |           2 |
| politicienii   |           2 |
| putea          |           2 |
| numărătoare    |           2 |
| corect         |           2 |
| atât           |           2 |
| problemă       |           1 |
| felici         |           1 |
| seară          |           1 |
| votant         |           1 |
| contracandidat |           1 |

### 2025-05-05 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| dezbatere      |           5 |
| direcție       |           4 |
| economie       |           4 |
| românia        |           3 |
| opțiune        |           3 |
| lucru          |           2 |
| românie        |           2 |
| ură            |           2 |
| societate      |           2 |
| sine           |           2 |
| ăă             |           2 |
| opinie         |           2 |
| politică       |           2 |
| românesc       |           2 |
| investiție     |           2 |
| deveni         |           1 |
| simplu         |           1 |
| procidental    |           1 |
| antioccidental |           1 |
| liber          |           1 |

### 2025-05-05 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           6 |
| românia    |           5 |
| tur        |           4 |
| direcție   |           4 |
| vreau      |           3 |
| mulțumi    |           3 |
| român      |           3 |
| aplauze    |           3 |
| sine       |           3 |
| vot        |           2 |
| loc        |           2 |
| vota       |           2 |
| dezbatere  |           2 |
| occidental |           2 |
| sarcină    |           2 |
| convinge   |           2 |
| campanie   |           2 |
| crinonescu |           2 |
| important  |           2 |
| om         |           2 |

### 2025-05-06 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| financiar   |           6 |
| românia     |           4 |
| față        |           3 |
| piață       |           3 |
| vrea        |           3 |
| aduce       |           3 |
| aminte      |           3 |
| optimism    |           2 |
| absoarbă    |           2 |
| ban         |           2 |
| societate   |           2 |
| românesc    |           2 |
| urmă        |           2 |
| săptămână   |           2 |
| schimbare   |           2 |
| primărie    |           2 |
| capitală    |           2 |
| obligațiune |           2 |
| încredere   |           2 |
| evoluție    |           1 |

### 2025-05-07 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| vrea     |         159 |
| spune    |         106 |
| sine     |          89 |
| putea    |          67 |
| românia  |          63 |
| om       |          62 |
| domn     |          60 |
| alegere  |          48 |
| crede    |          45 |
| partid   |          41 |
| trebui   |          39 |
| tur      |          38 |
| vedea    |          37 |
| moment   |          36 |
| candidat |          35 |
| economie |          35 |
| mesaj    |          33 |
| guvern   |          32 |
| psd      |          31 |
| exista   |          31 |

### 2025-05-07 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| românia       |          32 |
| vrea          |          26 |
| om            |          23 |
| ăă            |          22 |
| putea         |          19 |
| dumneavoastră |          17 |
| domn          |          15 |
| partid        |          15 |
| sine          |          15 |
| spune         |          15 |
| lucru         |          14 |
| stat          |          14 |
| fapt          |          13 |
| trebui        |          13 |
| față          |          12 |
| discuție      |          11 |
| simion        |          10 |
| schimbare     |          10 |
| vorbi         |          10 |
| moment        |          10 |

### 2025-05-07 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| bugetar       |           2 |
| sine          |           2 |
| putea         |           2 |
| profesor      |           2 |
| medic         |           2 |
| personal      |           2 |
| administrație |           2 |
| public        |           2 |
| domn          |           1 |
| simeion       |           1 |
| referire      |           1 |
| interviu      |           1 |
| fapt          |           1 |
| afară         |           1 |
| economie      |           1 |
| acuma         |           1 |
| merge         |           1 |
| spune         |           1 |
| dumnealui     |           1 |
| argument      |           1 |

### 2025-05-07 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| dori        |           4 |
| guvern      |           3 |
| partid      |           3 |
| domn        |           3 |
| putea       |           3 |
| premier     |           2 |
| nume        |           2 |
| occidental  |           2 |
| evident     |           2 |
| discuție    |           2 |
| promi       |           2 |
| lucru       |           2 |
| lega        |           1 |
| minte       |           1 |
| imediat     |           1 |
| pro         |           1 |
| îvea        |           1 |
| procidental |           1 |
| susținere   |           1 |
| parlament   |           1 |

### 2025-05-07 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           3 |
| economic   |           3 |
| schimbare  |           3 |
| plată      |           3 |
| duce       |           2 |
| incapacita |           2 |
| nivel      |           2 |
| lucru      |           2 |
| serios     |           2 |
| permite    |           1 |
| șoc        |           1 |
| vedea      |           1 |
| bursă      |           1 |
| curs       |           1 |
| ăă         |           1 |
| voiam      |           1 |
| întreba    |           1 |
| arăta      |           1 |
| viață      |           1 |
| om         |           1 |

### 2025-05-07 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| românia        |           5 |
| schimbare      |           4 |
| economic       |           4 |
| duce           |           3 |
| putea          |           3 |
| plată          |           3 |
| imposibilitate |           2 |
| plăti          |           2 |
| vorbi          |           2 |
| situație       |           2 |
| vrea           |           2 |
| nivel          |           2 |
| lucru          |           2 |
| serios         |           2 |
| nicușordan     |           1 |
| spune          |           1 |
| țară           |           1 |
| pensie         |           1 |
| salariu        |           1 |
| candidat       |           1 |

### 2025-05-10 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| zonă          |           8 |
| afară         |           5 |
| putea         |           5 |
| adică         |           4 |
| domn          |           3 |
| stat          |           3 |
| sine          |           3 |
| om            |           3 |
| personal      |           3 |
| vrea          |           2 |
| plăti         |           2 |
| zic           |           2 |
| trebui        |           2 |
| crește        |           2 |
| privat        |           2 |
| moment        |           2 |
| insuficient   |           2 |
| sanitar       |           2 |
| administrație |           2 |
| vorbim        |           2 |

### 2025-05-14 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           9 |
| taxă       |           5 |
| românia    |           4 |
| tva        |           4 |
| crește     |           4 |
| candidat   |           3 |
| situație   |           3 |
| stat       |           3 |
| zonă       |           2 |
| spune      |           2 |
| prezent    |           2 |
| important  |           2 |
| bază       |           2 |
| impozitare |           2 |
| economie   |           2 |
| încasa     |           2 |
| trebui     |           2 |
| sine       |           2 |
| mediu      |           2 |
| uita       |           1 |

### 2025-05-15 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sistem     |           8 |
| problemă   |           6 |
| trebui     |           6 |
| vrea       |           5 |
| educație   |           4 |
| rural      |           4 |
| zonă       |           4 |
| oraș       |           4 |
| mic        |           4 |
| sănătate   |           3 |
| crede      |           3 |
| românia    |           3 |
| spital     |           3 |
| chestiune  |           3 |
| copie      |           2 |
| securitate |           2 |
| național   |           2 |
| spune      |           2 |
| copil      |           2 |
| mediu      |           2 |

### 2025-05-15 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| nicușordan    |           3 |
| seara         |           3 |
| dumneavoastră |           3 |
| perioadă      |           3 |
| implica       |           3 |
| campanie      |           3 |
| nicușor       |           3 |
| sine          |           3 |
| mamă          |           3 |
| dezbatere     |           2 |
| participa     |           2 |
| emisiune      |           2 |
| trăi          |           2 |
| ține          |           2 |
| familie       |           2 |
| idee          |           2 |
| arăta         |           2 |
| coleg         |           2 |
| ajuta         |           2 |
| atât          |           2 |

### 2025-05-15 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| suveranist   |           3 |
| român        |           3 |
| izolaționist |           2 |
| stat         |           2 |
| vrea         |           2 |
| declara      |           1 |
| nicușordan   |           1 |
| diasporă     |           1 |
| începe       |           1 |
| scrutin      |           1 |
| tur          |           1 |
| alegere      |           1 |
| prezidențial |           1 |
| declarație   |           1 |
| dezbatere    |           1 |
| organiza     |           1 |
| micuțu       |           1 |
| cosmin       |           1 |
| nedelcu      |           1 |
| george       |           1 |

### 2025-05-15 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| autist        |           4 |
| hai           |           4 |
| candidat      |           3 |
| vedea         |           3 |
| românia       |           3 |
| sine          |           3 |
| față          |           2 |
| simion        |           2 |
| spune         |           2 |
| nicușordan    |           2 |
| copil         |           2 |
| mesaj         |           2 |
| doamnă        |           2 |
| dumneavoastră |           2 |
| trimite       |           2 |
| comunicat     |           2 |
| presă         |           2 |
| purta         |           2 |
| nicușor       |           1 |
| dan           |           1 |

### 2025-05-15 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          10 |
| domn          |           5 |
| simion        |           5 |
| dumneavoastră |           5 |
| vorbi         |           5 |
| românia       |           5 |
| motiv         |           5 |
| pune          |           4 |
| spune         |           4 |
| donald        |           4 |
| trump         |           4 |
| listă         |           3 |
| stat          |           3 |
| român         |           3 |
| război        |           3 |
| om            |           3 |
| plăti         |           3 |
| ucraina       |           3 |
| ruga          |           3 |
| parlament     |           2 |

### 2025-05-16 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| bun        |           2 |
| aproape    |           2 |
| opinie     |           1 |
| nicușodan  |           1 |
| calitate   |           1 |
| președinte |           1 |
| direct     |           1 |
| pretenție  |           1 |
| deștept    |           1 |
| cinstit    |           1 |
| spune      |           1 |
| vedeți     |           1 |
| bucurești  |           1 |
| raște      |           1 |
| milion     |           1 |
| țară       |           1 |
| manager    |           1 |
| experiență |           1 |
| putea      |           1 |
| încredere  |           1 |

### 2025-05-18 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |          26 |
| nicușor    |          25 |
| comunitate |          11 |
| român      |           8 |
| societate  |           7 |
| unitate    |           7 |
| vrea       |           6 |
| aplauze    |           5 |
| nicuș      |           5 |
| alegere    |           4 |
| românesc   |           4 |
| moment     |           4 |
| vreau      |           3 |
| forță      |           3 |
| țară       |           3 |
| muzică     |           2 |
| stat       |           2 |
| economic   |           2 |
| mulțumi    |           2 |
| dovedi     |           2 |

### 2025-05-18 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| om         |           2 |
| amat       |           1 |
| gând       |           1 |
| tăcut      |           1 |
| cinstit    |           1 |
| muncitor   |           1 |
| simți      |           1 |
| reprezenta |           1 |
| alege      |           1 |
| voteza     |           1 |
| făgăraș    |           1 |
| transmite  |           1 |
| important  |           1 |
| ști        |           1 |
| pleca      |           1 |
| trebui     |           1 |
| exista     |           1 |
| român      |           1 |

### 2025-05-18 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| românia   |           8 |
| împreună  |           6 |
| aplauze   |           4 |
| construi  |           4 |
| român     |           4 |
| victorie  |           3 |
| opțiune   |           3 |
| campanie  |           2 |
| uita      |           2 |
| săptămână |           2 |
| începe    |           2 |
| basarabia |           2 |
| ști       |           1 |
| om        |           1 |
| crede     |           1 |
| putea     |           1 |
| sine      |           1 |
| schimba   |           1 |
| direcție  |           1 |
| corect    |           1 |

### 2025-05-18 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |          20 |
| nicușor    |          17 |
| comunitate |          12 |
| român      |           8 |
| societate  |           7 |
| unitate    |           7 |
| vrea       |           6 |
| aplauze    |           5 |
| vreau      |           4 |
| românesc   |           4 |
| moment     |           4 |
| seara      |           3 |
| alegere    |           3 |
| forță      |           3 |
| țară       |           3 |
| bun        |           2 |
| stat       |           2 |
| economic   |           2 |
| dovedi     |           2 |
| politic    |           2 |

### 2025-05-18 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| aplauze  |          26 |
| românia  |          24 |
| nicușor  |          18 |
| muzică   |          10 |
| europa   |          10 |
| unitate  |           9 |
| împreună |           6 |
| stângă   |           5 |
| ria      |           5 |
| nicușar  |           5 |
| romia    |           5 |
| român    |           5 |
| uita     |           4 |
| dreaptă  |           4 |
| vrea     |           4 |
| campanie |           4 |
| construi |           4 |
| mulțime  |           3 |
| hai      |           3 |
| începe   |           3 |

### 2025-05-18 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| nicușor    |          84 |
| sine       |          60 |
| românia    |          58 |
| om         |          54 |
| vrea       |          47 |
| dan        |          46 |
| domn       |          40 |
| spune      |          34 |
| putea      |          29 |
| român      |          25 |
| președinte |          24 |
| ști        |          22 |
| crede      |          21 |
| trebui     |          21 |
| țară       |          20 |
| uita       |          18 |
| simion     |          16 |
| vedea      |          14 |
| europa     |          13 |
| merge      |          13 |

### 2025-05-19 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| moment     |          10 |
| românia    |           9 |
| economic   |           6 |
| european   |           6 |
| câștiga    |           5 |
| vedea      |           4 |
| putea      |           4 |
| spune      |           4 |
| uniune     |           4 |
| însemna    |           3 |
| bloca      |           3 |
| muzică     |           3 |
| simion     |           2 |
| înfunda    |           2 |
| geopolitic |           2 |
| limită     |           2 |
| față       |           2 |
| țară       |           2 |
| scădere    |           2 |
| bursă      |           2 |

### 2025-05-19 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          11 |
| sine          |           7 |
| vedea         |           6 |
| domn          |           5 |
| trebui        |           4 |
| partid        |           4 |
| guvern        |           4 |
| dumneavoastră |           3 |
| românia       |           3 |
| săptămână     |           3 |
| moment        |           3 |
| important     |           3 |
| om            |           3 |
| spațiu        |           2 |
| public        |           2 |
| urma          |           2 |
| perioadă      |           2 |
| dificil       |           2 |
| lună          |           2 |
| discuție      |           2 |

### 2025-05-19 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| românia   |          11 |
| european  |           7 |
| crede     |           7 |
| uniune    |           5 |
| sine      |           5 |
| spune     |           5 |
| an        |           4 |
| pandemie  |           4 |
| practic   |           4 |
| moment    |           4 |
| credință  |           4 |
| vorbi     |           4 |
| domn      |           3 |
| rusia     |           3 |
| uita      |           3 |
| om        |           3 |
| greși     |           3 |
| sentiment |           3 |
| ușurare   |           3 |
| fapt      |           3 |

### 2025-05-20 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          10 |
| guvern     |           7 |
| sine       |           5 |
| primar     |           4 |
| președinte |           3 |
| țară       |           3 |
| viitor     |           3 |
| primărie   |           3 |
| capitală   |           3 |
| lucru      |           3 |
| important  |           3 |
| interimar  |           3 |
| psd        |           3 |
| vorbi      |           2 |
| ales       |           2 |
| problemă   |           2 |
| termen     |           2 |
| scurt      |           2 |
| dorință    |           2 |
| numi       |           2 |

### 2025-05-21 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| stat       |           4 |
| america    |           4 |
| mesaj      |           3 |
| unit       |           3 |
| românia    |           3 |
| vrea       |           3 |
| răspunde   |           2 |
| ambasadă   |           2 |
| ferm       |           2 |
| alege      |           1 |
| transmite  |           1 |
| angajament |           1 |
| declara    |           1 |
| aștepta    |           1 |
| interes    |           1 |
| colabora   |           1 |
| șef        |           1 |
| nicușordan |           1 |
| asigura    |           1 |
| partener   |           1 |

### 2025-05-21 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           4 |
| social     |           4 |
| președinte |           3 |
| partid     |           3 |
| sine       |           3 |
| nicușor    |           3 |
| dan        |           3 |
| psd        |           3 |
| discuție   |           3 |
| ilie       |           3 |
| bolojan    |           3 |
| masă       |           3 |
| nicușordan |           2 |
| guvern     |           2 |
| funcție    |           2 |
| moment     |           2 |
| urma       |           2 |
| opoziție   |           2 |
| spune      |           2 |
| radu       |           2 |

### 2025-05-22 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |          46 |
| românia     |          26 |
| spune       |          19 |
| sine        |          15 |
| moldova     |          14 |
| ăă          |          13 |
| discuție    |          13 |
| trebui      |          12 |
| guvern      |          10 |
| deficit     |           9 |
| an          |           9 |
| domn        |           9 |
| ucraina     |           9 |
| bineînțeles |           9 |
| republică   |           9 |
| partid      |           9 |
| stat        |           8 |
| parte       |           8 |
| securitate  |           8 |
| față        |           7 |

### 2025-05-22 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| președinte     |           6 |
| românia        |           5 |
| vrea           |           5 |
| nicușor        |           4 |
| dan            |           4 |
| ceremonie      |           4 |
| urma           |           4 |
| spune          |           3 |
| sine           |           3 |
| curte          |           2 |
| constituțional |           2 |
| ccr            |           2 |
| încheia        |           2 |
| oficial        |           2 |
| discuție       |           2 |
| următor        |           2 |
| ilie           |           2 |
| bolojan        |           2 |
| interimar      |           2 |
| imagine        |           1 |

### 2025-05-22 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           4 |
| stat       |           4 |
| democratic |           3 |
| președinte |           3 |
| românia    |           3 |
| sine       |           3 |
| violență   |           2 |
| fizic      |           2 |
| verbal     |           2 |
| ales       |           2 |
| george     |           2 |
| simion     |           2 |
| spune      |           2 |
| instituție |           2 |
| vedea      |           2 |
| partid     |           2 |
| încet      |           2 |
| campanie   |           2 |
| tolera     |           1 |
| reacție    |           1 |

### 2025-05-22 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| minister   |           2 |
| hibrid     |           2 |
| afacere    |           1 |
| extern     |           1 |
| spune      |           1 |
| referire   |           1 |
| articol    |           1 |
| falsificat |           1 |
| purta      |           1 |
| marcă      |           1 |
| euron      |           1 |
| news       |           1 |
| element    |           1 |
| standard   |           1 |
| set        |           1 |
| instrument |           1 |
| rusesc     |           1 |
| vrea       |           1 |
| evita      |           1 |
| românia    |           1 |

### 2025-05-22 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| mesaj         |           5 |
| vota          |           4 |
| vrea          |           3 |
| milogule      |           2 |
| vot           |           2 |
| băga          |           2 |
| seamă         |           2 |
| alegere       |           2 |
| premier       |           2 |
| românia       |           2 |
| treabă        |           2 |
| felicitare    |           2 |
| georgiei      |           2 |
| meloni        |           2 |
| român         |           2 |
| dumneavoastră |           2 |
| important     |           2 |
| lucru         |           2 |
| încerca       |           2 |
| muzică        |           1 |

### 2025-05-22 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| deficit    |           9 |
| vrea       |           7 |
| economic   |           5 |
| bugetar    |           4 |
| însemna    |           4 |
| nicușor    |           4 |
| dan        |           4 |
| creștere   |           4 |
| parte      |           4 |
| președinte |           3 |
| ales       |           3 |
| românia    |           3 |
| țintă      |           3 |
| european   |           3 |
| moment     |           3 |
| recesiune  |           3 |
| taxă       |           3 |
| guvern     |           3 |
| estima     |           2 |
| ajunge     |           2 |

### 2025-05-22 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           7 |
| sine         |           7 |
| trebui       |           6 |
| exista       |           6 |
| român        |           6 |
| afacere      |           6 |
| diasporă     |           5 |
| spune        |           5 |
| ban          |           5 |
| om           |           4 |
| sistematic   |           4 |
| partid       |           4 |
| discuție     |           4 |
| minister     |           3 |
| românia      |           3 |
| reprezentant |           2 |
| președinte   |           2 |
| inițiativă   |           2 |
| lucru        |           2 |
| parte        |           2 |

### 2025-05-22 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           4 |
| alegere      |           3 |
| trebui       |           2 |
| anulare      |           2 |
| an           |           2 |
| trecut       |           2 |
| președinte   |           2 |
| putea        |           2 |
| noiembrie    |           2 |
| interior     |           2 |
| legitim      |           2 |
| american     |           2 |
| alina        |           1 |
| mulțumi      |           1 |
| nicușordan   |           1 |
| anunța       |           1 |
| lămurit      |           1 |
| clar         |           1 |
| problemă     |           1 |
| prezidențial |           1 |

### 2025-05-22 — video-transcript

| cuvânt           |   frecvență |
|:-----------------|------------:|
| vrea             |           4 |
| românia          |           2 |
| provocare        |           2 |
| lupta            |           2 |
| aplauze          |           1 |
| urma             |           1 |
| capitol          |           1 |
| istorie          |           1 |
| recent           |           1 |
| contemporană     |           1 |
| vreau            |           1 |
| asigur           |           1 |
| cetățean         |           1 |
| român            |           1 |
| înțelege         |           1 |
| responsabilitate |           1 |
| mandat           |           1 |
| spera            |           1 |
| duce             |           1 |
| bun              |           1 |

### 2025-05-22 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| rus          |           8 |
| românia      |           6 |
| parte        |           6 |
| federație    |           5 |
| spune        |           5 |
| cameră       |           4 |
| supraveghere |           4 |
| acredita     |           4 |
| idee         |           4 |
| extern       |           4 |
| alegere      |           3 |
| atac         |           3 |
| reprezentant |           3 |
| ucraina      |           3 |
| hibrid       |           2 |
| prezidențial |           2 |
| serviciu     |           2 |
| securitate   |           2 |
| britanic     |           2 |
| cibernetic   |           2 |

### 2025-05-23 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| deficit    |          12 |
| bugetar    |           8 |
| vrea       |           8 |
| taxă       |           7 |
| sine       |           6 |
| românia    |           5 |
| situație   |           4 |
| economic   |           4 |
| țintă      |           4 |
| creștere   |           4 |
| afla       |           3 |
| măsură     |           3 |
| țară       |           3 |
| președinte |           3 |
| spune      |           3 |
| european   |           3 |
| guvern     |           3 |
| moment     |           3 |
| ron        |           3 |
| impozit    |           3 |

### 2025-05-24 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           5 |
| educație     |           3 |
| crede        |           3 |
| ăă           |           3 |
| avantaj      |           2 |
| competitiv   |           2 |
| trebui       |           2 |
| zonă         |           2 |
| stat         |           2 |
| schimba      |           2 |
| autoritate   |           2 |
| mediu        |           2 |
| universitar  |           2 |
| aștepta      |           2 |
| oportunitate |           1 |
| sistem       |           1 |
| greu         |           1 |
| recuperezi   |           1 |
| tradiție     |           1 |
| oricâți      |           1 |

### 2025-05-26 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |         251 |
| președinte |         120 |
| moment     |          98 |
| sine       |          87 |
| vedea      |          87 |
| spune      |          86 |
| domn       |          82 |
| românia    |          80 |
| trebui     |          72 |
| important  |          62 |
| nicușor    |          61 |
| dan        |          60 |
| putea      |          59 |
| guvern     |          48 |
| crede      |          43 |
| parlament  |          41 |
| psd        |          39 |
| discuție   |          39 |
| veni       |          37 |
| guvernare  |          36 |

### 2025-05-26 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| președinte |           4 |
| nicușor    |           3 |
| dan        |           3 |
| parlament  |           3 |
| guvern     |           3 |
| oră        |           2 |
| deveni     |           2 |
| vrea       |           2 |
| actual     |           2 |
| interimar  |           2 |
| mandat     |           2 |
| formare    |           2 |
| psd        |           2 |
| oficial    |           1 |
| țară       |           1 |
| colegă     |           1 |
| ruth       |           1 |
| novakovici |           1 |
| prezenta   |           1 |
| agendă     |           1 |

### 2025-05-26 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          32 |
| sine       |          20 |
| președinte |          16 |
| psd        |          14 |
| putea      |          10 |
| guvernare  |          10 |
| vedea      |           9 |
| spune      |           8 |
| crede      |           8 |
| om         |           8 |
| parte      |           7 |
| guvern     |           7 |
| vorbă      |           7 |
| usr        |           7 |
| domn       |           6 |
| rămâne     |           6 |
| opoziție   |           6 |
| iohannis   |           6 |
| extern     |           5 |
| același    |           5 |

### 2025-05-26 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| președinte     |          30 |
| vrea           |          23 |
| muzică         |          21 |
| vedea          |          13 |
| românia        |          13 |
| șef            |          13 |
| stat           |          13 |
| jurământ       |          11 |
| față           |          11 |
| parlament      |          11 |
| nicușor        |          11 |
| sine           |          10 |
| dan            |          10 |
| oficial        |           9 |
| prezent        |           9 |
| putea          |           9 |
| constituțional |           9 |
| moment         |           9 |
| palat          |           8 |
| ales           |           8 |

### 2025-05-26 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |           4 |
| ieși          |           2 |
| majoritate    |           2 |
| spune         |           2 |
| guvern        |           2 |
| românia       |           2 |
| întâmpla      |           2 |
| lună          |           2 |
| rezolvăm      |           2 |
| vrea          |           1 |
| iată          |           1 |
| nicușor       |           1 |
| dan           |           1 |
| plen          |           1 |
| încercui      |           1 |
| jurnalist     |           1 |
| asculta       |           1 |
| identifica    |           1 |
| profesioniști |           1 |
| om            |           1 |

### 2025-05-26 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          86 |
| sine       |          47 |
| românia    |          29 |
| președinte |          27 |
| român      |          19 |
| putea      |          17 |
| spune      |          16 |
| vedea      |          15 |
| țară       |          15 |
| nicușor    |          15 |
| moment     |          14 |
| palat      |          14 |
| dan        |          14 |
| sistem     |          14 |
| nicușordan |          13 |
| reformă    |          13 |
| cotroceni  |          12 |
| atât       |          12 |
| trebui     |          11 |
| ști        |          11 |

### 2025-05-27 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| plictisi    |           2 |
| președinte  |           2 |
| dimineața   |           2 |
| muzică      |           1 |
| fetiță      |           1 |
| nicușor     |           1 |
| dan         |           1 |
| cotroceni   |           1 |
| ceremonie   |           1 |
| învestitură |           1 |
| declara     |           1 |
| adăuga      |           1 |
| fapt        |           1 |
| vrea        |           1 |
| rămâne      |           1 |
| actual      |           1 |
| casă        |           1 |
| final       |           1 |
| an          |           1 |
| școlar      |           1 |

### 2025-05-28 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| discuție   |           2 |
| loc        |           2 |
| vrea       |           2 |
| sta        |           1 |
| cotu       |           1 |
| tehnic     |           1 |
| găsi       |           1 |
| putea      |           1 |
| tăiem      |           1 |
| cheltuială |           1 |
| stat       |           1 |
| vedea      |           1 |
| viziune    |           1 |
| partid     |           1 |
| preconizat |           1 |
| guvern     |           1 |
| domn       |           1 |
| spere      |           1 |
| săptămână  |           1 |
| cară       |           1 |

### 2025-05-29 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| discuție      |          10 |
| vrea          |           9 |
| moment        |           8 |
| guvern        |           7 |
| începe        |           6 |
| informație    |           5 |
| serviciu      |           4 |
| stat          |           4 |
| variantă      |           4 |
| premier       |           4 |
| bun           |           3 |
| partid        |           3 |
| cheltuială    |           3 |
| om            |           3 |
| ști           |           3 |
| dumneavoastră |           3 |
| economic      |           3 |
| reprezentant  |           3 |
| politic       |           3 |
| apărea        |           3 |

### 2025-05-29 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| muzică     |          10 |
| erou       |           3 |
| sine       |           3 |
| președinte |           2 |
| mormânt    |           2 |
| ostaș      |           2 |
| necunoscut |           2 |
| domn       |           2 |
| câmp       |           2 |
| luptă      |           2 |
| religios   |           2 |
| parte      |           2 |
| nicușordan |           1 |
| sosi       |           1 |
| doamnă     |           1 |
| comemorăm  |           1 |
| femeie     |           1 |
| bărbat     |           1 |
| sacrifica  |           1 |
| urmărim    |           1 |

### 2025-05-30 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| declarație |           2 |
| ccr        |           2 |
| acces      |           2 |
| probabil   |           2 |
| chestiune  |           2 |
| ține       |           2 |
| lege       |           2 |
| publica    |           2 |
| ăă         |           1 |
| desigur    |           1 |
| avere      |           1 |
| decizie    |           1 |
| sine       |           1 |
| referi     |           1 |
| public     |           1 |
| afere      |           1 |
| surprinde  |           1 |
| personal   |           1 |
| trebui     |           1 |
| redacta    |           1 |

### 2025-05-30 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           4 |
| discuție   |           3 |
| trebui     |           3 |
| creștere   |           3 |
| impozitare |           3 |
| președinte |           2 |
| stat       |           2 |
| lucru      |           2 |
| tva        |           2 |
| muncă      |           2 |
| taxă       |           2 |
| crește     |           2 |
| oră        |           1 |
| programa   |           1 |
| nicușor    |           1 |
| dan        |           1 |
| șefii      |           1 |
| partid     |           1 |
| pro        |           1 |
| occidental |           1 |

### 2025-05-30 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| donald     |           4 |
| trump      |           4 |
| merge      |           4 |
| românia    |           3 |
| probabil   |           3 |
| președinte |           2 |
| invita     |           2 |
| crede      |           2 |
| întâi      |           2 |
| stat       |           2 |
| unit       |           2 |
| ocupa      |           2 |
| decât      |           2 |
| deocamdată |           2 |
| lună       |           2 |
| summit     |           2 |
| extrem     |           2 |
| nicușordan |           1 |
| spune      |           1 |
| curs       |           1 |

### 2025-06-02 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| psd        |          44 |
| vrea       |          43 |
| sine       |          39 |
| partid     |          38 |
| domn       |          30 |
| putea      |          30 |
| guvern     |          29 |
| președinte |          28 |
| spune      |          24 |
| crede      |          23 |
| guvernare  |          21 |
| vedea      |          21 |
| ști        |          16 |
| nicușor    |          15 |
| moment     |          14 |
| dan        |          14 |
| politic    |          13 |
| intra      |          13 |
| bolojan    |          12 |
| săptămână  |          10 |

### 2025-06-02 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| țară                            |           5 |
| militar                         |           5 |
| an                              |           4 |
| parte                           |           4 |
| summit                          |           4 |
| gata                            |           3 |
| northatlantictreatyorganization |           3 |
| simți                           |           3 |
| război                          |           3 |
| ucraina                         |           3 |
| haga                            |           3 |
| vrea                            |           3 |
| cheltuială                      |           3 |
| spune                           |           2 |
| bucurești                       |           2 |
| inițiativă                      |           2 |
| românia                         |           2 |
| flanc                           |           2 |
| estic                           |           2 |
| amenințare                      |           2 |

### 2025-06-03 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| discuție |           8 |
| ron      |           8 |
| sine     |           6 |
| european |           6 |
| țară     |           5 |
| comisie  |           5 |
| putea    |           5 |
| stat     |           4 |
| spor     |           4 |
| deficit  |           4 |
| românia  |           3 |
| nicușor  |           3 |
| dan      |           3 |
| fond     |           3 |
| măsură   |           3 |
| număr    |           3 |
| spune    |           3 |
| salariu  |           3 |
| excesiv  |           3 |
| promite  |           2 |

### 2025-06-03 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| domn       |           3 |
| serviciu   |           3 |
| informație |           3 |
| sri        |           3 |
| stat       |           2 |
| sine       |           2 |
| ban        |           2 |
| evaziune   |           2 |
| asear      |           1 |
| discuție   |           1 |
| prim       |           1 |
| ministru   |           1 |
| interimar  |           1 |
| predoiu    |           1 |
| șică       |           1 |
| trebui     |           1 |
| strategie  |           1 |
| național   |           1 |
| apărare    |           1 |
| aducem     |           1 |

### 2025-06-03 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| sine     |         126 |
| trebui   |         105 |
| vrea     |          97 |
| putea    |          97 |
| spune    |          83 |
| vedea    |          65 |
| ști      |          53 |
| problemă |          50 |
| victimă  |          47 |
| violență |          41 |
| femeie   |          38 |
| an       |          36 |
| lucru    |          34 |
| moment   |          33 |
| serviciu |          33 |
| exista   |          32 |
| om       |          30 |
| românia  |          29 |
| măsură   |          29 |
| crede    |          28 |

### 2025-06-04 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| moment    |           8 |
| vrea      |           7 |
| discuție  |           6 |
| program   |           6 |
| spune     |           6 |
| iunie     |           6 |
| începe    |           5 |
| lucru     |           5 |
| deficit   |           5 |
| imediat   |           5 |
| partid    |           4 |
| grup      |           4 |
| parte     |           4 |
| ăă        |           4 |
| summit    |           4 |
| guvern    |           3 |
| lucra     |           3 |
| guvernare |           3 |
| lună      |           3 |
| prim      |           3 |

### 2025-06-04 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| discuție    |           7 |
| stat        |           6 |
| moment      |           6 |
| unit        |           4 |
| palier      |           4 |
| neîncredere |           3 |
| crede       |           3 |
| amenințare  |           2 |
| rus         |           2 |
| întreg      |           2 |
| europă      |           2 |
| trebui      |           2 |
| relație     |           2 |
| alegere     |           2 |
| depăși      |           2 |
| militar     |           2 |
| important   |           2 |
| cheltuială  |           2 |
| viza        |           1 |
| regiune     |           1 |

### 2025-06-04 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| octavian  |           1 |
| vasilescu |           1 |
| euronews  |           1 |
| românia   |           1 |

### 2025-06-04 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| președinte |           1 |
| nicușor    |           1 |
| dan        |           1 |
| vorbi      |           1 |
| măsură     |           1 |
| analogie   |           1 |
| pizza      |           1 |
| interesant |           1 |

### 2025-06-04 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| exclude      |           3 |
| discuție     |           3 |
| moment       |           3 |
| program      |           2 |
| guvernare    |           2 |
| guvern       |           2 |
| variantă     |           2 |
| premier      |           2 |
| tehnocrat    |           2 |
| posibilitate |           2 |
| grup         |           2 |
| partid       |           2 |
| schiță       |           1 |
| vrea         |           1 |
| prezenta     |           1 |
| putea        |           1 |
| gata         |           1 |
| săptămână    |           1 |
| spune        |           1 |
| nicușordan   |           1 |

### 2025-06-04 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| domn       |          11 |
| veni       |           5 |
| ști        |           5 |
| fotografie |           5 |
| poză       |           5 |
| lucrare    |           5 |
| tiktok     |           4 |
| obliga     |           4 |
| femeie     |           4 |
| real       |           4 |
| vedea      |           4 |
| adevărat   |           4 |
| spune      |           4 |
| bun        |           4 |
| bărbat     |           3 |
| fustă      |           3 |
| președinte |           3 |
| trebui     |           3 |
| jos        |           3 |
| sine       |           3 |

### 2025-06-05 — video-transcript

| cuvânt   | frecvență   |
|----------|-------------|

### 2025-06-09 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| partid    |           4 |
| vrea      |           4 |
| moment    |           3 |
| lucru     |           3 |
| discuție  |           3 |
| discuta   |           3 |
| scenarii  |           2 |
| cotroceni |           2 |
| lider     |           2 |
| aștepta   |           2 |
| om        |           2 |
| exista    |           2 |
| extrem    |           2 |
| intra     |           2 |
| guvernare |           2 |
| spune     |           1 |
| oară      |           1 |
| vede      |           1 |
| pachet    |           1 |
| asuma     |           1 |

### 2025-06-10 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| moldova    |          36 |
| românia    |          33 |
| vrea       |          20 |
| republică  |          19 |
| președinte |          18 |
| european   |          18 |
| proiect    |          15 |
| domn       |          14 |
| sine       |          14 |
| vorbi      |          14 |
| ucraina    |          13 |
| sprijin    |          12 |
| parte      |          12 |
| uniune     |           9 |
| spune      |           9 |
| republicii |           8 |
| putea      |           8 |
| mulțumi    |           8 |
| important  |           8 |
| veni       |           7 |

### 2025-06-10 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| moldova    |           3 |
| același    |           3 |
| garanție   |           2 |
| republicii |           2 |
| important  |           2 |
| uniune     |           2 |
| european   |           2 |
| evident    |           2 |
| război     |           2 |
| prezență   |           1 |
| continuare |           1 |
| sprijin    |           1 |
| românia    |           1 |
| acorda     |           1 |
| moment     |           1 |
| republică  |           1 |
| trăi       |           1 |
| început    |           1 |
| proces     |           1 |
| aderare    |           1 |

### 2025-06-10 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| moldova    |          21 |
| republică  |          14 |
| românia    |          13 |
| nicușor    |          12 |
| dan        |          12 |
| vizită     |          10 |
| chișinău   |           9 |
| președinte |           8 |
| spune      |           8 |
| republicii |           7 |
| oficial    |           6 |
| sine       |           6 |
| european   |           6 |
| vot        |           5 |
| vrea       |           5 |
| vedea      |           5 |
| român      |           5 |
| lucru      |           5 |
| vota       |           5 |
| putea      |           5 |

### 2025-06-10 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| spune         |          41 |
| vrea          |          33 |
| pensie        |          33 |
| măsură        |          28 |
| domn          |          25 |
| putea         |          24 |
| ron           |          24 |
| discuție      |          23 |
| sine          |          21 |
| discuta       |          16 |
| susține       |          15 |
| clar          |          14 |
| coleg         |          13 |
| moment        |          13 |
| partid        |          13 |
| dumneavoastră |          13 |
| taxă          |          13 |
| psd           |          12 |
| usr           |          12 |
| cass          |          12 |

### 2025-06-11 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          89 |
| sine       |          74 |
| partid     |          41 |
| românia    |          37 |
| trebui     |          36 |
| putea      |          35 |
| taxă       |          34 |
| spune      |          32 |
| vedea      |          29 |
| cheltuială |          29 |
| președinte |          28 |
| exista     |          28 |
| discuție   |          27 |
| măsură     |          25 |
| bun        |          24 |
| vorbi      |          24 |
| domn       |          23 |
| an         |          21 |
| veni       |          21 |
| stat       |          20 |

### 2025-06-11 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| posibilitate |           3 |
| vorbi        |           3 |
| taxă         |           3 |
| ăă           |           2 |
| parte        |           2 |
| ajunge       |           2 |
| blocaj       |           1 |
| discuție     |           1 |
| tehnic       |           1 |
| efect        |           1 |
| evident      |           1 |
| continuu     |           1 |
| spune        |           1 |
| semnare      |           1 |
| prim         |           1 |
| ministru     |           1 |
| săptămână    |           1 |
| rămâne       |           1 |
| promisiune   |           1 |
| comisie      |           1 |

### 2025-06-20 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| partid     |           6 |
| vrea       |           6 |
| românia    |           6 |
| guvern     |           5 |
| domn       |           4 |
| majoritate |           4 |
| discuție   |           4 |
| parte      |           4 |
| politic    |           3 |
| dificil    |           3 |
| guvernare  |           3 |
| român      |           3 |
| persoană   |           3 |
| președinte |           3 |
| țară       |           3 |
| gata       |           2 |
| ilie       |           2 |
| prim       |           2 |
| ministru   |           2 |
| mulțumi    |           2 |

### 2025-06-25 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| sacrificiu  |           2 |
| decât       |           2 |
| speranță    |           1 |
| guvern      |           1 |
| ajustările  |           1 |
| necesar     |           1 |
| funcționare |           1 |
| aparat      |           1 |
| stat        |           1 |
| deficit     |           1 |
| reduce      |           1 |
| evident     |           1 |
| lume        |           1 |
| ideal       |           1 |
| ban         |           1 |
| educație    |           1 |
| armată      |           1 |
| continuăm   |           1 |
| crește      |           1 |
| cheltuială  |           1 |

### 2025-06-26 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| trebui   |           8 |
| vrea     |           8 |
| românia  |           8 |
| împrumut |           7 |
| spune    |           6 |
| moldova  |           5 |
| produce  |           5 |
| european |           4 |
| guvern   |           4 |
| sine     |           4 |
| degrabă  |           4 |
| asuma    |           4 |
| lua      |           4 |
| ucraina  |           4 |
| putea    |           4 |
| explica  |           4 |
| domn     |           3 |
| comisie  |           3 |
| discuție |           3 |
| proiect  |           3 |

### 2025-06-26 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| reafirma      |           3 |
| prezență      |           3 |
| românia       |           3 |
| reafirmare    |           2 |
| aliat         |           2 |
| sine          |           1 |
| unitate       |           1 |
| transatlantic |           1 |
| implicit      |           1 |
| continuare    |           1 |
| american      |           1 |
| europa        |           1 |
| rusia         |           1 |
| pericol       |           1 |
| sprijin       |           1 |
| ucraina       |           1 |
| mulțumi       |           1 |
| prezent       |           1 |
| operațiun     |           1 |
| regiune       |           1 |

### 2025-07-14 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          70 |
| spune         |          37 |
| ăă            |          36 |
| moment        |          36 |
| românia       |          32 |
| lege          |          25 |
| ron           |          25 |
| guvern        |          23 |
| întrebare     |          22 |
| sine          |          22 |
| trebui        |          21 |
| chestiune     |          20 |
| putea         |          20 |
| persoană      |          20 |
| măsură        |          19 |
| președinte    |          19 |
| an            |          18 |
| vedea         |          17 |
| dumneavoastră |          16 |
| om            |          14 |

### 2025-07-14 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| moment     |           3 |
| vrea       |           3 |
| măsură     |           3 |
| tva        |           2 |
| octombrie  |           2 |
| comisie    |           2 |
| putea      |           2 |
| angajament |           1 |
| guvern     |           1 |
| investi    |           1 |
| crește     |           1 |
| reevaluare |           1 |
| început    |           1 |
| lună       |           1 |
| evaluare   |           1 |
| vedea      |           1 |
| suficient  |           1 |
| ăă         |           1 |
| românia    |           1 |
| trece      |           1 |

### 2025-07-14 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| problemă |           4 |
| ăă       |           3 |
| vrea     |           3 |
| femeie   |           2 |
| stat     |           2 |
| român    |           2 |
| lege     |           2 |
| aplica   |           2 |
| moment   |           2 |
| fenomen  |           2 |
| grav     |           2 |
| jumătate |           1 |
| an       |           1 |
| vorbim   |           1 |
| caz      |           1 |
| știută   |           1 |
| femicid  |           1 |
| vorbi    |           1 |
| număr    |           1 |
| supune   |           1 |

### 2025-07-14 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| moment        |           6 |
| lege          |           6 |
| vrea          |           4 |
| pensie        |           3 |
| magistraților |           2 |
| ăă            |           2 |
| decât         |           2 |
| salariu       |           2 |
| ieși          |           2 |
| prevedere     |           2 |
| tranzitoriu   |           2 |
| pensionară    |           2 |
| extrem        |           2 |
| parlament     |           2 |
| chestiune     |           1 |
| important     |           1 |
| vorbi         |           1 |
| set           |           1 |
| măsură        |           1 |
| special       |           1 |

### 2025-07-14 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |           3 |
| rusia      |           3 |
| dori       |           2 |
| vecin      |           2 |
| spune      |           2 |
| ucraina    |           2 |
| muzică     |           1 |
| nicușor    |           1 |
| dan        |           1 |
| președinte |           1 |
| anunța     |           1 |
| țară       |           1 |
| vrea       |           1 |
| continua   |           1 |
| ajuta      |           1 |
| război     |           1 |
| românia    |           1 |
| sprijini   |           1 |
| inclusiv   |           1 |
| echipament |           1 |

### 2025-07-14 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| președinte    |          11 |
| fiscal        |           6 |
| măsură        |           5 |
| informație    |           5 |
| serviciu      |           5 |
| dan           |           4 |
| guvern        |           4 |
| reacție       |           4 |
| administrație |           4 |
| prezidențial  |           4 |
| nicușordan    |           4 |
| nicușor       |           3 |
| pachet        |           3 |
| aștepta       |           3 |
| vasile        |           3 |
| problemă      |           3 |
| trebui        |           3 |
| clarifica     |           3 |
| moment        |           3 |
| spune         |           3 |

### 2025-07-15 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| stat     |           7 |
| măsură   |           6 |
| vrea     |           6 |
| putea    |           5 |
| majorare |           4 |
| tva      |           4 |
| pachet   |           4 |
| șef      |           4 |
| bugetar  |           4 |
| buget    |           4 |
| românia  |           3 |
| moment   |           3 |
| guvern   |           3 |
| fiscal   |           3 |
| lua      |           3 |
| reducere |           3 |
| deficit  |           3 |
| ron      |           3 |
| trece    |           2 |
| sine     |           2 |

### 2025-07-16 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| spune     |           4 |
| stat      |           3 |
| trebui    |           2 |
| ajunge    |           2 |
| transmite |           2 |
| român     |           2 |
| vrea      |           2 |
| violență  |           1 |
| domestic  |           1 |
| grav      |           1 |
| caz       |           1 |
| ucidere   |           1 |
| decurge   |           1 |
| vedea     |           1 |
| ultim     |           1 |
| perioadă  |           1 |
| minister  |           1 |
| afacere   |           1 |
| intern    |           1 |
| parchet   |           1 |

### 2025-07-16 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| trebui      |          10 |
| minister    |           8 |
| stat        |           7 |
| român       |           6 |
| spune       |           5 |
| afacere     |           5 |
| intern      |           5 |
| transmite   |           5 |
| sine        |           5 |
| muncă       |           4 |
| partener    |           4 |
| an          |           4 |
| uita        |           3 |
| rând        |           3 |
| societate   |           3 |
| caz         |           3 |
| ajunge      |           3 |
| bineînțeles |           3 |
| consum      |           3 |
| drog        |           3 |

### 2025-07-18 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| european      |          36 |
| vrea          |          25 |
| românia       |          24 |
| uniune        |          21 |
| sine          |          20 |
| ucraina       |          19 |
| țară          |          18 |
| discuta       |          16 |
| privi         |          15 |
| germania      |          13 |
| an            |          13 |
| parte         |          13 |
| trebui        |          12 |
| rusia         |          12 |
| vedere        |          11 |
| președinte    |          10 |
| plan          |          10 |
| proces        |          10 |
| întrebare     |          10 |
| dumneavoastră |           9 |

### 2025-07-18 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| vrea      |          19 |
| spune     |          19 |
| moment    |          18 |
| sine      |          16 |
| vedea     |          15 |
| discuție  |          14 |
| putea     |          13 |
| om        |          11 |
| evident   |           8 |
| exista    |           8 |
| românia   |           8 |
| persoană  |           7 |
| parte     |           7 |
| lucru     |           6 |
| mesaj     |           6 |
| față      |           6 |
| poliție   |           6 |
| trebui    |           6 |
| întrebare |           6 |
| stat      |           6 |

### 2025-07-21 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| românia      |           6 |
| stat         |           6 |
| spune        |           6 |
| domn         |           5 |
| alegere      |           5 |
| președinte   |           4 |
| nicușor      |           4 |
| dan          |           4 |
| vorbi        |           4 |
| sine         |           4 |
| comunitate   |           4 |
| semnal       |           4 |
| interferență |           3 |
| european     |           3 |
| inclusiv     |           3 |
| evident      |           3 |
| intelligence |           3 |
| ministru     |           3 |
| important    |           3 |
| postare      |           3 |

### 2025-07-25 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| președinte |           8 |
| austria    |           7 |
| stat       |           7 |
| românia    |           6 |
| iată       |           5 |
| doamnă     |           5 |
| viena      |           4 |
| vizită     |           4 |
| vedea      |           4 |
| vrea       |           4 |
| salzburg   |           4 |
| sine       |           4 |
| domeniu    |           4 |
| oră        |           3 |
| oficial    |           3 |
| omolog     |           3 |
| austriac   |           3 |
| moment     |           3 |
| muzică     |           3 |
| copil      |           3 |

### 2025-07-25 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           7 |
| sine         |           4 |
| oră          |           4 |
| an           |           3 |
| școlar       |           3 |
| coleg        |           3 |
| rată         |           3 |
| renunța      |           3 |
| anunța       |           2 |
| spune        |           2 |
| putea        |           2 |
| analfabetism |           2 |
| funcțional   |           2 |
| loc          |           2 |
| ști          |           2 |
| permite      |           2 |
| rămâne       |           2 |
| reluare      |           1 |
| protestelor  |           1 |
| afla         |           1 |

### 2025-07-30 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |          46 |
| ăă         |          44 |
| spune      |          34 |
| vrea       |          32 |
| domn       |          27 |
| trebui     |          25 |
| putea      |          22 |
| moment     |          20 |
| om         |          19 |
| românia    |          18 |
| parte      |          18 |
| vedea      |          17 |
| întrebare  |          16 |
| magistrat  |          15 |
| președinte |          15 |
| pensie     |          14 |
| rămâne     |          14 |
| pensionară |          14 |
| justiție   |          13 |
| ști        |          13 |

### 2025-07-30 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |         104 |
| sine       |          97 |
| spune      |          77 |
| ăă         |          76 |
| trebui     |          57 |
| putea      |          56 |
| om         |          51 |
| domn       |          46 |
| întrebare  |          44 |
| vedea      |          44 |
| parte      |          42 |
| moment     |          41 |
| exista     |          36 |
| românia    |          35 |
| ști        |          32 |
| președinte |          32 |
| crede      |          31 |
| sistem     |          29 |
| lege       |          29 |
| an         |          29 |

### 2025-07-30 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |           9 |
| coaliție    |           5 |
| ședință     |           3 |
| dragoș      |           3 |
| anastasiu   |           3 |
| ilie        |           3 |
| bolojan     |           3 |
| reformă     |           3 |
| companiilor |           3 |
| stat        |           3 |
| însă        |           3 |
| trebui      |           3 |
| găsi        |           3 |
| discuta     |           3 |
| pachet      |           3 |
| număr       |           3 |
| ban         |           3 |
| primar      |           3 |
| sine        |           3 |
| oră         |           2 |

### 2025-07-31 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |         102 |
| sine          |          95 |
| ăă            |          79 |
| spune         |          78 |
| trebui        |          57 |
| putea         |          55 |
| om            |          50 |
| domn          |          46 |
| vedea         |          44 |
| întrebare     |          43 |
| parte         |          42 |
| moment        |          41 |
| exista        |          36 |
| românia       |          35 |
| ști           |          32 |
| președinte    |          31 |
| crede         |          31 |
| lege          |          29 |
| an            |          29 |
| dumneavoastră |          28 |

### 2025-07-31 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| pensionară    |           4 |
| cerere        |           3 |
| președinte    |           2 |
| om            |           2 |
| sine          |           2 |
| pensiona      |           2 |
| nicușor       |           1 |
| dan           |           1 |
| lua           |           1 |
| poziție       |           1 |
| trimite       |           1 |
| aprobare      |           1 |
| număr         |           1 |
| magistraților |           1 |
| analiză       |           1 |
| rezulta       |           1 |
| întrebare     |           1 |
| csm           |           1 |
| debandadă     |           1 |
| indica        |           1 |

### 2025-08-24 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| ucraina      |           7 |
| and          |           7 |
| the          |           5 |
| vrea         |           5 |
| for          |           4 |
| zelenschi    |           4 |
| ucrainian    |           4 |
| moscova      |           4 |
| președinte   |           3 |
| față         |           3 |
| ukraines     |           3 |
| to           |           3 |
| european     |           3 |
| independență |           3 |
| centrală     |           3 |
| lider        |           3 |
| volodimir    |           3 |
| garanție     |           3 |
| anunța       |           3 |
| mesaj        |           2 |

### 2025-08-26 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          15 |
| trebui        |          15 |
| românia       |          13 |
| sine          |           8 |
| dumneavoastră |           7 |
| economic      |           6 |
| strategie     |           6 |
| domn          |           5 |
| român         |           5 |
| economie      |           5 |
| continua      |           5 |
| muzică        |           4 |
| direct        |           4 |
| putea         |           4 |
| an            |           4 |
| evident       |           4 |
| european      |           4 |
| parteneriat   |           4 |
| strategic     |           4 |
| securitate    |           4 |

### 2025-08-29 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |          94 |
| vrea       |          76 |
| spune      |          63 |
| trebui     |          57 |
| putea      |          51 |
| an         |          45 |
| stat       |          38 |
| vedea      |          34 |
| om         |          31 |
| ajunge     |          30 |
| veni       |          29 |
| lucru      |          28 |
| președinte |          27 |
| întâmpla   |          26 |
| moment     |          24 |
| crede      |          24 |
| elev       |          24 |
| bun        |          23 |
| ron        |          23 |
| începe     |          22 |

### 2025-08-31 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           2 |
| opinie     |           1 |
| exemplu    |           1 |
| europa     |           1 |
| lume       |           1 |
| întreg     |           1 |
| încerca    |           1 |
| apăra      |           1 |
| democrație |           1 |
| față       |           1 |
| acelorași  |           1 |
| tip        |           1 |
| presiune   |           1 |
| veni       |           1 |
| același    |           1 |
| parte      |           1 |
| dovedi     |           1 |
| decât      |           1 |
| europene   |           1 |
| loc        |           1 |

### 2025-09-01 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| măsură     |           3 |
| sine       |           3 |
| moment     |           3 |
| vrea       |           3 |
| chestiune  |           3 |
| președinte |           2 |
| spune      |           2 |
| dificil    |           2 |
| presiune   |           2 |
| greșeli    |           2 |
| trebui     |           2 |
| corecta    |           2 |
| lună       |           2 |
| rămâne     |           2 |
| an         |           2 |
| putea      |           2 |
| săptămână  |           2 |
| nicușordan |           1 |
| urma       |           1 |
| perioadă   |           1 |

### 2025-09-02 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |          17 |
| românia    |          17 |
| vrea       |          14 |
| ști        |          13 |
| putea      |          12 |
| trebui     |          10 |
| important  |          10 |
| sine       |           9 |
| vorbi      |           9 |
| safe       |           9 |
| apărare    |           9 |
| economic   |           8 |
| domn       |           7 |
| europa     |           7 |
| program    |           7 |
| investiție |           7 |
| stat       |           7 |
| președinte |           6 |
| parte      |           6 |
| constanța  |           6 |

### 2025-09-03 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| coaliție   |           5 |
| funcționa  |           4 |
| spune      |           3 |
| merge      |           3 |
| partid     |           2 |
| vrea       |           2 |
| moment     |           2 |
| guvernare  |           1 |
| nicuan     |           1 |
| negociere  |           1 |
| locier     |           1 |
| palat      |           1 |
| cotroceni  |           1 |
| lidere     |           1 |
| președinte |           1 |
| preciza    |           1 |
| însă       |           1 |
| fapt       |           1 |
| actual     |           1 |
| haideți    |           1 |

### 2025-09-03 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| energie     |           6 |
| lucrare     |           5 |
| vrea        |           5 |
| nuclear     |           4 |
| important   |           4 |
| electric    |           4 |
| românia     |           4 |
| domn        |           3 |
| avantaj     |           3 |
| competitiv  |           3 |
| ambasador   |           2 |
| tehnologie  |           2 |
| putea       |           2 |
| vorbi       |           2 |
| reactoar    |           2 |
| partener    |           2 |
| stat        |           2 |
| inteligență |           2 |
| artificial  |           2 |
| domnilor    |           1 |

### 2025-09-05 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| pensie         |           5 |
| om             |           4 |
| special        |           3 |
| curte          |           3 |
| constituțional |           3 |
| sine           |           3 |
| vrea           |           3 |
| putea          |           3 |
| guvern         |           3 |
| președinte     |           2 |
| declara        |           2 |
| uita           |           2 |
| fapt           |           2 |
| constat        |           2 |
| magistrații    |           2 |
| nicușord       |           1 |
| intervine      |           1 |
| scandal        |           1 |
| tăiere         |           1 |
| creștere       |           1 |

### 2025-09-05 — video-transcript

| cuvânt          |   frecvență |
|:----------------|------------:|
| pace            |           5 |
| ucraina         |           3 |
| eventual        |           3 |
| vrea            |           2 |
| trimite         |           2 |
| menținere       |           2 |
| președinte      |           2 |
| decizie         |           2 |
| rusia           |           2 |
| încetare        |           2 |
| foc             |           2 |
| românia         |           1 |
| trupă           |           1 |
| înunț           |           1 |
| nicușordan      |           1 |
| oră             |           1 |
| participa       |           1 |
| videoconferință |           1 |
| întâlnire       |           1 |
| lider           |           1 |

### 2025-09-10 — video-transcript

| cuvânt   | frecvență   |
|----------|-------------|

### 2025-09-10 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| reacționa  |           3 |
| polonia    |           3 |
| românia    |           2 |
| vrea       |           2 |
| președinte |           2 |
| nicușordan |           2 |
| dron       |           1 |
| vladimir   |           1 |
| putin      |           1 |
| ajunge     |           1 |
| teritoriu  |           1 |
| țară       |           1 |
| spune      |           1 |
| reacție    |           1 |
| incidentă  |           1 |
| loc        |           1 |
| adăuga     |           1 |
| fapt       |           1 |
| nivel      |           1 |
| alertă     |           1 |

### 2025-09-11 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| diasporă   |           5 |
| român      |           4 |
| america    |           3 |
| vrea       |           3 |
| chestiune  |           2 |
| relație    |           2 |
| bun        |           2 |
| an         |           2 |
| consistent |           2 |
| parte      |           2 |
| securitate |           2 |
| sine       |           2 |
| vorbi      |           2 |
| niciun     |           2 |
| preocupare |           2 |
| vizita     |           1 |
| loc        |           1 |
| coordonată |           1 |
| dori       |           1 |
| putea      |           1 |

### 2025-09-11 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| ban       |          14 |
| sine      |          10 |
| spune     |           8 |
| ucraina   |           7 |
| românia   |           6 |
| trebui    |           6 |
| vrea      |           5 |
| apărare   |           4 |
| chestiune |           4 |
| țară      |           4 |
| parte     |           4 |
| decât     |           4 |
| ști       |           3 |
| public    |           3 |
| ajuta     |           3 |
| adică     |           3 |
| lume      |           3 |
| apăra     |           3 |
| vedea     |           3 |
| aur       |           3 |

### 2025-09-11 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| stat       |          15 |
| exista     |          15 |
| românia    |          14 |
| zonă       |          13 |
| sine       |          13 |
| serviciu   |          12 |
| rus        |           9 |
| putea      |           9 |
| om         |           8 |
| spune      |           7 |
| an         |           7 |
| adică      |           7 |
| moment     |           7 |
| vrea       |           7 |
| coaliție   |           7 |
| funcționa  |           6 |
| informație |           6 |
| discuție   |           6 |
| lung       |           6 |
| sigur      |           6 |

### 2025-09-11 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| exista    |           7 |
| partid    |           6 |
| arăta     |           6 |
| coaliție  |           5 |
| trebui    |           5 |
| sine      |           4 |
| guvern    |           4 |
| spune     |           4 |
| putea     |           4 |
| pro       |           4 |
| societate |           4 |
| republică |           4 |
| moldova   |           4 |
| crede     |           4 |
| bucurești |           3 |
| problemă  |           3 |
| evident   |           3 |
| alegere   |           3 |
| vrea      |           3 |
| zonă      |           3 |

### 2025-09-12 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| parte      |           3 |
| an         |           2 |
| atac       |           2 |
| hibrid     |           2 |
| federației |           2 |
| rus        |           2 |
| influența  |           2 |
| societate  |           2 |
| spune      |           2 |
| stat       |           2 |
| românia    |           2 |
| începe     |           2 |
| moment     |           2 |
| încet      |           2 |
| captura    |           2 |
| zonă       |           2 |
| țară       |           1 |
| declara    |           1 |
| președinte |           1 |
| nicușordan |           1 |

### 2025-09-16 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| putea      |           4 |
| trebui     |           3 |
| președinte |           2 |
| decizie    |           2 |
| teritoriu  |           2 |
| românesc   |           2 |
| comandant  |           2 |
| operațiune |           2 |
| pagubă     |           2 |
| colateral  |           2 |
| știm       |           2 |
| interval   |           2 |
| spune      |           2 |
| exista     |           2 |
| caz        |           2 |
| moment     |           2 |
| nicușor    |           1 |
| dan        |           1 |
| declara    |           1 |
| lega       |           1 |

### 2025-09-16 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| putea      |           4 |
| armată     |           3 |
| spune      |           3 |
| ucraina    |           3 |
| urmări     |           3 |
| ști        |           2 |
| dronă      |           2 |
| ruseasc    |           2 |
| aerian     |           2 |
| veni       |           2 |
| avion      |           2 |
| dispărea   |           2 |
| radar      |           2 |
| duce       |           2 |
| președinte |           1 |
| nicușor    |           1 |
| dan        |           1 |
| recunoaște |           1 |
| român      |           1 |
| intra      |           1 |

### 2025-09-23 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| președinte    |          11 |
| coaliție      |           9 |
| discuție      |           9 |
| parte         |           9 |
| veni          |           5 |
| arăta         |           4 |
| ședință       |           4 |
| informație    |           4 |
| administrație |           4 |
| susținere     |           4 |
| sine          |           3 |
| rămâne        |           3 |
| vrea          |           3 |
| premier       |           3 |
| singur        |           3 |
| măsură        |           3 |
| moment        |           3 |
| urmă          |           3 |
| guvernare     |           3 |
| românia       |           3 |

### 2025-09-25 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| spune       |           2 |
| zonă        |           2 |
| cibernetic  |           2 |
| vedea       |           2 |
| exista      |           1 |
| direcție    |           1 |
| acțiune     |           1 |
| ăă          |           1 |
| online      |           1 |
| numită      |           1 |
| securitate  |           1 |
| același     |           1 |
| raport      |           1 |
| parchetului |           1 |
| general     |           1 |
| perioadă    |           1 |
| alegere     |           1 |
| atac        |           1 |
| diferit     |           1 |
| structură   |           1 |

### 2025-09-25 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| moment       |           3 |
| rețea        |           2 |
| concepe      |           2 |
| călin        |           2 |
| georgescu    |           2 |
| ști          |           2 |
| prefer       |           2 |
| viziune      |           2 |
| om           |           2 |
| susține      |           1 |
| complicitate |           1 |
| instituție   |           1 |
| românia      |           1 |
| lucru        |           1 |
| răspuns      |           1 |
| putea        |           1 |
| spune        |           1 |
| călăreț      |           1 |
| singuratic   |           1 |
| convinge     |           1 |

### 2025-09-25 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| extrem                          |           4 |
| moment                          |           3 |
| conflict                        |           3 |
| northatlantictreatyorganization |           2 |
| provocăre                       |           2 |
| vrea                            |           2 |
| continua                        |           2 |
| dronă                           |           2 |
| situație                        |           2 |
| militar                         |           2 |
| mic                             |           2 |
| sine                            |           2 |
| vedea                           |           1 |
| rusia                           |           1 |
| capabil                         |           1 |
| atace                           |           1 |
| așteptare                       |           1 |
| încercare                       |           1 |
| destabiliza                     |           1 |
| încredere                       |           1 |

### 2025-09-25 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          45 |
| spune         |          31 |
| sine          |          30 |
| om            |          25 |
| moment        |          24 |
| românia       |          23 |
| lucru         |          21 |
| președinte    |          19 |
| putea         |          19 |
| ăă            |          18 |
| trebui        |          17 |
| rusia         |          16 |
| bun           |          16 |
| vedea         |          16 |
| parte         |          15 |
| exista        |          14 |
| țară          |          13 |
| partid        |          12 |
| dumneavoastră |          11 |
| ști           |          11 |

### 2025-09-25 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          55 |
| spune         |          48 |
| românia       |          39 |
| sine          |          37 |
| putea         |          28 |
| ăă            |          27 |
| președinte    |          25 |
| om            |          25 |
| moment        |          24 |
| lucru         |          24 |
| parte         |          19 |
| vedea         |          19 |
| exista        |          18 |
| țară          |          17 |
| trebui        |          17 |
| ști           |          16 |
| rusia         |          15 |
| partid        |          15 |
| dumneavoastră |          14 |
| lume          |          14 |

### 2025-09-26 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           5 |
| parte      |           4 |
| ăă         |           4 |
| influență  |           3 |
| serviciu   |           3 |
| sri        |           3 |
| trebui     |           3 |
| decizie    |           2 |
| politic    |           2 |
| economic   |           2 |
| român      |           2 |
| stat       |           2 |
| moment     |           2 |
| potrivit   |           2 |
| sine       |           2 |
| discuție   |           2 |
| persoană   |           2 |
| lucru      |           2 |
| președinte |           1 |
| nicușor    |           1 |

### 2025-09-26 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           9 |
| trebui       |           4 |
| sine         |           4 |
| serviciu     |           3 |
| politic      |           3 |
| sri          |           3 |
| lucru        |           3 |
| parte        |           3 |
| vedea        |           2 |
| român        |           2 |
| viață        |           2 |
| economic     |           2 |
| numire       |           2 |
| civil        |           2 |
| interferență |           2 |
| spune        |           2 |
| stat         |           2 |
| discuție     |           2 |
| influență    |           2 |
| persoană     |           2 |

### 2025-09-30 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| context   |           4 |
| românia   |           3 |
| raport    |           3 |
| european  |           3 |
| important |           2 |
| specific  |           2 |
| societate |           2 |
| rus       |           2 |
| țară      |           2 |
| sine      |           2 |
| putea     |           2 |
| general   |           2 |
| întrebare |           1 |
| rând      |           1 |
| dosar     |           1 |
| față      |           1 |
| noiembrie |           1 |
| element   |           1 |
| relativ   |           1 |
| eveniment |           1 |

### 2025-09-30 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| dovadă       |           3 |
| sită         |           3 |
| moment       |           2 |
| față         |           2 |
| bănui        |           2 |
| plăti        |           2 |
| rețea        |           2 |
| uri          |           2 |
| metodă       |           2 |
| promovare    |           2 |
| euro         |           2 |
| ordin        |           2 |
| milion       |           2 |
| intuiție     |           2 |
| lucru        |           1 |
| componentă   |           1 |
| interferență |           1 |
| rus          |           1 |
| social       |           1 |
| dosar        |           1 |

### 2025-09-30 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| moldova      |           5 |
| aderare      |           4 |
| putea        |           3 |
| pas          |           3 |
| transnistria |           3 |
| moment       |           3 |
| ucraina      |           3 |
| republicii   |           2 |
| crede        |           2 |
| statut       |           2 |
| graniță      |           2 |
| uniune       |           2 |
| european     |           2 |
| sine         |           2 |
| vrea         |           2 |
| capitol      |           2 |
| an           |           2 |
| reascultam   |           1 |
| declarație   |           1 |
| maia         |           1 |

### 2025-09-30 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| raport      |           6 |
| vrea        |           4 |
| context     |           4 |
| rusia       |           4 |
| spune       |           3 |
| moment      |           3 |
| față        |           3 |
| românia     |           3 |
| european    |           3 |
| duce        |           3 |
| general     |           3 |
| fapt        |           3 |
| publicitate |           3 |
| public      |           2 |
| lucru       |           2 |
| important   |           2 |
| ăă          |           2 |
| noiembrie   |           2 |
| specific    |           2 |
| societate   |           2 |

### 2025-09-30 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           7 |
| lege       |           6 |
| ăă         |           3 |
| important  |           3 |
| militar    |           3 |
| voluntar   |           3 |
| plăti      |           3 |
| putea      |           2 |
| pregătirii |           2 |
| populație  |           2 |
| parlament  |           2 |
| detaliu    |           2 |
| sine       |           2 |
| transmite  |           2 |
| apărare    |           2 |
| stat       |           2 |
| român      |           2 |
| dori       |           2 |
| lună       |           2 |
| pregăti    |           2 |

### 2025-10-02 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| moment     |           2 |
| rusia      |           2 |
| vedea      |           2 |
| aeroport   |           2 |
| discuta    |           1 |
| schiță     |           1 |
| plan       |           1 |
| acțiune    |           1 |
| chestiune  |           1 |
| vecinătate |           1 |
| eveniment  |           1 |
| întâmpla   |           1 |
| dronă      |           1 |
| parcurge   |           1 |
| belarus    |           1 |
| respectiv  |           1 |
| amenințare |           1 |
| confrunta  |           1 |
| nuanță     |           1 |
| discuție   |           1 |

### 2025-10-02 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           8 |
| zid        |           6 |
| discuție   |           5 |
| dronă      |           5 |
| copenhaga  |           4 |
| flanc      |           4 |
| estic      |           4 |
| antidronă  |           4 |
| stat       |           4 |
| membră     |           4 |
| președinte |           3 |
| reuniune   |           3 |
| sine       |           3 |
| ajunge     |           3 |
| consens    |           3 |
| vedea      |           3 |
| rusia      |           3 |
| spațiu     |           3 |
| aerian     |           3 |
| părere     |           3 |

### 2025-10-14 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |          50 |
| vrea       |          48 |
| spune      |          38 |
| putea      |          38 |
| trebui     |          34 |
| vedea      |          34 |
| partid     |          33 |
| psd        |          30 |
| parte      |          28 |
| crede      |          28 |
| domn       |          27 |
| lucru      |          26 |
| aur        |          25 |
| ști        |          25 |
| an         |          20 |
| social     |          20 |
| instituție |          19 |
| bun        |          18 |
| serviciu   |          17 |
| ministru   |          16 |

### 2025-10-21 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| mandat       |           2 |
| spune        |           2 |
| devreme      |           2 |
| societate    |           2 |
| exclude      |           1 |
| candidatură  |           1 |
| cotroceni    |           1 |
| președinte   |           1 |
| românia      |           1 |
| încă         |           1 |
| decizie      |           1 |
| final        |           1 |
| dor          |           1 |
| continua     |           1 |
| schimbare    |           1 |
| semnificativ |           1 |
| decide       |           1 |
| merge        |           1 |
| apropo       |           1 |
| principiu    |           1 |

### 2025-10-23 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| discuție |          12 |
| sine     |           7 |
| discuta  |           5 |
| ucraina  |           5 |
| putea    |           5 |
| rusia    |           5 |
| moldova  |           5 |
| vedea    |           5 |
| vrea     |           5 |
| uniune   |           4 |
| românia  |           3 |
| moment   |           3 |
| ban      |           3 |
| buget    |           3 |
| european |           3 |
| stat     |           3 |
| membră   |           3 |
| exista   |           3 |
| amiază   |           3 |
| caz      |           3 |

### 2025-10-23 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| trebui        |           3 |
| pregătim      |           3 |
| rusia         |           3 |
| apărare       |           2 |
| pregăti       |           2 |
| șef           |           1 |
| stat          |           1 |
| major         |           1 |
| francez       |           1 |
| spune         |           1 |
| confruntare   |           1 |
| dumneavoastră |           1 |
| strategie     |           1 |
| național      |           1 |
| țară          |           1 |
| scenariu      |           1 |
| război        |           1 |
| hibrid        |           1 |
| an            |           1 |
| estimare      |           1 |

### 2025-10-24 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| mediu        |           6 |
| universitate |           5 |
| crede        |           5 |
| trebui       |           5 |
| instituție   |           4 |
| important    |           4 |
| universitar  |           4 |
| reprezentant |           2 |
| academic     |           2 |
| inclusiv     |           2 |
| onora        |           2 |
| național     |           2 |
| rațiune      |           2 |
| emoție       |           2 |
| societate    |           2 |
| lucru        |           2 |
| spune        |           2 |
| bineînțeles  |           2 |
| rol          |           2 |
| pune         |           2 |

### 2025-10-27 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| român        |           5 |
| stat         |           4 |
| catedrală    |           3 |
| românesc     |           3 |
| dori         |           2 |
| simbol       |           2 |
| unitate      |           2 |
| credință     |           2 |
| neam         |           2 |
| românia      |           2 |
| ortodox      |           2 |
| reconciliere |           2 |
| respect      |           2 |
| față         |           2 |
| moment       |           2 |
| societate    |           2 |
| speranță     |           2 |
| finalizare   |           1 |
| național     |           1 |
| sfințire     |           1 |

### 2025-11-02 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          22 |
| președinte    |          11 |
| românia       |          11 |
| bucurești     |           9 |
| merge         |           9 |
| spune         |           8 |
| domn          |           8 |
| trebui        |           8 |
| lucru         |           8 |
| putea         |           8 |
| stat          |           6 |
| american      |           6 |
| exista        |           6 |
| coaliție      |           6 |
| usr           |           5 |
| vedea         |           5 |
| bun           |           5 |
| moment        |           5 |
| dumneavoastră |           5 |
| declarație    |           4 |

### 2025-11-06 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| northatlantictreatyorganization |          26 |
| apărare                         |          20 |
| industrie                       |          14 |
| românia                         |          13 |
| vrea                            |          12 |
| trebui                          |          11 |
| putea                           |          10 |
| aliat                           |           8 |
| rusia                           |           7 |
| bun                             |           6 |
| amenințările                    |           6 |
| securitate                      |           6 |
| alianță                         |           6 |
| precum                          |           6 |
| puternic                        |           6 |
| important                       |           6 |
| sine                            |           6 |
| forum                           |           5 |
| inovație                        |           5 |
| secretar                        |           5 |

### 2025-11-07 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| întrebare      |           4 |
| premier        |           3 |
| pune           |           3 |
| vrea           |           2 |
| caz            |           2 |
| bolojan        |           2 |
| sine           |           2 |
| bun            |           2 |
| săptămână      |           2 |
| viitor         |           2 |
| ultim          |           2 |
| normal         |           2 |
| interacțiune   |           2 |
| om             |           2 |
| bineînțeles    |           2 |
| limită         |           2 |
| principialitat |           2 |
| depăși         |           2 |
| domn           |           2 |
| dumneavoastră  |           2 |

### 2025-11-07 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| salariu       |           4 |
| minim         |           3 |
| putea         |           3 |
| sine          |           2 |
| permite       |           2 |
| românia       |           2 |
| salariile     |           2 |
| sindicat      |           2 |
| om            |           2 |
| situație      |           1 |
| bugetar       |           1 |
| domn          |           1 |
| președinte    |           1 |
| majora        |           1 |
| an            |           1 |
| ianuarie      |           1 |
| punct         |           1 |
| dumneavoastră |           1 |
| vedere        |           1 |
| spune         |           1 |

### 2025-11-11 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |          27 |
| vedea      |          20 |
| vrea       |          19 |
| gheorghiu  |          15 |
| parte      |          14 |
| justiție   |          12 |
| putea      |          12 |
| politic    |          12 |
| guvern     |          11 |
| declarație |          11 |
| oana       |          11 |
| veni       |          11 |
| csm        |          10 |
| spune      |          10 |
| penal      |          10 |
| pensie     |           9 |
| sistem     |           9 |
| trebui     |           8 |
| față       |           7 |
| special    |           7 |

### 2025-11-11 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| putea     |          12 |
| sine      |          11 |
| acțiune   |          11 |
| condiție  |          10 |
| militar   |           9 |
| zonă      |           9 |
| influența |           9 |
| stare     |           9 |
| categorie |           8 |
| dronă     |           7 |
| moment    |           7 |
| vrea      |           7 |
| general   |           7 |
| apărare   |           6 |
| situație  |           6 |
| domn      |           6 |
| obiectiv  |           6 |
| trebui    |           6 |
| vedea     |           6 |
| aerian    |           5 |

### 2025-11-11 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| problemă      |           6 |
| politic       |           3 |
| deveni        |           3 |
| salariile     |           2 |
| trebui        |           2 |
| campanie      |           2 |
| administrativ |           1 |
| fapt          |           1 |
| printr        |           1 |
| decizie       |           1 |
| an            |           1 |
| întâi         |           1 |
| pensie        |           1 |
| decât         |           1 |
| egal          |           1 |
| absolut       |           1 |
| nefiresc      |           1 |
| exista        |           1 |
| societate     |           1 |
| corectat      |           1 |

### 2025-11-12 — video-transcript

| cuvânt          |   frecvență |
|:----------------|------------:|
| administrație   |           5 |
| public          |           3 |
| ști             |           2 |
| ăă              |           2 |
| vedea           |           2 |
| cauză           |           2 |
| vreau           |           1 |
| insista         |           1 |
| chestiune       |           1 |
| intern          |           1 |
| capitol         |           1 |
| vulnerabilitate |           1 |
| problemă        |           1 |
| rând            |           1 |
| șoc             |           1 |
| caz             |           1 |
| surprinder      |           1 |
| inclusiv        |           1 |
| nivel           |           1 |
| național        |           1 |

### 2025-11-12 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| vrea      |          71 |
| spune     |          50 |
| ăă        |          46 |
| sine      |          42 |
| parte     |          33 |
| stat      |          29 |
| vedea     |          29 |
| lucru     |          28 |
| trebui    |          23 |
| an        |          23 |
| românia   |          22 |
| societate |          21 |
| strategie |          20 |
| om        |          19 |
| serviciu  |          19 |
| corupție  |          18 |
| putea     |          18 |
| exista    |          18 |
| crede     |          18 |
| rând      |          16 |

### 2025-11-12 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          66 |
| sine          |          44 |
| spune         |          37 |
| vedea         |          26 |
| serviciu      |          25 |
| putea         |          25 |
| ăă            |          23 |
| an            |          21 |
| om            |          21 |
| parte         |          20 |
| strategie     |          18 |
| trebui        |          18 |
| moment        |          17 |
| românia       |          17 |
| stat          |          16 |
| administrație |          15 |
| pune          |          15 |
| context       |          14 |
| creștere      |          13 |
| național      |          13 |

### 2025-11-12 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| ăă            |           5 |
| ucraina       |           3 |
| sine          |           3 |
| nivel         |           3 |
| insista       |           2 |
| vecin         |           2 |
| stat          |           2 |
| respecta      |           2 |
| ordine        |           2 |
| internațional |           2 |
| spune         |           2 |
| parte         |           2 |
| document      |           2 |
| implementare  |           2 |
| întâi         |           1 |
| răspuns       |           1 |
| întrebare     |           1 |
| rând          |           1 |
| românia       |           1 |
| încerca       |           1 |

### 2025-11-12 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| rusia         |           5 |
| sine          |           5 |
| românia       |           4 |
| ucraina       |           4 |
| pace          |           4 |
| decât         |           3 |
| ăă            |           3 |
| spune         |           3 |
| dori          |           3 |
| nivel         |           3 |
| august        |           3 |
| lega          |           2 |
| rus           |           2 |
| insista       |           2 |
| vecin         |           2 |
| stat          |           2 |
| respecta      |           2 |
| ordine        |           2 |
| internațional |           2 |
| lucru         |           2 |

### 2025-11-12 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          33 |
| ăă            |          20 |
| vedea         |          16 |
| sine          |          13 |
| administrație |          12 |
| românia       |          11 |
| strategie     |          10 |
| parte         |          10 |
| apărare       |           9 |
| rând          |           8 |
| stat          |           7 |
| public        |           7 |
| context       |           7 |
| trebui        |           7 |
| oportunitate  |           7 |
| important     |           6 |
| adică         |           6 |
| creștere      |           6 |
| militar       |           6 |
| chestiune     |           6 |

### 2025-11-12 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| expres     |           2 |
| implicare  |           2 |
| informație |           2 |
| fenomen    |           2 |
| cunoaște   |           2 |
| greu       |           1 |
| vrea       |           1 |
| identific  |           1 |
| apere      |           1 |
| stat       |           1 |
| corupt     |           1 |
| menționa   |           1 |
| lucru      |           1 |
| colaborare |           1 |
| instituție |           1 |
| atribuție  |           1 |
| rând       |           1 |
| serviciu   |           1 |
| culegere   |           1 |
| privire    |           1 |

### 2025-11-21 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| întâmpla   |           3 |
| lucru      |           2 |
| minister   |           2 |
| instituție |           2 |
| evident    |           2 |
| repede     |           1 |
| felicita   |           1 |
| justiția   |           1 |
| interne    |           1 |
| însemna    |           1 |
| funcționa  |           1 |
| chestiune  |           1 |
| întrebare  |           1 |
| informare  |           1 |
| seară      |           1 |
| anulare    |           1 |
| alegere    |           1 |
| imediat    |           1 |
| următor    |           1 |
| sta        |           1 |

### 2025-11-21 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |          29 |
| vrea          |          29 |
| trebui        |          26 |
| spune         |          19 |
| putea         |          19 |
| întâmpla      |          14 |
| discuție      |          13 |
| an            |          11 |
| moment        |          11 |
| partid        |          11 |
| lucru         |          10 |
| vedea         |          10 |
| evident       |          10 |
| termen        |          10 |
| dumneavoastră |           8 |
| funcționa     |           8 |
| român         |           8 |
| parte         |           7 |
| președinte    |           7 |
| instituție    |           7 |

### 2025-11-21 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| partid    |           7 |
| sine      |           4 |
| trebui    |           4 |
| discuție  |           4 |
| principiu |           3 |
| duce      |           3 |
| ban       |           3 |
| întrebare |           2 |
| ăă        |           2 |
| răspuns   |           2 |
| prim      |           2 |
| subvenție |           2 |
| lucru     |           2 |
| moment    |           2 |
| sacoșe    |           2 |
| vrea      |           1 |
| plăti     |           1 |
| emisiune  |           1 |
| oră       |           1 |
| mulțumi   |           1 |

### 2025-11-26 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| important                       |          11 |
| zonă                            |          10 |
| românia                         |          10 |
| vrea                            |           9 |
| dezvoltare                      |           8 |
| oportunitate                    |           8 |
| corupție                        |           7 |
| vorbi                           |           6 |
| exista                          |           6 |
| strategie                       |           6 |
| uniune                          |           5 |
| european                        |           5 |
| trebui                          |           5 |
| privi                           |           4 |
| plan                            |           4 |
| parte                           |           4 |
| northatlantictreatyorganization |           4 |
| program                         |           4 |
| industrie                       |           4 |
| apărare                         |           4 |

### 2025-11-26 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vedea      |           7 |
| discuție   |           5 |
| coaliție   |           5 |
| moment     |           5 |
| lua        |           4 |
| atât       |           4 |
| sine       |           4 |
| vrea       |           4 |
| vorbă      |           3 |
| transfer   |           3 |
| om         |           3 |
| față       |           3 |
| exista     |           3 |
| an         |           3 |
| femeie     |           3 |
| autoritate |           3 |
| începe     |           2 |
| oară       |           2 |
| adopta     |           2 |
| măsură     |           2 |

### 2025-11-26 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| întâmpla     |           4 |
| dronă        |           3 |
| putea        |           2 |
| spune        |           2 |
| vorbă        |           2 |
| lucru        |           2 |
| chestiune    |           2 |
| explicație   |           2 |
| ministru     |           2 |
| discuție     |           2 |
| intra        |           1 |
| teritoriu    |           1 |
| accident     |           1 |
| precizie     |           1 |
| acțiune      |           1 |
| ostil        |           1 |
| rusia        |           1 |
| campanie     |           1 |
| dezinformare |           1 |
| manipulare   |           1 |

### 2025-11-26 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| susține     |           3 |
| continuare  |           2 |
| stabilitate |           2 |
| dezvoltare  |           1 |
| republicii  |           1 |
| moldova     |           1 |
| obiectiv    |           1 |
| important   |           1 |
| politică    |           1 |
| extern      |           1 |
| sprijini    |           1 |
| ucraina     |           1 |
| securitate  |           1 |
| zonă        |           1 |
| balcanilor  |           1 |
| vest        |           1 |
| vrea        |           1 |
| integrare   |           1 |
| uniune      |           1 |
| european    |           1 |

### 2025-12-01 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| moment     |          15 |
| militar    |          13 |
| național   |          11 |
| românia    |           9 |
| sine       |           9 |
| forță      |           9 |
| apărare    |           8 |
| înzestrare |           8 |
| program    |           8 |
| detașament |           8 |
| președinte |           7 |
| domn       |           7 |
| armată     |           7 |
| vrea       |           7 |
| defilare   |           7 |
| stat       |           6 |
| român      |           6 |
| operație   |           6 |
| vedea      |           6 |
| război     |           6 |

### 2025-12-01 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| spune      |           3 |
| domn       |           3 |
| important  |           2 |
| țară       |           2 |
| șef        |           2 |
| relație    |           2 |
| stat       |           2 |
| ministru   |           2 |
| sărbătoare |           2 |
| președinte |           2 |
| an         |           2 |
| american   |           1 |
| trimite    |           1 |
| semnal     |           1 |
| bun        |           1 |
| oară       |           1 |
| unit       |           1 |
| trainic    |           1 |
| consolida  |           1 |
| paliere    |           1 |

### 2025-12-01 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |           4 |
| uniune      |           2 |
| caz         |           2 |
| muzică      |           1 |
| membru      |           1 |
| european    |           1 |
| poziție     |           1 |
| primi       |           1 |
| aproximativ |           1 |
| miliard     |           1 |
| euro        |           1 |
| oară        |           1 |
| voce        |           1 |
| auzi        |           1 |
| interior    |           1 |
| schengen    |           1 |
| clar        |           1 |
| nedreptățit |           1 |
| maturitate  |           1 |
| exersa      |           1 |

### 2025-12-02 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| trăim     |           5 |
| decât     |           4 |
| moment    |           3 |
| an        |           3 |
| corupt    |           3 |
| românia   |           2 |
| om        |           2 |
| țară      |           2 |
| român     |           2 |
| dreptate  |           2 |
| corupție  |           2 |
| față      |           2 |
| celebrăm  |           1 |
| unire     |           1 |
| istoric   |           1 |
| vis       |           1 |
| generație |           1 |
| împlini   |           1 |
| cred      |           1 |
| trebui    |           1 |

### 2025-12-02 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |         104 |
| an         |          68 |
| țară       |          55 |
| muzică     |          52 |
| sine       |          51 |
| român      |          46 |
| putea      |          41 |
| președinte |          40 |
| spune      |          39 |
| vrea       |          32 |
| corupție   |          31 |
| moment     |          29 |
| stat       |          27 |
| decât      |          26 |
| corupt     |          22 |
| exista     |          20 |
| vedea      |          19 |
| parte      |          18 |
| trebui     |          18 |
| om         |          17 |

### 2025-12-03 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| domn       |          15 |
| sine       |          14 |
| vrea       |          12 |
| spune      |          12 |
| moment     |          10 |
| fapt       |           9 |
| ministru   |           8 |
| situație   |           7 |
| trebui     |           7 |
| președinte |           7 |
| politic    |           7 |
| public     |           7 |
| față       |           6 |
| declarație |           6 |
| instituție |           6 |
| exista     |           6 |
| apă        |           5 |
| om         |           5 |
| vedea      |           5 |
| poziție    |           5 |

### 2025-12-03 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| opinie      |           3 |
| energie     |           2 |
| uita        |           1 |
| ultim       |           1 |
| săptămână   |           1 |
| campanie    |           1 |
| electoral   |           1 |
| citim       |           1 |
| declarație  |           1 |
| cheie       |           1 |
| rând        |           1 |
| evident     |           1 |
| urmă        |           1 |
| situație    |           1 |
| trebui      |           1 |
| stabilim    |           1 |
| vinovații   |           1 |
| bineînțeles |           1 |
| autoritate  |           1 |
| control     |           1 |

### 2025-12-03 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| declara    |           5 |
| declarație |           3 |
| public     |           3 |
| putin      |           2 |
| domn       |           2 |
| intern     |           2 |
| muzică     |           1 |
| nicușordan |           1 |
| reacționa  |           1 |
| vladimir   |           1 |
| doamnelor  |           1 |
| pregăti    |           1 |
| război     |           1 |
| europa     |           1 |
| președinte |           1 |
| spune      |           1 |
| citez      |           1 |
| rusia      |           1 |
| iată       |           1 |
| românia    |           1 |

### 2025-12-03 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| apă        |           6 |
| vrea       |           6 |
| sine       |           6 |
| situație   |           5 |
| domn       |           4 |
| spune      |           4 |
| instituție |           4 |
| urmă       |           3 |
| trebui     |           3 |
| opinie     |           3 |
| român      |           3 |
| susține    |           3 |
| calitate   |           3 |
| ajunge     |           3 |
| om         |           3 |
| stat       |           3 |
| președinte |           2 |
| declarație |           2 |
| autoritate |           2 |
| control    |           2 |

### 2025-12-04 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| ști            |           4 |
| reuși          |           4 |
| călin          |           3 |
| georgescu      |           3 |
| detecta        |           3 |
| adică          |           2 |
| evident        |           2 |
| serviciu       |           2 |
| afinitățe      |           2 |
| infrastructură |           2 |
| comunicare     |           2 |
| însă           |           2 |
| exista         |           2 |
| muzică         |           1 |
| președinte     |           1 |
| domn           |           1 |
| nicușor        |           1 |
| dan            |           1 |
| declara        |           1 |
| secret         |           1 |

### 2025-12-04 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| an           |           4 |
| raport       |           3 |
| alegere      |           3 |
| prezenta     |           3 |
| moment       |           3 |
| schimba      |           3 |
| explica      |           2 |
| trecut       |           2 |
| putea        |           2 |
| ianuarie     |           2 |
| spune        |           2 |
| campanie     |           2 |
| dezinformare |           2 |
| vrea         |           2 |
| ăă           |           2 |
| lucru        |           2 |
| crede        |           2 |
| decizie      |           2 |
| anulare      |           1 |
| final        |           1 |

### 2025-12-04 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| ministru     |           7 |
| sine         |           6 |
| fapt         |           5 |
| apărare      |           4 |
| decizie      |           4 |
| usr          |           3 |
| spune        |           3 |
| moșteanu     |           3 |
| protocol     |           2 |
| coaliție     |           2 |
| intensitate  |           2 |
| blama        |           2 |
| diferit      |           2 |
| spațiu       |           2 |
| public       |           2 |
| niciodată    |           2 |
| proporțional |           2 |
| vrea         |           2 |
| lua          |           2 |
| numire       |           2 |

### 2025-12-04 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| sine     |          82 |
| apă      |          70 |
| vrea     |          49 |
| domn     |          45 |
| vedea    |          41 |
| spune    |          38 |
| ministru |          24 |
| ști      |          24 |
| trebui   |          24 |
| exista   |          23 |
| situație |          22 |
| moment   |          22 |
| putea    |          21 |
| om       |          21 |
| problemă |          21 |
| român    |          18 |
| psd      |          18 |
| veni     |          17 |
| centrală |          16 |
| energie  |          16 |

### 2025-12-07 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| vota     |           2 |
| alegere  |           2 |
| an       |           2 |
| adică    |           2 |
| afară    |           1 |
| personal |           1 |
| românie  |           1 |
| occident |           1 |
| valoare  |           1 |
| crede    |           1 |
| defini   |           1 |
| oraș     |           1 |
| cunosc   |           1 |
| milita   |           1 |
| jumătate |           1 |
| simbolic |           1 |
| direcție |           1 |
| politic  |           1 |
| național |           1 |
| atât     |           1 |

### 2025-12-08 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| inclusiv     |           5 |
| alegere      |           4 |
| vrea         |           4 |
| nicușor      |           3 |
| dan          |           3 |
| mesaj        |           3 |
| ciprian      |           3 |
| special      |           3 |
| rând         |           3 |
| ciprianciucu |           3 |
| președinte   |           3 |
| campanie     |           3 |
| sine         |           3 |
| felicitare   |           2 |
| ciucu        |           2 |
| aleși        |           2 |
| primărie     |           2 |
| evident      |           2 |
| general      |           2 |
| gest         |           2 |

### 2025-12-09 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| politic       |           3 |
| ăă            |           2 |
| declarație    |           2 |
| trebui        |           2 |
| răzbat        |           2 |
| acțiune       |           2 |
| crede         |           1 |
| bineînțeles   |           1 |
| printre       |           1 |
| așteptăre     |           1 |
| om            |           1 |
| față          |           1 |
| politician    |           1 |
| funcție       |           1 |
| conducere     |           1 |
| tip           |           1 |
| fine          |           1 |
| anumit        |           1 |
| situație      |           1 |
| administrativ |           1 |

### 2025-12-10 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| spune      |           6 |
| vrea       |           4 |
| aur        |           3 |
| sine       |           3 |
| ăă         |           3 |
| extremist  |           2 |
| nemulțumi  |           2 |
| politic    |           2 |
| partid     |           2 |
| lucru      |           2 |
| alegător   |           2 |
| putea      |           2 |
| adică      |           2 |
| românia    |           2 |
| moment     |           2 |
| îndrepta   |           2 |
| nicușordan |           1 |
| considera  |           1 |
| majoritate |           1 |
| votanț     |           1 |

### 2025-12-10 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| vrea      |         112 |
| sine      |          95 |
| european  |          86 |
| europa    |          83 |
| spune     |          68 |
| stat      |          60 |
| uniune    |          58 |
| putea     |          57 |
| românia   |          51 |
| unit      |          50 |
| adică     |          42 |
| vedea     |          38 |
| exista    |          38 |
| trump     |          37 |
| ști       |          34 |
| război    |          33 |
| parte     |          32 |
| important |          29 |
| trebui    |          28 |
| ăă        |          28 |

### 2025-12-11 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| justiție   |           6 |
| sistem     |           5 |
| spune      |           4 |
| interior   |           3 |
| trebui     |           3 |
| fapt       |           3 |
| material   |           2 |
| problemă   |           2 |
| investiga  |           2 |
| probă      |           2 |
| raport     |           2 |
| vorbi      |           2 |
| vorbim     |           2 |
| magistrat  |           2 |
| președinte |           1 |
| nicușor    |           1 |
| dan        |           1 |
| anunța     |           1 |
| vedea      |           1 |
| presă      |           1 |

### 2025-12-12 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| spune         |          33 |
| sine          |          32 |
| trebui        |          29 |
| putea         |          26 |
| justiție      |          20 |
| domn          |          20 |
| lucru         |          16 |
| documentar    |          16 |
| vrea          |          16 |
| judecător     |          16 |
| vedea         |          16 |
| ști           |          15 |
| crede         |          12 |
| magistrat     |          12 |
| problemă      |          11 |
| bun           |          11 |
| moment        |          11 |
| sistem        |          11 |
| dumneavoastră |          10 |
| răspunde      |          10 |

### 2025-12-15 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vedea         |           4 |
| societate     |           3 |
| ăă            |           3 |
| românia       |           3 |
| același       |           3 |
| privi         |           3 |
| diasporă      |           2 |
| om            |           2 |
| decât         |           2 |
| țară          |           2 |
| român         |           2 |
| asociație     |           2 |
| reprezentant  |           2 |
| reuși         |           2 |
| dumneavoastră |           2 |
| folosi        |           2 |
| discuție      |           2 |
| deschide      |           2 |
| putea         |           2 |
| dorință       |           2 |

### 2025-12-15 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| domn       |          13 |
| nicolae    |          12 |
| duce       |          11 |
| crede      |          11 |
| sine       |          10 |
| ști        |           9 |
| bă         |           9 |
| nicușor    |           8 |
| om         |           8 |
| vrea       |           6 |
| guță       |           6 |
| președinte |           5 |
| emisiune   |           5 |
| putea      |           5 |
| păi        |           5 |
| părea      |           5 |
| bun        |           5 |
| situație   |           5 |
| trebui     |           5 |
| veni       |           5 |

### 2025-12-15 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           5 |
| perioadă   |           5 |
| președinte |           3 |
| problemă   |           3 |
| spune      |           3 |
| țară       |           3 |
| grup       |           3 |
| lucru      |           3 |
| trimite    |           3 |
| mesaj      |           2 |
| helsinki   |           2 |
| sistem     |           2 |
| interior   |           2 |
| același    |           2 |
| guvern     |           2 |
| analiza    |           2 |
| vasile     |           2 |
| mail       |           2 |
| primi      |           2 |
| parte      |           2 |

### 2025-12-16 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| vrea     |           6 |
| buget    |           4 |
| grav     |           4 |
| an       |           4 |
| primărie |           3 |
| datorie  |           3 |
| lucru    |           3 |
| stb      |           3 |
| primar   |           2 |
| capitală |           2 |
| găsi     |           2 |
| mic      |           2 |
| șoc      |           2 |
| sine     |           2 |
| atât     |           2 |
| vedea    |           2 |
| trebui   |           2 |
| ști      |           2 |
| acumula  |           2 |
| începe   |           2 |

### 2025-12-16 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| vrea                            |          13 |
| sine                            |           9 |
| parte                           |           8 |
| românia                         |           7 |
| coaliție                        |           7 |
| spune                           |           6 |
| european                        |           6 |
| moment                          |           6 |
| sistem                          |           6 |
| interior                        |           5 |
| discuție                        |           5 |
| trebui                          |           5 |
| președinte                      |           4 |
| rusia                           |           4 |
| program                         |           4 |
| northatlantictreatyorganization |           4 |
| nivel                           |           4 |
| apărare                         |           4 |
| război                          |           4 |
| ucraina                         |           4 |

### 2025-12-16 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| ucraina    |           8 |
| vrea       |           5 |
| negociere  |           5 |
| rusia      |           4 |
| pace       |           4 |
| important  |           4 |
| the        |           4 |
| președinte |           3 |
| stat       |           3 |
| an         |           3 |
| were       |           3 |
| merge      |           2 |
| ucrainean  |           2 |
| zelenschi  |           2 |
| vedea      |           2 |
| susține    |           2 |
| înalt      |           2 |
| comisie    |           2 |
| agresiune  |           2 |
| cerere     |           2 |

### 2025-12-16 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| țară                            |           3 |
| northatlantictreatyorganization |           2 |
| rusia                           |           2 |
| apărare                         |           2 |
| sine                            |           2 |
| amenințare                      |           2 |
| secretar                        |           1 |
| general                         |           1 |
| marc                            |           1 |
| rute                            |           1 |
| afirma                          |           1 |
| recent                          |           1 |
| discurs                         |           1 |
| putea                           |           1 |
| folosi                          |           1 |
| forță                           |           1 |
| militar                         |           1 |
| alianță                         |           1 |
| următor                         |           1 |
| an                              |           1 |

### 2025-12-17 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| vrea      |          30 |
| sine      |          11 |
| reformă   |           8 |
| coaliție  |           7 |
| spune     |           7 |
| impozit   |           7 |
| om        |           7 |
| buget     |           7 |
| trebui    |           6 |
| întrebare |           6 |
| public    |           6 |
| discuție  |           5 |
| putea     |           5 |
| ăă        |           5 |
| românia   |           5 |
| exista    |           5 |
| întreba   |           5 |
| justiție  |           5 |
| lega      |           4 |
| vedea     |           4 |

### 2025-12-17 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| niciun      |           3 |
| impozit     |           3 |
| catastrofă  |           2 |
| fericire    |           2 |
| lume        |           2 |
| proprietate |           2 |
| mări        |           2 |
| președinte  |           1 |
| nicușor     |           1 |
| dan         |           1 |
| reacție     |           1 |
| taxă        |           1 |
| crește      |           1 |
| spune       |           1 |
| haideți     |           1 |
| vedea       |           1 |
| evident     |           1 |
| ideal       |           1 |
| plăti       |           1 |
| venit       |           1 |

### 2025-12-17 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          18 |
| spune      |          13 |
| problemă   |          12 |
| chestiune  |           9 |
| trebui     |           9 |
| sine       |           8 |
| justiție   |           8 |
| discuție   |           8 |
| coaliție   |           8 |
| lucru      |           7 |
| opinie     |           6 |
| președinte |           5 |
| parte      |           5 |
| material   |           4 |
| măsură     |           4 |
| lega       |           4 |
| rezolva    |           4 |
| vedea      |           3 |
| bun        |           3 |
| sistem     |           3 |

### 2025-12-18 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| raport       |           4 |
| important    |           3 |
| alegere      |           3 |
| om           |           3 |
| românia      |           3 |
| întâmpla     |           3 |
| ieșim        |           3 |
| rus          |           2 |
| stat         |           2 |
| vrea         |           2 |
| trebui       |           2 |
| lună         |           2 |
| sine         |           2 |
| campanie     |           2 |
| urma         |           1 |
| întrebare    |           1 |
| roșu         |           1 |
| dovedi       |           1 |
| interferență |           1 |
| ăă           |           1 |

### 2025-12-18 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| rege        |           3 |
| charles     |           3 |
| președinte  |           2 |
| nicușordan  |           2 |
| palat       |           2 |
| buckingham  |           2 |
| scurt       |           2 |
| mesaj       |           2 |
| transmite   |           2 |
| primi       |           1 |
| atenție     |           1 |
| londra      |           1 |
| vizit       |           1 |
| lucru       |           1 |
| întrevedere |           1 |
| românia     |           1 |
| posta       |           1 |
| rețea       |           1 |
| social      |           1 |
| fotografie  |           1 |

### 2025-12-18 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| problemă    |           2 |
| fundamental |           2 |
| an          |           2 |
| crede       |           1 |
| reuși       |           1 |
| rezolvăm    |           1 |
| faptă       |           1 |
| corupție    |           1 |
| adică       |           1 |
| trebui      |           1 |
| tre         |           1 |
| persoană    |           1 |
| viza        |           1 |
| dosar       |           1 |
| sine        |           1 |
| termina     |           1 |
| cercetare   |           1 |
| judecarea   |           1 |
| soluție     |           1 |

### 2025-12-18 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |          10 |
| partid     |           9 |
| vrea       |           6 |
| an         |           6 |
| politic    |           6 |
| putea      |           5 |
| domn       |           5 |
| interior   |           5 |
| liberal    |           5 |
| trebui     |           4 |
| subiect    |           4 |
| președinte |           4 |
| moment     |           4 |
| următor    |           4 |
| decizie    |           4 |
| bolojan    |           4 |
| majoritate |           4 |
| analiză    |           4 |
| fapt       |           3 |
| corupție   |           3 |

### 2025-12-18 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| ucraina     |           5 |
| discuție    |           5 |
| spune       |           5 |
| vrea        |           5 |
| public      |           5 |
| an          |           4 |
| domn        |           4 |
| problemă    |           4 |
| bineînțeles |           3 |
| consiliu    |           3 |
| ungaria     |           3 |
| sine        |           3 |
| discuta     |           3 |
| parte       |           3 |
| vest        |           3 |
| moment      |           3 |
| trebui      |           3 |
| ăă          |           3 |
| spațiu      |           3 |
| fundamental |           3 |

### 2025-12-19 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| justiție    |           3 |
| președinte  |           3 |
| niciun      |           2 |
| înaltei     |           2 |
| curți       |           2 |
| casație     |           2 |
| urmă        |           2 |
| șef         |           2 |
| numire      |           2 |
| nicușordan  |           1 |
| anunța      |           1 |
| contribuție |           1 |
| desemnare   |           1 |
| conducerii  |           1 |
| afirmație   |           1 |
| veni        |           1 |
| întâlnire   |           1 |
| lună        |           1 |
| palat       |           1 |
| cotroceni   |           1 |

### 2025-12-21 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |          15 |
| sine        |          15 |
| ăă          |          13 |
| chestiune   |          12 |
| public      |          10 |
| magistrat   |           9 |
| trebui      |           8 |
| justiție    |           8 |
| față        |           8 |
| sistem      |           8 |
| spune       |           8 |
| fapt        |           7 |
| interes     |           7 |
| rând        |           6 |
| discuție    |           6 |
| exista      |           6 |
| scrie       |           5 |
| inclusiv    |           5 |
| instanțelor |           5 |
| semnala     |           5 |

### 2025-12-21 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| sine           |          14 |
| putere         |          12 |
| președinte     |           9 |
| putea          |           9 |
| sistem         |           8 |
| fapt           |           7 |
| judecătoresc   |           7 |
| stat           |           7 |
| vrea           |           6 |
| curte          |           6 |
| problemă       |           6 |
| domn           |           5 |
| nicușor        |           5 |
| dan            |           5 |
| parte          |           5 |
| spune          |           5 |
| interior       |           5 |
| referendum     |           5 |
| constituțional |           5 |
| justiție       |           5 |

### 2025-12-21 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| grup        |           3 |
| magistrat   |           2 |
| acționa     |           2 |
| interes     |           2 |
| inclusiv    |           2 |
| înalt       |           2 |
| curte       |           2 |
| justiție    |           2 |
| criteriu    |           2 |
| concluzie   |           1 |
| sesizare    |           1 |
| majoritate  |           1 |
| exista      |           1 |
| categorie   |           1 |
| membru      |           1 |
| csm         |           1 |
| conducere   |           1 |
| instanțelor |           1 |
| public      |           1 |
| constitui   |           1 |

### 2025-12-21 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          39 |
| sine       |          35 |
| spune      |          30 |
| public     |          24 |
| magistrat  |          23 |
| vedea      |          18 |
| interes    |          17 |
| președinte |          15 |
| sistem     |          15 |
| discuție   |          14 |
| ști        |          14 |
| putea      |          13 |
| parte      |          11 |
| urmă       |          10 |
| veni       |          10 |
| moment     |          10 |
| justiție   |           9 |
| lucru      |           9 |
| grup       |           9 |
| csm        |           9 |

### 2025-12-21 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| exista       |           2 |
| lume         |           2 |
| vedea        |           2 |
| sine         |           2 |
| mesaj        |           1 |
| influențare  |           1 |
| intimidar    |           1 |
| scrie        |           1 |
| solicita     |           1 |
| întâlni      |           1 |
| decembrie    |           1 |
| teamă        |           1 |
| fineare      |           1 |
| întâlnire    |           1 |
| repercusiune |           1 |
| ajunge       |           1 |
| inclusiv     |           1 |
| fine         |           1 |
| ăă           |           1 |
| propunere    |           1 |

### 2025-12-21 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| interes       |           5 |
| consiliu      |           4 |
| superior      |           4 |
| magistraturii |           4 |
| vrea          |           4 |
| acționa       |           3 |
| public        |           3 |
| spune         |           3 |
| situație      |           2 |
| grav          |           2 |
| sistem        |           2 |
| judiciar      |           2 |
| fapt          |           1 |
| exista        |           1 |
| suspiciune    |           1 |
| privire       |           1 |
| integritate   |           1 |
| față          |           1 |
| apreciez      |           1 |
| iniție        |           1 |

### 2025-12-21 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| spune         |           5 |
| interes       |           5 |
| consiliu      |           4 |
| superior      |           4 |
| magistraturii |           4 |
| vrea          |           4 |
| acționa       |           3 |
| public        |           3 |
| fapt          |           2 |
| situație      |           2 |
| grav          |           2 |
| sistem        |           2 |
| judiciar      |           2 |
| lucru         |           1 |
| sine          |           1 |
| regăsi        |           1 |
| material      |           1 |
| raport        |           1 |
| acuzație      |           1 |
| sesizare      |           1 |

### 2025-12-22 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| sine      |         265 |
| putea     |         175 |
| judecător |         110 |
| trebui    |         103 |
| procuror  |         102 |
| vrea      |         101 |
| spune     |          99 |
| ăă        |          88 |
| sistem    |          83 |
| justiție  |          75 |
| exista    |          75 |
| judiciar  |          75 |
| coleg     |          71 |
| moment    |          67 |
| dosar     |          66 |
| bun       |          64 |
| secție    |          63 |
| public    |          62 |
| an        |          61 |
| lucru     |          58 |

### 2025-12-22 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| interes       |           7 |
| acționa       |           5 |
| public        |           4 |
| consiliu      |           4 |
| superior      |           4 |
| magistraturii |           4 |
| vrea          |           4 |
| spune         |           3 |
| sesizare      |           2 |
| majoritate    |           2 |
| magistrat     |           2 |
| grup          |           2 |
| concluzie     |           1 |
| exista        |           1 |
| categorie     |           1 |
| membru        |           1 |
| csm           |           1 |
| conducere     |           1 |
| instanțelor   |           1 |
| constitui     |           1 |

### 2025-12-22 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| președinte   |           3 |
| nicușor      |           2 |
| dan          |           2 |
| față         |           2 |
| verificare   |           2 |
| reprezentant |           1 |
| magistrațe   |           1 |
| merge        |           1 |
| discuta      |           1 |
| oră          |           1 |
| jumătate     |           1 |
| anunța       |           1 |
| lucru        |           1 |
| sesiza       |           1 |
| necesita     |           1 |
| însă         |           1 |
| vrea         |           1 |
| lua          |           1 |
| reveni       |           1 |
| informație   |           1 |

### 2025-12-22 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| președinte  |           4 |
| românia     |           3 |
| încălca     |           2 |
| constituție |           2 |
| procedură   |           2 |
| suspendare  |           2 |
| deputat     |           2 |
| semnătură   |           2 |
| forma       |           2 |
| sos         |           2 |
| membru      |           2 |
| senator     |           1 |
| ninel       |           1 |
| pea         |           1 |
| trimite     |           1 |
| scrisoare   |           1 |
| adresat     |           1 |
| conducere   |           1 |
| parlament   |           1 |
| arăta       |           1 |

### 2026-01-01 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| președinte   |           7 |
| vrea         |           6 |
| trebui       |           4 |
| anulare      |           4 |
| alegere      |           4 |
| nicușordan   |           3 |
| prezidențial |           3 |
| prezenta     |           3 |
| românia      |           3 |
| lună         |           3 |
| muzică       |           2 |
| numire       |           2 |
| șef          |           2 |
| serviciu     |           2 |
| secret       |           2 |
| dosar        |           2 |
| veni         |           2 |
| detaliu      |           2 |
| promite      |           2 |
| spune        |           2 |

### 2026-01-01 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| transmite   |           2 |
| condoleanță |           2 |
| victimă     |           2 |
| răni        |           2 |
| nicușor     |           1 |
| dan         |           1 |
| mesaj       |           1 |
| incendi     |           1 |
| elveția     |           1 |
| început     |           1 |
| an          |           1 |
| profund     |           1 |
| întrista    |           1 |
| afla        |           1 |
| explozie    |           1 |
| incendiu    |           1 |
| loc         |           1 |
| cran        |           1 |
| montana     |           1 |
| urmă        |           1 |

### 2026-01-06 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          37 |
| parte      |          23 |
| românia    |          19 |
| ăă         |          17 |
| ucraina    |          13 |
| spune      |          13 |
| coaliție   |          12 |
| an         |          11 |
| președinte |          11 |
| stat       |          11 |
| țară       |          11 |
| lucru      |          11 |
| militar    |           9 |
| exista     |           8 |
| rând       |           8 |
| putea      |           8 |
| vedea      |           8 |
| declarație |           7 |
| mecanism   |           7 |
| seara      |           6 |

### 2026-01-06 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| doa           |           2 |
| schimbare     |           2 |
| gradual       |           2 |
| românia       |           2 |
| context       |           2 |
| încet         |           2 |
| dorință       |           1 |
| pune          |           1 |
| revenion      |           1 |
| ăă            |           1 |
| subliniez     |           1 |
| însemna       |           1 |
| internațional |           1 |
| dificil       |           1 |
| moment        |           1 |
| revoluție     |           1 |
| dezabilizr    |           1 |
| fa            |           1 |

### 2026-01-06 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| gradual       |           3 |
| coaliție      |           3 |
| schimbare     |           2 |
| stat          |           2 |
| context       |           2 |
| internațional |           2 |
| dificil       |           2 |
| moment        |           2 |
| românia       |           2 |
| stabilizare   |           2 |
| încet         |           2 |
| țară          |           1 |
| cuvânt        |           1 |
| rosti         |           1 |
| președinte    |           1 |
| nicușordan    |           1 |
| reuniuni      |           1 |
| voință        |           1 |
| paris         |           1 |
| șef           |           1 |

### 2026-01-07 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          44 |
| sine       |          22 |
| românia    |          22 |
| parte      |          21 |
| ăă         |          19 |
| an         |          18 |
| spune      |          17 |
| taxă       |          17 |
| ucraina    |          14 |
| putea      |          13 |
| coaliție   |          12 |
| trebui     |          12 |
| președinte |          11 |
| vedea      |          11 |
| lucru      |          11 |
| declarație |          10 |
| rând       |          10 |
| seara      |           9 |
| domn       |           9 |
| exista     |           9 |

### 2026-01-07 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| zăpadă   |           5 |
| avion    |           4 |
| sine     |           3 |
| bloca    |           3 |
| moment   |           3 |
| bucura   |           3 |
| noapte   |           2 |
| franța   |           2 |
| trebui   |           2 |
| ceai     |           2 |
| cald     |           2 |
| decât    |           2 |
| înăuntru |           2 |
| tren     |           2 |
| copilări |           2 |
| bun      |           1 |
| aseară   |           1 |
| decide   |           1 |
| pleca    |           1 |
| ajunge   |           1 |

### 2026-01-07 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| taxă      |           6 |
| guvern    |           3 |
| niciun    |           3 |
| vrea      |           3 |
| plăcea    |           2 |
| scedea    |           2 |
| decizie   |           2 |
| sine      |           2 |
| crește    |           2 |
| chestiune |           2 |
| ține      |           2 |
| parte     |           2 |
| vedea     |           2 |
| bucurești |           2 |
| nicuordan |           1 |
| spune     |           1 |
| sublinia  |           1 |
| privind   |           1 |
| afla      |           1 |
| sarcină   |           1 |

### 2026-01-12 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| președinte   |           6 |
| sine         |           6 |
| justiție     |           5 |
| putere       |           5 |
| spune        |           4 |
| sistem       |           4 |
| matematic    |           4 |
| control      |           3 |
| judecătoresc |           3 |
| judecător    |           3 |
| merge        |           3 |
| conduce      |           3 |
| șefa         |           2 |
| cere         |           2 |
| dan          |           2 |
| scenariu     |           2 |
| preluare     |           2 |
| cinic        |           2 |
| plan         |           2 |
| grup         |           2 |

### 2026-01-15 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| măsură       |           3 |
| lua          |           2 |
| dureros      |           2 |
| deficit      |           2 |
| an           |           2 |
| austeritate  |           1 |
| absolut      |           1 |
| necesar      |           1 |
| declarație   |           1 |
| aparține     |           1 |
| președinte   |           1 |
| nicușor      |           1 |
| dan          |           1 |
| anunța       |           1 |
| metodă       |           1 |
| scădea       |           1 |
| bugetar      |           1 |
| imperativele |           1 |
| special      |           1 |
| ultim        |           1 |

### 2026-01-15 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| față          |           2 |
| democrație    |           1 |
| românesc      |           1 |
| reuși         |           1 |
| test          |           1 |
| maturitate    |           1 |
| aplica        |           1 |
| lege          |           1 |
| asigura       |           1 |
| funcționare   |           1 |
| instituție    |           1 |
| democratic    |           1 |
| început       |           1 |
| proces        |           1 |
| profund       |           1 |
| reconciliere  |           1 |
| național      |           1 |
| cadru         |           1 |
| societate     |           1 |
| reconsolidare |           1 |

### 2026-01-15 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          39 |
| românia    |          25 |
| stat       |          20 |
| sine       |          16 |
| european   |          16 |
| an         |          12 |
| securitate |          12 |
| politică   |          10 |
| extern     |          10 |
| putea      |          10 |
| partener   |          10 |
| global     |           9 |
| continua   |           9 |
| uniune     |           9 |
| țară       |           8 |
| economic   |           8 |
| reprezenta |           8 |
| cooperare  |           7 |
| național   |           7 |
| efort      |           7 |

### 2026-01-20 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| președinte |          10 |
| consiliu   |          10 |
| parte      |           8 |
| european   |           7 |
| veni       |           7 |
| sine       |           6 |
| răspuns    |           6 |
| dan        |           5 |
| joi        |           5 |
| românia    |           5 |
| oră        |           4 |
| nicușor    |           4 |
| trump      |           4 |
| pace       |           4 |
| șef        |           4 |
| stat       |           4 |
| țară       |           4 |
| aștepta    |           3 |
| invita     |           3 |
| unit       |           3 |

### 2026-01-22 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| românia       |           9 |
| important     |           7 |
| moment        |           5 |
| dialog        |           4 |
| vorbă         |           4 |
| poziție       |           3 |
| parte         |           3 |
| chestiune     |           3 |
| trebui        |           3 |
| declarație    |           3 |
| consiliu      |           2 |
| european      |           2 |
| relație       |           2 |
| transatlantic |           2 |
| discuta       |           2 |
| europa        |           2 |
| ține          |           2 |
| internațional |           2 |
| pregăti       |           2 |
| lua           |           2 |

### 2026-01-23 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| european    |           3 |
| dincolo     |           2 |
| opinie      |           2 |
| român       |           2 |
| spune       |           2 |
| însemna     |           2 |
| lună        |           2 |
| întâlni     |           2 |
| lider       |           2 |
| cuvânt      |           1 |
| public      |           1 |
| redescoperi |           1 |
| ăă          |           1 |
| permite     |           1 |
| începe      |           1 |
| remarcă     |           1 |
| filozofic   |           1 |
| crede       |           1 |
| vota        |           1 |
| schimbare   |           1 |

### 2026-01-24 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| societate     |           7 |
| reuși         |           7 |
| proiect       |           5 |
| dumneavoastră |           5 |
| românia       |           5 |
| an            |           5 |
| pune          |           4 |
| vrea          |           4 |
| împreună      |           4 |
| loc           |           3 |
| român         |           3 |
| excepțional   |           3 |
| vedea         |           3 |
| unire         |           3 |
| competiție    |           3 |
| rând          |           2 |
| respect       |           2 |
| întrebare     |           2 |
| dincolo       |           2 |
| copil         |           2 |

### 2026-01-24 — video-transcript

| cuvânt           |   frecvență |
|:-----------------|------------:|
| patriotism       |           6 |
| însemna          |           6 |
| responsabilitate |           5 |
| moment           |           4 |
| om               |           4 |
| an               |           4 |
| pământ           |           3 |
| reuși            |           3 |
| asumare          |           3 |
| bucura           |           2 |
| sărbătoare       |           2 |
| trebui           |           2 |
| reflecta         |           2 |
| ianuarie         |           2 |
| istorie          |           2 |
| duce             |           2 |
| ideal            |           2 |
| potențial        |           2 |
| bun              |           2 |
| rău              |           2 |

### 2026-01-24 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |          13 |
| an         |          12 |
| unire      |          11 |
| vrea       |          11 |
| președinte |           7 |
| veni       |           7 |
| românia    |           7 |
| om         |           7 |
| începe     |           6 |
| piață      |           6 |
| oră        |           5 |
| moment     |           5 |
| iași       |           4 |
| român      |           4 |
| program    |           4 |
| spune      |           4 |
| loc        |           4 |
| vedea      |           4 |
| oficial    |           3 |
| principat  |           3 |

### 2026-01-24 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| românia       |          17 |
| spune         |          16 |
| putea         |          12 |
| vrea          |          12 |
| chestiune     |          10 |
| ăă            |          10 |
| coaliție      |           9 |
| dumneavoastră |           9 |
| trebui        |           8 |
| sine          |           8 |
| an            |           8 |
| urmă          |           8 |
| moment        |           7 |
| european      |           7 |
| partid        |           7 |
| om            |           6 |
| politic       |           6 |
| exista        |           6 |
| țară          |           6 |
| parte         |           6 |

### 2026-01-24 — video-transcript

| cuvânt           |   frecvență |
|:-----------------|------------:|
| responsabilitate |           5 |
| an               |           3 |
| autoritate       |           2 |
| public           |           2 |
| om               |           2 |
| însă             |           2 |
| gândi            |           2 |
| pas              |           2 |
| românia          |           2 |
| drag             |           1 |
| focșan           |           1 |
| huidui           |           1 |
| câștiga          |           1 |
| muri             |           1 |
| cetățean         |           1 |
| țară             |           1 |
| huiduie          |           1 |
| veni             |           1 |
| uita             |           1 |
| pune             |           1 |

### 2026-01-24 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| românia      |           3 |
| minister     |           2 |
| extern       |           2 |
| consiliu     |           2 |
| țară         |           2 |
| plăti        |           2 |
| moment       |           2 |
| an           |           2 |
| invita       |           2 |
| analiza      |           1 |
| oportunitate |           1 |
| participare  |           1 |
| pace         |           1 |
| recent       |           1 |
| crea         |           1 |
| donald       |           1 |
| trump        |           1 |
| președinte   |           1 |
| nicușor      |           1 |
| dan          |           1 |

### 2026-01-24 — video-transcript

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| guvern                  |           9 |
| premier                 |           6 |
| susține                 |           5 |
| partid                  |           5 |
| coaliție                |           5 |
| moment                  |           4 |
| partidulnaționalliberal |           3 |
| stat                    |           2 |
| fapt                    |           2 |
| sine                    |           2 |
| lege                    |           2 |
| sigur                   |           2 |
| parlament               |           2 |
| bolojan                 |           2 |
| forma                   |           2 |
| nicușordan              |           1 |
| vrea                    |           1 |
| numi                    |           1 |
| aduce                   |           1 |
| discuție                |           1 |

### 2026-01-24 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| muzică     |          24 |
| unire      |           9 |
| președinte |           7 |
| huidui     |           6 |
| românia    |           6 |
| an         |           5 |
| sine       |           5 |
| focșani    |           5 |
| român      |           4 |
| ceremonie  |           4 |
| vorbă      |           4 |
| parte      |           4 |
| spune      |           4 |
| fapt       |           4 |
| bravo      |           4 |
| simpatie   |           3 |
| național   |           3 |
| mesaj      |           3 |
| nicușor    |           3 |
| dan        |           3 |

### 2026-01-30 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| om         |           4 |
| nume       |           3 |
| apărea     |           3 |
| caz        |           2 |
| ăă         |           2 |
| listă      |           2 |
| lung       |           2 |
| discuție   |           2 |
| șansă      |           2 |
| afara      |           2 |
| partid     |           2 |
| exista     |           1 |
| sistem     |           1 |
| democratic |           1 |
| mecanism   |           1 |
| echilibru  |           1 |
| putere     |           1 |
| președinte |           1 |
| propune    |           1 |
| parlament  |           1 |

### 2026-01-30 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| sine        |          35 |
| exista      |          27 |
| spune       |          24 |
| vrea        |          21 |
| ăă          |          19 |
| partid      |          16 |
| om          |          14 |
| stat        |          14 |
| moment      |          13 |
| trebui      |          12 |
| an          |          12 |
| discuție    |          12 |
| european    |          12 |
| președinte  |          11 |
| bineînțeles |          11 |
| putea       |          11 |
| țară        |          11 |
| bolojan     |          10 |
| problemă    |          10 |
| lucru       |          10 |

### 2026-01-30 — video-transcript

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| credeți                 |           2 |
| putea                   |           2 |
| ilie                    |           2 |
| bolojan                 |           2 |
| președinte              |           2 |
| relație                 |           2 |
| sine                    |           1 |
| guverna                 |           1 |
| moment                  |           1 |
| exista                  |           1 |
| alternativ              |           1 |
| partidulnaționalliberal |           1 |
| ocupa                   |           1 |
| poziție                 |           1 |
| prim                    |           1 |
| ministru                |           1 |
| context                 |           1 |
| lucru                   |           1 |
| merge                   |           1 |
| psd                     |           1 |

### 2026-01-30 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| exista     |           3 |
| economic   |           3 |
| martie     |           2 |
| probabil   |           2 |
| curs       |           2 |
| an         |           2 |
| vizită     |           2 |
| invitație  |           2 |
| mergeți    |           1 |
| stat       |           1 |
| unit       |           1 |
| aprilie    |           1 |
| iunie      |           1 |
| vedea      |           1 |
| washington |           1 |
| vrea       |           1 |
| trata      |           1 |
| serios     |           1 |
| discuție   |           1 |
| palier     |           1 |

### 2026-01-30 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| guvern    |           2 |
| măsură    |           2 |
| putea     |           2 |
| chestiune |           1 |
| același   |           1 |
| opinie    |           1 |
| însă      |           1 |
| ăă        |           1 |
| alinia    |           1 |
| fapt      |           1 |
| iulie     |           1 |
| august    |           1 |
| an        |           1 |
| trecut    |           1 |
| lua       |           1 |
| intra     |           1 |
| vigoare   |           1 |
| ieunțate  |           1 |
| spune     |           1 |
| ține      |           1 |

### 2026-01-30 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| exista      |           5 |
| bolojan     |           4 |
| discuta     |           3 |
| coaliție    |           3 |
| domn        |           3 |
| lider       |           2 |
| partid      |           2 |
| ilie        |           2 |
| sorin       |           2 |
| grindeanu   |           2 |
| friț        |           2 |
| probabil    |           2 |
| teoretic    |           2 |
| matematică  |           2 |
| posibil     |           2 |
| bineînțeles |           2 |
| moment      |           2 |
| niciun      |           2 |
| președinte  |           1 |
| nicușor     |           1 |

### 2026-02-09 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| domn       |          53 |
| sine       |          52 |
| românia    |          51 |
| spune      |          45 |
| vrea       |          36 |
| om         |          29 |
| ști        |          27 |
| an         |          25 |
| putea      |          24 |
| simion     |          21 |
| președinte |          20 |
| trump      |          20 |
| american   |          19 |
| crede      |          19 |
| duce       |          19 |
| lua        |          18 |
| stat       |          18 |
| veni       |          18 |
| consiliu   |          17 |
| român      |          17 |

### 2026-02-12 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| discuție   |           4 |
| vrea       |           3 |
| parte      |           2 |
| american   |           2 |
| putea      |           2 |
| țară       |           2 |
| românia    |           2 |
| observator |           2 |
| merge      |           2 |
| anunța     |           2 |
| important  |           2 |
| încă       |           1 |
| obiect     |           1 |
| statut     |           1 |
| moment     |           1 |
| decât      |           1 |
| adică      |           1 |
| format     |           1 |
| eventual   |           1 |
| rol        |           1 |

### 2026-02-12 — video-transcript

| cuvânt          |   frecvență |
|:----------------|------------:|
| vrea            |          18 |
| țară            |          15 |
| românia         |          11 |
| putea           |           9 |
| europa          |           9 |
| european        |           8 |
| important       |           8 |
| sine            |           8 |
| preț            |           7 |
| discuție        |           7 |
| consiliu        |           6 |
| ban             |           6 |
| merge           |           6 |
| energie         |           6 |
| exista          |           6 |
| componentă      |           5 |
| chestiune       |           5 |
| trebui          |           5 |
| lua             |           5 |
| competitivitate |           4 |

### 2026-02-12 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| vrea     |          20 |
| sine     |          17 |
| europa   |          17 |
| discuție |          17 |
| trebui   |          16 |
| energie  |          13 |
| an       |          13 |
| exista   |          13 |
| spune    |          13 |
| companie |          12 |
| uniune   |          12 |
| piață    |          12 |
| european |          11 |
| preț     |          11 |
| putea    |          11 |
| lucru    |          11 |
| parte    |          10 |
| țară     |          10 |
| adică    |           9 |
| consiliu |           8 |

### 2026-02-12 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |           8 |
| părea         |           6 |
| interesant    |           4 |
| vedea         |           3 |
| vrea          |           3 |
| om            |           3 |
| putea         |           2 |
| concurs       |           2 |
| nume          |           2 |
| niciun        |           2 |
| instituție    |           2 |
| privire       |           1 |
| șefu          |           1 |
| parchetelor   |           1 |
| listă         |           1 |
| propunere     |           1 |
| vedere        |           1 |
| dumneavoastră |           1 |
| ultim         |           1 |
| cuvânt        |           1 |

### 2026-02-12 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| sine     |          42 |
| discuție |          37 |
| vrea     |          33 |
| spune    |          26 |
| parte    |          24 |
| trebui   |          22 |
| exista   |          21 |
| moment   |          21 |
| putea    |          18 |
| lucru    |          18 |
| europa   |          17 |
| vedea    |          15 |
| an       |          15 |
| buget    |          15 |
| uniune   |          14 |
| european |          14 |
| energie  |          13 |
| piață    |          13 |
| companie |          12 |
| adică    |          12 |

### 2026-02-12 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| curte          |           4 |
| constituțional |           4 |
| vedea          |           3 |
| vrea           |           3 |
| putea          |           2 |
| spune          |           2 |
| majoritate     |           2 |
| parte          |           2 |
| sine           |           2 |
| pensie         |           2 |
| special        |           2 |
| trimitere      |           2 |
| cjue           |           2 |
| moment         |           2 |
| problemă       |           2 |
| societate      |           2 |
| tergiversare   |           2 |
| loc            |           1 |
| ședință        |           1 |
| schimbare      |           1 |

### 2026-02-12 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| preț         |           5 |
| energie      |           5 |
| important    |           2 |
| țară         |           2 |
| diferență    |           2 |
| chestiune    |           1 |
| discutat     |           1 |
| românia      |           1 |
| repede       |           1 |
| trebui       |           1 |
| merge        |           1 |
| tranziție    |           1 |
| verde        |           1 |
| printre      |           1 |
| dori         |           1 |
| proces       |           1 |
| lent         |           1 |
| industrie    |           1 |
| consumatoare |           1 |
| lume         |           1 |

### 2026-02-12 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| exista     |           7 |
| președinte |           4 |
| discuție   |           4 |
| posibil    |           4 |
| moment     |           4 |
| februarie  |           3 |
| întâlnire  |           3 |
| putea      |           3 |
| discuta    |           3 |
| partener   |           2 |
| american   |           2 |
| subiect    |           2 |
| donald     |           2 |
| trump      |           2 |
| spune      |           2 |
| statut     |           2 |
| observator |           2 |
| invitație  |           2 |
| sine       |           2 |
| reuniune   |           2 |

### 2026-02-13 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| sine     |          35 |
| discuție |          32 |
| vrea     |          24 |
| spune    |          22 |
| trebui   |          21 |
| moment   |          20 |
| exista   |          17 |
| putea    |          16 |
| lucru    |          16 |
| parte    |          15 |
| buget    |          13 |
| românia  |          12 |
| stat     |          12 |
| uniune   |          12 |
| ăă       |          12 |
| vedea    |          12 |
| piață    |          11 |
| european |          10 |
| același  |          10 |
| energie  |          10 |

### 2026-02-13 — video-transcript

| cuvânt          |   frecvență |
|:----------------|------------:|
| preț            |           3 |
| energie         |           3 |
| martie          |           2 |
| veni            |           2 |
| lega            |           2 |
| subiect         |           2 |
| ști             |           1 |
| consiliu        |           1 |
| comisie         |           1 |
| angaja          |           1 |
| propunere       |           1 |
| stabilire       |           1 |
| prioritate      |           1 |
| coborâre        |           1 |
| competitivitate |           1 |
| compani         |           1 |
| lume            |           1 |
| parte           |           1 |
| creștere        |           1 |
| speculator      |           1 |

### 2026-02-13 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| coaliție   |           7 |
| sine       |           5 |
| vrea       |           5 |
| întâlni    |           4 |
| funcționa  |           3 |
| moment     |           3 |
| percepție  |           3 |
| guvernare  |           2 |
| ambii      |           2 |
| parte      |           2 |
| preciza    |           2 |
| des        |           2 |
| lider      |           2 |
| individual |           2 |
| grup       |           2 |
| implica    |           2 |
| discuție   |           2 |
| buget      |           2 |
| decât      |           2 |
| coție      |           1 |

### 2026-02-17 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| președinte     |           3 |
| clar           |           3 |
| decizie        |           2 |
| politic        |           2 |
| idee           |           2 |
| subiect        |           2 |
| pro            |           2 |
| ăă             |           2 |
| putea          |           2 |
| organizație    |           2 |
| apartenență    |           2 |
| nicușori       |           1 |
| consultare     |           1 |
| lider          |           1 |
| partid         |           1 |
| contradictoriu |           1 |
| exprima        |           1 |
| opinie         |           1 |
| participare    |           1 |
| inițiativă     |           1 |

### 2026-02-17 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| românia       |           5 |
| spune         |           3 |
| ansamblu      |           3 |
| parte         |           3 |
| relație       |           3 |
| clarifica     |           2 |
| alegere       |           2 |
| anula         |           2 |
| trebui        |           2 |
| președinte    |           2 |
| putea         |           2 |
| parteneriat   |           2 |
| stat          |           2 |
| unit          |           2 |
| imagine       |           2 |
| exista        |           2 |
| american      |           2 |
| transatlantic |           2 |
| crede         |           2 |
| perspectivă   |           2 |

### 2026-02-17 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| ansamblu      |           3 |
| parte         |           3 |
| relație       |           3 |
| românia       |           3 |
| imagine       |           2 |
| exista        |           2 |
| american      |           2 |
| transatlantic |           2 |
| crede         |           2 |
| spune         |           2 |
| putea         |           2 |
| perspectivă   |           2 |
| ăă            |           2 |
| față          |           2 |
| cred          |           1 |
| trebui        |           1 |
| uita          |           1 |
| european      |           1 |
| dorință       |           1 |
| voință        |           1 |

### 2026-02-19 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |          14 |
| stat       |          11 |
| spune      |          10 |
| parte      |           8 |
| unit       |           8 |
| sine       |           8 |
| putea      |           7 |
| lume       |           7 |
| chestiune  |           7 |
| veni       |           7 |
| european   |           6 |
| securitate |           5 |
| angaja     |           5 |
| întâlnire  |           5 |
| președinte |           5 |
| relație    |           5 |
| discuție   |           5 |
| vorbi      |           5 |
| important  |           4 |
| partener   |           4 |

### 2026-02-19 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| moment     |          19 |
| spune      |          19 |
| românia    |          16 |
| vedea      |          15 |
| relație    |          15 |
| putea      |          14 |
| lucru      |          13 |
| președinte |          12 |
| vrea       |          11 |
| față       |          10 |
| om         |           9 |
| sine       |           9 |
| discuție   |           9 |
| român      |           8 |
| securitate |           8 |
| exista     |           8 |
| important  |           7 |
| trebui     |           7 |
| punct      |           7 |
| vedere     |           7 |

### 2026-02-19 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| putea        |           7 |
| parte        |           3 |
| lume         |           3 |
| rând         |           3 |
| experiență   |           3 |
| gaza         |           2 |
| lucru        |           2 |
| important    |           2 |
| românia      |           2 |
| copil        |           2 |
| putem        |           2 |
| bun          |           2 |
| ajuta        |           2 |
| refacere     |           2 |
| cred         |           1 |
| sine         |           1 |
| dori         |           1 |
| pace         |           1 |
| stabilitate  |           1 |
| prosperitate |           1 |

### 2026-02-19 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| trecut     |           2 |
| singur     |           1 |
| precizr    |           1 |
| președinte |           1 |
| trump      |           1 |
| greși      |           1 |
| titulatură |           1 |
| spune      |           1 |
| premier    |           1 |
| românia    |           1 |
| nicușor    |           1 |
| dan        |           1 |
| comenta    |           1 |
| sine       |           1 |
| întâmpl    |           1 |

### 2026-02-20 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| stat        |           3 |
| unit        |           3 |
| european    |           3 |
| veni        |           2 |
| partener    |           2 |
| parteneriat |           2 |
| sforăit     |           2 |
| subtext     |           2 |
| încă        |           2 |
| campanie    |           2 |
| electoral   |           2 |
| alege       |           2 |
| uniune      |           2 |
| explica     |           1 |
| politică    |           1 |
| extern      |           1 |
| important   |           1 |
| diferit     |           1 |
| format      |           1 |
| ales        |           1 |

### 2026-02-20 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |          13 |
| stat       |          13 |
| președinte |           9 |
| unit       |           9 |
| european   |           9 |
| sine       |           8 |
| domn       |           7 |
| important  |           7 |
| fapt       |           7 |
| bun        |           6 |
| donald     |           6 |
| trump      |           6 |
| duce       |           6 |
| discuta    |           6 |
| exista     |           6 |
| vrea       |           6 |
| spune      |           5 |
| lume       |           5 |
| europa     |           5 |
| adică      |           5 |

### 2026-02-24 — video-transcript

| cuvânt          |   frecvență |
|:----------------|------------:|
| lege            |           2 |
| sine            |           2 |
| ccr             |           2 |
| putea           |           2 |
| alina           |           1 |
| mulțumim        |           1 |
| încă            |           1 |
| proiect         |           1 |
| important       |           1 |
| deocamdată      |           1 |
| bloca           |           1 |
| vorbi           |           1 |
| modifica        |           1 |
| vârstă          |           1 |
| pensionară      |           1 |
| magistrață      |           1 |
| cuantum         |           1 |
| indemnizațiilor |           1 |
| afla            |           1 |
| promulgare      |           1 |

### 2026-02-24 — video-transcript

| cuvânt          |   frecvență |
|:----------------|------------:|
| ucraina         |           7 |
| președinte      |           4 |
| an              |           3 |
| european        |           3 |
| participa       |           2 |
| stat            |           2 |
| declanșare      |           2 |
| transmite       |           2 |
| mesaj           |           2 |
| securitate      |           2 |
| solidaritate    |           2 |
| premier         |           2 |
| kiev            |           2 |
| dimineață       |           2 |
| nicușor         |           1 |
| dan             |           1 |
| videoconferință |           1 |
| reuniune        |           1 |
| coaliție        |           1 |
| voință          |           1 |

### 2026-02-27 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| lege           |           6 |
| pensie         |           6 |
| moment         |           5 |
| vrea           |           5 |
| președinte     |           3 |
| promulga       |           3 |
| magistrață     |           3 |
| curte          |           3 |
| constituțional |           3 |
| reformă        |           3 |
| practic        |           3 |
| guvern         |           3 |
| informație     |           2 |
| nicușordan     |           2 |
| privind        |           2 |
| vasile         |           2 |
| veni           |           2 |
| bun            |           2 |
| special        |           2 |
| intra          |           2 |

### 2026-02-27 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| vrea           |           6 |
| trebui         |           6 |
| moment         |           5 |
| lege           |           4 |
| pensie         |           3 |
| românia        |           3 |
| jalon          |           3 |
| curte          |           2 |
| constituțional |           2 |
| xenia          |           2 |
| bun            |           2 |
| proiect        |           2 |
| vârstă         |           2 |
| pensionară     |           2 |
| primi          |           2 |
| vedea          |           2 |
| însă           |           2 |
| fapt           |           2 |
| comisie        |           2 |
| european       |           2 |

### 2026-03-05 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           9 |
| vorbi      |           9 |
| țară       |           5 |
| comun      |           5 |
| polonia    |           5 |
| uniune     |           3 |
| zonă       |           3 |
| securitate |           3 |
| polonez    |           3 |
| forum      |           3 |
| ști        |           3 |
| interesa   |           3 |
| viitor     |           3 |
| trebui     |           3 |
| dezvoltat  |           3 |
| inclusiv   |           2 |
| prezent    |           2 |
| împreună   |           2 |
| neagră     |           2 |
| economic   |           2 |

### 2026-03-05 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| domn         |          29 |
| președinte   |          21 |
| trebui       |          14 |
| românia      |          13 |
| polonia      |          12 |
| spune        |          12 |
| securitate   |          11 |
| situație     |          11 |
| întrebare    |          11 |
| privi        |          11 |
| european     |          10 |
| polonez      |          10 |
| discuta      |           9 |
| lucru        |           8 |
| cadru        |           8 |
| semna        |           8 |
| regiune      |           8 |
| țară         |           7 |
| ăă           |           7 |
| posibilitate |           7 |

### 2026-03-05 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| analiză   |           5 |
| aviz      |           3 |
| vrea      |           3 |
| amplu     |           3 |
| moment    |           3 |
| csm       |           2 |
| numire    |           2 |
| adică     |           2 |
| ăă        |           2 |
| spune     |           2 |
| sine      |           2 |
| recent    |           1 |
| propunere |           1 |
| șefie     |           1 |
| parchet   |           1 |
| românia   |           1 |
| aștepta   |           1 |
| întrebare |           1 |
| pozitiv   |           1 |
| negativ   |           1 |

### 2026-03-05 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |           8 |
| întâmpla   |           5 |
| spune      |           4 |
| preț       |           4 |
| putea      |           4 |
| președinte |           3 |
| consiliu   |           3 |
| concurență |           3 |
| situație   |           3 |
| sancționa  |           3 |
| românia    |           2 |
| eveniment  |           2 |
| începe     |           2 |
| avertiza   |           2 |
| crește     |           2 |
| discuție   |           2 |
| guvern     |           2 |
| veni       |           2 |
| efect      |           2 |
| populație  |           2 |

### 2026-03-05 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| ăă          |           4 |
| regiune     |           3 |
| vorbă       |           2 |
| convoca     |           2 |
| plânge      |           1 |
| republică   |           1 |
| islamic     |           1 |
| iran        |           1 |
| iranian     |           1 |
| regim       |           1 |
| sponsoriza  |           1 |
| terorism    |           1 |
| destabiliza |           1 |
| an          |           1 |
| rând        |           1 |
| consiliu    |           1 |
| suprem      |           1 |
| apărare     |           1 |
| țară        |           1 |
| vrea        |           1 |

### 2026-03-05 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| nuclear                         |           5 |
| românia                         |           5 |
| propunere                       |           3 |
| întrebare                       |           3 |
| northatlantictreatyorganization |           3 |
| public                          |           3 |
| subiect                         |           2 |
| franța                          |           2 |
| vrea                            |           2 |
| veni                            |           2 |
| răspunde                        |           2 |
| spune                           |           2 |
| moment                          |           2 |
| proteja                         |           2 |
| umbrelă                         |           2 |
| spațiu                          |           2 |
| element                         |           2 |
| teritoriu                       |           2 |
| sine                            |           2 |
| pune                            |           2 |

### 2026-03-05 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| putea         |           2 |
| spațiu        |           2 |
| bineînțeles   |           1 |
| ban           |           1 |
| categorie     |           1 |
| dumneavoastră |           1 |
| menționa      |           1 |
| domn          |           1 |
| nazare        |           1 |
| deosebire     |           1 |
| lună          |           1 |
| iunie         |           1 |
| an            |           1 |
| trece         |           1 |
| cunoșteam     |           1 |
| virgulă       |           1 |
| buget         |           1 |
| național      |           1 |
| încerca       |           1 |
| înțelege      |           1 |

### 2026-03-05 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| regiune  |           4 |
| ăă       |           2 |
| convoca  |           2 |
| țară     |           2 |
| coopera  |           2 |
| român    |           2 |
| vorbă    |           2 |
| lega     |           1 |
| situație |           1 |
| orientul |           1 |
| mijlociu |           1 |
| consiliu |           1 |
| suprem   |           1 |
| apărare  |           1 |
| vrea     |           1 |
| lucru    |           1 |
| prezenta |           1 |
| pericol  |           1 |
| imediat  |           1 |
| direct   |           1 |

### 2026-03-05 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| discuta      |           5 |
| securitate   |           4 |
| colaborare   |           4 |
| polonia      |           4 |
| românia      |           4 |
| context      |           3 |
| important    |           3 |
| participa    |           2 |
| posibilitate |           2 |
| industrie    |           2 |
| apărare      |           2 |
| păcat        |           2 |
| obliga       |           2 |
| comun        |           2 |
| inclusiv     |           2 |
| summit       |           2 |
| lucru        |           1 |
| trăim        |           1 |
| global       |           1 |
| complicat    |           1 |

### 2026-03-05 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| românia       |          23 |
| țară          |          16 |
| sine          |          15 |
| vorbi         |          14 |
| vrea          |          13 |
| discuție      |          11 |
| spune         |          10 |
| polonia       |           9 |
| moment        |           9 |
| putea         |           9 |
| buget         |           8 |
| președinte    |           7 |
| parte         |           7 |
| dumneavoastră |           7 |
| situație      |           7 |
| partid        |           7 |
| comun         |           6 |
| uniune        |           6 |
| ști           |           6 |
| lucru         |           6 |

### 2026-03-05 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| parteneriat                     |           3 |
| românia                         |           2 |
| nuclear                         |           2 |
| țară                            |           1 |
| membră                          |           1 |
| northatlantictreatyorganization |           1 |
| parte                           |           1 |
| decizie                         |           1 |
| program                         |           1 |
| componentă                      |           1 |
| sine                            |           1 |
| lua                             |           1 |
| cadru                           |           1 |
| alianță                         |           1 |
| punct                           |           1 |
| vedere                          |           1 |
| acoperi                         |           1 |
| umbrelă                         |           1 |
| relație                         |           1 |
| franța                          |           1 |

### 2026-03-05 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |           6 |
| întâmpla   |           4 |
| sancționa  |           3 |
| preț       |           2 |
| om         |           2 |
| jumătate   |           2 |
| taxă       |           2 |
| acciză     |           2 |
| stat       |           2 |
| consiliu   |           2 |
| concurență |           2 |
| președinte |           2 |
| ieși       |           2 |
| benzină    |           1 |
| plăti      |           1 |
| pompă      |           1 |
| brut       |           1 |
| petrol     |           1 |
| rafinat    |           1 |
| putea      |           1 |

### 2026-03-06 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| românia       |          23 |
| țară          |          16 |
| sine          |          16 |
| vorbi         |          14 |
| vrea          |          14 |
| discuție      |          11 |
| spune         |          11 |
| polonia       |          10 |
| moment        |           9 |
| putea         |           9 |
| buget         |           8 |
| președinte    |           7 |
| parte         |           7 |
| dumneavoastră |           7 |
| situație      |           7 |
| partid        |           7 |
| seara         |           6 |
| comun         |           6 |
| uniune        |           6 |
| ști           |           6 |

### 2026-03-06 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| nuclear                         |           8 |
| românia                         |           4 |
| umbrelă                         |           4 |
| northatlantictreatyorganization |           4 |
| teritoriu                       |           3 |
| găzdui                          |           2 |
| stat                            |           2 |
| presupune                       |           2 |
| prezență                        |           2 |
| veni                            |           2 |
| franța                          |           2 |
| proteja                         |           2 |
| întrebare                       |           2 |
| spațiu                          |           2 |
| public                          |           2 |
| pune                            |           2 |
| vrea                            |           1 |
| focoasă                         |           1 |
| anunț                           |           1 |
| șef                             |           1 |

### 2026-03-07 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          10 |
| semna      |           3 |
| muzică     |           3 |
| numirile   |           2 |
| asuma      |           2 |
| numire     |           2 |
| șef        |           2 |
| spune      |           2 |
| rezultat   |           2 |
| lună       |           2 |
| crede      |           2 |
| om         |           2 |
| veni       |           2 |
| instituție |           2 |
| sta        |           2 |
| mesaj      |           1 |
| transmite  |           1 |
| președinte |           1 |
| nicușor    |           1 |
| dan        |           1 |

### 2026-03-11 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| echipament   |           5 |
| românia      |           4 |
| subliniez    |           3 |
| țară         |           3 |
| vorbă        |           2 |
| fapt         |           2 |
| vrea         |           2 |
| stat         |           2 |
| unit         |           2 |
| colaborare   |           2 |
| sigur        |           2 |
| dislocare    |           1 |
| temporar     |           1 |
| forță        |           1 |
| militar      |           1 |
| american     |           1 |
| avioană      |           1 |
| realimentare |           1 |
| discuta      |           1 |
| spațiu       |           1 |

### 2026-03-11 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           7 |
| echipament |           7 |
| țară       |           6 |
| situație   |           6 |
| român      |           6 |
| discuta    |           5 |
| ministru   |           5 |
| parlament  |           4 |
| ședință    |           3 |
| militar    |           3 |
| expunere   |           3 |
| parte      |           3 |
| zonă       |           3 |
| evident    |           3 |
| consecință |           3 |
| vrea       |           3 |
| stat       |           3 |
| subliniez  |           3 |
| consiliu   |           2 |
| termen     |           2 |

### 2026-03-12 — video-transcript

| cuvânt   | frecvență   |
|----------|-------------|

### 2026-03-12 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |          10 |
| ucraina     |           8 |
| vorbi       |           8 |
| moment      |           7 |
| sine        |           5 |
| document    |           5 |
| președinte  |           4 |
| parteneriat |           4 |
| european    |           4 |
| țară        |           4 |
| război      |           4 |
| comun       |           4 |
| sprijin     |           4 |
| spune       |           3 |
| semna       |           3 |
| strategic   |           3 |
| vrea        |           3 |
| important   |           3 |
| minoritate  |           3 |
| volodimir   |           2 |

### 2026-03-13 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |          58 |
| vrea       |          38 |
| ucraina    |          32 |
| putea      |          28 |
| stat       |          22 |
| președinte |          20 |
| domn       |          19 |
| vorbi      |          18 |
| sine       |          16 |
| parte      |          15 |
| document   |          15 |
| dronă      |          15 |
| spune      |          14 |
| război     |          14 |
| important  |          13 |
| colaborare |          13 |
| europa     |          12 |
| sprijin    |          12 |
| european   |          12 |
| rusia      |          12 |

### 2026-03-16 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| putea        |           6 |
| președinte   |           5 |
| piață        |           4 |
| stat         |           3 |
| dan          |           3 |
| energetic    |           3 |
| petrol       |           3 |
| românia      |           3 |
| necesar      |           3 |
| guvern       |           3 |
| măsură       |           3 |
| nicușor      |           2 |
| reprezentant |           2 |
| omw          |           2 |
| petrom       |           2 |
| resursă      |           2 |
| insuficient  |           2 |
| acoperi      |           2 |
| intern       |           2 |
| motiv        |           2 |

### 2026-03-19 — video-transcript-diarizat

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| românia                         |           9 |
| discuta                         |           6 |
| domn                            |           5 |
| secretar                        |           4 |
| general                         |           4 |
| securitate                      |           4 |
| northatlantictreatyorganization |           4 |
| summit                          |           4 |
| ucraina                         |           4 |
| discuție                        |           3 |
| sine                            |           3 |
| sigur                           |           3 |
| vrea                            |           3 |
| echipament                      |           3 |
| vorbi                           |           3 |
| invitație                       |           2 |
| bineînțeles                     |           2 |
| spune                           |           2 |
| uita                            |           2 |
| țară                            |           2 |

### 2026-03-19 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| discuta                         |           4 |
| ucraina                         |           4 |
| românia                         |           2 |
| țară                            |           2 |
| sigur                           |           2 |
| est                             |           2 |
| neagră                          |           2 |
| northatlantictreatyorganization |           2 |
| securitate                      |           2 |
| reîntări                        |           1 |
| ăă                              |           1 |
| român                           |           1 |
| sine                            |           1 |
| uita                            |           1 |
| capabilitate                    |           1 |
| flanc                           |           1 |
| estic                           |           1 |
| cadru                           |           1 |
| program                         |           1 |
| santinela                       |           1 |

### 2026-03-19 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| discuta                         |           6 |
| domn                            |           5 |
| românia                         |           5 |
| secretar                        |           4 |
| general                         |           4 |
| securitate                      |           4 |
| summit                          |           4 |
| ucraina                         |           4 |
| northatlantictreatyorganization |           3 |
| vrea                            |           3 |
| echipament                      |           3 |
| invitație                       |           2 |
| discuție                        |           2 |
| sine                            |           2 |
| țară                            |           2 |
| sigur                           |           2 |
| est                             |           2 |
| neagră                          |           2 |
| ancara                          |           2 |
| partener                        |           2 |

### 2026-03-26 — video-transcript

| cuvânt   | frecvență   |
|----------|-------------|

### 2026-03-26 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| motivare       |           2 |
| curte          |           2 |
| veni           |           2 |
| veți           |           1 |
| promulga       |           1 |
| lege           |           1 |
| buget          |           1 |
| aprobat        |           1 |
| sigur          |           1 |
| formalita      |           1 |
| moment         |           1 |
| adică          |           1 |
| constituție    |           1 |
| interzica      |           1 |
| promulge       |           1 |
| primi          |           1 |
| constituțional |           1 |
| ști            |           1 |
| respinge       |           1 |
| text           |           1 |

### 2026-03-27 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |           6 |
| măsură     |           4 |
| preț       |           3 |
| spune      |           2 |
| pune       |           2 |
| problemă   |           2 |
| petrol     |           2 |
| guvern     |           2 |
| vrea       |           2 |
| dinamică   |           2 |
| reveni     |           2 |
| normal     |           2 |
| piață      |           2 |
| întâmpla   |           2 |
| vedea      |           2 |
| lume       |           2 |
| perfect    |           2 |
| împrumuta  |           2 |
| președinte |           1 |
| nicușordan |           1 |

### 2026-03-30 — video-transcript

| cuvânt   |   frecvență |
|:---------|------------:|
| crede    |           2 |
| vrea     |           2 |
| sine     |           2 |
| soluție  |           1 |
| ferici   |           1 |
| moment   |           1 |
| trăim    |           1 |
| aștepta  |           1 |
| fapt     |           1 |
| partid   |           1 |
| forma    |           1 |
| coaliție |           1 |
| spune    |           1 |
| guverna  |           1 |
| condiție |           1 |
| întâmpla |           1 |
| duce     |           1 |
| idee     |           1 |
| ajunge   |           1 |
| înțelege |           1 |

### 2026-03-30 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| guvern        |          15 |
| vrea          |          15 |
| sine          |          14 |
| crede         |           9 |
| lua           |           9 |
| moment        |           8 |
| măsură        |           7 |
| bun           |           6 |
| minoritar     |           5 |
| partid        |           5 |
| discuție      |           5 |
| spune         |           5 |
| dumneavoastră |           5 |
| săptămână     |           5 |
| preț          |           5 |
| tva           |           4 |
| față          |           3 |
| președinte    |           3 |
| românia       |           3 |
| ăă            |           3 |

### 2026-03-31 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| guvern     |           2 |
| sine       |           2 |
| coaliție   |           2 |
| joi        |           2 |
| vrea       |           1 |
| speranță   |           1 |
| vorbi      |           1 |
| nume       |           1 |
| crede      |           1 |
| profiza    |           1 |
| lucru      |           1 |
| scădere    |           1 |
| consticare |           1 |
| sensibil   |           1 |
| intenție   |           1 |
| partid     |           1 |
| forma      |           1 |
| guvernare  |           1 |
| rezolve    |           1 |
| măcar      |           1 |

### 2026-03-31 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| preț          |           4 |
| crede         |           3 |
| guvern        |           3 |
| joi           |           3 |
| coaliție      |           3 |
| vrea          |           2 |
| scădere       |           2 |
| ședință       |           2 |
| formulă       |           2 |
| scazi         |           2 |
| acciza        |           2 |
| tva           |           2 |
| scădea        |           2 |
| sine          |           2 |
| președinte    |           1 |
| nicu          |           1 |
| jordan        |           1 |
| vedea         |           1 |
| carburanților |           1 |
| spera         |           1 |

### 2026-04-01 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           3 |
| românia    |           2 |
| euro       |           2 |
| atât       |           2 |
| șansă      |           2 |
| ajunge     |           2 |
| deficit    |           2 |
| devreme    |           1 |
| adera      |           1 |
| firmă      |           1 |
| veni       |           1 |
| europa     |           1 |
| acoperi    |           1 |
| țară       |           1 |
| motiv      |           1 |
| context    |           1 |
| economic   |           1 |
| necesitate |           1 |
| trebui     |           1 |
| îndeplini  |           1 |

### 2026-04-07 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          41 |
| domn          |          28 |
| românia       |          28 |
| putea         |          25 |
| spune         |          24 |
| sine          |          24 |
| vedea         |          23 |
| președinte    |          21 |
| lucru         |          19 |
| an            |          19 |
| parte         |          17 |
| trebui        |          16 |
| important     |          15 |
| exista        |          13 |
| european      |          13 |
| timișoara     |          12 |
| țară          |          12 |
| crede         |          12 |
| dumneavoastră |          11 |
| bun           |          11 |

### 2026-04-07 — video-transcript

| cuvânt          |   frecvență |
|:----------------|------------:|
| trebui          |           2 |
| spune           |           2 |
| veți            |           1 |
| cere            |           1 |
| demisie         |           1 |
| ilie            |           1 |
| bolojan         |           1 |
| calitate        |           1 |
| crede           |           1 |
| analiză         |           1 |
| scenariil       |           1 |
| posibil         |           1 |
| vehicula        |           1 |
| spațiu          |           1 |
| public          |           1 |
| putea           |           1 |
| exista          |           1 |
| responsabilitat |           1 |
| medie           |           1 |
| discuta         |           1 |

### 2026-04-07 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          22 |
| românia       |          15 |
| spune         |          13 |
| președinte    |          12 |
| putea         |          12 |
| domn          |          11 |
| sine          |          10 |
| exista        |           9 |
| parte         |           9 |
| moment        |           9 |
| vedea         |           8 |
| public        |           7 |
| întrebare     |           7 |
| dumneavoastră |           7 |
| partid        |           6 |
| criză         |           6 |
| discuție      |           6 |
| coaliție      |           6 |
| crede         |           5 |
| trebui        |           5 |

### 2026-04-07 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| mircea      |           5 |
| lucescu     |           5 |
| condoleanță |           3 |
| deces       |           3 |
| românia     |           3 |
| fotbal      |           3 |
| urmă        |           2 |
| mesaj       |           2 |
| președinte  |           2 |
| nicușor     |           2 |
| dan         |           2 |
| spune       |           2 |
| românesc    |           2 |
| lăsa        |           2 |
| jucător     |           2 |
| echipă      |           2 |
| transmite   |           1 |
| marți       |           1 |
| aprilie     |           1 |
| următor     |           1 |

### 2026-04-07 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| exista       |           4 |
| criză        |           4 |
| discuta      |           2 |
| moment       |           2 |
| românia      |           2 |
| țară         |           2 |
| parte        |           2 |
| scenarii     |           2 |
| procurare    |           1 |
| posibilitate |           1 |
| lipsă        |           1 |
| combustibil  |           1 |
| piață        |           1 |
| poziție      |           1 |
| bun          |           1 |
| decât        |           1 |
| european     |           1 |
| producție    |           1 |
| intern       |           1 |
| rafinare     |           1 |

### 2026-04-08 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| procuror   |          54 |
| șef        |          35 |
| vrea       |          33 |
| spune      |          33 |
| sine       |          33 |
| parchet    |          21 |
| general    |          21 |
| trebui     |          21 |
| discuție   |          20 |
| românia    |          20 |
| activitate |          19 |
| bun        |          19 |
| președinte |          18 |
| ști        |          18 |
| dna        |          17 |
| putea      |          17 |
| trimite    |          17 |
| moment     |          16 |
| om         |          16 |
| vedea      |          15 |

### 2026-04-08 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| spune      |           4 |
| arăta      |           3 |
| însă       |           3 |
| campanie   |           3 |
| sine       |           3 |
| fotografie |           3 |
| victor     |           2 |
| ponta      |           2 |
| sursă      |           2 |
| crin       |           2 |
| antonescu  |           2 |
| nicușor    |           2 |
| dan        |           2 |
| fotograf   |           2 |
| elena      |           2 |
| lasconi    |           2 |
| respectiv  |           2 |
| apropiat   |           2 |
| ști        |           2 |
| informație |           1 |

### 2026-04-08 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| procuror   |          31 |
| șef        |          18 |
| spune      |          15 |
| sine       |          14 |
| parchet    |          12 |
| vrea       |          12 |
| judecată   |          12 |
| trimite    |          11 |
| ști        |          11 |
| bun        |          11 |
| penal      |          10 |
| dosar      |           9 |
| iași       |           9 |
| public     |           8 |
| general    |           8 |
| întâmpla   |           8 |
| discuție   |           8 |
| românia    |           8 |
| dna        |           8 |
| activitate |           7 |

### 2026-04-08 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          18 |
| dumneavoastră |          16 |
| spune         |          14 |
| sine          |          11 |
| putea         |          10 |
| campanie      |           8 |
| bun           |           7 |
| penaliza      |           7 |
| adică         |           7 |
| crede         |           7 |
| întrebare     |           7 |
| domn          |           7 |
| ăă            |           7 |
| persoană      |           7 |
| echipă        |           7 |
| românia       |           6 |
| președinte    |           6 |
| român         |           6 |
| apărea        |           6 |
| informație    |           6 |

### 2026-04-08 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| român       |           3 |
| propunere   |           3 |
| psd         |           3 |
| parchetelor |           2 |
| activitate  |           2 |
| președinte  |           2 |
| aproba      |           2 |
| procuror    |           2 |
| ministru    |           2 |
| justiție    |           2 |
| moment      |           1 |
| așteptare   |           1 |
| parchet     |           1 |
| implicit    |           1 |
| șef         |           1 |
| dinamizare  |           1 |
| răspunde    |           1 |
| așteptăre   |           1 |
| vedea       |           1 |
| corupție    |           1 |

### 2026-04-09 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| procuror      |          38 |
| spune         |          38 |
| vrea          |          24 |
| sine          |          23 |
| șef           |          22 |
| bun           |          21 |
| dumneavoastră |          21 |
| trimite       |          17 |
| parchet       |          17 |
| ști           |          17 |
| putea         |          16 |
| discuție      |          15 |
| întrebare     |          15 |
| românia       |          15 |
| trebui        |          14 |
| judecată      |          14 |
| parte         |          13 |
| general       |          13 |
| exista        |          13 |
| vedea         |          12 |

### 2026-04-17 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| verificare |           3 |
| mesaj      |           3 |
| postare    |           3 |
| președinte |           2 |
| românia    |           2 |
| polițiștii |           2 |
| timiș      |           2 |
| bărbat     |           2 |
| fond       |           2 |
| om         |           2 |
| lege       |           2 |
| încerca    |           2 |
| găsi       |           2 |
| mihai      |           2 |
| caz        |           2 |
| vorbă      |           2 |
| persoană   |           2 |
| grav       |           2 |
| inițări    |           1 |
| moarte     |           1 |

### 2026-04-17 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| vrea           |           3 |
| public         |           3 |
| final          |           3 |
| an             |           3 |
| lucru          |           3 |
| călin          |           2 |
| georgescu      |           2 |
| susține        |           2 |
| alegere        |           2 |
| infrastructură |           2 |
| crea           |           2 |
| federație      |           2 |
| rus            |           2 |
| vedea          |           2 |
| dovezile       |           2 |
| raport         |           2 |
| categoric      |           2 |
| prezidențial   |           1 |
| cuvânt         |           1 |
| președinte     |           1 |

### 2026-04-20 — video-transcript

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| sine                    |          74 |
| vrea                    |          73 |
| psd                     |          55 |
| partid                  |          48 |
| putea                   |          36 |
| liberal                 |          29 |
| domn                    |          27 |
| vedea                   |          27 |
| spune                   |          27 |
| președinte              |          26 |
| național                |          25 |
| premier                 |          22 |
| partidulnaționalliberal |          20 |
| lucru                   |          20 |
| ilie                    |          20 |
| întâmpla                |          19 |
| criză                   |          19 |
| ști                     |          19 |
| merge                   |          18 |
| politic                 |          17 |

### 2026-04-20 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| financiar |           9 |
| educație  |           6 |
| om        |           5 |
| vrea      |           5 |
| economie  |           5 |
| spune     |           4 |
| sine      |           4 |
| zonă      |           4 |
| societate |           4 |
| rând      |           3 |
| nivel     |           3 |
| parte     |           3 |
| duce      |           3 |
| capital   |           3 |
| invita    |           3 |
| merge     |           2 |
| studiu    |           2 |
| important |           2 |
| putea     |           2 |
| investi   |           2 |

### 2026-04-20 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| financiar      |           4 |
| vrea           |           4 |
| economie       |           4 |
| societate      |           3 |
| educație       |           3 |
| capital        |           3 |
| zonă           |           3 |
| spune          |           3 |
| invita         |           3 |
| sănătos        |           2 |
| antreprenoriat |           2 |
| trăim          |           2 |
| profesional    |           2 |
| război         |           2 |
| informațional  |           2 |
| inclusiv       |           2 |
| reclam         |           2 |
| domn           |           2 |
| guvernator     |           2 |
| profit         |           2 |

### 2026-04-20 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| spune         |          19 |
| vrea          |          15 |
| exista        |          12 |
| sine          |          11 |
| românia       |          10 |
| domn          |          10 |
| vedea         |           9 |
| lucru         |           8 |
| important     |           7 |
| financiar     |           7 |
| ilie          |           7 |
| politic       |           6 |
| consens       |           6 |
| dumneavoastră |           6 |
| parte         |           6 |
| bolojan       |           6 |
| președinte    |           6 |
| putea         |           6 |
| transmite     |           6 |
| întrebare     |           5 |

### 2026-04-22 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| politic    |           7 |
| partid     |           4 |
| moment     |           3 |
| viitor     |           3 |
| criză      |           3 |
| sine       |           3 |
| vrea       |           3 |
| consultare |           2 |
| coaliție   |           2 |
| evident    |           2 |
| diferență  |           2 |
| opinie     |           2 |
| discuție   |           2 |
| public     |           2 |
| uita       |           2 |
| decât      |           2 |
| dialog     |           2 |
| forță      |           2 |
| pro        |           2 |
| stat       |           2 |

### 2026-04-22 — video-transcript

| cuvânt    |   frecvență |
|:----------|------------:|
| greu      |           4 |
| vrea      |           4 |
| moment    |           4 |
| urmă      |           3 |
| coaliție  |           3 |
| soluție   |           3 |
| partid    |           2 |
| ști       |           2 |
| funcționa |           2 |
| înțelege  |           2 |
| împreună  |           2 |
| sine      |           2 |
| dificil   |           2 |
| românia   |           2 |
| impui     |           1 |
| premier   |           1 |
| spune     |           1 |
| domn      |           1 |
| ruga      |           1 |
| politică  |           1 |

### 2026-04-23 — video-transcript

| cuvânt          |   frecvență |
|:----------------|------------:|
| vrea            |          14 |
| discuție        |           7 |
| important       |           7 |
| românia         |           6 |
| spune           |           6 |
| uniune          |           5 |
| dori            |           5 |
| țară            |           4 |
| competitivitate |           4 |
| ban             |           4 |
| european        |           4 |
| seară           |           4 |
| lider           |           3 |
| ști             |           3 |
| lucru           |           3 |
| buget           |           3 |
| ajuta           |           3 |
| formă           |           3 |
| întâmpla        |           3 |
| psd             |           3 |

### 2026-04-24 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          28 |
| discuție      |          18 |
| spune         |          16 |
| putea         |          14 |
| situație      |          14 |
| dumneavoastră |          14 |
| sine          |          12 |
| exista        |          11 |
| guvern        |          11 |
| țară          |          10 |
| vedea         |          10 |
| sforăit       |          10 |
| ăă            |          10 |
| românia       |           9 |
| mesaj         |           9 |
| ucraina       |           9 |
| întreba       |           9 |
| psd           |           9 |
| vorbi         |           8 |
| criză         |           8 |

### 2026-04-24 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| om            |           3 |
| dumneavoastră |           2 |
| vedea         |           2 |
| declarație    |           2 |
| vot           |           2 |
| categorie     |           2 |
| sine          |           2 |
| argument      |           2 |
| george        |           1 |
| simion        |           1 |
| adversar      |           1 |
| campanie      |           1 |
| prezidențial  |           1 |
| declara       |           1 |
| adresă        |           1 |
| citez         |           1 |
| individus     |           1 |
| cotroceni     |           1 |
| paraplegic    |           1 |
| vrea          |           1 |

### 2026-04-25 — video-transcript

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| vrea                    |          18 |
| partid                  |           6 |
| aur                     |           6 |
| situație                |           4 |
| psd                     |           4 |
| coaliție                |           4 |
| partidulnaționalliberal |           4 |
| european                |           3 |
| președinte              |           3 |
| politic                 |           3 |
| palat                   |           3 |
| discuție                |           3 |
| lider                   |           3 |
| parte                   |           3 |
| proiect                 |           3 |
| parlament               |           3 |
| informal                |           2 |
| consiliu                |           2 |
| șef                     |           2 |
| stat                    |           2 |

### 2026-04-29 — video-transcript

| cuvânt         |   frecvență |
|:---------------|------------:|
| suspendare     |           3 |
| parte          |           3 |
| constituțional |           3 |
| declarație     |           2 |
| acționa        |           2 |
| dori           |           2 |
| vrea           |           2 |
| crede          |           2 |
| serios         |           2 |
| psd            |           2 |
| alianță        |           2 |
| mânie          |           1 |
| evident        |           1 |
| menține        |           1 |
| direcție       |           1 |
| românia        |           1 |
| guverna        |           1 |
| forță          |           1 |
| procidental    |           1 |
| chestiune      |           1 |

### 2026-05-04 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |           5 |
| europa      |           5 |
| stat        |           3 |
| unit        |           3 |
| sine        |           2 |
| pas         |           2 |
| compensa    |           2 |
| surpriză    |           1 |
| încă        |           1 |
| mandat      |           1 |
| președinte  |           1 |
| trump       |           1 |
| strategie   |           1 |
| apărare     |           1 |
| spune       |           1 |
| concentra   |           1 |
| indopacific |           1 |
| decât       |           1 |
| exista      |           1 |
| gradual     |           1 |

### 2026-05-04 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |          31 |
| sine        |          16 |
| european    |          13 |
| discuție    |          13 |
| uniune      |          12 |
| moldova     |          12 |
| exista      |          12 |
| putea       |          11 |
| românia     |          11 |
| moțiune     |          11 |
| politic     |           9 |
| parte       |           9 |
| țară        |           8 |
| stat        |           8 |
| spune       |           8 |
| ucraina     |           7 |
| bineînțeles |           7 |
| chestiune   |           7 |
| întâmpla    |           7 |
| direcție    |           7 |

### 2026-05-04 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| putea        |           4 |
| moțiune      |           3 |
| cenzură      |           2 |
| trece        |           2 |
| vrea         |           2 |
| moment       |           2 |
| aur          |           2 |
| predicție    |           2 |
| tv           |           1 |
| domn         |           1 |
| președinte   |           1 |
| matematician |           1 |
| bază         |           1 |
| informație   |           1 |
| șansă        |           1 |
| evident      |           1 |
| opinie       |           1 |
| speculație   |           1 |
| aștepta      |           1 |
| trăda        |           1 |

### 2026-05-05 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| consens    |           7 |
| exista     |           6 |
| guvern     |           5 |
| vrea       |           4 |
| parlament  |           3 |
| românia    |           3 |
| stat       |           3 |
| direcție   |           3 |
| buget      |           3 |
| program    |           3 |
| pnrr       |           3 |
| calm       |           2 |
| partid     |           2 |
| pro        |           2 |
| occidental |           2 |
| următor    |           2 |
| safe       |           2 |
| procedură  |           2 |
| formare    |           2 |
| înțeleg    |           2 |

### 2026-05-05 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| guvern     |           5 |
| vrea       |           4 |
| stat       |           3 |
| parlament  |           2 |
| calm       |           2 |
| românia    |           2 |
| formare    |           2 |
| înțeleg    |           2 |
| așteptără  |           2 |
| român      |           2 |
| lega       |           2 |
| demite     |           1 |
| moment     |           1 |
| fericit    |           1 |
| niciun     |           1 |
| democrație |           1 |
| însă       |           1 |
| decizie    |           1 |
| democratic |           1 |
| invit      |           1 |

### 2026-05-06 — video-transcript

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| guvern                  |           6 |
| partid                  |           5 |
| moment                  |           5 |
| psd                     |           5 |
| udmr                    |           5 |
| parte                   |           4 |
| aur                     |           4 |
| vot                     |           4 |
| combinație              |           3 |
| majoritate              |           3 |
| sine                    |           3 |
| partidulnaționalliberal |           3 |
| vedea                   |           3 |
| forma                   |           3 |
| parlamentar             |           3 |
| variantă                |           2 |
| octav                   |           2 |
| calculă                 |           2 |
| președinte              |           2 |
| formare                 |           2 |

### 2026-05-06 — video-transcript

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| usr                     |           3 |
| dan                     |           2 |
| coaliție                |           2 |
| psd                     |           2 |
| vrea                    |           2 |
| alegere                 |           2 |
| partidulnaționalliberal |           2 |
| sondajă                 |           2 |
| asculta                 |           1 |
| declarație              |           1 |
| cristian                |           1 |
| ghina                   |           1 |
| nicușor                 |           1 |
| naș                     |           1 |
| politic                 |           1 |
| năși                    |           1 |
| complet                 |           1 |
| dezinteresa             |           1 |
| funcționare             |           1 |
| târziu                  |           1 |

### 2026-05-07 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| președinte  |           9 |
| guvernare   |           7 |
| veni        |           6 |
| spune       |           5 |
| guvern      |           5 |
| asuma       |           5 |
| suspendare  |           4 |
| aur         |           4 |
| psd         |           4 |
| românia     |           4 |
| chema       |           4 |
| procedură   |           3 |
| politic     |           3 |
| palmă       |           3 |
| crește      |           3 |
| domn        |           2 |
| nicușor     |           2 |
| dan         |           2 |
| constituție |           2 |
| exista      |           2 |

### 2026-05-08 — video-transcript

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| domn                    |          20 |
| spune                   |          19 |
| psd                     |          19 |
| vrea                    |          16 |
| sine                    |          16 |
| premier                 |          14 |
| bolojan                 |          13 |
| vedea                   |          13 |
| partid                  |          12 |
| majoritate              |          12 |
| putea                   |          11 |
| partidulnaționalliberal |          10 |
| moment                  |           9 |
| ști                     |           9 |
| președinte              |           8 |
| udmr                    |           8 |
| coaliție                |           8 |
| politic                 |           8 |
| ilie                    |           7 |
| nicușor                 |           7 |

### 2026-05-09 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |          18 |
| european   |          16 |
| uniune     |          12 |
| europa     |          10 |
| vrea       |           7 |
| an         |           6 |
| moment     |           5 |
| duce       |           5 |
| dezbatere  |           5 |
| greșeală   |           5 |
| sine       |           4 |
| adevărat   |           4 |
| decât      |           4 |
| loc        |           4 |
| exista     |           4 |
| român      |           4 |
| politică   |           4 |
| interior   |           4 |
| occidental |           3 |
| pace       |           3 |

### 2026-05-09 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           5 |
| românia    |           3 |
| guvern     |           3 |
| pro        |           3 |
| occidental |           3 |
| partid     |           3 |
| întru      |           2 |
| termen     |           2 |
| rezonabil  |           2 |
| încheia    |           2 |
| negociere  |           2 |
| lider      |           2 |
| veni       |           2 |
| începe     |           2 |
| exista     |           2 |
| reafirma   |           1 |
| președinte |           1 |
| nicușordan |           1 |
| șef        |           1 |
| stat       |           1 |

### 2026-05-12 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| europa        |          17 |
| spune         |          15 |
| discurs       |           6 |
| românia       |           5 |
| european      |           5 |
| dumneavoastră |           5 |
| dezbatere     |           5 |
| exemplu       |           4 |
| ăă            |           4 |
| crede         |           3 |
| lume          |           3 |
| opinie        |           3 |
| vorbi         |           3 |
| vrea          |           3 |
| participa     |           3 |
| societate     |           3 |
| politică      |           3 |
| sine          |           2 |
| critica       |           2 |
| acționa       |           2 |

### 2026-05-12 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           9 |
| partid     |           4 |
| consultare |           3 |
| formal     |           3 |
| premier    |           3 |
| majoritate |           3 |
| exista     |           3 |
| avansa     |           3 |
| viitor     |           2 |
| președinte |           2 |
| propunere  |           2 |
| spune      |           2 |
| variantă   |           2 |
| tehnocrat  |           2 |
| șansă      |           2 |
| chema      |           2 |
| minte      |           2 |
| nicușor    |           1 |
| dan        |           1 |
| convoca    |           1 |

### 2026-05-12 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| northatlantictreatyorganization |          12 |
| vrea                            |          12 |
| neagră                          |           9 |
| summit                          |           8 |
| românia                         |           8 |
| președinte                      |           7 |
| nivel                           |           7 |
| spune                           |           6 |
| discuție                        |           5 |
| important                       |           5 |
| bucurești                       |           4 |
| uniune                          |           4 |
| stat                            |           4 |
| sine                            |           4 |
| obiectiv                        |           4 |
| loc                             |           4 |
| relație                         |           4 |
| puternic                        |           4 |
| putea                           |           4 |
| asculta                         |           3 |

### 2026-05-13 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| summit                          |           8 |
| northatlantictreatyorganization |           7 |
| stat                            |           5 |
| alianță                         |           5 |
| general                         |           4 |
| declarație                      |           4 |
| țară                            |           4 |
| ucraina                         |           4 |
| important                       |           4 |
| moldova                         |           4 |
| discuție                        |           3 |
| bucurești                       |           3 |
| vreau                           |           3 |
| salut                           |           3 |
| prezență                        |           3 |
| secretar                        |           3 |
| comun                           |           3 |
| amenințare                      |           3 |
| rusia                           |           3 |
| parte                           |           3 |

### 2026-05-13 — video-transcript

| cuvânt       |   frecvență |
|:-------------|------------:|
| moldova      |           4 |
| alianță      |           3 |
| stat         |           2 |
| important    |           2 |
| linie        |           1 |
| decizie      |           1 |
| asuma        |           1 |
| respectare   |           1 |
| angajamentă  |           1 |
| suplimentare |           1 |
| cheltuială   |           1 |
| militar      |           1 |
| transformare |           1 |
| ban          |           1 |
| capabilitate |           1 |
| pregăti      |           1 |
| amenințare   |           1 |
| bineînțeles  |           1 |
| echilibrare  |           1 |
| interior     |           1 |

### 2026-05-13 — video-transcript

| cuvânt     |   frecvență |
|:-----------|------------:|
| trebui     |           4 |
| apropiere  |           3 |
| veni       |           2 |
| prezență   |           2 |
| stat       |           2 |
| ucraina    |           2 |
| aliat      |           2 |
| alianță    |           2 |
| spori      |           2 |
| doamnelor  |           1 |
| domn       |           1 |
| bucurești  |           1 |
| palat      |           1 |
| cotroceni  |           1 |
| membră     |           1 |
| prieten    |           1 |
| nordică    |           1 |
| unit       |           1 |
| participa  |           1 |
| observator |           1 |

### 2026-05-13 — video-transcript

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| trebui                          |           7 |
| securitate                      |           5 |
| ucraina                         |           3 |
| apropiere                       |           3 |
| alianță                         |           3 |
| exista                          |           3 |
| prioritate                      |           3 |
| transatlantic                   |           3 |
| veni                            |           2 |
| prezență                        |           2 |
| stat                            |           2 |
| sine                            |           2 |
| desfășura                       |           2 |
| summit                          |           2 |
| northatlantictreatyorganization |           2 |
| aliat                           |           2 |
| consolidare                     |           2 |
| reuniune                        |           2 |
| rând                            |           2 |
| spori                           |           2 |

### 2026-05-15 — video-transcript

| cuvânt           |   frecvență |
|:-----------------|------------:|
| răspuns          |           5 |
| general          |           3 |
| guvern           |           3 |
| parlamentar      |           3 |
| responsabilitate |           3 |
| refacere         |           2 |
| usr              |           2 |
| partid           |           2 |
| întrebare        |           2 |
| majoritate       |           2 |
| trebui           |           2 |
| particular       |           1 |
| vrea             |           1 |
| numi             |           1 |
| nască            |           1 |
| criză            |           1 |
| putea            |           1 |
| sorin            |           1 |
| grindeanu        |           1 |
| spune            |           1 |

### 2026-05-15 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |          26 |
| exista      |          15 |
| parlamentar |          14 |
| sine        |          14 |
| majoritate  |          14 |
| spune       |          14 |
| discuție    |          13 |
| trebui      |          13 |
| guvern      |          13 |
| lună        |          11 |
| românia     |          11 |
| parte       |          11 |
| întrebare   |          10 |
| partid      |          10 |
| bun         |          10 |
| răspuns     |           9 |
| președinte  |           8 |
| politic     |           8 |
| veni        |           7 |
| domn        |           7 |

### 2026-05-20 — video-transcript

| cuvânt      |   frecvență |
|:------------|------------:|
| guvern      |           7 |
| partid      |           7 |
| muzică      |           6 |
| variantă    |           5 |
| social      |           5 |
| politic     |           4 |
| președinte  |           4 |
| sine        |           3 |
| parlamentar |           3 |
| democrat    |           3 |
| nicușor     |           3 |
| dan         |           3 |
| jur         |           3 |
| însă        |           3 |
| discuție    |           3 |
| psd         |           2 |
| monocolor   |           2 |
| vrea        |           2 |
| consultăre  |           2 |
| sprijin     |           2 |

### 2026-05-20 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| președinte    |          12 |
| românia       |          10 |
| vrea          |           6 |
| dan           |           4 |
| trebui        |           4 |
| stat          |           4 |
| unit          |           4 |
| spune         |           4 |
| plăcea        |           3 |
| trump         |           3 |
| bun           |           3 |
| sine          |           3 |
| țară          |           3 |
| fapt          |           3 |
| relație       |           3 |
| ocazie        |           2 |
| întâlni       |           2 |
| dumneavoastră |           2 |
| veni          |           2 |
| întâlnire     |           2 |


## Top 30 cuvinte — corpus integral

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |        4437 |
| sine          |        3671 |
| spune         |        2803 |
| românia       |        2465 |
| putea         |        2261 |
| trebui        |        1876 |
| vedea         |        1655 |
| domn          |        1625 |
| președinte    |        1610 |
| moment        |        1588 |
| om            |        1321 |
| parte         |        1231 |
| an            |        1176 |
| exista        |        1141 |
| lucru         |        1122 |
| stat          |        1119 |
| ști           |        1102 |
| partid        |        1072 |
| discuție      |        1046 |
| crede         |        1039 |
| ăă            |        1024 |
| bun           |         930 |
| veni          |         872 |
| dumneavoastră |         849 |
| țară          |         833 |
| român         |         798 |
| european      |         797 |
| important     |         793 |
| vorbi         |         773 |
| guvern        |         754 |

## Stopwords folosite

Listă **stopwordsiso RO** (438 cuvinte) + domain extras (cardinali, câteva auxiliare nestockate).


## Note metodologice

- **Tokenizare + lemmatizare**: spaCy `ro_core_news_sm`. Token-ele sunt reduse la lemma (formă canonică): `românia/româniei/român/români` → `românia`/`român`, `anunț/anunțul` → `anunța`, `săptămânile` → `săptămână`.
- **Stopwords**: `stopwordsiso` (RO) + extensii pentru cardinali și conjuncții scurte.
- **Numerele și punctuația** sunt eliminate; diacriticele cedilă (ş, ţ) sunt normalizate la virgulă-below (ș, ț).
- **TTR** (type-token ratio) e biased de lungime — discursurile scurte au TTR mai mare. Util doar comparativ pe lungimi similare.