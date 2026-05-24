# Findings so far — analiza discurs Nicușor Dan (Dec 2024 → Mai 2026)

Sumar al concluziilor după Pasul 1 (basic stats + wordclouds) și Pasul 2 (TF-IDF temporal) pe 3 proiecții (overall, scris, vorbit).

Data sumar: 2026-05-24. Corpus: 1062 docs overall (724 scris FB, 338 vorbit video). 272k cuvinte raw / 127k lemmas clean.

---

## 1. Doi Nicușor Dan: registru scris vs vorbit complet diferit

Cea mai puternică observație. Top 10 cuvinte pe fiecare proiecție diverg radical:

- **Scris (FB)**: `românia, sine, vrea, european, putea, român, stat, țară, romaniaonesta` → **instituțional / identitar / branding**

- **Vorbit (video)**: `vrea, sine, spune, trebui, putea, moment, om, exista` → **deliberativ / reflexiv / abstract**

**Interpretare**: FB e folosit ca *billboard* (mesaj formalizat), video ca *gândit cu voce tare*. Două registre comunicative în același om.

## 2. Vocabular dominant abstract, nu concret

Top 6 cuvinte overall sunt toate **verbe modale + abstracte**: `vrea (2396), sine (2179), spune (1482), trebui (1252), putea (1197), moment (1002)`.

Nu sunt în top 30: `lege, buget, salariu, pensie, școală, spital, oraș, drum` (substantive de policy concretă).

**Interpretare**: vorbește despre **intenții și posibilități**, nu despre **livrabile**. Stil deliberativ-reflexiv, nu managerial-enumerativ.

## 3. Volum prăbușit post-mandat (drop 3.6×)

| Perioadă | Docs |
|---|---:|
| Q2 2025 (campanie + investitură) | 468 |
| Q3 2025 (deficit) | 96 |
| Q4 2025 | 136 |
| Q4-Q1 2026 | 157 |
| Q2 2026 | 150 |

Media trimestrială post-investitură: ~130 docs vs 468 ca candidat. **Comunică radical mai puțin de când e președinte.**

## 4. Pivot tematic abrupt de la trimestru la trimestru

TF-IDF lemmas distinctive per perioadă:

- **Q1 2025** (precampanie): `anula, sondaj, parchet, onest, candidatură, ciolacu` → anti-PSD + alegerea anulată

- **Q2 2025** (campanie): `romaniaonesta, schimbare, simion, capitală` → brand + adversar

- **Q3 2025** (deficit): `pensionară, magistrat, pensie, csm, evaziune` → **pivot brusc spre justiție + pensii speciale**

- **Q4 2025** (stabilizare): `apărare, militar` → geopolitică

Nu este *un* președinte — sunt 3-4 segmente narative distincte.

## 5. Brand-shedding "România onestă"

- Q2 2025: `romaniaonesta` = TF-IDF 0.596 (top-1 distinctive lemma)

- Q3 2025 încoace: **dispare complet din top 25 per perioadă**

**Interpretare**: brand-shedding clasic. Slogan-ul a fost electoral, nu guvernamental.

---

## Concluzii presentable

1. **Articol / longform**: "Doi Nicușor Dan: ce arată 1062 de discursuri analizate algoritmic" — combină findings #1, #3, #5.

2. **Thread X**: 5-7 vizuale cu hook scris-vs-vorbit + drop-ul de volum.

3. **Open data release**: corpus + scripts pe GitHub ca infrastructură pentru jurnaliști.

## Întrebări deschise (drive next steps)

- Care e *agenda lui coerentă* peste timp (nu doar lemme distinctive)? → **BERTopic** (Pasul 3).

- Promisiunile de campanie au fost ținute / abandonate / reframuite? → **Promise Tracker** (Pasul 4).

- Cum se compară `sine` + `vrea` cu Iohannis/Băsescu? E tic personal sau pattern politic RO? → baseline comparativ.

- Cine apare în discursul lui și cum se schimbă rolul? → **NER + entity timeline**.

- De ce pivot brusc pe magistrați/pensii Q3 2025? → reporting jurnalistic.
