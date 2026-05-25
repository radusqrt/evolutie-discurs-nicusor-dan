# Findings so far — analiza discurs Nicușor Dan (Dec 2024 → Mai 2026)

Sumar al concluziilor după Pasul 1 (basic stats + wordclouds) și Pasul 2 (TF-IDF temporal) pe 3 proiecții (overall, scris, vorbit).

Data sumar: 2026-05-24. Corpus: 1062 docs overall (724 scris FB, 338 vorbit video). 272k cuvinte raw / 127k lemmas clean.

---

## 1. Două registre comunicative: scris (FB) vs vorbit (video) — diferențe radicale

Cea mai puternică observație. Top 10 cuvinte pe fiecare proiecție diverg radical:

- **Scris (FB)**: `românia, sine, vrea, european, putea, român, stat, țară, romaniaonesta` → **instituțional / identitar / branding**

- **Vorbit (video)**: `vrea, sine, spune, trebui, putea, moment, om, exista` → **deliberativ / reflexiv / abstract**

**Interpretare**: FB e folosit ca *billboard* (mesaj formalizat), video ca *gândit cu voce tare*. Două registre comunicative în același om.

## 2. Vocabular dominant abstract, nu concret

Top 6 cuvinte overall sunt toate **verbe modale + abstracte**: `vrea (2396), sine (2179), spune (1482), trebui (1252), putea (1197), moment (1002)`.

Nu sunt în top 30: `lege, buget, salariu, pensie, școală, spital, oraș, drum` (substantive de policy concretă).

**Interpretare**: vorbește despre **intenții și posibilități**, nu despre **livrabile**. Stil deliberativ-reflexiv, nu managerial-enumerativ.

## 3. Volum prăbușit post-investitură (drop 3.6×)

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

---

## Pasul 3 (BERTopic) — findings noi

Rulat pe Colab T4 GPU cu `multilingual-e5-large` (fp16) + UMAP 5-dim + HDBSCAN (min_cluster_size=8) + c-TF-IDF.

| Proiecție | Docs | Topice | Outliers | % outliers |
|---|---:|---:|---:|---:|
| overall | 1062 | **26** | 333 | 31% |
| scris (FB) | 724 | **7** | 27 | **4%** |
| vorbit (video) | 338 | **8** | 83 | 25% |

### 6. **FB e ULTRA-disciplinat: 76% într-un singur topic**

Topic 0 din `scris` are **554 din 724 docs** (76%) cu vocabular dominant `românia, romaniaonesta, româniei, trebuie, nicusorpresedinte, europene, nato, european`.

ND folosește FB pentru *un singur macro-mesaj instituțional*, repetat. Discipline mesaj extremă, confirmă brutal finding #1.

### 7. **Vorbit are toate topicele "abstracte": cuvintele modale dominate fiecare cluster**

5 din 8 topice pe vorbit au în top-5 cuvinte: `trebuie, există, cred, momentul, spus`. Verbele modale + reflexive nu dispar nici după ce HDBSCAN forțează separare semantică.

Confirmă: registrul deliberativ-abstract nu e doar agregat — e *în fiecare cluster*.

### 8. **Adversarii politici sunt topice distincte cu framing-uri diferite**

- **T9 (overall)** — Georgescu / **frame dezinformare**: `georgescu, dezinformare, plătit, raport, întâmplat`

- **T16 (overall)** — Georgescu / **frame alegeri**: `cred, alegerile, georgescu, partide, oamenii`

- **T21 (overall)** — Simion: `simion, george simion, femei, georgesimion`

Două frame-uri distincte pentru Georgescu = retorica adaptată în funcție de context (acuzație vs. analiză rezultate).

### 9. **Justiție/CSM e axă constantă, nu doar Q3**

T5 (overall, 36 docs): `csm, magistrați, procuror, justiție, public`. Apare ca topic propriu, peste perioade — nu e doar reformă pensii Q3, ci tematică constantă.

### 10. **Mesajele funerare sunt topic separat (T25, 9 docs)**

Funcție prezidențială ceremonială. Vocabular formal: `familiei, transmit, profundă, victimelor`. Worth note ca categorie distinctă de discurs.

### 11. **Trei brand-uri co-existente, nu doar "România onestă"**

- `romaniaonesta` — campanie (T0+T3+T22, dominant Q2)

- `romaniaputernica` — T13 (post-investitură)

- `nicusorpresedinte` — peste toate

Merită mapare temporală: când a apărut `romaniaputernica`? E înlocuitor de `romaniaonesta`?

### 12. **Topice de policy efective identificate**

Justiție, NATO/apărare, energie/UE, măsuri fiscale, legi promulgate, Ucraina/Rusia, Polonia, R. Moldova, SUA/UE, diaspora/Basarabia. **10 axe substanțiale de discurs** descoperite. Devin scaffolding-ul pentru Promise Tracker (Pasul 4).

### 13. **Artifacts identificate (excluderi pentru viitoare runs)**

- T8 — `live presă declarații` (titluri docs)

- T18 (overall) + T4 (scris) — `cmf, cod material publicitar` (disclosure required FB ads)

Se vor adăuga în stopwords sau filtru pentru runs viitoare.

---

---

## Pasul 4 (Promise Tracker) — findings explosive

**Metoda**: 150 promisiuni extrase cu Gemini 2.5 Flash din corpusul de campanie (≤ 25 mai 2025, 319 docs). Dedup embedding cu paraphrase-multilingual-mpnet → 131 unice. Match vs corpusul mandat (≥ 26 mai 2025, ~540 docs, top-8 paragrafe per promisiune) + clasificare LLM cu taxonomie {KEPT, IN_PROGRESS, REFRAMED, ABANDONED, CONTRADICTED, NO_MENTION}.

**Status global**:

| Status | Count | % |
|---|---:|---:|
| ✅ KEPT | 26 | **20%** |
| 🔄 IN_PROGRESS | 77 | **59%** |
| ⚠️ CONTRADICTED | 1 | 0.8% |
| ❓ NO_MENTION | 27 | 21% |
| ABANDONED | 0 | 0% |
| REFRAMED | 0 | 0% |

### 14. **20% KEPT după 1 an de mandat — rată modestă, dar zero promisiuni rupte explicit**

Doar 1 contradicție vizibilă (vice-primar interimar București nepromis) și **zero promisiuni abandonate sau redefinite**. ND nu rupe vizibil promisiuni — fie le ține (20%), fie le tace (21%), fie le tot menționează fără finalizare (59%).

### 15. **București/local: pierdere completă de focus (4% KEPT, 67% NO_MENTION)**

Din 27 promisiuni făcute ca primar/candidat pentru București, **18 (67%) n-au mai fost menționate** după investitură. Plus 1 contradicție explicită (vice-primar interimar promis, dar a felicitat Ciucu ca primar ales).

ND a "abandonat narativ" rolul de primar.

### 16. **Politica internă: ZERO promisiuni clar îndeplinite**

Pe domenii de policy internă — **sănătate, educație, măsuri fiscale, diaspora, anti-corupție, R. Moldova** — *toate* au rată **0% KEPT**. Toate cele 30+ promisiuni din aceste zone sunt **IN_PROGRESS** (vorbite, nu livrate) sau **NO_MENTION**.

### 17. **Diplomația = singurul domeniu de livrare reală**

- **Diplomație: 60% KEPT, 0% NO_MENTION** — cel mai înalt rate de livrare
- **Ucraina/Rusia: 67% KEPT** (2 din 3)
- **NATO/apărare: 29% KEPT** (2 din 7)
- **Justiție electorală: 41% KEPT** (dar parțial auto-fulfilling — "voi candida independent")

**ND livrează vizibil în zona externă. Politica internă e in-progress sau tăcută.**

### 18. **Top contradicție explicită**

- Promisiune (20 mai 2025): "*Imediat ce mă voi instala la Cotroceni, unul dintre viceprimari va deveni primar interimar al Capitalei.*"
- Realitate post-investitură: ND a felicitat Ciprian Ciucu ca primar ales, fără numire de interimar. **Promisiune rupta în prima săptămână.**

### 19. **Calitate clasificator: validată prin audit dublu (32 sample-uri)**

Audit-uri manuale stratificate (5 per status × 2 seed-uri: 42 + 1337):

| Verdict audit | Count | % |
|---|---:|---:|
| ✅ Corect | 24 | **75%** |
| ⚠️ Debatable | 5 | 16% |
| ❌ Greșit | 3 | 9% |

**Eroare sistematică**: toate cele 3 "greșit" sunt **promisiuni pre-mandate fulfilled** în topic-ul *justiție electorală* (ex: "Voi candida independent", "Voi informa partidele", "Voi face apel forțe pro-occidentale în turul 2"). Clasificatorul caută evidence în corpus mandat (≥ 26 mai 2025), unde promisiuni îndeplinite *înainte* nu mai sunt menționate → fals NO_MENTION/IN_PROGRESS.

**Impact pe findings**:
- Justiție electorală: 41% KEPT corectat → estimat ~75% KEPT
- Overall: 20% KEPT corectat → estimat ~25-27% KEPT
- **Findings principale rămân**: 4% pe București/local, 0% pe policy internă, 60% pe diplomație. Eroarea metodologică e izolată la topic-ul electoral și nu schimbă concluziile narative.

Audit-urile complete: `results/04_promises/AUDIT_seed42.md`, `AUDIT_seed1337.md`.

### 20. **BLIND SPOT METODOLOGIC: clasificator "ND-centric"**

Fact-check independent (web search, mai 2026) pe 5 promisiuni București/local etichetate NO_MENTION/CONTRADICTED:

| Promisiune | Classifier | Realitate verificată | Real verdict |
|---|---|---|---|
| Vigheciu (PSD) primar interimar | CONTRADICTED | Bujduveanu (PNL) instalat (ND însuși a propus PNL) | ⚠️ Persoana schimbată, spiritul respectat |
| 250 tramvaie noi PMB | NO_MENTION | Documentație gata, fonduri 2025, 63 buc primă fază | 🔄 IN_PROGRESS (PMB) |
| PUG dezbatere publică | NO_MENTION | 25 studii publicate, ~40 instituții avizare | 🔄 IN_PROGRESS (PMB) |
| 50km reabilitare linii tramvai | NO_MENTION | **16/16 loturi atribuite, contracte semnate, ~475M€** | ✅ KEPT (PMB sub Bujduveanu/Ciucu) |
| 5 șantiere consolidare clădiri | NO_MENTION | **AMCCRS are 8 șantiere active** (depășește promisiunea) | ✅ KEPT (PMB) |

**Implicație critică**: classifier-ul măsoară *ce vorbește ND*, nu *ce se întâmplă în lume*. 2 din 5 promisiuni NO_MENTION sunt de fapt **KEPT în realitate** — doar că au fost executate sub succesorii săi (Bujduveanu, Ciucu) iar ND nu mai e narrator.

**Reinterpretare finding #15 (București 4% KEPT, 67% NO_MENTION)**: NU înseamnă "promisiuni abandonate" — înseamnă "ND a încetat să fie *narator* al lor". Proiectele continuă sub PMB. Asta e diferență substanțială.

Findings ne-PMB (policy internă 0% KEPT, diplomație 60% KEPT) NU sunt afectate de acest blind spot — pe acelea ND e *singurul actor relevant*.

### 21. **Pattern documentat: ND livrează acțiuni pe care nu le menționează explicit**

Fact-check pe **10 promisiuni selectate pentru vizibilitate** (5 PMB local + 5 policy internă mari): pensii speciale magistrați, DNA/DIICOT, cheltuieli militare, deficit, OCDE, 50km tramvai, 8 șantiere consolidare, etc. Sursă: CCR, MAE, Eurostat, NATO, OECD + media (Digi24, HotNews, Profit, Recorder).

| Promisiune | Classifier (ce spune ND) | Realitate (ce s-a executat) |
|---|---|---|
| Pensii speciale magistrați | (n/a în top 131) | ✅ KEPT — lege CCR-validată 6-3 (feb 2026), promulgată |
| Numire DNA/DIICOT integritate | IN_PROGRESS | ✅ KEPT — decrete semnate apr 2026, 1 respins |
| Cheltuieli militare graduale | KEPT | ✅ CONFIRMAT — 2.24% PIB 2025, angajament 5% până 2035 |
| Corecție deficit din cheltuieli | IN_PROGRESS | 🔄 IN_PROGRESS avansat — 9.3%→7.9% (cea mai mare corecție UE) |
| OCDE aderare 2026 | (n/a în top 131) | 🔄 IN_PROGRESS foarte avansat — 22/25 opinii |

**Combined (10 promisiuni)**: 6 KEPT real / 3 IN_PROGRESS / 1 contradicție nuanțată.

⚠️ **Cele 10 NU sunt eșantion random**. Au fost alese tocmai pentru vizibilitate (proiecte PMB executate de succesori + policy mari verificabile public). Pe acest eșantion, da, vedem livrare reală mai mare decât transpare în discurs. **Dar nu putem extrapola "60% real vs 20% classifier" pe toate 131 fără verificare sistematică.**

**Ce putem afirma cu încredere**:

- **Pattern documentat**: pe cazuri verificate independent, ND a executat concret (decrete, legi, contracte) chiar dacă clasificatorul ND-centric (care vede doar discursul) le-a marcat NO_MENTION/IN_PROGRESS.
- **Reformulare finding #16 ("Policy internă 0% KEPT")**: clasificatorul subestimează livrarea concretă pentru *acest tip de promisiuni* — măsoară discursul, nu acțiunile. Anti-corupție, justiție, fiscale, OCDE au fost executate, dar ND nu se laudă explicit cu realizările.
- **Concluzia narativă onestă**: *ND tinde să vorbească mai mult despre intenții decât despre realizările sale concrete*. Pentru a cuantifica gap-ul, ar fi nevoie de verificare sistematică pe eșantion random din cele 131.

Surse fact-check: `results/04_promises/FACT_CHECK_realworld.md` + `FACT_CHECK_policy.md`.

---

## Pasul 5-9 — analize SotA suplimentare

### 22. **Discourse complexity confirmă scris vs vorbit divergence (Pasul 5)**

Pe spaCy parser: sentence length, dependency tree depth, MTLD, TTR, function ratio.

- **Scris (FB)**: cuvinte 5.5-6.3 chars, function ratio 0.36-0.44, **MTLD growing 34 → 87 post-investitură**
- **Vorbit (video)**: cuvinte 4.5-4.7 chars, function ratio 0.52-0.56, MTLD stabil 42-54

FB **își diversifică lexicon-ul dramatic post-investitură** (MTLD 2.5× growth), video rămâne stabil. Schimbarea bruscă coincide cu schimbarea rolului (candidat → președinte) — *consistentă cu* o schimbare de proces de producție FB, dar cauza exactă rămâne neclară.

### 23. **Ezitare / nuanțare în limbaj — diferență 4-5× FB vs video (Pasul 6)**

Lexicon custom RO: 35+ markeri nuanțare/ezitare ("cred că", "probabil", "mi se pare"), 24 markeri certitudine ("evident", "sigur", "categoric"), 19 markeri personali ("eu", "mie", "personal"). În literatura de specialitate, asta se numește "hedging".

| Proiecție | Hedge:Cert ratio | Personal/1000w |
|---|---:|---:|
| **Scris (FB)** | **0.13-0.23** (ULTRA categoric) | 0.7-3.3 |
| **Vorbit (video)** | **0.51-1.06** (deliberativ) | 5.3-9.5 |

**4-5× diferență** între cele 2 registere pe nuanțare lingvistică și pronume personale. FB e scris în registru "instituțional formalizat", video e ND vorbind spontan.

**Evoluție temporală overall**: Q2 campanie = cel mai categoric (0.27), Q1 2026 reformă judiciară = revenire la deliberativ (0.66). ND e **categoric când vinde mesaj** și **deliberativ când are putere și complexitate**.

### 24. **Semantic drift confirmă schimbări majore de framing (Pasul 7)**

Centroid embedding per (topic × perioadă), cosine drift vs prima perioadă cu ≥3 docs.

**Top drifts overall**:
- T0 brand `nicusorpresedinte/romaniaonesta`: **0.37** — major brand-evolution
- T9 `Georgescu campania`: **0.32** — frame schimbat (electoral → dezinformare)
- T5 `JUSTIȚIE/csm`: **0.30** — framing al justiției substanțial mutat
- T3 alt brand `romaniaonesta`: 0.04 — STABIL

**Vorbit drifts mai mari decât scris** (justiție 0.23 vs scris 0.18) — confirmă din nou că video e dinamic, FB e static repetitiv.

### 25. **Entity timeline — adversari electorali dispar, geopolitica explodează (Pasul 8)**

GLiNER multi-v2.1 zero-shot NER (3,755 mențiuni extrase, curățate la ~700 cu top 30 entități canonice).

| Entitate | Q1 2025 | Q2 2025 | Q4 2025 | Q2 2026 |
|---|---:|---:|---:|---:|
| ROMÂNIA | 114 | **515** | 280 | 333 |
| UCRAINA | 2 | 12 | 41 | **85** |
| SUA | 2 | 20 | 11 | 29 |
| (Q1 2026 SUA spike) | — | — | — | **97** |
| RUSIA | 3 | 9 | **68** | 14 |
| NATO | 8 | 16 | **33** | **50** |
| POLONIA | 0 | 8 | 3 | **47** |
| GEORGESCU | **21** | 18 | 8 | 1 |
| SIMION | 1 | **31** | 0 | 0 |
| CIOLACU / BOLOJAN | — | — | — | **17 / 14 total** |

**Findings**:

- **Georgescu / Simion DISPAR complet** după Q2 2025 (1, 0 mențiuni Q2 2026 vs 21, 31 peak)
- **Colegii de guvernare sub-menționați**: Ciolacu 17 total, Bolojan doar 14 — *premierul actual abia apare în discurs*
- **SUA Q1 2026 spike (97)** — relația cu administrația Trump
- **Polonia Q2 2026 explozie (47)** — vizita oficială
- **CSM Q3 2025 (32)** — reforma pensii magistrați
- **Rusia peak Q4 2025 (68)** — cea mai îngrijorată perioadă

### 26. **Sentiment per entitate — ND nu atacă deschis, dar TRUMP e MIXT (Pasul 9)**

Gemini 2.5 Flash sentiment classification pe 107 buckets (entitate × perioadă cu ≥3 mențiuni).

**Distribuție** (după retry pentru bug-uri de parsing JSON): 47% pozitiv, 35% mixt, 14% negativ, 5% neutru — **doar 14% buckets explicit negative**.

**Trajectories cheie**:

| Entitate | Pattern | Interpretare |
|---|---|---|
| NATO, POLONIA, OCDE, FRANȚA | pozi × 4 | Aliat necontestat |
| RUSIA | nega × 2 | Singur negativ constant |
| CSM | **mixt × 3** | Reformă complicată, fără condamnare |
| **TRUMP** | **MIXT × 2** | **NU îl laudă, are rezerve** |
| GERMANIA | mixt → pozi | Îmbunătățire |
| USR | pozi → neutru | Răcire post-investitură |
| GUVERN | nega → mixt | Schimbare odată cu Bolojan |

**Insighturi devastatoare**:

- **Doar 5 sentimente NEGATIVE** în tot corpus-ul — ND e **diplomat, non-confrontational**.
- **TRUMP = MIXT, nu pozitiv** — surprinzător; ND are rezerve față de Trump.
- **USR a trecut pozitiv → neutru** — răcire față de partidul de origine după ce a devenit independent.
- **Georgescu/Simion = N/A constant** — mențiuni superficiale fără sentiment polarizat → **i-a IGNORAT** explicit.

### 27. **Sentiment scris vs vorbit — FB e POLARIZAT, video e NUANȚAT (extensie Pasul 9 pe scris + vorbit)**

Pasul 9 rulat și pe scris + vorbit separat (overall: 107 buckets; scris: 52; vorbit: 100). Distribuții comparative:

| Sentiment | Scris (FB) | Vorbit (video) |
|---|---:|---:|
| pozitiv | **56%** | 43% |
| negativ | **13%** | 12% |
| mixt | 2% | **38%** |
| neutru | 0% | 7% |
| n/a (mențiuni superficiale) | 29% | 0% |

**FB are 69% sentiment polarizat (pozitiv+negativ) — video are 55% polarizat, restul 38% mixt + 7% neutru.** FB e mai categoric, video e mai nuanțat.

**Entități cu sentiment DIFERIT scris vs vorbit ÎN ACEEAȘI PERIOADĂ**:

| Entitate | Perioadă | Scris | Vorbit | Interpretare |
|---|---|---|---|---|
| TRUMP | Q1 2026 | POZITIV | **MIXT** | FB îl prezintă pozitiv pentru diplomația oficială; video are rezerve |
| PSD | Q2 2025 (campanie) | NEGATIV | MIXT | FB atacă explicit; video tempereazăa cu recunoașterea necesității |
| SIMION | Q2 2025 (campanie) | **NEGATIV** (atac direct: "ipocrizie", "lașitate", "manipulare") | **NEGATIV** (haos economic, cultura urii) | Ambele canale = negativ; pe FB cu epitete personale, în video cu argumente policy |

**Notă PSD**: pe FB apare DOAR în Q2 2025 (campanie). Post-electoral dispare complet de pe FB. Pe video are trajectory completă: campanie NEGATIV → formare guvern NEUTRU → coaliție MIXT → criza Pfizer Q2 2026 **NEGATIV** din nou.

**Sub-finding pentru diferențele de registru**: FB = instrument de polarizare clară (pro/contra explicit); video = instrument de nuanță și echivoc. ND în video e mai prudent; pe FB apare un registru categoric. Această diferență poate veni din mai multe surse (vezi secțiunea "Convergent evidence" mai jos cu cele 4 ipoteze plauzibile).

---

### 28. **Raportul ND-Bolojan: de la "uitat de el" la TENSIONAT pe Pfizer (Pasul 10)**

Pasul 10 (`scripts/10_nd_bolojan_relation.py`): extract toate mențiunile Bolojan + "premier/prim-ministru" din corpus ND, clasifică ton relațional per perioadă cu Gemini, plus fact-check web.

**Sumar mențiuni**: 86 spans Bolojan/premier vs 22 Ciolacu (4× mai des) — dar premier Bolojan **sub-menționat raportat la rolul instituțional**.

**Evoluție ton relațional**:

| Perioadă | Ton | Note |
|---|---|---|
| Q1 2025 | **distant** | "Am uitat de el" — neîncredere precampanie |
| Q2 2025 | mixt | Acceptă dezbatere Cotroceni, "persoană foarte serioasă" |
| Q3 2025 | **colaborativ** ← peak | Îl desemnează: "cel mai potrivit", "partener" |
| Q4 2025 | mixt | "Premierul executiv într-o coaliție" + apăra principialitatea |
| Q1 2026 | colaborativ/deferent | "Nu există altă alternativă" |
| **Q2 2026** | **TENSIONAT** ⚠️ | Cazul Pfizer — cere transparență publică |

**Q2 2026 — prima fisură publică (cazul Pfizer 600M€)**:

- 1 apr 2026: Tribunal Bruxelles condamnă RO la **>600 milioane € către Pfizer** pentru vaccinuri COVID 2021 neutilizate.
- 8 apr 2026: ND cere public desecretizarea: *"I-am cerut premierului acest lucru... Tot ce s-a semnat de către oficiali ai statului român să fie făcut public."*
- Bolojan **NU desecretizează direct** — negociază privat eșalonarea + transformarea datoriei în alte produse medicale; dă vina pe *"greaua moștenire"* (guv. Cîțu 2021, Alexandru Nazare avizase achiziția).
- ND folosește presiunea publică; Bolojan preferă negocierea privată. **Aliniați pe diagnostic, divergenți pe răspuns**.

**Verdict**: prima divergență publică vizibilă între președinte și premier — confirmată atât de corpus (Gemini Q2 2026 = "tensionat") cât și de surse media (Recorder: *"coaliția, cu un picior în groapă"*).

**Fact-check complet pe toate 6 perioade** (`results/10_nd_bolojan/FACT_CHECK.md`):
- Q1 2025: distant ✅ (Bolojan = preș. interimar din 12 feb după demisia Iohannis)
- Q2 2025: mixt ✅ (Bolojan a anunțat că votează ND în turul 2, primire la Cotroceni 15 mai)
- Q3 2025: colaborativ ⚠️ (Gemini a RATAT dezacordul TVA dintre ND și Bolojan în negocieri; Bolojan a câștigat)
- Q4 2025: mixt ✅ (scandal Fănel Bogoș — afacerist plătit 1.5M€ acces la birou Bolojan; ND a apărat indirect prin "limita de principialitate")
- Q1 2026: colaborativ/deferent ✅ (PNRR 231M€ + EastInvest 20mld €, vizita Bruxelles)
- Q2 2026: tensionat ✅ (Pfizer 600M€, ND cere transparență publică)

**Calitate clasificare Gemini**: 5/6 perioade complet confirmate + 1 cu nuanță ratată (TVA Q3). **~83% spot-on**, 100% direcțional.

**Arc narativ real**: distanță → primă întâlnire → desemnare (cu friction pe TVA) → apărare nuanțată în scandal Bogoș → coordonare EU → prima fisură publică (Pfizer). **ND-Bolojan = aliat tactic, niciodată prieten** — stil formal-instituțional consistent.

---

## Convergent evidence — diferențe cantitative scris vs vorbit (4 metrici independente)

Din Pasul 1-9, am acumulat **4 metrici convergente** care arată că FB-ul și video-ul lui Nicușor Dan au registre comunicative **radical diferite**:

1. **Ezitare / nuanțare în limbaj (Pasul 6)**: FB ezitare:certitudine ratio = 0.13-0.23 vs video 0.51-1.06 = **4-5× diferență**
2. **Discourse complexity (Pasul 5)**: FB MTLD growth 34→87 post-investitură, video MTLD stabil 42-54
3. **Sentiment polarization (Pasul 9)**: FB 69% polarizat pro/contra, video 55% polarizat + 38% mixt (mai nuanțat)
4. **BERTopic (Pasul 3)**: FB are 76% într-un singur mega-topic instituțional; video are 8 topice + 25% outliers

**Diferențele sunt reale și consistente. Cauza lor este însă o întrebare separată, la care datele actuale nu pot răspunde univoc.**

### Ipoteze plauzibile (nu putem distinge între ele)

a. **Diferențe naturale de gen comunicativ** — orice persoană scrie diferit de cum vorbește. Universal.
b. **Constraint-uri de medium** — FB e editabil/scurt; video e spontan/lung. Diferit de natură.
c. **Audiență diferită** — FB pentru susținători/public; video pentru jurnaliști/critici. Stiluri adaptate la audiență.
d. **Colaborare cu echipă PR pentru FB** — postările sunt redactate sau adaptate de un team de comunicare. Compatibilă cu datele observate.

### Ce ar fi nevoie să distingă

- **Stylometry formală** (Burrows' Delta + PCA pe function words) — **EFECTUATĂ** în Pasul 11 (vezi finding #29).
- **Baseline politic comparativ** — Iohannis, Băsescu, Macron prezintă același pattern? Dacă da, e pattern instituție, nu unic pentru ND.

**Concluzia onestă**: diferențele cantitative dintre cele 2 registre sunt mari și documentate. Interpretarea cauzei (ghostwriting vs adaptare naturală) rămâne deschisă.

---

Fact-check extins pe 5 promisiuni policy internă suplimentare (deficit, OCDE, pensii speciale magistrați, DNA/DIICOT, cheltuieli militare) confirmat prin surse oficiale (CCR, MAE, Eurostat, NATO, OECD):

| Promisiune | Classifier | Realitate verificată |
|---|---|---|
| Pensii speciale magistrați | (n/a în top 131) | ✅ KEPT — lege CCR-validată 6-3 (feb 2026), promulgată |
| Numire DNA/DIICOT integritate | IN_PROGRESS | ✅ KEPT — decrete semnate apr 2026, 1 respins |
| Cheltuieli militare graduale | KEPT | ✅ CONFIRMAT — 2.24% PIB 2025, angajament 5% până 2035 |
| Corecție deficit din cheltuieli | IN_PROGRESS | 🔄 IN_PROGRESS avansat — 9.3%→7.9% (cea mai mare corecție din UE) |
| OCDE aderare 2026 | (n/a în top 131) | 🔄 IN_PROGRESS foarte avansat — 22/25 opinii, 15/25 comitete favorabile |

**Combined (10 promisiuni selectate, NU random)**: 6 KEPT real / 3 IN_PROGRESS avansat / 1 contradicție nuanțată.

Pe acest eșantion ne-random observăm un pattern clar — livrare concretă mai mare decât transpare în discurs. **Nu putem extrapola rata exactă pe toate 131 fără verificare sistematică pe eșantion random**.

**Reformulare finding #16 ("Policy internă 0% KEPT")**: clasificatorul ND-centric subestimează livrarea concretă pentru *acest tip de promisiuni* (anti-corupție, justiție, fiscale, OCDE — executate prin decrete/legi/numiri) fiindcă măsoară doar ce *spune* ND, nu ce *face* guvernul. ND tinde să **vorbească mai mult despre intenții decât despre realizările sale concrete**.

Surse fact-check: `results/04_promises/FACT_CHECK_realworld.md` + `FACT_CHECK_policy.md`.

---

### 29. **Stylometry formală: cele 2 registre confirmate stilometric distinct (Pasul 11)**

**Setup**: 718 documente (≥50 cuvinte), top 100 function words (POS: ADP/AUX/CCONJ/DET/PART/PRON/SCONJ), frecvențe relative z-normalizate. Aplicat: Burrows' Delta, PCA 2D, Random Forest classifier.

**Rezultate**:

| Metoda | Rezultat |
|---|---|
| Burrows' Delta — distanță centroidă scris↔vorbit | 0.297 |
| Burrows' Delta — nearest-centroid accuracy | **78.1%** (vs ~50% random) |
| Random Forest — 5-fold CV accuracy | **92.1% ± 1.7%** |
| Held-out 30% test | 94.9% (116/118 FB + 89/98 video corect) |

**Concluzie principală**: cele 2 registre **sunt clar distincte stilometric**. Un model simplu distinge FB de video cu **92% acuratețe doar din 100 function words** (cuvinte ca *de, și, în, să, fi*).

**Top features discriminative** — diferențe dramatice:

- `niște` 259× mai des în video (indefinit colocvial)
- `o` 56× mai des în video
- `ăă` 41× mai des în video (filler ezitare)
- `într` 28× mai des în video
- `deci` 26× mai des în video (conector argumentativ oral)
- `acesta` 4.9× mai des în video (deictic)

**Veste mai nuanțată**: features care discriminează sunt **markeri clasici ai vorbirii spontane** (fillere, deictice, conectori orali, indefinite colocviale). Adică **majoritatea separabilității vine din diferența naturală oral-vs-scris formal**, NU dintr-o "altă voce" producând FB.

**Stilometria singură NU poate distinge**:
- a) ND adaptează natural stilul la medium
- b) Echipă PR scrie FB cu adăugire în stil formal
- c) Combinație

**Pentru a tranșa** ar fi nevoie de **baseline politic comparativ** (Iohannis FB vs video, Băsescu, Macron). Dacă pattern-ul similar apare la alți politici → e natural. Dacă e dramatic mai mare la ND → e specific (posibil ghostwriting).

---

## Verificări de calitate (post-projection)

- **Dedup secundar pe ND-only**: verificat cu `scripts/check_nd_dup.py` — doar **4 perechi** cu Jaccard ≥ 0.85 din 835 docs substantive (≥20 token-uri unice). Toate sunt aceeași declarație publicată în 2 zile consecutive (conferința 2025-07-30/31, declarația Ucraina 2026-01-06/07, vizita Polonia 2026-03-05/06). Impact negligibil (0.5%), **nu se aplică al doilea dedup**.

## Întrebări deschise (drive next steps)

- Care e *agenda lui coerentă* peste timp (nu doar lemme distinctive)? → **BERTopic** (Pasul 3).

- Promisiunile de campanie au fost ținute / abandonate / reframuite? → **Promise Tracker** (Pasul 4).

- Cum se compară `sine` + `vrea` cu Iohannis/Băsescu? E tic personal sau pattern politic RO? → baseline comparativ.

- Cine apare în discursul lui și cum se schimbă rolul? → **NER + entity timeline**.

- De ce pivot brusc pe magistrați/pensii Q3 2025? → reporting jurnalistic.
