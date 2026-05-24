# Pasul 8 — NER + Entity timeline (vorbit)

**Model**: GLiNER multi-v2.1 (zero-shot multilingv, threshold 0.45)
**Labels**: persoană politică, țară, instituție națională, instituție internațională, partid politic
**Docs procesate**: 335 | **Mentions extrase**: 2177
**Entități canonice unice**: 573

## Top 30 entități (by mention count)

| canonical              | label                     |   count |
|:-----------------------|:--------------------------|--------:|
| românia                | țară                      |     939 |
| româniei               | țară                      |     220 |
| ucraina                | țară                      |     135 |
| sua                    | țară                      |     115 |
| csm                    | instituție națională      |      84 |
| ue                     | instituție internațională |      83 |
| nato                   | instituție internațională |      81 |
| rusia                  | țară                      |      70 |
| președintele           | persoană politică         |      65 |
| psd                    | partid politic            |      62 |
| r. moldova             | țară                      |      62 |
| parlament              | instituție națională      |      53 |
| georgescu              | persoană politică         |      47 |
| curtea constituțională | instituție națională      |      39 |
| polonia                | țară                      |      39 |
| statul român           | instituție națională      |      37 |
| președinte             | persoană politică         |      34 |
| ucrainei               | țară                      |      33 |
| republicii moldova     | țară                      |      33 |
| uniunii europene       | instituție internațională |      32 |
| rusiei                 | țară                      |      31 |
| pnrr                   | partid politic            |      30 |
| președintelui          | persoană politică         |      30 |
| guvernul               | instituție națională      |      30 |
| usr                    | partid politic            |      26 |
| moldova                | țară                      |      25 |
| csat                   | instituție națională      |      24 |
| franța                 | țară                      |      24 |
| statelor unite         | țară                      |      24 |
| pnl                    | partid politic            |      24 |

## Entity timeline (top 25, count per perioadă)

| canonical              |   2024Q4-2025Q1 candidatură-precampanie |   2025Q2 campanie + investitură |   2025Q3 deficit + reforma economică |   2025Q4 stabilizare + diplomație |   2025Q4-2026Q1 reformă judiciară |   2026Q2 cotitură UE + criză guvern |
|:-----------------------|----------------------------------------:|--------------------------------:|-------------------------------------:|----------------------------------:|----------------------------------:|------------------------------------:|
| românia                |                                      80 |                             233 |                                  126 |                               133 |                               184 |                                 183 |
| româniei               |                                      15 |                              58 |                                   34 |                                31 |                                38 |                                  44 |
| ucraina                |                                       1 |                               8 |                                   21 |                                32 |                                29 |                                  44 |
| sua                    |                                       2 |                              10 |                                   13 |                                10 |                                65 |                                  16 |
| ue                     |                                       7 |                              12 |                                   20 |                                 4 |                                27 |                                  16 |
| csm                    |                                       2 |                               0 |                                   31 |                                 6 |                                23 |                                  22 |
| nato                   |                                       8 |                               9 |                                   12 |                                22 |                                 2 |                                  30 |
| rusia                  |                                       1 |                               1 |                                   13 |                                41 |                                 7 |                                   7 |
| președintele           |                                      12 |                               8 |                                   21 |                                 1 |                                11 |                                  12 |
| r. moldova             |                                       0 |                              25 |                                   28 |                                 5 |                                 2 |                                   2 |
| psd                    |                                       2 |                              24 |                                    5 |                                 7 |                                 5 |                                  19 |
| parlament              |                                      12 |                              14 |                                    7 |                                 5 |                                 7 |                                   9 |
| statul român           |                                       2 |                              12 |                                   16 |                                14 |                                 6 |                                   3 |
| georgescu              |                                      21 |                              15 |                                    2 |                                 8 |                                 0 |                                   1 |
| curtea constituțională |                                       5 |                              10 |                                   11 |                                12 |                                 2 |                                   1 |
| polonia                |                                       0 |                               3 |                                    6 |                                 2 |                                 2 |                                  26 |
| președinte             |                                       8 |                               9 |                                    2 |                                 4 |                                 6 |                                   5 |
| ucrainei               |                                       0 |                               1 |                                    4 |                                 4 |                                 5 |                                  19 |
| pnrr                   |                                       0 |                               3 |                                    3 |                                 3 |                                 4 |                                  20 |
| uniunii europene       |                                       0 |                               6 |                                    2 |                                10 |                                 9 |                                   6 |
| republicii moldova     |                                       0 |                               5 |                                   22 |                                 2 |                                 3 |                                   1 |
| rusiei                 |                                       1 |                               0 |                                    8 |                                17 |                                 5 |                                   0 |
| guvernul               |                                       3 |                               9 |                                    7 |                                 2 |                                 6 |                                   3 |
| președintelui          |                                       9 |                               5 |                                    8 |                                 3 |                                 4 |                                   1 |
| usr                    |                                       4 |                              11 |                                    3 |                                 2 |                                 4 |                                   2 |