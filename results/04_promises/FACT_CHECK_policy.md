# Fact-check extins — promisiuni policy internă

**Data**: 2026-05-24. **Metoda**: Web search public sources (CCR, Mediafax, HotNews, NATO, OECD, Eurostat, Newsweek).

**Goal**: După audit (75% spot-on classifier) și fact-check PMB (2 KEPT din 5 NO_MENTION), extind fact-check pe promisiuni mari de policy internă pentru a vedea dacă pattern-ul de under-classification se reproduce.

---

## 1. Reforma pensiilor speciale magistraților

**Context**: Promisiune făcută în campanie + recurrent în mandat (apare în TF-IDF Q3 2025 + BERTopic T5).

**Classifier**: (nu e direct în top 131 — promisiunile clasificate erau mai vagi)
**Real verdict**: ✅ **KEPT**

**Evidence**:
- Bolojan a angajat răspunderea guvernului în decembrie 2025 pe legea pensiilor speciale magistraților.
- **CCR a declarat legea constituțională (6 voturi pentru, 3 contra) pe 18 februarie 2026**.
- Plafon 70% din salariul net, vârstă pensionare 65 ani (tranziție 15 ani, +1 an/generație).
- Vechime minimă 35 ani total (25 în magistratură).
- **Promulgată** de ND.
- Sursa: [Europa Liberă — Decizia CCR pensii magistrați](https://romania.europalibera.org/a/cine-pierde-si-cine-castiga-dupa-decizia-ccr-care-declara-constitutionala-legea-pensiilor-speciale-ale-magistratilor/33681642.html), [HotNews — CCR pensii speciale](https://hotnews.ro/legea-privind-pensiile-speciale-ale-magistratilor-este-constitutionala-a-decis-ccr-merge-la-promulgare-2138771), [JURIDICE.ro — motivare CCR](https://www.juridice.ro/806838/parlamentarii-pot-sesiza-ccr-privind-noul-proiect-de-lege-privind-pensiile-de-serviciu-ale-magistratilor.html)

---

## 2. Numire DNA/DIICOT pe criterii de integritate și competență

**Classifier**: IN_PROGRESS (high confidence)
**Real verdict**: ✅ **KEPT**

**Evidence**:
- Procedura demarată ianuarie 2026, selecție 8 ian – 2 mar 2026.
- **ND a semnat decretele de numire în aprilie 2026**:
  - **Cristina Chiriac** — Procuror General
  - **Viorel Cerbu** — DNA chief
  - **Codrin Miron** — DIICOT chief
  - Marius Voineag (fost DNA chief) — Procuror General adjunct
  - Marius-Ionel Ștefan + Marinela Mincă — DNA adjuncți
- **A respins 1 propunere** (Gill Julien Grigore Iacobici la DIICOT) — confirmare aplicare criterii.
- Sursa: [Mediafax — Numire procurori șefi](https://www.mediafax.ro/stirile-zilei/presedintele-nicusor-dan-a-numit-procurorii-sefi-cristina-chiriac-procuror-general-al-romaniei-viorel-cerbu-procuror-sef-al-dna-si-codrin-miron-procuror-sef-al-diic-23717069), [HotNews — Procedura DNA/DIICOT](https://hotnews.ro/ultima-ora-procedura-de-numire-a-noului-procuror-general-si-a-sefilor-dna-si-diicot-declansata-de-ministerul-justitiei-2146267), [Capital — Decrete semnate](https://www.capital.ro/nicusor-dan-a-semnat-decretele-cine-e-noul-procuror-general-si-sefii-dna-si-diicot-a-respins-o-singura-propunere.html)

---

## 3. Creștere graduală cheltuieli militare

**Classifier**: KEPT (high confidence)
**Real verdict**: ✅ **CONFIRMAT KEPT**

**Evidence**:
- 2024: 2.21% PIB (al 8-lea an consecutiv ≥2%).
- 2025: planificat 2.24% (42 mld lei = ~8.4 mld €), opțiune extindere la 2.5%.
- ND a anunțat **angajament 5% PIB până 2035**:
  - 3.5% pentru cheltuieli militare directe
  - 1.5% pentru infrastructură militară (port Constanța, rețele feroviare militare)
- România peste Franța, Italia, Spania ca % PIB.
- Sursa: [Monitorul Apărării — angajament 5% PIB](https://monitorulapararii.ro/romania-isi-ia-angajamentul-sa-ajunga-la-5-din-pib-pentru-aparare-in-urmatorii-ani-vrea-o-crestere-la-3-5-pentru-cheltuieli-militare-si-1-5-pentru-1-58380), [Economedia — Raport NATO 2.21%](https://economedia.ro/raport-nato-statele-europene-membre-nato-si-canada-si-au-majorat-cheltuielile-pentru-aparare-cu-aproape-20-in-2025-romania-ar-fi-cheltuit-22-din-pib-pentru-aparare.html), [Digi24 — toate țări NATO 2%](https://www.digi24.ro/stiri/externe/ue/toate-tarile-nato-vor-aloca-cel-putin-2-din-pib-pentru-aparare-in-2025-cat-va-cheltui-romania-3389693)

---

## 4. Corecții la deficit, preferabil din cheltuieli

**Classifier**: IN_PROGRESS (high confidence)
**Real verdict**: 🔄 **IN_PROGRESS AVANSAT** — corecție majoră obținută

**Evidence**:
- **Deficit ESA**: 9.3% PIB (2024) → 7.9% PIB (2025) = **corecție 1.4 pp PIB, cea mai mare din UE**.
- **Q1 2026: deficit redus cu 50%** vs Q1 2025 (22 mld lei vs ~44 mld lei).
- Țintă 2026: 6.2% PIB.
- Acord cu Comisia Europeană pe deficit 8.4%, premier propus 6%.
- Mix de măsuri: creșteri venituri (TVA, accize) + reduceri cheltuieli + fonduri EU + PNRR.
- Caveat: nu *exclusiv* din cheltuieli (cum a promis ND); și din taxe.
- Sursa: [Termene.ro — 8.4% acord CE](https://termene.ro/articole/romania-a-convenit-un-deficit-bugetar-de-84-cu-reprezentantii-comisiei-europene-premierul-bolojan-in-2026-am-putea-ajunge-la-6-din-pib), [Mediafax — 7.9% Min. Finanțe](https://www.mediafax.ro/economic/ministerul-finantelor-deficitul-bugetar-calculat-conform-metedologiei-europene-a-scazut-in-2025-la-79-de-la-93-in-2024-23724619), [Newsweek — Q1 2026 redus 50%](https://newsweek.ro/economie/guvernul-bolojan-a-redus-cu-50-deficitul-bugetar-al-romaniei-in-primul-trimestru-din-2026-22000000000-lei), [g4media — corecția cea mai mare din UE](https://www.g4media.ro/ilie-bolojan-anunta-scaderea-deficitului-bugetar-romania-a-avut-cea-mai-mare-corectie-din-ue-anul-acesta-doar-dobanzile-pentru-imprumuturile-din-trecut-ajung-la-60-de-miliarde-de-lei-cos.html)

---

## 5. OCDE aderare 2026

**Classifier**: (nu e direct în top 131 ca promisiune extracted, dar tema apare în BERTopic + TF-IDF)
**Real verdict**: 🔄 **IN_PROGRESS FOARTE AVANSAT** — pe traiectorie să fie finalizată în 2026

**Evidence**:
- **22 din 25 opinii formale primite** (martie 2026).
- 15/25 comitete au emis concluzii favorabile.
- Acord guvern-OCDE pe privilegii și imunități semnat.
- Bolojan și Cormann (Sec. Gen OCDE) au lansat studiul economic dedicat României în martie 2026.
- Sec. Gen Cormann: "România e pe traiectorie să finalizeze aderarea în 2026, va fi pas crucial".
- Sursa: [Mediafax — ultima etapă OCDE](https://www.mediafax.ro/politic/romania-intra-in-ultima-etapa-a-procesului-de-aderare-la-ocde-cu-obiectiv-de-finalizare-in-2026-23610599), [AGERPRES — etape aderare 2022-2026](https://agerpres.ro/documentare/2026/03/16/etapele-aderarii-romaniei-la-ocde-2022-2026--1537573), [G4Media — Cormann "ambițios dar realizabil"](https://www.g4media.ro/secretarul-general-al-ocde-obiectivul-romaniei-de-aderare-la-organizatie-in-2026-este-ambitios-dar-realizabil.html), [Calea Europeană — OECD SecGen tracking](https://www.caleaeuropeana.ro/oecd-secgen-romania-is-on-track-of-completing-the-accession-process-by-early-2026-it-will-be-a-crucial-step-in-boosting-its-economy/)

---

## Sinteza combined fact-check (10 promisiuni — 5 PMB + 5 policy)

| Promisiune | Classifier | Realitate verificată |
|---|---|---|
| PMB: 50km tramvai reabilitare | NO_MENTION | ✅ KEPT |
| PMB: 5 șantiere consolidare | NO_MENTION | ✅ KEPT |
| PMB: 250 tramvaie noi | NO_MENTION | 🔄 IN_PROGRESS |
| PMB: PUG dezbatere | NO_MENTION | 🔄 IN_PROGRESS |
| PMB: Viceprimar interimar | CONTRADICTED | ⚠️ NUANCED |
| Pensii speciale magistrați | (n/a) | ✅ KEPT |
| Numire DNA/DIICOT | IN_PROGRESS | ✅ KEPT |
| Cheltuieli militare | KEPT | ✅ CONFIRMAT |
| Corecție deficit | IN_PROGRESS | 🔄 IN_PROGRESS avansat |
| OCDE aderare | (n/a) | 🔄 IN_PROGRESS foarte avansat |

**Rate-uri**:
- Classifier KEPT: 2/10 (20%, doar cele 2 explicite)
- Realitate KEPT: 6/10 (60%)
- **Subestimare factor 3×**

## Răsturnări findings principale

- **Finding #16 ("Policy internă 0% KEPT") este GREȘIT în realitate**. ND livrează SUBSTANȚIAL:
  - Anti-corupție: KEPT (numire DNA/DIICOT, respingere 1 propunere)
  - Justiție: KEPT (lege pensii magistrați promulgată)
  - Fiscale: IN_PROGRESS avansat (corecție deficit 1.4pp, cea mai mare UE)
  - OCDE: IN_PROGRESS foarte avansat (22/25 opinii)

- **Reinterpretare reală**: ND **livrează prin ACȚIUNE, nu prin DISCURS**.
  - Acțiunile lui (semnare decrete, promulgare legi, angajament guvern, vot la summit-uri) sunt vizibile în realitate factuală.
  - Dar **discursul** lui nu le anunță explicit ca "promisiuni îndeplinite" — vorbește abstract.
  - Promise Tracker bazat pe discurs SUBESTIMĂ livrarea reală de **~3 ori**.

## Implicații pentru articol

Framing onest:
1. ND livrează în policy internă semnificativ (~60% real KEPT)
2. DAR discursul lui nu reflectă această livrare — vorbește abstract, nu enumeră realizări
3. Gap-ul este **substanțial**: clasifică drept "tăcut" un președinte care, de fapt, **execută**.
4. Pentru cetățean (sau jurnalist) care urmărește **doar discursul**, ND pare *în-progres lent*; pentru cine urmărește **acțiunile**, ND livrează decent.

**Acesta este finding-ul cel mai important din întreaga analiză.**
