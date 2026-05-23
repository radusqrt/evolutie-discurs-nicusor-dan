# Pasul 1 — Statistici de bază + word clouds

## Sumar corpus

| id                                                                      | data       | tip                       |   n_words_raw |   n_lemmas_clean |   n_unique_lemmas |   ttr_lemma |   n_sentences |
|:------------------------------------------------------------------------|:-----------|:--------------------------|--------------:|-----------------:|------------------:|------------:|--------------:|
| 2025-05-08_dezbatere-euronews-simion                                    | 2025-05-08 | dezbatere-electorala      |            63 |               34 |                28 |       0.824 |             5 |
| 2024-12-16_anunt-candidatura                                            | 2024-12-16 | anunt-candidatura         |           113 |               55 |                44 |       0.8   |             9 |
| 2025-02-03_lansare-campanie-romania-onesta                              | 2025-02-03 | lansare-campanie          |           184 |               90 |                68 |       0.756 |            13 |
| 2025-05-19_discurs-victorie                                             | 2025-05-19 | discurs-victorie          |           255 |              102 |                70 |       0.686 |            17 |
| 2025-05-26_discurs-investitura                                          | 2025-05-26 | discurs-investitura       |           992 |              528 |               325 |       0.616 |            26 |
| 2025-06-04_conferinta-presa-cotroceni                                   | 2025-06-04 | conferinta-presa          |           108 |               50 |                44 |       0.88  |             9 |
| 2025-09-04_autoevaluare-100-zile                                        | 2025-09-04 | interviu-autoevaluare     |           157 |               67 |                59 |       0.881 |            17 |
| 2025-12-31_mesaj-anul-nou                                               | 2025-12-31 | mesaj-anul-nou            |           277 |              142 |               116 |       0.817 |            16 |
| 2025-06-04_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus | 2025-06-04 | video-transcript          |           584 |              272 |               155 |       0.57  |            33 |
| 2025-06-20_declaratie-de-presa-sustinuta-de-presedintele-romaniei-nicus | 2025-06-20 | video-transcript          |           417 |              205 |               138 |       0.673 |            24 |
| 2025-06-26_declaratia-presedintelui-romaniei-nicusor-dan-dupa-participa | 2025-06-26 | video-transcript          |           753 |              345 |               207 |       0.6   |            54 |
| 2025-07-14_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus | 2025-07-14 | video-transcript          |          4808 |             2200 |               852 |       0.387 |           298 |
| 2025-07-31_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus | 2025-07-31 | video-transcript          |         11017 |             5061 |              1527 |       0.302 |           705 |
| 2025-11-12_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus | 2025-11-12 | video-transcript          |          6289 |             2811 |              1017 |       0.362 |           377 |
| 2025-12-17_declaratia-presedintelui-romaniei-nicusor-dan-in-regatul-mar | 2025-12-17 | video-transcript          |          1259 |              575 |               324 |       0.563 |            86 |
| 2025-12-21_declaratia-presedintelui-romaniei-nicusor-dan-pe-tema-proble | 2025-12-21 | video-transcript          |          1321 |              565 |               288 |       0.51  |            50 |
| 2025-12-22_discutii-publice-la-cotroceni-intre-presedintele-romaniei-ni | 2025-12-22 | video-transcript          |         23573 |            11107 |              2562 |       0.231 |          1181 |
| 2026-01-06_declaratia-presedintelui-romaniei-nicusor-dan-dupa-participa | 2026-01-06 | video-transcript          |          2177 |              998 |               488 |       0.489 |           135 |
| 2026-02-12_declaratii-de-presa-sustinute-de-presedintele-romaniei-nicus | 2026-02-12 | video-transcript          |          1098 |              515 |               263 |       0.511 |            66 |
| 2026-02-19_declaratii-de-presa-sustinute-de-presedintele-romaniei-nicus | 2026-02-19 | video-transcript          |          1237 |              565 |               338 |       0.598 |            78 |
| 2026-03-06_declaratii-de-presa-sustinute-de-presedintele-romaniei-nicus | 2026-03-06 | video-transcript          |          1931 |              935 |               481 |       0.514 |            95 |
| 2026-03-11_declaratie-sustinuta-de-presedintele-romaniei-nicusor-dan-du | 2026-03-11 | video-transcript          |           504 |              246 |               159 |       0.646 |            27 |
| 2026-03-19_conferinta-presedintelui-romaniei-nicusor-dan-si-a-secretaru | 2026-03-19 | video-transcript-diarizat |           461 |              194 |               125 |       0.644 |            26 |
| 2026-04-09_conferinta-de-presa-sustinuta-de-presedintele-romaniei-nicus | 2026-04-09 | video-transcript          |          3971 |             1826 |               745 |       0.408 |           246 |
| 2026-04-22_declaratie-de-presa-sustinuta-de-presedintele-romaniei-nicus | 2026-04-22 | video-transcript          |           273 |              130 |                97 |       0.746 |            17 |
| 2026-05-05_declaratii-de-presa-sustinute-de-presedintele-romaniei-nicus | 2026-05-05 | video-transcript          |           234 |              133 |                89 |       0.669 |            23 |
| 2026-05-09_mesajul-presedintelui-romaniei-nicusor-dan-cu-prilejul-zilei | 2026-05-09 | video-transcript          |           719 |              357 |               202 |       0.566 |            42 |

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
| summit    |           4 |
| ăă        |           4 |
| guvern    |           3 |
| lucra     |           3 |
| guvernare |           3 |
| lună      |           3 |
| prim      |           3 |

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

### 2025-07-14 — video-transcript

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |          68 |
| spune         |          35 |
| ăă            |          35 |
| moment        |          29 |
| putea         |          25 |
| românia       |          23 |
| ron           |          23 |
| sine          |          20 |
| măsură        |          19 |
| președinte    |          19 |
| persoană      |          17 |
| dumneavoastră |          16 |
| crede         |          16 |
| întrebare     |          15 |
| an            |          15 |
| om            |          14 |
| lege          |          14 |
| exista        |          14 |
| veni          |          13 |
| față          |          13 |

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


## Top 30 cuvinte — corpus integral

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |         545 |
| vrea          |         534 |
| spune         |         374 |
| putea         |         352 |
| ăă            |         302 |
| românia       |         281 |
| trebui        |         261 |
| moment        |         215 |
| parte         |         208 |
| exista        |         201 |
| an            |         179 |
| lucru         |         176 |
| vedea         |         171 |
| om            |         163 |
| discuție      |         153 |
| sistem        |         151 |
| public        |         148 |
| procuror      |         148 |
| ști           |         146 |
| domn          |         146 |
| președinte    |         145 |
| justiție      |         143 |
| bun           |         141 |
| stat          |         139 |
| întrebare     |         137 |
| crede         |         133 |
| chestiune     |         132 |
| judecător     |         130 |
| dumneavoastră |         129 |
| important     |         111 |

## Stopwords folosite

Listă **stopwordsiso RO** (438 cuvinte) + domain extras (cardinali, câteva auxiliare nestockate).


## Note metodologice

- **Tokenizare + lemmatizare**: spaCy `ro_core_news_sm`. Token-ele sunt reduse la lemma (formă canonică): `românia/româniei/român/români` → `românia`/`român`, `anunț/anunțul` → `anunța`, `săptămânile` → `săptămână`.
- **Stopwords**: `stopwordsiso` (RO) + extensii pentru cardinali și conjuncții scurte.
- **Numerele și punctuația** sunt eliminate; diacriticele cedilă (ş, ţ) sunt normalizate la virgulă-below (ș, ț).
- **TTR** (type-token ratio) e biased de lungime — discursurile scurte au TTR mai mare. Util doar comparativ pe lungimi similare.