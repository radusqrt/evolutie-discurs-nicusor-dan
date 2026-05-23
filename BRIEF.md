# Evoluția discursului — Nicușor Dan

## Subiect

**Nicușor Dan**, matematician, fondator Salvați Bucureștiul (2007) și USR (2016), primar general al Bucureștiului (2020–2025), Președinte al României din **26 mai 2025**.

Momente-cheie de raportare în analiză:

- **16 decembrie 2024** — anunțul candidaturii independente la prezidențiale (după anularea alegerilor din nov. 2024)
- **18 mai 2025** — câștigă turul al doilea împotriva lui George Simion (~53,6%)
- **26 mai 2025** — depunere jurământ, preluare mandat
- **23 mai 2026** — astăzi (~1 an de mandat)

## Goal

Analiza **evoluției discursului** lui Nicușor Dan în perioada candidatură → mandat, pornind de la cele mai simple metode și avansând progresiv către analize mai sofisticate. Întrebarea-țintă: *cum s-a schimbat discursul lui din momentul în care a anunțat candidatura, prin campanie, până în primul an de președinție?*

## Decizii inițiale

### Surse de date

- **YouTube** — discursuri oficiale, conferințe, declarații (transcriere cu Gemini/Whisper)
- **Facebook** — postări (text direct, ușor de colectat)
- **Comunicate oficiale + presă** — site Primărie, Administrația Prezidențială, declarații preluate
- **Interviuri / podcasturi** — apariții lungi, conținut bogat

### Perioadă

**Decembrie 2024 → mai 2026** (candidatură + primul an de mandat, ~18 luni).

### Stack tehnic

**Python + Jupyter Notebook.** Biblioteci principale: `spaCy` (cu model românesc), `scikit-learn`, `BERTopic`, `transformers`, `pandas`, `matplotlib`/`plotly`.

## Reguli de extracție (CRITICE pentru validitate)

1. **Păstrăm tot textul, dar cu delimitare strictă pe vorbitor.** În interviuri / conferințe / dezbateri / podcasturi, transcriem **integral** dialogul, dar fiecare replică e etichetată cu vorbitorul (`[ND]`, `[JURNALIST: Nume]`, `[MODERATOR]`, `[SIMION]` etc.). Asta ne permite două analize: (a) doar vocea lui ND — analiza principală, (b) interacțiunea (ce întrebări i se pun, cum răspunde la atacuri) — analiză secundară.
2. **Verbatim, nu rezumat.** Nu acceptăm parafrazări jurnalistice ("Dan a spus că..."). Doar citate directe sau transcripturi integrale.
3. **Provenanță trasabilă.** Fiecare fișier are header YAML cu: `data`, `tip` (discurs/post/interviu/comunicat/dezbatere), `sursa` (URL), `vorbitori` (lista), `verificat` (`true` dacă etichetele pe vorbitor sunt curate).
4. **Format de etichetare** într-un fișier multi-voce:
   ```
   [JURNALIST] Întrebarea...
   [ND] Răspunsul lui Nicușor Dan.
   [MODERATOR] Intervenție.
   [ND] Continuare.
   ```
5. **Discursuri monologate** (jurământ, anunț, victorie, mesaje TV, postări FB) — nu necesită etichetare, întregul text e implicit `[ND]`.
6. **Pipeline-ul de analiză** are un prim pas de **filtrare** care, pentru fiecare fișier multi-voce, extrage doar liniile `[ND]` în corpus-ul "voce_nd". Corpus-ul complet rămâne disponibil pentru analize de interacțiune.

## Roadmap (simplu → complex)

1. **Colectare & curățare text** — fundație
2. **Statistici de bază** — număr cuvinte, frecvențe, word cloud cu stopwords RO
3. **TF-IDF & n-grame** — cuvinte și sintagme distinctive
4. **Sentiment & pronume/modalitate** — *cum* vorbește
5. **Topic modeling pe timeline** — *despre ce* vorbește și cum se schimbă
6. **Comparativ** — pre/post candidatură, pre/post mandat; eventual vs. alți politicieni
