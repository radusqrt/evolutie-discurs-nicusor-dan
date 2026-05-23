# Pasul 1 — Statistici de bază + word clouds

## Sumar corpus

| id                                                                             | data       | tip                       |   n_words_raw |   n_lemmas_clean |   n_unique_lemmas |   ttr_lemma |   n_sentences |
|:-------------------------------------------------------------------------------|:-----------|:--------------------------|--------------:|-----------------:|------------------:|------------:|--------------:|
| 2025-02-20_in-orasele-din-moldova-pe-care-le-am-vizitat-recent-am-intal        | 2025-02-20 | facebook-post             |            18 |               10 |                10 |       1     |             1 |
| 2025-02-20_romania-asteapta-o-schimbare-reala-romania-puternica-are-nev        | 2025-02-20 | facebook-post             |            13 |               10 |                 9 |       0.9   |             2 |
| 2025-02-21_discutiile-internationale-despre-reconfigurarea-securitatii         | 2025-02-21 | facebook-post             |            83 |               47 |                40 |       0.851 |             4 |
| 2025-02-21_impreuna-pentru-romania-onesta                                      | 2025-02-21 | facebook-post             |             4 |                3 |                 3 |       1     |             1 |
| 2025-02-21_presedintele-trebuie-sa-uneasca-energiile-din-societate-doar        | 2025-02-21 | facebook-post             |            17 |               10 |                 9 |       0.9   |             2 |
| 2025-02-21_ultimul-dintre-studiile-de-fundamentare-necesare-pentru-actu        | 2025-02-21 | facebook-post             |           234 |              139 |               109 |       0.784 |             9 |
| 2025-02-21_vrei-sa-fii-parte-din-schimbare-alatura-te-echipei-de-volunt        | 2025-02-21 | facebook-post             |            56 |               40 |                38 |       0.95  |             6 |
| 2025-02-22_bucurestiul-este-finalist-la-premiile-saptamanii-europene-a         | 2025-02-22 | facebook-post             |            59 |               44 |                41 |       0.932 |             3 |
| 2025-02-22_in-vremuri-complicate-singura-resursa-ramane-discernamantul         | 2025-02-22 | facebook-post             |             8 |                7 |                 7 |       1     |             1 |
| 2025-02-23_am-discutat-in-acest-week-end-cu-oameni-din-ploiesti-brasov         | 2025-02-23 | facebook-post             |           149 |               85 |                68 |       0.8   |             8 |
| 2025-02-23_felicit-blocul-de-centru-dreapta-pro-european-cdu-csu-pentru        | 2025-02-23 | facebook-post             |           114 |               77 |                65 |       0.844 |             6 |
| 2025-02-23_grup-de-suport-pentru-femeile-afectate-de-violenta-domestica        | 2025-02-23 | facebook-post             |            75 |               49 |                45 |       0.918 |             7 |
| 2025-02-24_proiectul-politic-care-va-avea-cei-mai-multi-cei-mai-entuzia        | 2025-02-24 | facebook-post             |            57 |               28 |                25 |       0.893 |             3 |
| 2025-02-25_cifrele-vorbesc-clar-suntem-pe-drumul-cel-bun-si-romania-one        | 2025-02-25 | facebook-post             |            70 |               41 |                39 |       0.951 |             8 |
| 2025-02-25_impreuna-vom-reusi-romaniaonesta-romaniputernica-nicusorpres        | 2025-02-25 | facebook-post             |             6 |                6 |                 6 |       1     |             1 |
| 2025-02-25_mai-bine-mai-tarziu-decat-niciodata-alegerile-trebuie-organi        | 2025-02-25 | facebook-post             |            12 |                8 |                 8 |       1     |             2 |
| 2025-02-26_daca-voi-avea-increderea-romanilor-voi-fi-un-presedinte-acti        | 2025-02-26 | facebook-post             |            35 |               22 |                20 |       0.909 |             1 |
| 2025-02-26_suntem-aproape-de-100-000-de-semnaturi-pentru-depunerea-cand        | 2025-02-26 | facebook-post             |            78 |               44 |                39 |       0.886 |             6 |
| 2025-02-27_500-de-copii-vor-fi-ajutati-sa-ramana-alaturi-de-familiile-l        | 2025-02-27 | facebook-post             |           172 |              105 |                83 |       0.79  |             6 |
| 2025-02-27_in-sibiu-am-descoperit-aceleasi-probleme-ca-la-bucuresti-cup        | 2025-02-27 | facebook-post             |            54 |               28 |                26 |       0.929 |             5 |
| 2025-02-27_mai-multe-despre-copilaria-mea-la-fagaras-maine-dimineata-ro        | 2025-02-27 | facebook-post             |            11 |                5 |                 5 |       1     |             1 |
| 2025-02-27_maine-dimineata-lansam-un-video-despre-copilaria-mea-la-faga        | 2025-02-27 | facebook-post             |            14 |                8 |                 8 |       1     |             2 |
| 2025-02-27_toata-viata-mea-am-luptat-pentru-dreptate-pentru-protectia-c        | 2025-02-27 | facebook-post             |            98 |               50 |                47 |       0.94  |             6 |
| 2025-02-28_casa-bunicii-romaniaonesta-nicusorpresedinte                        | 2025-02-28 | facebook-post             |             4 |                4 |                 4 |       1     |             1 |
| 2025-02-28_cred-ca-e-important-sa-stiti-de-unde-vin-daca-si-voua-vi-se         | 2025-02-28 | facebook-post             |            20 |               10 |                 9 |       0.9   |             2 |
| 2025-02-28_despre-mentinerea-legaturii-cu-parintii-cand-eram-in-straina        | 2025-02-28 | facebook-post             |            11 |                6 |                 6 |       1     |             1 |
| 2025-02-28_este-profund-ingrijorator-ca-romania-a-fost-retrogradata-in         | 2025-02-28 | facebook-post             |           156 |               96 |                86 |       0.896 |             6 |
| 2025-02-28_in-politica-noastra-externa-trebuie-sa-punem-intotdeauna-pe         | 2025-02-28 | facebook-post             |            15 |               11 |                11 |       1     |             1 |
| 2025-02-28_mergeam-la-colindat-romaniaonesta-nicusorpresedinte                 | 2025-02-28 | facebook-post             |             5 |                4 |                 4 |       1     |             1 |
| 2025-02-28_sust-in-ferm-ucraina-i-n-lupta-sa-pentru-o-pace-justa-s-i-su        | 2025-02-28 | facebook-post             |            59 |               34 |                32 |       0.941 |             5 |
| 2025-03-01_ce-le-as-spune-copiilor-din-orasele-mici-ale-romaniei-asa-cu        | 2025-03-01 | facebook-post             |            18 |                7 |                 7 |       1     |             1 |
| 2025-03-01_filmele-si-cartile-din-copilarie-romaniaonesta-nicusorpresed        | 2025-03-01 | facebook-post             |             7 |                5 |                 5 |       1     |             1 |
| 2025-03-01_haideti-sa-stam-de-vorba-va-astept-mesajele-pe-whatsapp-la-0        | 2025-03-01 | facebook-post             |            34 |               23 |                22 |       0.957 |             3 |
| 2025-03-01_rolul-scolii-romaniaonesta-nicusorpresedinte                        | 2025-03-01 | facebook-post             |             4 |                4 |                 4 |       1     |             1 |
| 2025-03-01_solidaritatea-dintre-noi-romaniaonesta-nicusorpresedinte            | 2025-03-01 | facebook-post             |             5 |                3 |                 3 |       1     |             1 |
| 2025-03-01_traim-poate-cele-mai-provocatoare-vremuri-din-ultimele-decen        | 2025-03-01 | facebook-post             |            28 |               15 |                15 |       1     |             2 |
| 2025-03-02_91-de-statii-stb-vor-primi-denumiri-noi-mai-precise-care-ref        | 2025-03-02 | facebook-post             |           106 |               71 |                60 |       0.845 |             9 |
| 2025-03-02_cea-mai-entuziasta-echipa-de-voluntari-la-nivel-national-ei         | 2025-03-02 | facebook-post             |            42 |               25 |                25 |       1     |             3 |
| 2025-03-02_educatia-primita-de-la-parinti-romaniaonesta-nicusorpresedin        | 2025-03-02 | facebook-post             |             7 |                5 |                 5 |       1     |             1 |
| 2025-03-02_mancarea-de-la-bunici-lapte-cu-mamaliga-romaniaonesta-nicuso        | 2025-03-02 | facebook-post             |             9 |                6 |                 6 |       1     |             1 |
| 2025-03-02_marim-capacitatea-de-cazare-a-adapostului-de-caini-aspa-miha        | 2025-03-02 | facebook-post             |            73 |               50 |                39 |       0.78  |             4 |
| 2025-03-02_romania-pe-primul-loc-din-lume-la-matematica-romaniaonesta-n        | 2025-03-02 | facebook-post             |             9 |                6 |                 6 |       1     |             1 |
| 2025-03-02_satul-bunicilor-romaniaonesta-nicusorpresedinte                     | 2025-03-02 | facebook-post             |             4 |                4 |                 4 |       1     |             1 |
| 2025-03-03_am-avut-onoarea-sa-primesc-astazi-la-sediul-primariei-capita        | 2025-03-03 | facebook-post             |           144 |               95 |                78 |       0.821 |            12 |
| 2025-03-03_bucuria-de-a-merge-la-scoala-romaniaonesta-nicusorpresedinte        | 2025-03-03 | facebook-post             |             7 |                5 |                 5 |       1     |             1 |
| 2025-03-03_cand-vom-alege-pentru-urmatorii-5-ani-sa-nu-uitam-de-tinerii        | 2025-03-03 | facebook-post             |            21 |               13 |                13 |       1     |             2 |
| 2025-03-03_pe-panoul-de-la-liceul-radu-negru-din-fagaras-romaniaonesta         | 2025-03-03 | facebook-post             |            11 |                7 |                 7 |       1     |             1 |
| 2025-03-03_vacantele-la-tara-la-bunici-romaniaonesta-nicusorpresedinte         | 2025-03-03 | facebook-post             |             7 |                5 |                 5 |       1     |             1 |
| 2025-03-04_astazi-se-implinesc-48-de-ani-de-la-cutremurul-devastator-ca        | 2025-03-04 | facebook-post             |           189 |              108 |                88 |       0.815 |             8 |
| 2025-03-04_azi-serviciul-de-informatii-externe-al-rusiei-a-dat-un-comun        | 2025-03-04 | facebook-post             |           121 |               60 |                55 |       0.917 |             5 |
| 2025-03-04_in-2019-am-facut-o-promisiune-simpla-dar-esentiala-primaria         | 2025-03-04 | facebook-post             |            35 |               18 |                17 |       0.944 |             2 |
| 2025-03-04_viziunea-mea-pentru-un-viitor-guvern                                | 2025-03-04 | facebook-post             |             6 |                3 |                 3 |       1     |             1 |
| 2025-03-05_astazi-am-avut-o-intalnire-extrem-de-interesanta-cu-reprezen        | 2025-03-05 | facebook-post             |           241 |              134 |               102 |       0.761 |             9 |
| 2025-03-05_interventia-presedintelui-trump-de-azi-noapte-din-congres-es        | 2025-03-05 | facebook-post             |           127 |               68 |                60 |       0.882 |             5 |
| 2025-03-05_organizam-cursuri-de-initiere-in-lumea-digitala-pentru-senio        | 2025-03-05 | facebook-post             |           194 |              124 |                85 |       0.685 |            12 |
| 2025-03-06_copiii-familia-iubirea-care-ne-tine-ancorati-in-aceasta-lume        | 2025-03-06 | facebook-post             |            33 |               15 |                13 |       0.867 |             5 |
| 2025-03-06_ne-vedem-la-cluj-sambata-vom-fi-la-cluj-dar-pana-atunci-trim        | 2025-03-06 | facebook-post             |            40 |               19 |                16 |       0.842 |             4 |
| 2025-03-06_o-afacere-de-familie-infiintata-in-1995-in-bacau-a-crescut-s        | 2025-03-06 | facebook-post             |            78 |               46 |                44 |       0.957 |             3 |
| 2025-03-07_acum-trei-luni-romanii-au-spus-clar-nu-se-mai-poate-au-cerut        | 2025-03-07 | facebook-post             |            84 |               46 |                44 |       0.957 |             5 |
| 2025-03-07_candidez-pentru-toti-romanii-onesti-din-tara-si-din-diaspora        | 2025-03-07 | facebook-post             |           162 |               81 |                69 |       0.852 |             8 |
| 2025-03-07_vrei-sa-fii-parte-din-schimbare-alatura-te-echipei-de-volunt        | 2025-03-07 | facebook-post             |            56 |               39 |                37 |       0.949 |             6 |
| 2025-03-08_am-avut-ieri-placerea-de-a-oferi-flori-doamnelor-care-lucrea        | 2025-03-08 | facebook-post             |           103 |               55 |                48 |       0.873 |             5 |
| 2025-03-08_ce-ne-am-face-fara-femeile-din-viata-noastra-azi-sa-le-sarba        | 2025-03-08 | facebook-post             |            30 |                9 |                 8 |       0.889 |             3 |
| 2025-03-08_de-8-martie-femeile-sunt-sarbatorite-cu-flori-si-complimente        | 2025-03-08 | facebook-post             |           130 |               74 |                68 |       0.919 |             9 |
| 2025-03-08_peste-15-000-de-puieti-si-arbori-forestieri-sunt-plantati-in        | 2025-03-08 | facebook-post             |            84 |               50 |                49 |       0.98  |             6 |
| 2025-03-08_vocea-oamenilor-va-conta-mai-mult-decat-vocea-politicienilor        | 2025-03-08 | facebook-post             |            14 |               12 |                11 |       0.917 |             2 |
| 2025-03-09_fiecare-conversatie-cu-tinerii-este-o-lectie-despre-dorinta         | 2025-03-09 | facebook-post             |            28 |               17 |                17 |       1     |             2 |
| 2025-03-09_interventii-pentru-repararea-strazilor-administratia-strazil        | 2025-03-09 | facebook-post             |           149 |              106 |                92 |       0.868 |            21 |
| 2025-03-09_sa-nu-uitam-niciodata-am-depus-astazi-o-coroana-de-flori-la         | 2025-03-09 | facebook-post             |            53 |               25 |                25 |       1     |             5 |
| 2025-03-11_facem-curatenia-de-primavara-in-parcurile-pe-care-le-adminis        | 2025-03-11 | facebook-post             |           126 |               90 |                78 |       0.867 |             8 |
| 2025-03-11_onest-cu-el-insusi-onest-cu-membrii-familiei-onest-cu-cei-di        | 2025-03-11 | facebook-post             |            15 |                9 |                 7 |       0.778 |             1 |
| 2025-03-11_partidele-politice-corupte-care-au-promovat-incompetenti-in         | 2025-03-11 | facebook-post             |            92 |               57 |                46 |       0.807 |             8 |
| 2025-03-11_pe-nicusor-l-am-vazut-mereu-ca-pe-un-invingator-romaniaonest        | 2025-03-11 | facebook-post             |            12 |                5 |                 5 |       1     |             1 |
| 2025-03-11_responsabilitate-tenacitate-si-acasa-si-in-societate-romania        | 2025-03-11 | facebook-post             |             9 |                6 |                 6 |       1     |             1 |
| 2025-03-12_am-semnat-un-acord-cadru-pe-patru-ani-prin-administratia-str        | 2025-03-12 | facebook-post             |           138 |               83 |                71 |       0.855 |             5 |
| 2025-03-12_cand-m-am-intors-din-franta-n-am-suportat-nedreptatea-lupta         | 2025-03-12 | facebook-post             |            14 |                8 |                 8 |       1     |             2 |
| 2025-03-12_domnul-cristian-tudor-popescu-mi-a-solicitat-la-finalul-inte        | 2025-03-12 | facebook-post             |            48 |               32 |                31 |       0.969 |             3 |
| 2025-03-12_m-am-revazut-la-alba-iulia-cu-un-prieten-vechi-alaturi-de-ca        | 2025-03-12 | facebook-post             |            42 |               19 |                19 |       1     |             2 |
| 2025-03-12_nicusor-ar-putea-sa-faca-din-romania-o-tara-din-care-sa-nu-s        | 2025-03-12 | facebook-post             |            17 |                8 |                 8 |       1     |             1 |
| 2025-03-12_schimbari-prin-puterea-exemplului-romaniaonesta-nicusorprese        | 2025-03-12 | facebook-post             |             6 |                5 |                 5 |       1     |             1 |
| 2025-03-13_34-4-milioane-de-euro-pentru-modernizarea-sistemului-de-term        | 2025-03-13 | facebook-post             |           173 |               99 |                74 |       0.747 |             6 |
| 2025-03-13_cea-mai-violenta-problema-cu-care-se-confrunta-multe-familii        | 2025-03-13 | facebook-post             |            16 |                9 |                 9 |       1     |             1 |
| 2025-03-13_lucrurile-importante-nu-sunt-doar-cele-care-se-vad-la-supraf        | 2025-03-13 | facebook-post             |            22 |               13 |                12 |       0.923 |             2 |
| 2025-03-13_lupta-de-10-ani-cu-institutiile-strambe-ale-statului-si-cu-m        | 2025-03-13 | facebook-post             |            34 |               19 |                19 |       1     |             3 |
| 2025-03-13_niciodata-nu-am-suportat-nedreptatea-am-luptat-peste-10-ani         | 2025-03-13 | facebook-post             |            54 |               31 |                28 |       0.903 |             4 |
| 2025-03-13_tomograful-sonic-picus-detecteaza-in-mod-non-invaziv-eventua        | 2025-03-13 | facebook-post             |           141 |               77 |                68 |       0.883 |             6 |
| 2025-03-14_am-avut-o-intalnire-importanta-la-sediul-primariei-capitalei        | 2025-03-14 | facebook-post             |           172 |              109 |                83 |       0.761 |            11 |
| 2025-03-14_arcul-de-triumf-va-fi-deschis-permanent-pentru-vizitare-ince        | 2025-03-14 | facebook-post             |           135 |               74 |                62 |       0.838 |             9 |
| 2025-03-14_ce-le-as-spune-tinerilor-e-nevoie-de-o-schimbare-si-simt-si         | 2025-03-14 | facebook-post             |            15 |                6 |                 6 |       1     |             2 |
| 2025-03-14_daca-vrem-sa-i-aducem-pe-romanii-plecati-acasa-trebuie-sa-le        | 2025-03-14 | facebook-post             |            20 |               12 |                12 |       1     |             1 |
| 2025-03-14_sarut-mana-aglaia-romaniaonesta-nicusorpresedinte                   | 2025-03-14 | facebook-post             |             5 |                5 |                 5 |       1     |             1 |
| 2025-03-14_te-astept-sambata-15-martie-in-orasele-tulcea-si-constanta-s        | 2025-03-14 | facebook-post             |            56 |               37 |                35 |       0.946 |             5 |
| 2025-03-14_tinerii-au-nevoie-de-motive-sa-ramana-in-romania-si-sa-conti        | 2025-03-14 | facebook-post             |            33 |               18 |                18 |       1     |             2 |
| 2025-03-15_anul-acesta-se-implinesc-35-de-ani-de-la-citirea-proclamatie        | 2025-03-15 | facebook-post             |           106 |               55 |                48 |       0.873 |             5 |
| 2025-03-15_de-ziua-internationala-a-raurilor-angajatii-alpab-impreuna-c        | 2025-03-15 | facebook-post             |           184 |              113 |                98 |       0.867 |             8 |
| 2025-03-15_felicit-comunitatea-maghiara-din-romania-cu-ocazia-zilei-mag        | 2025-03-15 | facebook-post             |            37 |               20 |                20 |       1     |             2 |
| 2025-03-15_la-constanta-am-simtit-ca-oamenii-vor-cu-adevarat-o-schimbar        | 2025-03-15 | facebook-post             |            74 |               42 |                39 |       0.929 |             3 |
| 2025-03-15_romania-trebuie-sa-se-dezvolte-mult-mai-echilibrat-si-sa-imp        | 2025-03-15 | facebook-post             |           140 |               80 |                62 |       0.775 |             6 |
| 2025-03-16_in-zgomotul-electoral-a-fost-tratata-prea-discret-stirea-ca         | 2025-03-16 | facebook-post             |           187 |               95 |                80 |       0.842 |             7 |
| 2025-03-16_o-noua-actiune-de-informare-si-control-pentru-verificarea-ca        | 2025-03-16 | facebook-post             |           111 |               58 |                50 |       0.862 |            10 |
| 2025-03-16_tulcea-si-ivan-patzaichinivan-patzaichin-un-model-de-modesti        | 2025-03-16 | facebook-post             |            13 |                9 |                 9 |       1     |             1 |
| 2025-03-17_un-bloc-de-locuinte-situat-pe-calea-victoriei-nr-101-va-fi-c        | 2025-03-17 | facebook-post             |            93 |               60 |                52 |       0.867 |             5 |
| 2025-03-17_unii-ma-considera-incapatanat-altii-ma-vad-perseverent-acest        | 2025-03-17 | facebook-post             |            49 |               27 |                26 |       0.963 |             4 |
| 2025-03-18_am-acordat-un-interviu-pentru-cotidianul-le-monde-in-care-am        | 2025-03-18 | facebook-post             |            51 |               28 |                26 |       0.929 |             2 |
| 2025-03-18_am-semnat-autorizatia-de-construire-pentru-restaurarea-palat        | 2025-03-18 | facebook-post             |            75 |               46 |                41 |       0.891 |             5 |
| 2025-03-18_transparenta-cheltuirii-banilor-cetatenilor-trebuie-sa-devin        | 2025-03-18 | facebook-post             |            87 |               50 |                42 |       0.84  |             6 |
| 2025-03-19_deschidem-inca-doua-noi-santiere-pentru-modernizarea-a-21-5         | 2025-03-19 | facebook-post             |           162 |              111 |                78 |       0.703 |            16 |
| 2025-03-19_multumesc-diaspora-sunt-impresionat-de-gestul-romanilor-din         | 2025-03-19 | facebook-post             |            23 |               14 |                13 |       0.929 |             3 |
| 2025-03-20_am-o-mare-admiratie-pentru-romanii-care-au-plecat-din-tara-a        | 2025-03-20 | facebook-post             |            94 |               43 |                37 |       0.86  |             5 |
| 2025-03-20_daca-voi-fi-ales-presedinte-voi-pune-in-practica-toata-exper        | 2025-03-20 | facebook-post             |            64 |               37 |                35 |       0.946 |             4 |
| 2025-03-20_ne-vedem-la-19-00-cu-amintiri-din-studentia-de-la-paris-nicu        | 2025-03-20 | facebook-post             |            11 |                5 |                 5 |       1     |             2 |
| 2025-03-21_am-atribuit-contractul-pentru-realizarea-unui-nou-plan-integ        | 2025-03-21 | facebook-post             |           152 |               99 |                76 |       0.768 |             7 |
| 2025-03-21_combaterea-ferma-a-evaziunii-fiscale-si-recuperarea-justa-a         | 2025-03-21 | facebook-post             |           102 |               57 |                56 |       0.982 |             6 |
| 2025-03-21_increderea-cetatenilor-se-castiga-greu-si-se-pierde-usor-ale        | 2025-03-21 | facebook-post             |            56 |               35 |                33 |       0.943 |             4 |
| 2025-03-21_politicienii-sunt-alesi-pentru-a-servi-interesele-cetatenilo        | 2025-03-21 | facebook-post             |            21 |               12 |                12 |       1     |             1 |
| 2025-03-22_andrei-m-a-intrebat-ce-masuri-putem-lua-pentru-reducerea-def        | 2025-03-22 | facebook-post             |            21 |               13 |                13 |       1     |             2 |
| 2025-03-22_echipa-se-sustine-si-in-momente-dificile                            | 2025-03-22 | facebook-post             |             7 |                5 |                 5 |       1     |             1 |
| 2025-03-22_luna-sanatatii-orale-campanie-educationala-pentru-copii-in-s        | 2025-03-22 | facebook-post             |           122 |               77 |                58 |       0.753 |             8 |
| 2025-03-22_pozitia-11-pe-buletinul-de-vot-nicusorpresedinte-romaniaones        | 2025-03-22 | facebook-post             |             8 |                6 |                 6 |       1     |             1 |
| 2025-03-23_anul-acesta-continuam-investitiile-in-modernizarea-transport        | 2025-03-23 | facebook-post             |            40 |               26 |                24 |       0.923 |             3 |
| 2025-03-23_romania-se-confrunta-cu-o-criza-de-datorie-si-cheltuieli-far        | 2025-03-23 | facebook-post             |           121 |               78 |                67 |       0.859 |             6 |
| 2025-03-23_suntem-multi-si-energici-impreuna-suntem-romania-onesta-volu        | 2025-03-23 | facebook-post             |            31 |               27 |                27 |       1     |             2 |
| 2025-03-23_week-end-in-bucuresti-romaniaonesta-nicusorpresedinte-nd11          | 2025-03-23 | facebook-post             |             6 |                5 |                 5 |       1     |             1 |
| 2025-03-24_asociatia-salvati-bucurestiul-a-fost-o-scoala-de-dreptul-urb        | 2025-03-24 | facebook-post             |            10 |                7 |                 7 |       1     |             1 |
| 2025-03-24_fara-ego-pana-la-capat-pentru-a-opri-abuzurile-urbanistice-d        | 2025-03-24 | facebook-post             |            13 |                8 |                 8 |       1     |             1 |
| 2025-03-24_tramvaiele-imperio-de-la-astra-arad-sunt-exemplul-perfect-ca        | 2025-03-24 | facebook-post             |           102 |               47 |                41 |       0.872 |             5 |
| 2025-03-24_un-presedinte-inovator-nicusorpresedinte-romaniaonesta              | 2025-03-24 | facebook-post             |             5 |                4 |                 4 |       1     |             1 |
| 2025-03-24_una-dintre-cele-mai-importante-lupte-in-activitatea-mea-publ        | 2025-03-24 | facebook-post             |           117 |               72 |                65 |       0.903 |             6 |
| 2025-03-25_ce-ar-putea-face-nicusor-dan-ca-presedinte-nicusorpresedinte        | 2025-03-25 | facebook-post             |            10 |                6 |                 6 |       1     |             1 |
| 2025-03-25_mergeai-cu-nicusor-dan-la-o-actiune-si-stiai-ca-merita-sa-lu        | 2025-03-25 | facebook-post             |            17 |               10 |                10 |       1     |             1 |
| 2025-03-25_nicusor-dan-a-avut-curajul-de-a-merge-dincolo-de-protest-ca         | 2025-03-25 | facebook-post             |            14 |               10 |                10 |       1     |             1 |
| 2025-03-25_si-alte-lucruri-ipotetice-despre-care-am-vorbit                     | 2025-03-25 | facebook-post             |             8 |                3 |                 3 |       1     |             1 |
| 2025-03-26_am-gestionat-o-situatie-financiara-complicata-la-primaria-ca        | 2025-03-26 | facebook-post             |            31 |               19 |                17 |       0.895 |             3 |
| 2025-03-26_de-ce-candidez-nicusorpresedinte-romaniaonesta-panalacapat          | 2025-03-26 | facebook-post             |             6 |                4 |                 4 |       1     |             1 |
| 2025-03-26_incepem-modernizarea-liniei-de-tramvai-pe-bulevardul-expozit        | 2025-03-26 | facebook-post             |           151 |               97 |                71 |       0.732 |             7 |
| 2025-03-26_o-schimbare-profunda-a-sistemului-nicusorpresedinte-romaniao        | 2025-03-26 | facebook-post             |             5 |                5 |                 5 |       1     |             1 |
| 2025-03-26_romania-e-pe-minus-e-nevoie-urgenta-de-reforme-pentru-a-echi        | 2025-03-26 | facebook-post             |            20 |               15 |                14 |       0.933 |             2 |
| 2025-03-26_un-presedinte-onest-care-poate-reforma-statul-roman-nicusorp        | 2025-03-26 | facebook-post             |            10 |                8 |                 8 |       1     |             1 |
| 2025-03-26_viziunea-puterea-cuvantului-dat-pot-aduce-schimbarea-de-care        | 2025-03-26 | facebook-post             |            13 |                8 |                 8 |       1     |             1 |
| 2025-03-27_4-ani-si-jumatate-de-munca-pentru-un-bucuresti-mai-functiona        | 2025-03-27 | facebook-post             |            56 |               38 |                37 |       0.974 |             4 |
| 2025-03-27_am-fost-invitat-de-mihai-morar-la-podcastul-fain-simplu-unde        | 2025-03-27 | facebook-post             |            46 |               24 |                24 |       1     |             1 |
| 2025-03-27_astazi-27-martie-marcam-107-ani-de-la-un-moment-esential-in         | 2025-03-27 | facebook-post             |           135 |               80 |                67 |       0.838 |             6 |
| 2025-03-27_astazi-este-ziua-internationala-a-teatrului-un-bun-prilej-sa        | 2025-03-27 | facebook-post             |            48 |               21 |                21 |       1     |             3 |
| 2025-03-27_telul-meu-este-sa-reconstruim-increderea-oamenilor-in-autori        | 2025-03-27 | facebook-post             |            17 |               10 |                10 |       1     |             1 |
| 2025-03-28_am-acordat-un-interviu-publicatiei-politico-si-am-raspuns-in        | 2025-03-28 | facebook-post             |            41 |               21 |                21 |       1     |             1 |
| 2025-03-28_functiile-publice-nu-sunt-mosteniri-de-familie-romania-are-n        | 2025-03-28 | facebook-post             |            28 |               17 |                17 |       1     |             2 |
| 2025-03-28_presedintele-trebuie-sa-fie-acolo-unde-se-iau-deciziile-voi         | 2025-03-28 | facebook-post             |            25 |               17 |                16 |       0.941 |             2 |
| 2025-03-28_vom-relua-lucrarile-pentru-finalizarea-proiectului-prelungir        | 2025-03-28 | facebook-post             |           131 |               84 |                64 |       0.762 |            12 |
| 2025-03-29_aderarea-republicii-moldova-la-uniunea-europeana-este-o-prio        | 2025-03-29 | facebook-post             |            59 |               34 |                29 |       0.853 |             4 |
| 2025-03-29_am-deschis-astazi-oficial-sediul-de-campanie-pentru-candidat        | 2025-03-29 | facebook-post             |           160 |               87 |                74 |       0.851 |            18 |
| 2025-03-29_primul-transplant-hepatic-din-2025-a-fost-realizat-cu-succes        | 2025-03-29 | facebook-post             |           150 |               89 |                69 |       0.775 |             7 |
| 2025-03-29_un-raspuns-scurt-la-o-intrebare-clara-nicusorpresedinte-roma        | 2025-03-29 | facebook-post             |             8 |                6 |                 6 |       1     |             1 |
| 2025-03-30_am-fost-invitatul-lui-radu-andrei-tudor-la-the-news-man-podc        | 2025-03-30 | facebook-post             |            38 |               21 |                21 |       1     |             1 |
| 2025-03-30_astazi-am-discutat-cu-sustinatorii-din-chisinau-despre-impor        | 2025-03-30 | facebook-post             |           177 |              105 |                79 |       0.752 |             8 |
| 2025-03-30_romanii-vor-o-schimbare-alegerile-prezidentiale-din-mai-vor         | 2025-03-30 | facebook-post             |            17 |               13 |                12 |       0.923 |             2 |
| 2025-03-31_am-vizitat-ieri-la-chisinau-cramele-cricova-un-adevarat-simb        | 2025-03-31 | facebook-post             |            68 |               41 |                35 |       0.854 |             3 |
| 2025-03-31_asa-cum-v-am-obisnuit-in-spiritul-transparentei-va-impartase        | 2025-03-31 | facebook-post             |            16 |                8 |                 8 |       1     |             1 |
| 2025-03-31_voluntarii-campaniei-au-fost-si-in-acest-week-end-prezenti-i        | 2025-03-31 | facebook-post             |            38 |               28 |                28 |       1     |             3 |
| 2025-04-01_psd-care-a-cheltuit-peste-50-de-milioane-de-euro-din-bani-pu        | 2025-04-01 | facebook-post             |           118 |               64 |                54 |       0.844 |             6 |
| 2025-04-01_situatia-financiara-actuala-a-romaniei-este-similara-cu-cea         | 2025-04-01 | facebook-post             |            61 |               35 |                34 |       0.971 |             4 |
| 2025-04-02_nicusor-dan-ar-putea-fi-un-presedinte-care-sa-aduca-prestigi        | 2025-04-02 | facebook-post             |            14 |                9 |                 9 |       1     |             1 |
| 2025-04-02_o-finala-ponta-simion-ar-fi-cea-mai-rea-varianta-pentru-roma        | 2025-04-02 | facebook-post             |            12 |                7 |                 7 |       1     |             1 |
| 2025-04-02_teatrul-ion-creanga-a-fost-abandonat-desi-are-multa-istorie         | 2025-04-02 | facebook-post             |            31 |               19 |                18 |       0.947 |             2 |
| 2025-04-03_acum-si-la-new-york-multumesc-romanilor-din-new-york-care-mi        | 2025-04-03 | facebook-post             |            18 |                9 |                 7 |       0.778 |             2 |
| 2025-04-03_am-avut-astazi-o-intalnire-cu-directori-ai-teatrelor-aflate         | 2025-04-03 | facebook-post             |           147 |               85 |                69 |       0.812 |             5 |
| 2025-04-03_am-semnat-astazi-un-protocol-de-colaborare-cu-untold-univers        | 2025-04-03 | facebook-post             |           180 |               98 |                78 |       0.796 |             8 |
| 2025-04-03_in-cateva-ore-incepe-oficial-campania-electorala-voluntarii         | 2025-04-03 | facebook-post             |            79 |               41 |                36 |       0.878 |             5 |
| 2025-04-03_madrid-londra-roma-paris-berlin-bruxelles-new-york-acolo-und        | 2025-04-03 | facebook-post             |            79 |               52 |                47 |       0.904 |            16 |
| 2025-04-03_si-la-berlin-multumesc-si-danke-sch-n-romanilor-din-berlin-c        | 2025-04-03 | facebook-post             |            18 |               10 |                 9 |       0.9   |             2 |
| 2025-04-03_suntem-la-98-sa-atingem-obiectivul-de-donatii-cu-deadline-pa        | 2025-04-03 | facebook-post             |            22 |               12 |                11 |       0.917 |             4 |
| 2025-04-03_suntem-multi-si-impreuna-mergem-pana-la-capat-nd11-romaniaon        | 2025-04-03 | facebook-post             |            11 |                6 |                 6 |       1     |             1 |
| 2025-04-03_tarifele-impuse-de-statele-unite-vor-afecta-intreaga-lume-ia        | 2025-04-03 | facebook-post             |           209 |              128 |               109 |       0.852 |            12 |
| 2025-04-03_un-proiect-inceput-acum-48-de-ani-finalizat-de-noi-statia-de        | 2025-04-03 | facebook-post             |            32 |               20 |                19 |       0.95  |             2 |
| 2025-04-04_aniversam-azi-intr-un-context-geopolitic-foarte-complicat-76        | 2025-04-04 | facebook-post             |           254 |              143 |               115 |       0.804 |             8 |
| 2025-04-04_cred-in-noi-cred-in-romania-in-europa-romaniaonesta-nicusorp        | 2025-04-04 | facebook-post             |            10 |                6 |                 5 |       0.833 |             2 |
| 2025-04-04_voluntarii-nostri-au-inceput-campania-electorala-cu-multa-en        | 2025-04-04 | facebook-post             |            48 |               37 |                37 |       1     |             2 |
| 2025-04-05_dupa-o-zi-lunga-la-madrid-am-ajuns-in-camera-de-hotel-si-am         | 2025-04-05 | facebook-post             |           108 |               69 |                65 |       0.942 |             8 |
| 2025-04-05_forta-antreprenorilor-romani-din-regiunea-madrid-am-avut-o-d        | 2025-04-05 | facebook-post             |           161 |               93 |                81 |       0.871 |             9 |
| 2025-04-05_intalnire-romaneasca-la-arganda-del-rey-regiunea-madrid-am-f        | 2025-04-05 | facebook-post             |           177 |              101 |                79 |       0.782 |             9 |
| 2025-04-05_interviu-la-radio-romanul-alaturi-de-romanii-din-diaspora-am        | 2025-04-05 | facebook-post             |           186 |              103 |                78 |       0.757 |            11 |
| 2025-04-05_prima-pajiste-urbana-cu-flori-de-camp-salbatice-din-bucurest        | 2025-04-05 | facebook-post             |           177 |              108 |                82 |       0.759 |             8 |
| 2025-04-05_puterea-nu-ne-o-da-nimeni-o-construim-noi-romaniaonesta-nicu        | 2025-04-05 | facebook-post             |             9 |                4 |                 4 |       1     |             2 |
| 2025-04-05_sunt-incantat-sa-anunt-bucurestenii-ca-incepand-cu-12-aprili        | 2025-04-05 | facebook-post             |           151 |              106 |                85 |       0.802 |             6 |
| 2025-04-05_vizita-in-diaspora-romaneasca-din-spania-cubas-de-la-sagra-l        | 2025-04-05 | facebook-post             |           208 |              121 |                98 |       0.81  |            10 |
| 2025-04-06_daca-se-repara-romania-ma-intorc-cu-acest-mesaj-am-plecat-di        | 2025-04-06 | facebook-post             |            30 |               15 |                14 |       0.933 |             2 |
| 2025-04-06_impreuna-vindecam-romania-avem-medici-profesionisti-si-asist        | 2025-04-06 | facebook-post             |            50 |               32 |                32 |       1     |             4 |
| 2025-04-06_romania-joaca-in-liga-mare-nicusorpresedinte-romaniaonesta          | 2025-04-06 | facebook-post             |             7 |                5 |                 5 |       1     |             1 |
| 2025-04-06_romania-onesta-este-prezenta-peste-tot-voluntarii-nostri-au         | 2025-04-06 | facebook-post             |            42 |               22 |                21 |       0.955 |             3 |
| 2025-04-06_romanii-din-spania-poarta-in-suflet-o-dorinta-arzatoare-de-s        | 2025-04-06 | facebook-post             |            42 |               26 |                26 |       1     |             2 |
| 2025-04-06_traditii-si-flori-de-sarbatori-revine-in-bucuresti-primaria         | 2025-04-06 | facebook-post             |           167 |              110 |                97 |       0.882 |            13 |
| 2025-04-06_zi-reusita-la-targul-de-adoptii-aspa-din-parcul-carol-de-ier        | 2025-04-06 | facebook-post             |            83 |               37 |                32 |       0.865 |             4 |
| 2025-04-07_adevarul-acest-clip-demonteaza-o-minciuna-nu-am-afirmat-nici        | 2025-04-07 | facebook-post             |            34 |               20 |                19 |       0.95  |             4 |
| 2025-04-07_asa-arata-stabilitatea-psd-pnl-riscam-sa-pierdem-miliarde-de        | 2025-04-07 | facebook-post             |           156 |               96 |                83 |       0.865 |            14 |
| 2025-04-07_e-timpul-sa-ne-recapatam-increderea-in-noi-nicusorpresedinte        | 2025-04-07 | facebook-post             |             9 |                4 |                 4 |       1     |             1 |
| 2025-04-07_ieri-m-am-intalnit-cu-una-dintre-cele-mai-puternice-comunita        | 2025-04-07 | facebook-post             |           163 |               88 |                69 |       0.784 |             8 |
| 2025-04-07_marcel-ciolacu-prim-ministru-al-guvernului-romaniei-conduce         | 2025-04-07 | facebook-post             |           116 |               82 |                66 |       0.805 |             9 |
| 2025-04-07_patriotismul-inseamna-sa-pui-romania-in-valoare-nu-s-o-conda        | 2025-04-07 | facebook-post             |            16 |               10 |                10 |       1     |             1 |
| 2025-04-08_astazi-de-ziua-internationala-a-romilor-gandurile-mele-se-in        | 2025-04-08 | facebook-post             |           144 |               82 |                74 |       0.902 |             7 |
| 2025-04-08_consider-ca-propunerea-presedintelui-interimar-domnul-ilie-b        | 2025-04-08 | facebook-post             |           121 |               73 |                69 |       0.945 |             5 |
| 2025-04-08_multi-se-declara-luptatori-anti-sistem-putini-au-fapte-concr        | 2025-04-08 | facebook-post             |            29 |               15 |                15 |       1     |             2 |
| 2025-04-09_succes-tati-va-astept-la-21-00-la-antena-3-sa-vorbim-despre         | 2025-04-09 | facebook-post             |            21 |               11 |                11 |       1     |             3 |
| 2025-04-10_later-edit-steven-seagal-este-emisar-special-al-ministerului        | 2025-04-10 | facebook-post             |           190 |              119 |                87 |       0.731 |            10 |
| 2025-04-10_ponta-este-singurul-candidat-autoproclamat-anti-sorosist-car        | 2025-04-10 | facebook-post             |            21 |               13 |                12 |       0.923 |             2 |
| 2025-04-11_cuvintele-soacrei-mele-m-au-emotionat-profund-multumesc-lili        | 2025-04-11 | facebook-post             |             9 |                5 |                 5 |       1     |             2 |
| 2025-04-11_indemnizatiile-persoanelor-cu-dizabilitati-din-bucuresti-au         | 2025-04-11 | facebook-post             |           104 |               56 |                52 |       0.929 |             5 |
| 2025-04-11_la-finalul-anului-trecut-coalitia-stabilitatii-psd-pnl-infii        | 2025-04-11 | facebook-post             |           190 |              119 |               103 |       0.866 |             9 |
| 2025-04-12_am-fost-onorat-sa-particip-astazi-alaturi-de-e-s-katae-takas        | 2025-04-12 | facebook-post             |           181 |               89 |                75 |       0.843 |            11 |
| 2025-04-12_domnul-ciolacu-se-teme-ca-va-fi-obligat-sa-poarte-fusta-daca        | 2025-04-12 | facebook-post             |            56 |               38 |                32 |       0.842 |             3 |
| 2025-04-12_live-declaratii-de-presa-la-sediul-de-campanie                      | 2025-04-12 | facebook-post             |             8 |                5 |                 5 |       1     |             0 |
| 2025-04-12_sesizare-catre-autoritatea-electorala-permanenta-solicitam-r        | 2025-04-12 | facebook-post             |            45 |               28 |                27 |       0.964 |             2 |
| 2025-04-13_avand-in-vedere-lipsa-de-reactie-a-institutiilor-responsabil        | 2025-04-13 | facebook-post             |            42 |               26 |                26 |       1     |             2 |
| 2025-04-13_condamn-cu-fermitate-atacul-criminal-de-azi-al-rusiei-care-a        | 2025-04-13 | facebook-post             |            85 |               55 |                54 |       0.982 |             4 |
| 2025-04-13_coruptia-e-motivul-principal-pentru-care-oamenii-o-duc-greu         | 2025-04-13 | facebook-post             |            47 |               24 |                24 |       1     |             3 |
| 2025-04-13_primul-week-end-strazi-deschise-bucuresti-promenada-urbana-c        | 2025-04-13 | facebook-post             |           118 |               82 |                72 |       0.878 |             5 |
| 2025-04-13_targul-de-paste-traditii-si-flori-de-sarbatori-s-a-deschis-i        | 2025-04-13 | facebook-post             |            88 |               55 |                51 |       0.927 |             5 |
| 2025-04-14_de-la-ce-functie-in-sus-considera-biroul-electoral-central-c        | 2025-04-14 | facebook-post             |           231 |              125 |                91 |       0.728 |            10 |
| 2025-04-14_intarirea-pozitiei-romaniei-in-nato-si-ue-incepe-cu-consulta        | 2025-04-14 | facebook-post             |            22 |               14 |                14 |       1     |             1 |
| 2025-04-14_ne-dorim-ca-fetita-si-baietelul-nostru-sa-traiasca-in-romani        | 2025-04-14 | facebook-post             |            25 |               12 |                12 |       1     |             2 |
| 2025-04-14_presedintele-absent-iohannis-si-tandemul-psd-pnl-au-tolerat         | 2025-04-14 | facebook-post             |            54 |               31 |                30 |       0.968 |             2 |
| 2025-04-15_activitatea-suspecta-asupra-conturilor-mele-de-social-media         | 2025-04-15 | facebook-post             |            50 |               29 |                26 |       0.897 |             3 |
| 2025-04-15_avem-o-scadere-a-productiei-industriale-cu-3-9-in-primele-lu        | 2025-04-15 | facebook-post             |           131 |               82 |                73 |       0.89  |             9 |
| 2025-04-15_pe-conturile-mele-de-instagram-nicusor-dan-pg-si-tiktok-nicu        | 2025-04-15 | facebook-post             |           189 |              109 |                96 |       0.881 |            20 |
| 2025-04-15_romania-e-a-voastra-nu-o-lasati-pe-mana-lor-nicusorpresedint        | 2025-04-15 | facebook-post             |             9 |                5 |                 5 |       1     |             2 |
| 2025-04-16_astazi-a-mai-venit-o-veste-ingrozitoare-moartea-unui-tanar-d        | 2025-04-16 | facebook-post             |           197 |              107 |                91 |       0.85  |            10 |
| 2025-04-16_romanii-cenzurati-lui-marcel-ciolacu-i-se-permite-orice-ne-a        | 2025-04-16 | facebook-post             |            25 |               20 |                19 |       0.95  |             2 |
| 2025-04-16_trei-pasaje-importante-din-bucuresti-vor-fi-reabilitate-prim        | 2025-04-16 | facebook-post             |           131 |               89 |                66 |       0.742 |            14 |
| 2025-04-17_am-lansat-oficial-planul-de-actiune-pentru-oras-verde-paov-u        | 2025-04-17 | facebook-post             |           171 |              100 |                79 |       0.79  |             8 |
| 2025-04-17_o-veste-buna-astazi-primaria-capitalei-a-atras-555-de-milioa        | 2025-04-17 | facebook-post             |           105 |               55 |                52 |       0.945 |             8 |
| 2025-04-17_presedintele-imparat-nu-a-reprezentat-pe-nimeni-romania-are         | 2025-04-17 | facebook-post             |            13 |                7 |                 7 |       1     |             2 |
| 2025-04-17_suntem-atacati-cibernetic-de-2-zile-conturile-risca-sa-fie-b        | 2025-04-17 | facebook-post             |            25 |               12 |                12 |       1     |             2 |
| 2025-04-18_am-vizitat-o-fabrica-de-panificatie-unde-in-prag-de-paste-mi        | 2025-04-18 | facebook-post             |           129 |               67 |                57 |       0.851 |             7 |
| 2025-04-18_realitatea-e-simpla-ei-au-furat-romania-iar-acum-le-e-frica         | 2025-04-18 | facebook-post             |            24 |               15 |                14 |       0.933 |             3 |
| 2025-04-18_voi-fi-presedintele-care-va-face-schimbarile-dorite-de-oamen        | 2025-04-18 | facebook-post             |            14 |                9 |                 9 |       1     |             1 |
| 2025-04-19_in-noaptea-invierii-lumina-e-speranta-speranta-ca-binele-e-m        | 2025-04-19 | facebook-post             |            34 |               21 |                17 |       0.81  |             6 |
| 2025-04-19_ne-pregatim-de-paste-de-sarbatori-momentele-alaturi-de-famil        | 2025-04-19 | facebook-post             |            20 |               12 |                10 |       0.833 |             1 |
| 2025-04-20_pastele-ne-aduce-impreuna-si-ne-reaminteste-cat-de-important        | 2025-04-20 | facebook-post             |            33 |               17 |                17 |       1     |             2 |
| 2025-04-20_sarbatori-cu-bine-si-paste-luminat-tuturor-nicusordan-nd11-r        | 2025-04-20 | facebook-post             |            12 |                8 |                 7 |       0.875 |             1 |
| 2025-04-21_cu-profunda-tristete-am-aflat-vestea-trecerii-la-cele-vesnic        | 2025-04-21 | facebook-post             |            64 |               36 |                36 |       1     |             4 |
| 2025-04-22_dragi-romani-din-diaspora-ca-voi-vreau-o-tara-in-care-sa-vre        | 2025-04-22 | facebook-post             |            23 |               11 |                10 |       0.909 |             2 |
| 2025-04-22_prea-multa-nedreptate-e-in-romania-vreau-o-romanie-in-care-o        | 2025-04-22 | facebook-post             |            25 |               11 |                11 |       1     |             3 |
| 2025-04-22_preturile-mari-nu-apar-din-senin-exista-o-legatura-clara-int        | 2025-04-22 | facebook-post             |            35 |               19 |                19 |       1     |             3 |
| 2025-04-22_votul-tau-conteaza-chiar-daca-pe-unii-ii-enerveaza-asta-nicu        | 2025-04-22 | facebook-post             |            12 |                5 |                 5 |       1     |             2 |
| 2025-04-23_crin-antonescu-si-mafia-imobiliara                                  | 2025-04-23 | facebook-post             |             5 |                4 |                 4 |       1     |             1 |
| 2025-04-23_dragi-moldoveni-pe-4-mai-alegeti-o-romanie-onesta-si-puterni        | 2025-04-23 | facebook-post             |            16 |               11 |                11 |       1     |             1 |
| 2025-04-23_fara-profesori-bine-platiti-fara-investitii-in-institutiile         | 2025-04-23 | facebook-post             |            33 |               23 |                23 |       1     |             2 |
| 2025-04-23_sanatatea-e-un-drept-fundamental-in-romania-onesta-pe-care-o        | 2025-04-23 | facebook-post             |            87 |               48 |                41 |       0.854 |             6 |
| 2025-04-24_am-semnat-astazi-declaratia-universitatii-din-bucuresti-un-a        | 2025-04-24 | facebook-post             |           186 |              112 |                81 |       0.723 |             8 |
| 2025-04-24_crin-antonescu-reprezinta-garantia-ca-marcel-ciolacu-ramane         | 2025-04-24 | facebook-post             |            15 |               12 |                11 |       0.917 |             1 |
| 2025-04-24_educatia-este-temelia-unei-romanii-puternice-fiecare-copil-d        | 2025-04-24 | facebook-post             |            76 |               45 |                41 |       0.911 |             6 |
| 2025-04-24_in-loc-sa-cheltuim-pe-lucruri-care-dau-bine-in-bucuresti-am         | 2025-04-24 | facebook-post             |            60 |               32 |                29 |       0.906 |             3 |
| 2025-04-24_justitia-are-nevoie-de-o-reforma-reala-coruptia-sistemica-ti        | 2025-04-24 | facebook-post             |            29 |               20 |                19 |       0.95  |             3 |
| 2025-04-24_o-societate-dreapta-are-nevoie-de-o-justitie-libera-curajoas        | 2025-04-24 | facebook-post             |            31 |               14 |                14 |       1     |             2 |
| 2025-04-25_bucurestiul-a-facut-un-pas-important-spre-un-urbanism-respon        | 2025-04-25 | facebook-post             |           263 |              159 |               112 |       0.704 |            19 |
| 2025-04-25_haideti-alaturi-de-mine-sa-facem-dreptate-pentru-romania-nd1        | 2025-04-25 | facebook-post             |            11 |                6 |                 6 |       1     |             1 |
| 2025-04-25_la-bebe-bucuresti-familiile-gasesc-haine-si-jucarii-donate-c        | 2025-04-25 | facebook-post             |            58 |               36 |                33 |       0.917 |             3 |
| 2025-04-25_reconstruim-demnitatea-colectiva-printr-o-economie-puternica        | 2025-04-25 | facebook-post             |            12 |               11 |                11 |       1     |             1 |
| 2025-04-25_sunt-cel-mai-atacat-candidat-le-e-frica-de-schimbare-adica-d        | 2025-04-25 | facebook-post             |            17 |               10 |                10 |       1     |             2 |
| 2025-04-26_din-1990-si-pana-azi-ati-fost-si-ramaneti-un-exemplu-de-impl        | 2025-04-26 | facebook-post             |            22 |               11 |                11 |       1     |             3 |
| 2025-04-26_m-au-intrebat-multi-tineri-ce-pot-face-pentru-campania-roman        | 2025-04-26 | facebook-post             |            34 |               18 |                18 |       1     |             3 |
| 2025-04-26_o-veste-foarte-buna-toti-cateii-27-care-au-participat-astazi        | 2025-04-26 | facebook-post             |           100 |               54 |                44 |       0.815 |             7 |
| 2025-04-26_romania-are-nevoie-de-fapte-concrete-si-de-oameni-bine-inten        | 2025-04-26 | facebook-post             |            23 |               13 |                13 |       1     |             1 |
| 2025-04-26_romania-onesta-e-singura-varianta-de-schimbare-si-dreptate-p        | 2025-04-26 | facebook-post             |            16 |               10 |                10 |       1     |             2 |
| 2025-04-27_in-prea-multe-locuri-din-romania-oamenii-nu-au-acces-la-medi        | 2025-04-27 | facebook-post             |            30 |               14 |                13 |       0.929 |             3 |
| 2025-04-27_multumesc-tinerilor-bucuresteni-pentru-sustinere-pe-4-mai-ne        | 2025-04-27 | facebook-post             |            13 |                7 |                 7 |       1     |             2 |
| 2025-04-27_sa-ne-amintim-cine-e-crin-antonescu-candidatul-lui-marcel-ci        | 2025-04-27 | facebook-post             |            32 |               22 |                22 |       1     |             1 |
| 2025-04-27_se-intreaba-mamele-de-la-sate-si-din-orasele-mici-ce-viitor         | 2025-04-27 | facebook-post             |            30 |               17 |                15 |       0.882 |             2 |
| 2025-04-28_dezbaterea-s-a-incheiat-voi-cum-ati-perceput-aceasta-dezbate        | 2025-04-28 | facebook-post             |           104 |               57 |                53 |       0.93  |             7 |
| 2025-04-28_mai-e-putin-incepe-in-curand-prima-confruntare-intre-candida        | 2025-04-28 | facebook-post             |            27 |               14 |                13 |       0.929 |             4 |
| 2025-04-28_multumesc-mirabela-cand-voi-fi-presedinte-voi-face-tot-ce-mi        | 2025-04-28 | facebook-post             |            21 |                9 |                 8 |       0.889 |             2 |
| 2025-04-28_un-presedinte-care-asculta-oamenii-si-gaseste-solutii-pentru        | 2025-04-28 | facebook-post             |            12 |                7 |                 7 |       1     |             1 |
| 2025-04-28_voi-participa-la-toate-cele-trei-dezbateri-cu-candidatii-la         | 2025-04-28 | facebook-post             |            67 |               32 |                31 |       0.969 |             3 |
| 2025-04-29_adevarul-va-invinge-suntem-prea-multi-sa-nu-putem-reusi-nicu        | 2025-04-29 | facebook-post             |            12 |                7 |                 7 |       1     |             2 |
| 2025-04-29_de-ziua-veteranilor-de-razboi-cinstim-curajul-celor-care-au         | 2025-04-29 | facebook-post             |            53 |               26 |                24 |       0.923 |             3 |
| 2025-04-29_domnul-crin-antonescu-cere-documentele-pe-care-de-altfel-i-l        | 2025-04-29 | facebook-post             |           126 |               68 |                54 |       0.794 |            11 |
| 2025-04-29_multumesc-pentru-sprijinul-vostru-am-dovedit-in-bucuresti-re        | 2025-04-29 | facebook-post             |            17 |               10 |                 9 |       0.9   |             2 |
| 2025-04-29_sistemul-are-nume-de-20-de-ani-ma-lupt-cu-el-romaniaonesta-n        | 2025-04-29 | facebook-post             |            12 |                6 |                 6 |       1     |             2 |
| 2025-04-29_succes-nicusor-echipa-nd                                            | 2025-04-29 | facebook-post             |             4 |                4 |                 4 |       1     |             1 |
| 2025-04-30_actele-confirma-ce-spun-eu-va-multumesc-ca-va-uitati-la-dezb        | 2025-04-30 | facebook-post             |            13 |                7 |                 7 |       1     |             4 |
| 2025-04-30_de-la-mirabela-cu-drag-romaniaonesta                                | 2025-04-30 | facebook-post             |             6 |                3 |                 3 |       1     |             1 |
| 2025-04-30_diaspora-este-parte-din-viitorul-romaniei-romaniaonesta             | 2025-04-30 | facebook-post             |             7 |                5 |                 5 |       1     |             1 |
| 2025-05-01_disperarea-atinge-cote-maxime-marcel-ciolacu-a-ajuns-sa-trim        | 2025-05-01 | facebook-post             |            32 |               23 |                23 |       1     |             2 |
| 2025-05-01_este-incalificabil-sa-folosesti-romanii-bolnavi-de-cancer-ca        | 2025-05-01 | facebook-post             |           146 |               80 |                67 |       0.838 |             6 |
| 2025-05-01_in-cateva-minute-live-la-lucian-mindruta-material-publicitar        | 2025-05-01 | facebook-post             |            25 |               22 |                22 |       1     |             2 |
| 2025-05-01_ne-vedem-la-vot-daca-plecati-in-vacanta-nu-uitati-buletinele        | 2025-05-01 | facebook-post             |            14 |                9 |                 9 |       1     |             2 |
| 2025-05-01_pozele-pe-care-le-a-postat-elena-lasconi-sunt-un-fals-grosol        | 2025-05-01 | facebook-post             |            42 |               32 |                32 |       1     |             5 |
| 2025-05-01_sa-ne-amintim-cine-este-victor-ponta-alegeriprezidentiale           | 2025-05-01 | facebook-post             |             8 |                4 |                 4 |       1     |             1 |
| 2025-05-01_sunt-candidatul-pro-european-care-il-poate-invinge-pe-simion        | 2025-05-01 | facebook-post             |            11 |                7 |                 7 |       1     |             1 |
| 2025-05-02_ai-plecat-din-localitate-in-minivacanta-de-1-mai-poti-vota-o        | 2025-05-02 | facebook-post             |            15 |                8 |                 8 |       1     |             2 |
| 2025-05-02_astazi-celebram-energia-curajul-si-visurile-unei-generatii-c        | 2025-05-02 | facebook-post             |            47 |               26 |                24 |       0.923 |             4 |
| 2025-05-02_daca-esti-plecat-din-romania-pe-4-mai-poti-vota-in-tara-in-c        | 2025-05-02 | facebook-post             |            25 |               13 |                13 |       1     |             2 |
| 2025-05-02_dezinformare-marca-ciolacu-coalitia-lui-ciolacu-spune-ca-doa        | 2025-05-02 | facebook-post             |            24 |               15 |                14 |       0.933 |             2 |
| 2025-05-02_diaspora-voteaza-lista-cu-sectiile-de-votare-din-strainatate        | 2025-05-02 | facebook-post             |            12 |                9 |                 9 |       1     |             2 |
| 2025-05-02_iesim-la-vot-pentru-ca-romania-are-nevoie-de-oameni-care-sa         | 2025-05-02 | facebook-post             |            20 |               11 |                11 |       1     |             1 |
| 2025-05-02_multumesc-din-suflet-tuturor-voluntarilor-si-sustinatorilor         | 2025-05-02 | facebook-post             |            34 |               14 |                14 |       1     |             3 |
| 2025-05-02_multumim-bec-pentru-consecventa-fotografiile-false-vor-circu        | 2025-05-02 | facebook-post             |            37 |               31 |                31 |       1     |             4 |
| 2025-05-02_romani-din-diaspora-mergeti-la-vot-fiecare-vot-conteaza-pent        | 2025-05-02 | facebook-post             |            15 |               10 |                 9 |       0.9   |             2 |
| 2025-05-02_votati-cu-inima-impacata-nicusor-presedinte-romaniaonesta           | 2025-05-02 | facebook-post             |             7 |                6 |                 6 |       1     |             1 |
| 2025-05-03_ca-inainte-de-vot-tinerii-nostri-vor-avea-un-rol-decisiv-la         | 2025-05-03 | facebook-post             |            20 |               11 |                10 |       0.909 |             1 |
| 2025-05-03_cu-cravata-sau-fara-maine-iesim-la-vot-4mai-alegeriprezident        | 2025-05-03 | facebook-post             |            10 |                4 |                 4 |       1     |             1 |
| 2025-05-03_daca-sunteti-plecati-de-acasa-puteti-vota-in-orice-sectie-vo        | 2025-05-03 | facebook-post             |            21 |               12 |                12 |       1     |             2 |
| 2025-05-03_daca-sunteti-plecati-in-vacanta-va-rog-sa-votati-dimineata-d        | 2025-05-03 | facebook-post             |            22 |               13 |                13 |       1     |             2 |
| 2025-05-03_daca-votati-in-diaspora-tineti-cont-ca-sectiile-se-inchid-la        | 2025-05-03 | facebook-post             |            19 |               14 |                12 |       0.857 |             2 |
| 2025-05-03_in-doar-5-minute-poti-decide-cum-arata-urmatorii-5-ani-pentr        | 2025-05-03 | facebook-post             |            16 |               11 |                11 |       1     |             2 |
| 2025-05-03_romania-are-nevoie-de-o-presa-onesta-de-ziua-internationala         | 2025-05-03 | facebook-post             |            65 |               31 |                28 |       0.903 |             3 |
| 2025-05-03_viitorul-vostru-alegerea-voastra-nu-lasati-pe-altii-sa-decid        | 2025-05-03 | facebook-post             |            20 |               11 |                11 |       1     |             2 |
| 2025-05-04_a-mai-ramas-o-ora-dreptul-vostru-alegerea-voastra-hailavot-a        | 2025-05-04 | facebook-post             |            10 |                6 |                 6 |       1     |             2 |
| 2025-05-04_am-intrat-in-turul-2-multumesc-foto-credit-mihai-balanescu-p        | 2025-05-04 | facebook-post             |            12 |                9 |                 9 |       1     |             2 |
| 2025-05-04_astazi-decidem-soarta-romaniei-hai-la-vot-alegeriprezidentia        | 2025-05-04 | facebook-post             |            10 |                8 |                 7 |       0.875 |             2 |
| 2025-05-04_daca-la-ora-21-00-va-aflati-in-sectia-de-votare-sau-la-rand         | 2025-05-04 | facebook-post             |            24 |               12 |                11 |       0.917 |             4 |
| 2025-05-04_energie-pentru-echipa-hailavot                                      | 2025-05-04 | facebook-post             |             4 |                3 |                 3 |       1     |             1 |
| 2025-05-04_eu-si-mirabela-am-votat-voi-alegeriprezidentiale-romania-vot        | 2025-05-04 | facebook-post             |            10 |                6 |                 6 |       1     |             1 |
| 2025-05-04_hai-sa-le-aratam-ca-suntem-mai-puternici-decat-instrumentele        | 2025-05-04 | facebook-post             |            18 |               11 |                 9 |       0.818 |             2 |
| 2025-05-04_mai-sunt-3-ore-pana-la-inchiderea-urnelor-si-drumurile-de-la        | 2025-05-04 | facebook-post             |            29 |               16 |                15 |       0.938 |             3 |
| 2025-05-04_mai-sunt-5-ore-pana-la-inchiderea-sectiilor-de-votare-daca-s        | 2025-05-04 | facebook-post             |            37 |               19 |                16 |       0.842 |             3 |
| 2025-05-04_mai-sunt-cateva-ore-profitati-de-aceste-cateva-ore-si-merget        | 2025-05-04 | facebook-post             |            24 |                9 |                 8 |       0.889 |             3 |
| 2025-05-04_multumesc-tare-mult-pentru-sprijin-multumesc-celor-care-m-au        | 2025-05-04 | facebook-post             |            36 |               17 |                16 |       0.941 |             3 |
| 2025-05-04_o-prezenta-mare-la-urne-le-strica-planurile-alegerea-ta-poat        | 2025-05-04 | facebook-post             |            80 |               35 |                29 |       0.829 |             7 |
| 2025-05-05_prin-votul-romanilor-de-ieri-s-a-incheiat-o-epoca-politica-s        | 2025-05-05 | facebook-post             |            60 |               31 |                30 |       0.968 |             3 |
| 2025-05-05_romania-are-o-sansa-le-multumesc-tuturor-celor-care-au-votat        | 2025-05-05 | facebook-post             |           143 |               77 |                65 |       0.844 |            12 |
| 2025-05-06_6-mai-1990-podul-de-flori-ziua-in-care-prutul-a-unit-nu-a-de        | 2025-05-06 | facebook-post             |           121 |               62 |                52 |       0.839 |             6 |
| 2025-05-06_curajul-si-puterea-femeilor-care-aleg-sa-plece-din-relatii-t        | 2025-05-06 | facebook-post             |            97 |               52 |                46 |       0.885 |             5 |
| 2025-05-07_am-vorbit-azi-in-cadrul-unui-eveniment-organizat-de-romanian        | 2025-05-07 | facebook-post             |           119 |               65 |                57 |       0.877 |             5 |
| 2025-05-07_ce-ma-deosebeste-de-contracandidatul-meu-este-aventura-in-ca        | 2025-05-07 | facebook-post             |            30 |               15 |                14 |       0.933 |             2 |
| 2025-05-07_eu-sunt-aici-pentru-dezbateri-asa-cum-am-fost-si-in-primul-t        | 2025-05-07 | facebook-post             |            39 |               19 |                19 |       1     |             3 |
| 2025-05-08_clasa-politica-i-a-ignorat-si-tradat-pe-cetateni-dar-raspuns        | 2025-05-08 | facebook-post             |            16 |                9 |                 9 |       1     |             2 |
| 2025-05-08_fapte-sau-vorbe-alegeti-intelept-pe-18-mai-alegeriprezidenti        | 2025-05-08 | facebook-post             |             8 |                5 |                 5 |       1     |             2 |
| 2025-05-08_ipocrizia-lui-george-simion-este-clara-nu-si-asuma-opiniile         | 2025-05-08 | facebook-post             |            48 |               28 |                25 |       0.893 |             3 |
| 2025-05-08_prima-dezbatere-cu-contracandidatul-meu-sustinerea-voastra-i        | 2025-05-08 | facebook-post             |            12 |                5 |                 5 |       1     |             2 |
| 2025-05-08_salut-alegerea-noului-papa-leon-al-xiv-lea-si-sunt-alaturi-d        | 2025-05-08 | facebook-post             |            55 |               30 |                30 |       1     |             2 |
| 2025-05-09_alegerile-de-pe-18-mai-au-legatura-cu-facturile-pe-care-le-p        | 2025-05-09 | facebook-post             |            23 |               10 |                 9 |       0.9   |             2 |
| 2025-05-09_avem-un-potential-urias-romaniaonesta-nicusorpresedinte-nicu        | 2025-05-09 | facebook-post             |             8 |                6 |                 6 |       1     |             1 |
| 2025-05-09_la-multi-ani-europa-astazi-de-ziua-europei-celebram-nu-doar         | 2025-05-09 | facebook-post             |           206 |              117 |                94 |       0.803 |             8 |
| 2025-05-09_la-multi-ani-europa-foto-inquam-photos-octav-ganea                  | 2025-05-09 | facebook-post             |             9 |                7 |                 7 |       1     |             1 |
| 2025-05-09_oamenii-se-uita-la-fapte-alegeriprezidentiale                       | 2025-05-09 | facebook-post             |             6 |                5 |                 5 |       1     |             1 |
| 2025-05-09_pacea-se-obtine-prin-descurajarea-razboiului-romaniaonesta          | 2025-05-09 | facebook-post             |             7 |                6 |                 6 |       1     |             1 |
| 2025-05-09_ucraina-trebuie-sa-aiba-parte-de-o-pace-justa-securitatenati        | 2025-05-09 | facebook-post             |            10 |                7 |                 7 |       1     |             1 |
| 2025-05-10_astazi-10-mai-celebram-ziua-independentei-de-stat-a-romaniei        | 2025-05-10 | facebook-post             |           129 |               62 |                50 |       0.806 |             6 |
| 2025-05-10_de-ce-se-bucura-simion-de-pierderea-dreptului-romanilor-la-c        | 2025-05-10 | facebook-post             |            15 |                8 |                 8 |       1     |             1 |
| 2025-05-10_george-simion-si-a-dezvaluit-adevarata-fata-un-suveranist-de        | 2025-05-10 | facebook-post             |            65 |               34 |                33 |       0.971 |             3 |
| 2025-05-10_o-tara-care-isi-doreste-sa-fie-sigura-si-in-care-legea-este         | 2025-05-10 | facebook-post             |           106 |               55 |                50 |       0.909 |             6 |
| 2025-05-10_p-rerea-mea-despre-diaspora-diaspora-romaniaonesta-nicusorpr        | 2025-05-10 | facebook-post             |             7 |                5 |                 4 |       0.8   |             1 |
| 2025-05-10_romania-nu-si-permite-sa-faca-un-experiment-sa-vada-cum-ar-f        | 2025-05-10 | facebook-post             |            53 |               29 |                28 |       0.966 |             5 |
| 2025-05-11_atacurile-botilor-continua-si-nu-intamplator-sunt-vizate-pos        | 2025-05-11 | facebook-post             |            51 |               27 |                26 |       0.963 |             3 |
| 2025-05-11_multumesc-araicu-ca-ai-ales-sa-fii-o-voce-in-fata-romanilor         | 2025-05-11 | facebook-post             |            25 |               13 |                13 |       1     |             1 |
| 2025-05-11_multumesc-geluduminica-ca-ai-urcat-pe-scena-romaniainlumina         | 2025-05-11 | facebook-post             |            31 |               16 |                15 |       0.938 |             2 |
| 2025-05-11_nu-putem-trece-cu-vederea-faptul-ca-george-simion-a-dat-sper        | 2025-05-11 | facebook-post             |            44 |               24 |                20 |       0.833 |             2 |
| 2025-05-11_romania-are-nevoie-de-noi-toti-traim-vremuri-care-ne-pun-la         | 2025-05-11 | facebook-post             |            84 |               42 |                37 |       0.881 |             8 |
| 2025-05-11_scoala-trebuie-sa-i-ajute-pe-copii-sa-si-dezvolte-gandirea-c        | 2025-05-11 | facebook-post             |            15 |               11 |                11 |       1     |             1 |
| 2025-05-11_va-astept-in-piata-victoriei-incepand-cu-ora-18-00-romaniaco        | 2025-05-11 | facebook-post             |            11 |                8 |                 8 |       1     |             1 |
| 2025-05-12_aceasta-este-diploma-mea-de-bacalaureat-in-original-varianta        | 2025-05-12 | facebook-post             |            29 |               16 |                16 |       1     |             3 |
| 2025-05-12_credem-in-noi-si-in-romania-mai-avem-de-facut-un-ultim-efort        | 2025-05-12 | facebook-post             |            17 |                6 |                 6 |       1     |             2 |
| 2025-05-12_echilibru-si-o-schimbare-in-bine-sau-haos-social-si-dezastru        | 2025-05-12 | facebook-post             |            30 |               16 |                16 |       1     |             2 |
| 2025-05-12_impreuna-putem-construi-o-romanie-in-care-copiii-nostri-sa-r        | 2025-05-12 | facebook-post             |            41 |               19 |                17 |       0.895 |             2 |
| 2025-05-12_intotdeauna-inainte-de-primar-sau-presedinte-voi-fi-un-om-pr        | 2025-05-12 | facebook-post             |            43 |               23 |                22 |       0.957 |             3 |
| 2025-05-12_mari-si-mici-deopotriva-cu-acelasi-gand-romaniainlumina             | 2025-05-12 | facebook-post             |             8 |                5 |                 5 |       1     |             1 |
| 2025-05-12_multumesc-medeleanumelania-pentru-felul-in-care-in-care-ai-e        | 2025-05-12 | facebook-post             |            14 |                6 |                 6 |       1     |             1 |
| 2025-05-12_romania-are-nevoie-de-un-presedinte-curajos-care-se-prezinta        | 2025-05-12 | facebook-post             |            20 |               12 |                12 |       1     |             2 |
| 2025-05-12_romania-onesta-este-schimbarea-care-ne-uneste-nicusordan            | 2025-05-12 | facebook-post             |             8 |                5 |                 5 |       1     |             1 |
| 2025-05-13_contracandidatul-meu-este-inca-dator-sa-explice-cine-sunt-pa        | 2025-05-13 | facebook-post             |            14 |                8 |                 8 |       1     |             1 |
| 2025-05-13_iti-multumesc-delia-grigore-pentru-ca-esti-vocea-romilor-din        | 2025-05-13 | facebook-post             |            30 |               15 |                15 |       1     |             1 |
| 2025-05-13_multe-am-invatat-de-la-domnul-victor-rebengiuc-ii-multumesc         | 2025-05-13 | facebook-post             |            18 |                9 |                 9 |       1     |             2 |
| 2025-05-13_niciodata-nu-am-suportat-nedreptatea-de-20-ani-lupt-pentru-d        | 2025-05-13 | facebook-post             |            16 |                9 |                 9 |       1     |             2 |
| 2025-05-13_o-romanie-buna-pentru-toti-romanii-din-tara-din-diaspora-din        | 2025-05-13 | facebook-post             |            17 |               11 |                11 |       1     |             2 |
| 2025-05-13_oana-gheorghiu-este-omul-care-a-strans-milioane-de-romani-in        | 2025-05-13 | facebook-post             |            30 |               16 |                16 |       1     |             3 |
| 2025-05-13_totul-pleaca-de-la-educatie-un-popor-puternic-are-nevoie-de         | 2025-05-13 | facebook-post             |            17 |                7 |                 7 |       1     |             2 |
| 2025-05-13_vin-dintr-o-familie-simpla-dintr-un-oras-mic-al-romaniei-am         | 2025-05-13 | facebook-post             |            36 |               18 |                17 |       0.944 |             3 |
| 2025-05-13_vom-redresa-economia-si-vom-pune-ordine-in-cheltuielile-stat        | 2025-05-13 | facebook-post             |            18 |               14 |                13 |       0.929 |             2 |
| 2025-05-14_a-patra-dezbatere-consecutiva-a-patra-oara-cand-george-simio        | 2025-05-14 | facebook-post             |            23 |               17 |                17 |       1     |             2 |
| 2025-05-14_am-primit-cu-multa-emotie-si-recunostinta-mesajul-presedinte        | 2025-05-14 | facebook-post             |           108 |               67 |                64 |       0.955 |             7 |
| 2025-05-14_banii-folositi-de-stat-pentru-retetele-compensate-nu-sunt-si        | 2025-05-14 | facebook-post             |            39 |               24 |                23 |       0.958 |             2 |
| 2025-05-14_george-simion-nu-fuge-doar-de-dezbatere-ci-si-de-propriii-su        | 2025-05-14 | facebook-post             |            15 |                9 |                 9 |       1     |             1 |
| 2025-05-14_gicu-micu-din-spania-este-unul-dintre-milioanele-de-romani-c        | 2025-05-14 | facebook-post             |            25 |               14 |                13 |       0.929 |             2 |
| 2025-05-14_ii-multumesc-prim-ministrului-poloniei-donald-tusk-pentru-ac        | 2025-05-14 | facebook-post             |            65 |               36 |                33 |       0.917 |             2 |
| 2025-05-14_insusi-omul-pe-care-isi-cladeste-campania-george-simion-spun        | 2025-05-14 | facebook-post             |            31 |               19 |                17 |       0.895 |             2 |
| 2025-05-14_lapte-cu-mamaliga-amintiri-radacini                                 | 2025-05-14 | facebook-post             |             5 |                4 |                 4 |       1     |             1 |
| 2025-05-14_vocea-femeilor-trebuie-auzita-multumesc-din-inima-adagales-r        | 2025-05-14 | facebook-post             |             9 |                7 |                 7 |       1     |             2 |
| 2025-05-15_cine-pe-cine-ia-de-mana-imparte-sau-nu-george-simion-pareril        | 2025-05-15 | facebook-post             |            30 |               15 |                12 |       0.8   |             6 |
| 2025-05-15_contracandidatul-meu-minte-ca-o-gazeta-ruseasca-nu-exista-ni        | 2025-05-15 | facebook-post             |            94 |               54 |                53 |       0.981 |             6 |
| 2025-05-15_este-intolerabil-sa-jignesti-sute-de-mii-de-copii-si-adulti         | 2025-05-15 | facebook-post             |           127 |               73 |                66 |       0.904 |             6 |
| 2025-05-15_ii-multumesc-starului-imsebastianstan-care-a-castigat-globul        | 2025-05-15 | facebook-post             |            36 |               22 |                22 |       1     |             2 |
| 2025-05-15_romania-are-speranta-drumul-spre-stabilitate-cere-seriozitat        | 2025-05-15 | facebook-post             |            37 |               25 |                25 |       1     |             3 |
| 2025-05-15_simion-si-interlopii-spune-mi-cu-cine-umbli-ca-sa-iti-spun-c        | 2025-05-15 | facebook-post             |            41 |               24 |                20 |       0.833 |             3 |
| 2025-05-15_simion-si-partidul-lui-despre-femei-felul-in-care-un-barbat         | 2025-05-15 | facebook-post             |            61 |               28 |                22 |       0.786 |             3 |
| 2025-05-15_suntem-o-familie-cu-doi-copii-minunati-cladita-pe-iubire-si         | 2025-05-15 | facebook-post             |            27 |               13 |                13 |       1     |             2 |
| 2025-05-15_va-multumesc-pentru-sutele-de-mesaje-in-care-imi-spuneti-ca         | 2025-05-15 | facebook-post             |            36 |               21 |                21 |       1     |             3 |
| 2025-05-16_am-insotit-un-grup-de-lucratori-dintr-un-depozit-la-iesirea         | 2025-05-16 | facebook-post             |            34 |               15 |                15 |       1     |             2 |
| 2025-05-16_cirese-si-bujori-de-la-oamenii-vrednici-e-plina-romania-de-e        | 2025-05-16 | facebook-post             |            19 |               11 |                11 |       1     |             3 |
| 2025-05-16_eu-si-credinta-s-au-spus-multe-minciuni-despre-mine-in-aceas        | 2025-05-16 | facebook-post             |            42 |               24 |                20 |       0.833 |             3 |
| 2025-05-16_final-de-campanie-o-campanie-onesta-pentru-o-romanie-onesta         | 2025-05-16 | facebook-post             |            31 |               18 |                14 |       0.778 |             3 |
| 2025-05-16_in-timp-ce-contracandidatul-meu-jignea-poporul-francez-chiar        | 2025-05-16 | facebook-post             |            72 |               41 |                38 |       0.927 |             3 |
| 2025-05-16_multumesc-andreeamarinromania-romaniaonesta-faravotpierdemto        | 2025-05-16 | facebook-post             |             4 |                3 |                 3 |       1     |             1 |
| 2025-05-16_multumesc-horiatecau-romaniaonesta-faravotpierdemtot                | 2025-05-16 | facebook-post             |             4 |                3 |                 3 |       1     |             1 |
| 2025-05-16_nu-voi-vota-omul-perfect-votez-omul-onest-multumesc-mihaimor        | 2025-05-16 | facebook-post             |            17 |               14 |                12 |       0.857 |             2 |
| 2025-05-16_romania-care-munceste-merita-respect-si-sustinere-am-fost-la        | 2025-05-16 | facebook-post             |            54 |               30 |                26 |       0.867 |             4 |
| 2025-05-16_romania-nu-are-nevoie-de-vanzatori-de-iluzii-romaniaonesta-n        | 2025-05-16 | facebook-post             |            11 |                6 |                 6 |       1     |             1 |
| 2025-05-16_sa-ne-ascultam-unii-pe-altii-sa-nu-ne-certam-ne-unim-si-impr        | 2025-05-16 | facebook-post             |            19 |                8 |                 8 |       1     |             2 |
| 2025-05-16_sunt-oamenii-care-duc-romania-in-toata-europa-pe-ploaie-nins        | 2025-05-16 | facebook-post             |            29 |               15 |                15 |       1     |             2 |
| 2025-05-16_tractorul-porneste-si-pana-pe-camp-arzi-motorina-de-200-de-l        | 2025-05-16 | facebook-post             |            37 |               18 |                18 |       1     |             3 |
| 2025-05-16_voluntarii-au-fost-inima-campaniei-noastre-o-inima-care-bate        | 2025-05-16 | facebook-post             |            16 |               10 |                 9 |       0.9   |             3 |
| 2025-05-17_astazi-am-fost-invitat-de-studentii-din-grozavesti-la-o-lect        | 2025-05-17 | facebook-post             |            14 |                7 |                 7 |       1     |             2 |
| 2025-05-17_continuati-sa-credeti-in-romania-si-iesiti-la-vot-nu-e-o-ale        | 2025-05-17 | facebook-post             |            21 |               11 |                11 |       1     |             2 |
| 2025-05-17_dragi-romani-din-diaspora-dreptul-vostru-alegerea-voastra-do        | 2025-05-17 | facebook-post             |            32 |               14 |                14 |       1     |             3 |
| 2025-05-17_gust-romanesc-nimic-nu-se-compara-cu-legumele-proaspete-de-l        | 2025-05-17 | facebook-post             |            19 |               13 |                13 |       1     |             1 |
| 2025-05-17_maine-este-o-zi-importanta-pentru-romania-si-trebuie-sa-cont        | 2025-05-17 | facebook-post             |            17 |                8 |                 8 |       1     |             1 |
| 2025-05-17_romania-poate-fi-din-nou-locul-in-care-femeile-aleg-sa-raman        | 2025-05-17 | facebook-post             |            29 |                9 |                 9 |       1     |             1 |
| 2025-05-18_a-fost-o-mobilizare-fara-precedent-si-de-aceea-victoria-este        | 2025-05-18 | facebook-post             |            65 |               33 |                31 |       0.939 |             3 |
| 2025-05-18_am-plecat-spre-fagaras-cu-mic-cu-mare-votul-este-despre-noi         | 2025-05-18 | facebook-post             |            30 |               14 |                12 |       0.857 |             4 |
| 2025-05-18_am-votat-astazi-la-fagaras-in-orasul-meu-natal-in-scoala-in         | 2025-05-18 | facebook-post             |           173 |               71 |                60 |       0.845 |             8 |
| 2025-05-18_cand-te-intorci-acasa-stii-ca-ai-radacini-dar-si-ca-porti-o         | 2025-05-18 | facebook-post             |            13 |                6 |                 6 |       1     |             2 |
| 2025-05-18_cu-nostalgie-si-incredere-in-generatiile-tinere-de-azi-va-in        | 2025-05-18 | facebook-post             |            15 |                7 |                 7 |       1     |             2 |
| 2025-05-18_fiecare-vot-conteaza-iesim-la-vot-astazi-ca-sa-nu-regretam-m        | 2025-05-18 | facebook-post             |            12 |                5 |                 4 |       0.8   |             2 |
| 2025-05-18_important-daca-ora-21-00-va-prinde-la-sectia-de-votare-aveti        | 2025-05-18 | facebook-post             |            27 |               13 |                11 |       0.846 |             3 |
| 2025-05-18_multumesc-ne-vedem-in-cateva-minute-la-cismigiu                     | 2025-05-18 | facebook-post             |             8 |                3 |                 3 |       1     |             2 |
| 2025-05-18_putem-schimba-lumea-in-primul-rand-cu-implicare-e-timpul-vos        | 2025-05-18 | facebook-post             |             9 |                5 |                 5 |       1     |             3 |
| 2025-05-18_raman-recunoscator-fiecarui-roman-care-alege-sa-si-exercite         | 2025-05-18 | facebook-post             |            15 |                8 |                 7 |       0.875 |             2 |
| 2025-05-18_romaniaonesta-e-foarte-aproape-sa-se-implineasca-asteptam-nu        | 2025-05-18 | facebook-post             |            10 |                8 |                 8 |       1     |             2 |
| 2025-05-18_un-gand-special-de-recunostinta-si-multumiri-cetatenilor-rom        | 2025-05-18 | facebook-post             |            38 |               23 |                23 |       1     |             3 |
| 2025-05-18_votam-azi-ca-sa-nu-ne-para-rau-maine                                | 2025-05-18 | facebook-post             |             9 |                3 |                 3 |       1     |             1 |
| 2025-05-18_votul-este-un-drept-dar-si-o-responsabilitate-tu-decizi-pent        | 2025-05-18 | facebook-post             |            11 |                4 |                 4 |       1     |             2 |
| 2025-05-21_am-avut-o-prima-discutie-informala-cu-presedinta-parlamentul        | 2025-05-21 | facebook-post             |            20 |               12 |                12 |       1     |             2 |
| 2025-05-21_prioritatea-principala-in-aceasta-perioada-este-corectarea-d        | 2025-05-21 | facebook-post             |            67 |               41 |                40 |       0.976 |             3 |
| 2025-05-22_am-fost-bucuros-sa-particip-la-gala-repatriot-un-eveniment-d        | 2025-05-22 | facebook-post             |            62 |               36 |                32 |       0.889 |             4 |
| 2025-05-22_astazi-am-primit-validarea-mandatului-de-presedinte-al-roman        | 2025-05-22 | facebook-post             |            78 |               41 |                39 |       0.951 |             6 |
| 2025-05-23_dragi-bucuresteni-orasul-apartine-oamenilor-nu-functiilor-ia        | 2025-05-23 | facebook-post             |           175 |              103 |                89 |       0.864 |            10 |
| 2025-05-24_investitia-in-educatia-tinerilor-ii-va-ajuta-pe-ei-sa-creasc        | 2025-05-24 | facebook-post             |           149 |               83 |                71 |       0.855 |             8 |
| 2025-05-24_romania-continuam-pe-drumul-democratic-pro-european-si-trans        | 2025-05-24 | facebook-post             |           255 |              124 |               102 |       0.823 |            21 |
| 2025-05-25_am-ajuns-la-varsovia-unde-am-o-prima-discutie-cu-prim-minist        | 2025-05-25 | facebook-post             |            13 |                8 |                 7 |       0.875 |             1 |
| 2025-05-25_am-avut-astazi-o-discutie-utila-si-foarte-placuta-cu-o-parte        | 2025-05-25 | facebook-post             |            81 |               45 |                38 |       0.844 |             4 |
| 2025-05-25_am-participat-astazi-cu-emotie-si-speranta-la-marsul-milionu        | 2025-05-25 | facebook-post             |            95 |               52 |                47 |       0.904 |             6 |
| 2025-05-25_cu-ocazia-zilei-romanilor-de-pretutindeni-gandurile-mele-se         | 2025-05-25 | facebook-post             |            87 |               39 |                37 |       0.949 |             5 |
| 2025-05-26_astazi-am-depus-juramantul-in-fata-parlamentului-romaniei-ca        | 2025-05-26 | facebook-post             |           103 |               55 |                52 |       0.945 |             8 |
| 2025-05-28_am-fost-onorat-sa-port-o-discutie-cu-presedintele-donald-tru        | 2025-05-28 | facebook-post             |            74 |               41 |                37 |       0.902 |             4 |
| 2025-05-29_decizia-surprinzatoare-a-curtii-constitutionale-anuntata-ast        | 2025-05-29 | facebook-post             |            68 |               43 |                40 |       0.93  |             3 |
| 2025-05-29_gandurile-mele-se-indreapta-catre-familiile-lovite-de-inunda        | 2025-05-29 | facebook-post             |           113 |               67 |                62 |       0.925 |             6 |
| 2025-05-31_am-fost-astazi-in-comuna-bacel-grav-afectata-de-inundatii-am        | 2025-05-31 | facebook-post             |            78 |               37 |                34 |       0.919 |             6 |
| 2025-05-31_astazi-am-fost-la-praid-alaturi-de-o-comunitate-profund-afec        | 2025-05-31 | facebook-post             |           121 |               75 |                63 |       0.84  |            11 |
| 2025-06-01_astazi-de-1-iunie-celebram-inocenta-bucuria-si-speranta-pe-c        | 2025-06-01 | facebook-post             |           139 |               56 |                49 |       0.875 |             8 |
| 2025-06-02_am-incheiat-astazi-un-summit-b9-important-la-vilnius-alaturi        | 2025-06-02 | facebook-post             |           120 |               70 |                62 |       0.886 |             7 |
| 2025-06-04_astazi-am-prezentat-principalele-teme-care-se-afla-pe-agenda        | 2025-06-04 | facebook-post             |           191 |              127 |               102 |       0.803 |            10 |
| 2025-06-08_astazi-romania-a-celebrat-o-pe-una-dintre-cele-mai-mari-spor        | 2025-06-08 | facebook-post             |            46 |               22 |                21 |       0.955 |             4 |
| 2025-06-10_i-am-urat-un-calduros-bun-venit-in-romania-majestatii-sale-f        | 2025-06-10 | facebook-post             |           146 |               83 |                76 |       0.916 |             6 |
| 2025-06-10_impreuna-suntem-mai-puternici-republicamoldova-romania              | 2025-06-10 | facebook-post             |             6 |                4 |                 4 |       1     |             1 |
| 2025-06-10_ma-bucur-sa-ma-aflu-astazi-la-chisinau-in-prima-mea-vizita-o        | 2025-06-10 | facebook-post             |            65 |               34 |                29 |       0.853 |             3 |
| 2025-06-10_participare-la-evenimentul-viitorul-european-comun-al-romani        | 2025-06-10 | facebook-post             |            18 |               14 |                12 |       0.857 |             0 |
| 2025-06-11_astazi-la-odesa-am-avut-o-discutie-foarte-buna-cu-reprezenta        | 2025-06-11 | facebook-post             |            74 |               43 |                37 |       0.86  |             5 |
| 2025-06-11_astazi-la-odesa-in-marja-summitului-ucraina-europa-de-sud-es        | 2025-06-11 | facebook-post             |           102 |               71 |                62 |       0.873 |             3 |
| 2025-06-13_mineriada-din-13-15-iunie-1990-ramane-unul-dintre-cele-mai-d        | 2025-06-13 | facebook-post             |            97 |               46 |                45 |       0.978 |             5 |
| 2025-06-16_i-am-invitat-astazi-la-palatul-cotroceni-pe-reprezentantii-s        | 2025-06-16 | facebook-post             |           101 |               55 |                53 |       0.964 |             5 |
| 2025-06-18_romania-se-confrunta-cu-un-nivel-ingrijorator-de-violenta-im        | 2025-06-18 | facebook-post             |           218 |              120 |                95 |       0.792 |            16 |
| 2025-06-20_l-am-desemnat-astazi-pe-domnul-ilie-bolojan-in-functia-de-pr        | 2025-06-20 | facebook-post             |           144 |               73 |                62 |       0.849 |            12 |
| 2025-06-25_a-fost-o-reala-onoare-sa-ma-intalnesc-cu-prim-ministrul-rega        | 2025-06-25 | facebook-post             |            69 |               44 |                41 |       0.932 |             3 |
| 2025-06-25_am-avut-o-intalnire-productiva-si-consistenta-cu-presedintel        | 2025-06-25 | facebook-post             |            86 |               50 |                46 |       0.92  |             4 |
| 2025-06-25_am-avut-o-intrevedere-foarte-buna-cu-presedintele-petr-pavel        | 2025-06-25 | facebook-post             |            65 |               41 |                36 |       0.878 |             3 |
| 2025-06-25_natosummit-usa-presidenttrump-romania                               | 2025-06-25 | facebook-post             |             4 |                4 |                 4 |       1     |             0 |
| 2025-06-26_am-avut-o-prima-intalnire-cu-membrii-romani-ai-parlamentului        | 2025-06-26 | facebook-post             |            64 |               32 |                28 |       0.875 |             3 |
| 2025-06-26_am-avut-un-dialog-foarte-bun-cu-presedintele-consiliului-eur        | 2025-06-26 | facebook-post             |            45 |               26 |                24 |       0.923 |             2 |
| 2025-07-02_am-aflat-cu-profunda-tristete-vestea-disparitiei-lui-mihai-l        | 2025-07-02 | facebook-post             |            82 |               48 |                45 |       0.938 |             5 |
| 2025-07-08_l-am-numit-astazi-pe-dacian-cosmin-dragos-in-functia-de-jude        | 2025-07-08 | facebook-post             |           176 |              101 |                81 |       0.802 |             6 |
| 2025-07-14_asa-cum-am-promis-am-publicat-astazi-pe-site-ul-administrati        | 2025-07-14 | facebook-post             |            45 |               26 |                24 |       0.923 |             4 |
| 2025-07-14_masurile-fiscale-adoptate-acum-reprezinta-o-situatie-provizo        | 2025-07-14 | facebook-post             |           207 |              113 |                87 |       0.77  |             9 |
| 2025-07-18_am-avut-o-intalnire-foarte-buna-cu-cancelarul-federal-al-ger        | 2025-07-18 | facebook-post             |           106 |               60 |                55 |       0.917 |             5 |
| 2025-07-21_ii-indemn-pe-cei-care-inca-se-indoiesc-de-interferentele-rus        | 2025-07-21 | facebook-post             |           153 |               86 |                72 |       0.837 |            15 |
| 2025-07-22_ma-ingrijoreaza-profund-rezultatele-studiului-prezentat-asta        | 2025-07-22 | facebook-post             |           215 |              126 |               113 |       0.897 |             9 |
| 2025-07-24_ieri-am-avut-o-intalnire-cu-ministrul-mediului-diana-buzoian        | 2025-07-24 | facebook-post             |           127 |               73 |                68 |       0.932 |             7 |
| 2025-07-25_am-avut-o-intalnire-constructiva-cu-reprezentanti-ai-mediulu        | 2025-07-25 | facebook-post             |            73 |               46 |                42 |       0.913 |             4 |
| 2025-07-25_austria-si-romania-intra-intr-un-nou-capitol-al-relatiei-bil        | 2025-07-25 | facebook-post             |            44 |               22 |                19 |       0.864 |             2 |
| 2025-07-26_in-cadrul-intalnirii-de-astazi-cu-cancelarul-federal-al-aust        | 2025-07-26 | facebook-post             |            85 |               50 |                47 |       0.94  |             3 |
| 2025-07-27_alaturi-de-austria-al-treilea-mare-investitor-din-romania-in        | 2025-07-27 | facebook-post             |            32 |               20 |                18 |       0.9   |             1 |
| 2025-07-28_astazi-am-avut-placerea-de-a-l-primi-la-palatul-cotroceni-pe        | 2025-07-28 | facebook-post             |            84 |               49 |                49 |       1     |             4 |
| 2025-07-29_sunt-profund-afectat-de-pierderile-de-vieti-omenesti-si-de-d        | 2025-07-29 | facebook-post             |           146 |               86 |                81 |       0.942 |             7 |
| 2025-07-30_astazi-comemorand-ziua-internationala-pentru-lupta-impotriva        | 2025-07-30 | facebook-post             |           149 |               79 |                73 |       0.924 |             4 |
| 2025-07-30_este-total-aberant-ca-pensia-pe-care-o-ia-un-magistrat-sa-fi        | 2025-07-30 | facebook-post             |           219 |              111 |                93 |       0.838 |            14 |
| 2025-07-31_astazi-in-ziua-europeana-de-comemorare-a-holocaustului-impot        | 2025-07-31 | facebook-post             |           116 |               57 |                52 |       0.912 |             5 |
| 2025-08-10_astazi-am-facut-o-drumetie-in-natura-iar-copiii-au-fost-cei         | 2025-08-10 | facebook-post             |            14 |                5 |                 5 |       1     |             1 |
| 2025-08-10_orheiul-vechi-a-rasunat-de-muzica-folk-la-festivalul-lupilor        | 2025-08-10 | facebook-post             |            18 |               12 |                12 |       1     |             2 |
| 2025-08-12_aceste-zile-petrecute-dincolo-de-prut-ne-au-reamintit-cat-de        | 2025-08-12 | facebook-post             |            38 |               18 |                18 |       1     |             2 |
| 2025-08-12_salut-eforturile-presedintelui-donald-trump-de-a-contribui-l        | 2025-08-12 | facebook-post             |            94 |               59 |                50 |       0.847 |             3 |
| 2025-08-13_am-participat-astazi-la-videoconferinta-coalitiei-de-vointa         | 2025-08-13 | facebook-post             |           119 |               55 |                45 |       0.818 |             5 |
| 2025-08-17_astazi-in-cadrul-unei-noi-videoconferinte-a-coalitiei-de-voi        | 2025-08-17 | facebook-post             |           206 |              110 |                81 |       0.736 |            12 |
| 2025-08-17_cele-mai-frumoase-locuri-pe-care-le-am-vizitat-cu-familia-su        | 2025-08-17 | facebook-post             |            28 |                9 |                 9 |       1     |             1 |
| 2025-08-18_o-veste-buna-agentia-de-rating-fitch-a-confirmat-vineri-rati        | 2025-08-18 | facebook-post             |            67 |               47 |                34 |       0.723 |             5 |
| 2025-08-18_rusia-nu-isi-doreste-pacea-in-cadrul-coalitiei-pentru-vointa        | 2025-08-18 | facebook-post             |            40 |               21 |                20 |       0.952 |             2 |
| 2025-08-19_astazi-la-videoconferintele-coalitiei-de-vointa-si-ale-consi        | 2025-08-19 | facebook-post             |            44 |               26 |                25 |       0.962 |             2 |
| 2025-08-19_videoconferintele-coalitiei-de-vointa-si-ale-consiliului-eur        | 2025-08-19 | facebook-post             |           159 |               95 |                76 |       0.8   |             9 |
| 2025-08-20_mult-respect-si-recunostinta-pentru-militarii-din-comandamen        | 2025-08-20 | facebook-post             |            37 |               19 |                19 |       1     |             3 |
| 2025-08-21_am-avut-parte-de-o-primire-calduroasa-la-rosia-montana-trebu        | 2025-08-21 | facebook-post             |            30 |               19 |                19 |       1     |             2 |
| 2025-08-26_m-am-intalnit-astazi-la-palatul-cotroceni-cu-diplomatii-roma        | 2025-08-26 | facebook-post             |           249 |              133 |               103 |       0.774 |            11 |
| 2025-08-28_condamn-cu-fermitate-agresiunea-asupra-unui-tanar-venit-la-m        | 2025-08-28 | facebook-post             |           177 |               92 |                88 |       0.957 |            12 |
| 2025-08-31_astazi-am-avut-onoarea-de-a-fi-prezent-la-marea-dictare-nati        | 2025-08-31 | facebook-post             |            86 |               48 |                39 |       0.812 |             6 |
| 2025-08-31_participare-alaturi-de-presedintele-republicii-moldova-maia         | 2025-08-31 | facebook-post             |            20 |               15 |                14 |       0.933 |             0 |
| 2025-09-01_astazi-i-am-urat-bun-venit-pe-tarmul-marii-negre-doamnei-pre        | 2025-09-01 | facebook-post             |           126 |               80 |                72 |       0.9   |             5 |
| 2025-09-01_ii-multumesc-lui-manfred-weber-pentru-vizita-de-astazi-de-la        | 2025-09-01 | facebook-post             |            54 |               32 |                31 |       0.969 |             4 |
| 2025-09-02_ieri-la-malul-marii-negre-am-intampinat-o-pe-ursula-von-der         | 2025-09-02 | facebook-post             |            56 |               30 |                27 |       0.9   |             4 |
| 2025-09-03_am-semnat-astazi-cu-respect-si-consideratie-decretul-de-deco        | 2025-09-03 | facebook-post             |            79 |               60 |                54 |       0.9   |             3 |
| 2025-09-03_astazi-am-marcat-un-moment-important-pentru-securitatea-ener        | 2025-09-03 | facebook-post             |           242 |              133 |               105 |       0.789 |            15 |
| 2025-09-03_m-am-bucurat-sa-il-primesc-astazi-la-palatul-cotroceni-pe-pr        | 2025-09-03 | facebook-post             |            98 |               53 |                47 |       0.887 |             3 |
| 2025-09-10_am-avut-astazi-o-intalnire-importanta-cu-reprezentantii-inve        | 2025-09-10 | facebook-post             |            78 |               50 |                44 |       0.88  |             5 |
| 2025-09-15_am-avut-astazi-o-discutie-excelenta-cu-secretarul-general-al        | 2025-09-15 | facebook-post             |           137 |               80 |                69 |       0.863 |             8 |
| 2025-09-16_cercetarea-prezentata-azi-de-procurorul-general-reprezinta-o        | 2025-09-16 | facebook-post             |           107 |               60 |                49 |       0.817 |             4 |
| 2025-09-17_curtea-constitutionala-a-admis-astazi-sesizarea-pe-care-am-f        | 2025-09-17 | facebook-post             |           158 |               95 |                72 |       0.758 |             5 |
| 2025-09-23_am-avut-astazi-o-intalnire-cu-liderii-coalitiei-de-guvernare        | 2025-09-23 | facebook-post             |           133 |               77 |                70 |       0.909 |             5 |
| 2025-09-24_astazi-am-avut-o-intalnire-foarte-buna-la-palatul-cotroceni         | 2025-09-24 | facebook-post             |            82 |               52 |                46 |       0.885 |             5 |
| 2025-09-24_legatura-dintre-romania-si-republica-moldova-nu-este-doar-un        | 2025-09-24 | facebook-post             |            80 |               46 |                41 |       0.891 |             5 |
| 2025-09-26_sunt-profund-indurerat-de-tragedia-petrecuta-la-spitalul-de         | 2025-09-26 | facebook-post             |           180 |              109 |                93 |       0.853 |            11 |
| 2025-09-28_dragi-basarabeni-din-romania-astazi-este-o-zi-importanta-pen        | 2025-09-28 | facebook-post             |            35 |               17 |                17 |       1     |             3 |
| 2025-09-29_cu-ocazia-implinirii-a-30-de-ani-de-la-infiintarea-aliantei         | 2025-09-29 | facebook-post             |           150 |               80 |                62 |       0.775 |             8 |
| 2025-09-29_felicit-cetatenii-republicii-moldova-pentru-mobilizare-si-pe        | 2025-09-29 | facebook-post             |            76 |               44 |                41 |       0.932 |             5 |
| 2025-09-30_am-vizitat-azi-la-timisoara-doua-companii-care-folosesc-inte        | 2025-09-30 | facebook-post             |           101 |               55 |                51 |       0.927 |             7 |
| 2025-09-30_in-luna-iulie-am-spus-ca-administratia-prezidentiala-va-cont        | 2025-09-30 | facebook-post             |           127 |               72 |                59 |       0.819 |             8 |
| 2025-09-30_marile-orase-europene-sunt-motoarele-dezvoltarii-insa-de-pre        | 2025-09-30 | facebook-post             |           133 |               76 |                65 |       0.855 |             6 |
| 2025-10-01_am-trimis-inapoi-parlamentului-o-lege-care-ar-fi-anulat-una         | 2025-10-01 | facebook-post             |           174 |               94 |                75 |       0.798 |             6 |
| 2025-10-01_astazi-si-maine-sunt-la-copenhaga-pentru-a-participa-la-reun        | 2025-10-01 | facebook-post             |            47 |               27 |                25 |       0.926 |             2 |
| 2025-10-02_a-doua-zi-a-vizitei-mele-la-copenhaga-este-dedicata-particip        | 2025-10-02 | facebook-post             |            48 |               30 |                29 |       0.967 |             2 |
| 2025-10-02_am-avut-discutie-foarte-productiva-cu-premierul-suediei-ulf         | 2025-10-02 | facebook-post             |            72 |               39 |                36 |       0.923 |             4 |
| 2025-10-02_declaratii-de-presa-sustinute-inaintea-participarii-la-reuni        | 2025-10-02 | facebook-post             |            11 |                8 |                 8 |       1     |             0 |
| 2025-10-02_le-am-prezentat-colegilor-europeni-principalele-concluzii-di        | 2025-10-02 | facebook-post             |           120 |               68 |                65 |       0.956 |             4 |
| 2025-10-02_romania-s-a-alaturat-initiativei-lansate-de-presedintele-emm        | 2025-10-02 | facebook-post             |            57 |               37 |                35 |       0.946 |             3 |
| 2025-10-02_sprijinul-nostru-pentru-republica-moldova-nu-se-opreste-am-d        | 2025-10-02 | facebook-post             |            44 |               29 |                26 |       0.897 |             3 |
| 2025-10-03_am-promulgat-astazi-legea-privind-activitatea-anre-asf-si-an        | 2025-10-03 | facebook-post             |           167 |              101 |                87 |       0.861 |             8 |
| 2025-10-06_am-anuntat-astazi-numirea-urmatorilor-consilieri-prezidentia        | 2025-10-06 | facebook-post             |           264 |              190 |               101 |       0.532 |            20 |
| 2025-10-09_am-participat-astazi-la-ceremonia-dedicata-comemorarii-victi        | 2025-10-09 | facebook-post             |           157 |               80 |                66 |       0.825 |             5 |
| 2025-10-12_la-usa-inimii-cuiva-trebuie-sa-ne-rugam-sa-navalim-sau-sa-ci        | 2025-10-12 | facebook-post             |           180 |               90 |                71 |       0.789 |            18 |
| 2025-10-13_am-primit-astazi-la-palatul-cotroceni-o-delegatie-condusa-de        | 2025-10-13 | facebook-post             |           130 |               78 |                73 |       0.936 |             6 |
| 2025-10-13_am-promulgat-astazi-legea-de-aprobare-a-ordonantei-de-urgent        | 2025-10-13 | facebook-post             |           140 |               90 |                77 |       0.856 |             4 |
| 2025-10-14_fenomenul-coruptiei-trebuie-atacat-frontal-acest-flagel-care        | 2025-10-14 | facebook-post             |            55 |               32 |                31 |       0.969 |             3 |
| 2025-10-16_am-promulgat-astazi-legea-care-sanctioneaza-coruperea-functi        | 2025-10-16 | facebook-post             |           137 |               81 |                65 |       0.802 |             9 |
| 2025-10-17_explozia-produsa-astazi-intr-un-bloc-de-pe-calea-rahovei-din        | 2025-10-17 | facebook-post             |           189 |               97 |                84 |       0.866 |            12 |
| 2025-10-20_am-avut-astazi-la-palatul-cotroceni-un-dialog-constructiv-cu        | 2025-10-20 | facebook-post             |           167 |              101 |                87 |       0.861 |             7 |
| 2025-10-20_reforma-pensiilor-magistratilor-ramane-o-prioritate-nu-este         | 2025-10-20 | facebook-post             |            72 |               43 |                35 |       0.814 |             4 |
| 2025-10-21_am-semnat-astazi-decretul-pentru-trecerea-in-rezerva-a-doamn        | 2025-10-21 | facebook-post             |           108 |               62 |                57 |       0.919 |             6 |
| 2025-10-22_am-promulgat-o-lege-care-aduce-noi-reglementari-in-domeniul         | 2025-10-22 | facebook-post             |           142 |               85 |                67 |       0.788 |             6 |
| 2025-10-22_in-drum-spre-bruxelles-la-o-noua-reuniune-a-consiliului-euro        | 2025-10-22 | facebook-post             |             8 |                5 |                 5 |       1     |             1 |
| 2025-10-23_am-promulgat-saptamana-aceasta-legea-care-ne-va-permite-sa-f        | 2025-10-23 | facebook-post             |           172 |              110 |                92 |       0.836 |             8 |
| 2025-10-23_zi-extrem-de-incarcata-la-reuniunea-liderilor-ue-de-la-bruxe        | 2025-10-23 | facebook-post             |           113 |               61 |                54 |       0.885 |             6 |
| 2025-10-24_165-de-ani-de-traditie-si-excelenta-universitara-la-iasi-ast        | 2025-10-24 | facebook-post             |           193 |              116 |                86 |       0.741 |            10 |
| 2025-10-24_antibiotice-iasi-un-simbol-al-industriei-farmaceutice-romane        | 2025-10-24 | facebook-post             |            82 |               51 |                45 |       0.882 |             3 |
| 2025-10-25_astazi-am-onorat-la-brigada-15-mecanizata-podu-inalt-din-ias        | 2025-10-25 | facebook-post             |            88 |               45 |                38 |       0.844 |             8 |
| 2025-10-25_cea-mai-mica-inima-artificiala-complet-implantabila-cu-aplic        | 2025-10-25 | facebook-post             |           160 |               92 |                78 |       0.848 |             7 |
| 2025-10-26_am-participat-alaturi-de-familie-la-sfintirea-picturii-cated        | 2025-10-26 | facebook-post             |            33 |               19 |                19 |       1     |             2 |
| 2025-10-26_azi-la-sfintirea-picturii-catedralei-nationale                      | 2025-10-26 | facebook-post             |             6 |                4 |                 4 |       1     |             0 |
| 2025-10-28_am-avut-o-discutie-constructiva-astazi-cu-valdis-dombrovskis        | 2025-10-28 | facebook-post             |           167 |               87 |                69 |       0.793 |             7 |
| 2025-10-28_cu-profund-respect-si-in-semn-de-recunoastere-pentru-devotam        | 2025-10-28 | facebook-post             |           106 |               61 |                55 |       0.902 |             4 |
| 2025-10-29_prin-redimensionarea-fortei-rotationale-care-opera-si-in-rom        | 2025-10-29 | facebook-post             |           107 |               68 |                50 |       0.735 |             5 |
| 2025-10-30_se-implinesc-astazi-10-ani-de-la-tragedia-care-a-schimbat-ro        | 2025-10-30 | facebook-post             |           311 |              166 |               131 |       0.789 |            16 |
| 2025-11-04_am-aflat-cu-profunda-tristete-vestea-ca-romanul-prins-sub-da        | 2025-11-04 | facebook-post             |            74 |               43 |                40 |       0.93  |             5 |
| 2025-11-05_i-am-urat-astazi-bun-venit-in-romania-domnului-mark-rutte-in        | 2025-11-05 | facebook-post             |           245 |              135 |                97 |       0.719 |            12 |
| 2025-11-05_multumim-emeric-ienei-pentru-toata-bucuria-pe-care-ne-ai-adu        | 2025-11-05 | facebook-post             |           166 |               93 |                79 |       0.849 |             7 |
| 2025-11-06_romania-este-mai-aparata-ca-oricand-si-pregatita-sa-si-asume        | 2025-11-06 | facebook-post             |           276 |              149 |               124 |       0.832 |            12 |
| 2025-11-07_competitivitate-si-crestere-economica-acestea-sunt-doua-cuvi        | 2025-11-07 | facebook-post             |           223 |              120 |               105 |       0.875 |             9 |
| 2025-11-07_in-semn-de-profund-respect-si-consideratie-pentru-memoria-ul        | 2025-11-07 | facebook-post             |           165 |              114 |               100 |       0.877 |             8 |
| 2025-11-09_astazi-odata-cu-repatrierea-ramasitelor-pamantesti-ale-ultim        | 2025-11-09 | facebook-post             |           266 |              155 |               121 |       0.781 |            14 |
| 2025-11-10_am-semnat-sesizarea-catre-curtea-constitutionala-in-legatura        | 2025-11-10 | facebook-post             |           194 |              126 |                96 |       0.762 |             7 |
| 2025-11-10_romania-are-toate-datele-pentru-a-deveni-un-hub-de-inovatie         | 2025-11-10 | facebook-post             |           168 |               88 |                72 |       0.818 |             7 |
| 2025-11-11_in-urma-cu-trei-decenii-trecea-la-cele-vesnice-marele-om-pol        | 2025-11-11 | facebook-post             |           191 |              110 |                91 |       0.827 |            10 |
| 2025-11-12_am-pus-astazi-in-dezbatere-strategia-nationala-de-aparare-ce        | 2025-11-12 | facebook-post             |           356 |              212 |               168 |       0.792 |            17 |
| 2025-11-13_astazi-s-a-incheiat-la-baza-militara-de-la-cincu-exercitiulu        | 2025-11-13 | facebook-post             |           286 |              173 |               126 |       0.728 |            12 |
| 2025-11-13_l-am-primit-astazi-la-palatul-cotroceni-in-prima-sa-vizita-e        | 2025-11-13 | facebook-post             |            72 |               44 |                38 |       0.864 |             3 |
| 2025-11-17_l-am-primit-astazi-la-palatul-cotroceni-pe-enrico-letta-fost        | 2025-11-17 | facebook-post             |           171 |               96 |                79 |       0.823 |             6 |
| 2025-11-18_am-avut-astazi-o-discutie-cu-fatih-birol-presedintele-agenti        | 2025-11-18 | facebook-post             |           201 |              105 |                75 |       0.714 |             7 |
| 2025-11-18_ne-a-parasit-dumitru-lupescu-era-presedinte-de-asociatie-de         | 2025-11-18 | facebook-post             |            49 |               29 |                27 |       0.931 |             5 |
| 2025-11-18_ne-luam-astazi-ramas-bun-de-la-un-patriot-care-a-crezut-si-a        | 2025-11-18 | facebook-post             |           124 |               64 |                57 |       0.891 |             5 |
| 2025-11-19_am-sesizat-curtea-constitutionala-in-legatura-cu-legea-de-ap        | 2025-11-19 | facebook-post             |           175 |              105 |                93 |       0.886 |             8 |
| 2025-11-20_operatiunea-de-readucere-in-tara-sub-escorta-a-lui-horatiu-p        | 2025-11-20 | facebook-post             |            54 |               33 |                32 |       0.97  |             2 |
| 2025-11-20_romania-a-facut-inca-un-pas-decisiv-spre-aderarea-la-ocde-am        | 2025-11-20 | facebook-post             |           250 |              156 |               121 |       0.776 |            11 |
| 2025-11-21_am-avut-astazi-la-palatul-cotroceni-o-discutie-importanta-cu        | 2025-11-21 | facebook-post             |           302 |              185 |               132 |       0.714 |            12 |
| 2025-11-21_romania-are-in-acest-moment-maturitatea-si-expertiza-pentru         | 2025-11-21 | facebook-post             |           166 |               93 |                78 |       0.839 |             9 |
| 2025-11-23_am-promulgat-saptamana-aceasta-legea-care-introduce-amendare        | 2025-11-23 | facebook-post             |            55 |               30 |                29 |       0.967 |             4 |
| 2025-11-25_a-fost-o-onoare-sa-gazduiesc-astazi-la-palatul-cotroceni-sum        | 2025-11-25 | facebook-post             |           231 |              121 |               108 |       0.893 |            10 |
| 2025-11-26_parlamentul-romaniei-a-votat-astazi-strategia-nationala-de-a        | 2025-11-26 | facebook-post             |           178 |               99 |                78 |       0.788 |            11 |
| 2025-12-01_cu-prilejul-zilei-nationale-a-romaniei-l-am-decorat-pe-veter        | 2025-12-01 | facebook-post             |           198 |              102 |                86 |       0.843 |            10 |
| 2025-12-01_ziua-nationala-este-inainte-de-toate-o-sarbatoare-a-oamenilo        | 2025-12-01 | facebook-post             |           183 |               79 |                71 |       0.899 |            10 |
| 2025-12-02_am-promulgat-recent-legea-pentru-modificarea-statutului-depu        | 2025-12-02 | facebook-post             |           194 |              127 |               107 |       0.843 |             8 |
| 2025-12-03_astazi-am-avut-o-discutie-substantiala-cu-ambasadorii-statel        | 2025-12-03 | facebook-post             |           145 |               94 |                79 |       0.84  |             7 |
| 2025-12-03_situatia-dezastruoasa-de-la-barajul-paltinu-care-a-generat-o        | 2025-12-03 | facebook-post             |           164 |               94 |                82 |       0.872 |             8 |
| 2025-12-04_am-avut-astazi-onoarea-sa-l-felicit-pe-domnul-victor-rebengi        | 2025-12-04 | facebook-post             |           197 |               98 |                81 |       0.827 |             7 |
| 2025-12-04_am-transmis-parlamentului-cererea-de-reexaminare-a-legii-car        | 2025-12-04 | facebook-post             |           137 |               84 |                74 |       0.881 |             9 |
| 2025-12-05_am-semnat-astazi-decretul-de-promulgare-a-legii-care-introdu        | 2025-12-05 | facebook-post             |           160 |               97 |                82 |       0.845 |             6 |
| 2025-12-07_dragi-bucuresteni-va-invit-sa-mergeti-la-vot-indiferent-de-o        | 2025-12-07 | facebook-post             |            79 |               32 |                31 |       0.969 |             3 |
| 2025-12-08_felicitari-si-succes-alesilor-locali-confirmati-prin-votul-d        | 2025-12-08 | facebook-post             |           131 |               78 |                69 |       0.885 |             9 |
| 2025-12-09_a-fost-o-reala-placere-sa-il-intalnesc-pe-presedintele-repub        | 2025-12-09 | facebook-post             |           130 |               81 |                71 |       0.877 |             5 |
| 2025-12-09_am-avut-in-franta-o-intalnire-cu-reprezentantii-companiilor         | 2025-12-09 | facebook-post             |           184 |              102 |                79 |       0.775 |            10 |
| 2025-12-09_am-avut-o-excelenta-intrevedere-cu-primarul-parisului-anne-h        | 2025-12-09 | facebook-post             |           206 |              112 |                92 |       0.821 |             9 |
| 2025-12-10_am-vazut-cap-coada-documentarul-recorder-despre-justitie-cel        | 2025-12-10 | facebook-post             |           330 |              165 |               113 |       0.685 |            25 |
| 2025-12-11_cand-200-de-magistrati-spun-ca-este-o-problema-de-integritat        | 2025-12-11 | facebook-post             |           101 |               53 |                42 |       0.792 |             8 |
| 2025-12-15_plec-la-summitul-de-la-helsinki-dar-iau-cu-mine-ingrijoraril        | 2025-12-15 | facebook-post             |            89 |               48 |                42 |       0.875 |             7 |
| 2025-12-16_actiunile-rusiei-reprezinta-o-amenintare-majora-pentru-regiu        | 2025-12-16 | facebook-post             |           109 |               75 |                64 |       0.853 |             7 |
| 2025-12-16_am-trimis-curtii-constitutionale-o-sesizare-de-neconstitutio        | 2025-12-16 | facebook-post             |           171 |              108 |                92 |       0.852 |             8 |
| 2025-12-16_foarte-utile-si-aplicate-discutiile-pe-care-le-am-purtat-cu         | 2025-12-16 | facebook-post             |           198 |              117 |                99 |       0.846 |             8 |
| 2025-12-17_la-londra-intr-unul-dintre-cele-mai-competitive-ecosisteme-e        | 2025-12-17 | facebook-post             |           152 |               93 |                77 |       0.828 |             6 |
| 2025-12-17_multumesc-majestatii-sale-regele-charles-al-iii-lea-pentru-p        | 2025-12-17 | facebook-post             |            15 |                7 |                 7 |       1     |             1 |
| 2025-12-17_o-intalnire-extraordinar-de-buna-si-calda-cu-comunitatea-de         | 2025-12-17 | facebook-post             |            38 |               23 |                23 |       1     |             2 |
| 2025-12-18_a-inceput-ultima-reuniune-a-consiliului-european-din-acest-a        | 2025-12-18 | facebook-post             |           108 |               67 |                57 |       0.851 |             5 |
| 2025-12-18_dialog-cu-antreprenorii-romani-si-britanici-intalniri-cu-oam        | 2025-12-18 | facebook-post             |            54 |               33 |                33 |       1     |             3 |
| 2025-12-19_am-incheiat-turneul-european-cu-ultimul-consiliu-din-acest-a        | 2025-12-19 | facebook-post             |            32 |               20 |                19 |       0.95  |             1 |
| 2025-12-20_am-primit-de-la-magistrati-sute-de-pagini-de-materiale-relev        | 2025-12-20 | facebook-post             |           126 |               64 |                55 |       0.859 |             6 |
| 2025-12-20_curtea-constitutionala-a-decis-recent-o-schimbare-esentiala         | 2025-12-20 | facebook-post             |            75 |               44 |                40 |       0.909 |             3 |
| 2025-12-21_libertate-acesta-a-fost-strigatul-limpede-al-natiunii-romane        | 2025-12-21 | facebook-post             |           428 |              231 |               185 |       0.801 |            27 |
| 2025-12-21_voi-initia-in-ianuarie-imediat-dupa-sarbatori-un-referendum         | 2025-12-21 | facebook-post             |           259 |              139 |               100 |       0.719 |            10 |
| 2025-12-25_nasterea-lui-hristos-este-pentru-noi-crestinii-sarbatoarea-s        | 2025-12-25 | facebook-post             |           124 |               55 |                52 |       0.945 |             5 |
| 2025-12-26_in-cadrul-vizitelor-externe-din-ultimele-saptamani-am-avut-b        | 2025-12-26 | facebook-post             |           119 |               63 |                53 |       0.841 |             5 |
| 2025-12-26_o-intalnire-speciala-la-paris-cu-un-regizor-si-scenarist-de         | 2025-12-26 | facebook-post             |            64 |               34 |                30 |       0.882 |             5 |
| 2025-12-27_astept-cu-ner-bdare-s-aflu-ce-a-spus-mirabela-despre-mine-in        | 2025-12-27 | facebook-post             |            19 |               10 |                10 |       1     |             1 |
| 2025-12-27_l-am-revazut-cu-mare-emotie-la-paris-pe-profesorul-emerit-la        | 2025-12-27 | facebook-post             |            94 |               49 |                45 |       0.918 |             4 |
| 2025-12-27_pe-fiul-marelui-ion-ratiu-nicolae-ratiu-l-am-revazut-la-lond        | 2025-12-27 | facebook-post             |            59 |               33 |                29 |       0.879 |             2 |
| 2025-12-28_a-fost-o-veritabila-placere-sa-il-revad-la-londra-pe-sir-geo        | 2025-12-28 | facebook-post             |            70 |               45 |                43 |       0.956 |             3 |
| 2025-12-28_redactia-romana-a-bbc-a-ramas-pana-astazi-un-reper-de-jurnal        | 2025-12-28 | facebook-post             |            63 |               34 |                31 |       0.912 |             3 |
| 2026-01-01_2025-a-fost-un-an-al-provocarilor-dar-si-al-curajului-de-a-n        | 2026-01-01 | facebook-post             |           158 |               75 |                64 |       0.853 |            10 |
| 2026-01-04_am-sperat-pana-in-ultima-clipa-intr-un-deznodamant-diferit-i        | 2026-01-04 | facebook-post             |            47 |               31 |                31 |       1     |             3 |
| 2026-01-05_cheltuielile-administratiei-prezidentiale-in-2025-au-fost-re        | 2026-01-05 | facebook-post             |            21 |               10 |                10 |       1     |             1 |
| 2026-01-06_a-inceput-reuniunea-liderilor-de-state-si-de-guverne-la-pala        | 2026-01-06 | facebook-post             |            11 |                7 |                 7 |       1     |             1 |
| 2026-01-06_am-avut-placerea-de-a-l-reintalni-pe-presedintele-emmanuel-m        | 2026-01-06 | facebook-post             |            19 |               11 |                11 |       1     |             1 |
| 2026-01-07_am-ajuns-la-bucuresti-pe-parcursul-zborului-deasupra-spatiul        | 2026-01-07 | facebook-post             |            34 |               20 |                20 |       1     |             2 |
| 2026-01-08_puteti-asculta-inregistrarea-convorbirii-dintre-pilotul-roma        | 2026-01-08 | facebook-post             |           104 |               60 |                53 |       0.883 |             5 |
| 2026-01-09_romania-a-votat-in-favoarea-acordului-comercial-dintre-uniun        | 2026-01-09 | facebook-post             |           461 |              281 |               186 |       0.662 |            17 |
| 2026-01-13_parteneriatul-strategic-dintre-romania-si-statele-unite-ale         | 2026-01-13 | facebook-post             |           266 |              149 |               120 |       0.805 |            12 |
| 2026-01-15_reuniunea-anuala-cu-sefii-misiunilor-diplomatice-acreditati         | 2026-01-15 | facebook-post             |           438 |              273 |               203 |       0.744 |            18 |
| 2026-01-15_ziua-culturii-nationale-ne-reaminteste-ca-identitatea-romani        | 2026-01-15 | facebook-post             |           265 |              151 |               125 |       0.828 |            14 |
| 2026-01-16_decizia-comisiei-europene-de-a-aproba-aplicatia-romaniei-pen        | 2026-01-16 | facebook-post             |           202 |              112 |                94 |       0.839 |             7 |
| 2026-01-17_am-promulgat-legea-care-permite-politistilor-locali-sa-utili        | 2026-01-17 | facebook-post             |           142 |               92 |                79 |       0.859 |             6 |
| 2026-01-17_am-promulgat-legea-de-adoptare-a-unei-ordonante-a-guvernului        | 2026-01-17 | facebook-post             |           133 |               73 |                58 |       0.795 |             5 |
| 2026-01-19_l-am-primit-astazi-la-palatul-cotroceni-pe-generalul-alexus         | 2026-01-19 | facebook-post             |           234 |              135 |               109 |       0.807 |            10 |
| 2026-01-23_relatia-transatlantica-are-o-istorie-care-a-adus-stabilitate        | 2026-01-23 | facebook-post             |           240 |              143 |               115 |       0.804 |            10 |
| 2026-01-24_am-ales-sa-fiu-astazi-atat-la-iasi-cat-si-la-focsani-pentru         | 2026-01-24 | facebook-post             |           312 |              163 |               123 |       0.755 |            14 |
| 2026-01-24_la-implinirea-a-160-de-ani-de-la-infiintare-am-acordat-coleg        | 2026-01-24 | facebook-post             |           232 |              116 |               102 |       0.879 |             9 |
| 2026-01-24_traim-momente-complicate-dar-intr-o-zi-de-sarbatoare-cred-ca        | 2026-01-24 | facebook-post             |           249 |               98 |                79 |       0.806 |            13 |
| 2026-01-26_ziua-internationala-de-comemorare-a-victimelor-holocaustului        | 2026-01-26 | facebook-post             |           179 |              106 |                89 |       0.84  |             7 |
| 2026-02-04_am-avut-astazi-o-convorbire-consistenta-cu-antonio-costa-pre        | 2026-02-04 | facebook-post             |           221 |              138 |               112 |       0.812 |             8 |
| 2026-02-04_romania-nu-este-subiectul-raportului-preliminar-al-comitetul        | 2026-02-04 | facebook-post             |           314 |              193 |               150 |       0.777 |            10 |
| 2026-02-05_exercitiile-militare-desfasurate-in-ultimele-zile-la-smardan        | 2026-02-05 | facebook-post             |            99 |               61 |                53 |       0.869 |             3 |
| 2026-02-08_am-primit-invitatia-de-a-participa-la-prima-reuniune-a-consi        | 2026-02-08 | facebook-post             |           132 |               75 |                62 |       0.827 |             4 |
| 2026-02-11_am-avut-ieri-o-discutie-cu-liderii-marilor-companii-american        | 2026-02-11 | facebook-post             |           132 |               79 |                68 |       0.861 |             5 |
| 2026-02-12_o-importanta-dezbatere-la-care-particip-astazi-in-belgia-ala        | 2026-02-12 | facebook-post             |           233 |              120 |                95 |       0.792 |             8 |
| 2026-02-13_va-invit-sa-privim-cu-echilibru-datele-publicate-azi-de-ins         | 2026-02-13 | facebook-post             |           202 |              113 |                91 |       0.805 |            20 |
| 2026-02-15_voi-participa-s-pt-mana-viitoare-la-prima-reuniune-a-consili        | 2026-02-15 | facebook-post             |           109 |               71 |                61 |       0.859 |             4 |
| 2026-02-18_salut-decizia-curtii-constitutionale-privind-reforma-pensiil        | 2026-02-18 | facebook-post             |            42 |               24 |                23 |       0.958 |             3 |
| 2026-02-19_am-avut-o-interventie-astazi-la-washington-in-cadrul-reuniun        | 2026-02-19 | facebook-post             |           287 |              167 |               133 |       0.796 |            15 |
| 2026-02-20_pacea-si-securitatea-sunt-temelia-unei-tari-prospere-pentru         | 2026-02-20 | facebook-post             |            93 |               57 |                52 |       0.912 |             4 |
| 2026-02-24_am-avut-o-discutie-aplicat-cu-premierul-ilie-bolojan-inainte        | 2026-02-24 | facebook-post             |           114 |               70 |                62 |       0.886 |             6 |
| 2026-02-24_in-urma-cu-patru-ani-unul-dintre-cele-mai-teribile-scenarii         | 2026-02-24 | facebook-post             |           162 |               96 |                77 |       0.802 |            10 |
| 2026-02-27_am-promulgat-in-aceasta-dimineata-legea-privind-pensiile-mag        | 2026-02-27 | facebook-post             |            85 |               51 |                46 |       0.902 |             5 |
| 2026-02-27_referitor-la-informatia-privind-plangerea-penala-a-aep-in-le        | 2026-02-27 | facebook-post             |           201 |               97 |                78 |       0.804 |             8 |
| 2026-03-01_romania-este-in-deplina-siguranta-si-nu-se-afla-sub-niciun-f        | 2026-03-01 | facebook-post             |           159 |               95 |                78 |       0.821 |             8 |
| 2026-03-03_m-am-bucurat-sa-l-primesc-astazi-la-palatul-cotroceni-pe-dar        | 2026-03-03 | facebook-post             |            99 |               49 |                45 |       0.918 |             4 |
| 2026-03-05_am-avut-astazi-un-dialog-substantial-cu-premierul-polonez-do        | 2026-03-05 | facebook-post             |           158 |               93 |                83 |       0.892 |             6 |
| 2026-03-05_am-raspuns-cu-placere-invitatiei-presedintelui-karol-nawrock        | 2026-03-05 | facebook-post             |           221 |              126 |               103 |       0.817 |            10 |
| 2026-03-06_pe-5-martie-cu-ocazia-zilei-solidaritatii-romano-polone-sarb        | 2026-03-06 | facebook-post             |            65 |               40 |                39 |       0.975 |             3 |
| 2026-03-08_la-multi-ani-tuturor-doamnelor-si-domnisoarelor-de-ziua-inte        | 2026-03-08 | facebook-post             |           115 |               65 |                57 |       0.877 |             8 |
| 2026-03-09_am-avut-astazi-o-convorbire-cu-antonio-costa-presedintele-co        | 2026-03-09 | facebook-post             |           236 |              144 |               110 |       0.764 |             9 |
| 2026-03-09_ziua-detinutilor-politici-anticomunisti-marcata-in-fiecare-a        | 2026-03-09 | facebook-post             |           240 |              123 |               112 |       0.911 |             9 |
| 2026-03-10_am-avut-in-aceasta-seara-un-dialog-aplicat-cu-liderii-europe        | 2026-03-10 | facebook-post             |           170 |               98 |                82 |       0.837 |             6 |
| 2026-03-11_am-convocat-astazi-sedinta-csat-pentru-analiza-evolutiei-sit        | 2026-03-11 | facebook-post             |           235 |              116 |                94 |       0.81  |            13 |
| 2026-03-12_am-semnat-astazi-cu-presedintele-zelenski-doua-documente-ofi        | 2026-03-12 | facebook-post             |           130 |               79 |                64 |       0.81  |             4 |
| 2026-03-12_i-am-urat-bun-venit-la-bucuresti-presedintelui-volodimir-zel        | 2026-03-12 | facebook-post             |           269 |              148 |               116 |       0.784 |            12 |
| 2026-03-16_aderarea-romaniei-in-2026-la-organizatia-pentru-cooperare-si        | 2026-03-16 | facebook-post             |           170 |              105 |                86 |       0.819 |             6 |
| 2026-03-16_astazi-am-discutat-cu-alfred-stern-presedintele-consiliului         | 2026-03-16 | facebook-post             |           229 |              142 |               113 |       0.796 |            12 |
| 2026-03-17_donarea-de-sange-salveaza-vieti-impreuna-prin-gesturi-simple        | 2026-03-17 | facebook-post             |           160 |               97 |                83 |       0.856 |            10 |
| 2026-03-19_declaratii-de-presa-sustinute-la-bruxelles-regatul-belgiei          | 2026-03-19 | facebook-post             |             8 |                6 |                 6 |       1     |             0 |
| 2026-03-19_romania-este-aparata-este-parte-din-nato-are-un-parteneriat         | 2026-03-19 | facebook-post             |           213 |              114 |                88 |       0.772 |             9 |
| 2026-03-20_am-decis-sa-ne-alaturam-declaratiei-regatului-unit-frantei-g        | 2026-03-20 | facebook-post             |           117 |               73 |                69 |       0.945 |             7 |
| 2026-03-20_o-onoare-si-o-bucurie-sa-ma-intalnesc-astazi-la-bruxelles-cu        | 2026-03-20 | facebook-post             |            58 |               30 |                30 |       1     |             3 |
| 2026-03-21_cea-mai-mare-expozitie-din-europa-dedicata-lui-constantin-br        | 2026-03-21 | facebook-post             |           288 |              178 |               131 |       0.736 |            11 |
| 2026-03-22_am-avut-zilele-trecute-la-bruxelles-o-discutie-cu-oana-gheor        | 2026-03-22 | facebook-post             |           108 |               59 |                48 |       0.814 |             6 |
| 2026-03-23_francofonia-si-valorile-pe-care-le-promoveaza-fac-parte-din         | 2026-03-23 | facebook-post             |           196 |              108 |                89 |       0.824 |             7 |
| 2026-03-26_razboiul-informational-afecteaza-si-profesia-medicala-este-u        | 2026-03-26 | facebook-post             |           210 |               92 |                68 |       0.739 |            10 |
| 2026-03-27_l-am-primit-astazi-la-palatul-cotroceni-pe-prim-ministrul-sl        | 2026-03-27 | facebook-post             |           119 |               66 |                59 |       0.894 |             6 |
| 2026-03-27_m-am-intalnit-astazi-la-palatul-cotroceni-cu-numan-kurtulmus        | 2026-03-27 | facebook-post             |           171 |              100 |                88 |       0.88  |             9 |
| 2026-03-30_proiectul-european-trebuie-sa-se-concentreze-inainte-de-toat        | 2026-03-30 | facebook-post             |           156 |               94 |                82 |       0.872 |             7 |
| 2026-03-31_aderarea-romaniei-la-uniunea-europeana-a-fost-o-poveste-de-m        | 2026-03-31 | facebook-post             |           293 |              159 |               117 |       0.736 |            15 |
| 2026-03-31_discutia-aplicata-pe-care-am-avut-o-astazi-cu-prim-ministrul        | 2026-03-31 | facebook-post             |           152 |               93 |                78 |       0.839 |             5 |
| 2026-03-31_transportul-si-asigurarea-unor-rute-sigure-pentru-marfuri-ca        | 2026-03-31 | facebook-post             |           215 |              127 |                97 |       0.764 |             7 |
| 2026-04-02_ma-bucur-ca-bratarile-dacice-si-coiful-de-la-cotofenesti-au         | 2026-04-02 | facebook-post             |           114 |               67 |                63 |       0.94  |             4 |
| 2026-04-05_tuturor-credinciosilor-care-celebreaza-invierea-le-doresc-ca        | 2026-04-05 | facebook-post             |           120 |               64 |                60 |       0.938 |             7 |
| 2026-04-07_de-ziua-mondiala-a-sanatatii-transmit-un-gand-de-recunostint        | 2026-04-07 | facebook-post             |           209 |              101 |                87 |       0.861 |             9 |
| 2026-04-07_declaratiile-de-presa-sustinute-la-finalul-vizitei-la-centru        | 2026-04-07 | facebook-post             |            22 |               14 |                14 |       1     |             0 |
| 2026-04-08_fbi-impreuna-cu-mai-multi-parteneri-printre-care-sri-a-anunt        | 2026-04-08 | facebook-post             |            81 |               51 |                45 |       0.882 |             5 |
| 2026-04-12_hristos-a-inviat-este-certitudinea-care-ne-reaminteste-in-fi        | 2026-04-12 | facebook-post             |           129 |               60 |                58 |       0.967 |             6 |
| 2026-04-20_am-trecut-astazi-in-revista-impreuna-cu-ministrul-dragos-pas        | 2026-04-20 | facebook-post             |           147 |               69 |                65 |       0.942 |             5 |
| 2026-04-22_am-avut-azi-consultari-cu-partidele-pro-occidentale-din-actu        | 2026-04-22 | facebook-post             |           179 |               98 |                76 |       0.776 |            11 |
| 2026-04-22_consultari-cu-partide-si-formatiuni-politice-parlamentare-pa        | 2026-04-22 | facebook-post             |            11 |                9 |                 8 |       0.889 |             0 |
| 2026-04-22_live-consultari-cu-partide-si-formatiuni-politice-parlamenta        | 2026-04-22 | facebook-post             |            12 |               10 |                10 |       1     |             0 |
| 2026-04-22_live-consultari-cu-partide-si-formatiuni-politice-parlamenta_564296 | 2026-04-22 | facebook-post             |            14 |               11 |                11 |       1     |             0 |
| 2026-04-22_live-consultari-cu-partide-si-formatiuni-politice-parlamenta_597234 | 2026-04-22 | facebook-post             |            13 |               10 |                 9 |       0.9   |             0 |
| 2026-04-22_live-consultari-cu-partide-si-formatiuni-politice-parlamenta_669920 | 2026-04-22 | facebook-post             |            12 |               10 |                 9 |       0.9   |             0 |
| 2026-04-22_live-declaratie-de-presa-sustinuta-la-palatul-cotroceni             | 2026-04-22 | facebook-post             |             8 |                6 |                 6 |       1     |             0 |
| 2026-04-23_am-promulgat-astazi-legea-pentru-prevenirea-si-combaterea-fe        | 2026-04-23 | facebook-post             |           169 |               89 |                78 |       0.876 |             7 |
| 2026-04-23_particip-in-aceste-zile-in-cipru-la-reuniunea-informala-a-co        | 2026-04-23 | facebook-post             |           254 |              149 |               110 |       0.738 |            12 |
| 2026-04-24_live-declaratiile-de-presa-sustinute-la-finalul-reuniunii-in        | 2026-04-24 | facebook-post             |            16 |               12 |                12 |       1     |             0 |
| 2026-04-24_subiectul-cel-mai-important-pentru-romania-pe-care-l-am-abor        | 2026-04-24 | facebook-post             |           188 |               94 |                80 |       0.851 |             5 |
| 2026-04-25_am-semnat-asear-demisiile-ministrilor-social-democrati-si-pr        | 2026-04-25 | facebook-post             |            59 |               36 |                35 |       0.972 |             3 |
| 2026-04-28_astazi-la-dubrovnik-in-marja-summitului-initiativei-celor-tr        | 2026-04-28 | facebook-post             |           149 |               93 |                77 |       0.828 |             6 |
| 2026-04-28_in-marja-summitului-initiativei-celor-trei-mari-de-la-dubrov        | 2026-04-28 | facebook-post             |            82 |               46 |                43 |       0.935 |             4 |
| 2026-04-28_live-declaratii-de-presa-sustinute-in-marja-summitului-initi        | 2026-04-28 | facebook-post             |            16 |               10 |                10 |       1     |             0 |
| 2026-04-28_romania-a-participat-activ-si-cu-succes-la-efortul-transatla        | 2026-04-28 | facebook-post             |           122 |               82 |                69 |       0.841 |             5 |
| 2026-04-29_am-participat-astazi-la-sesiunea-speciala-a-forumului-de-afa        | 2026-04-29 | facebook-post             |            90 |               41 |                41 |       1     |             3 |
| 2026-04-29_live-declaratiile-de-presa-sustinute-dupa-participarea-la-fo        | 2026-04-29 | facebook-post             |            20 |               11 |                11 |       1     |             0 |
| 2026-05-03_felicitari-elevilor-romani-din-lotul-national-de-robotica-ca        | 2026-05-03 | facebook-post             |           124 |               77 |                57 |       0.74  |             9 |
| 2026-05-03_in-drum-spre-armenia-unde-voi-participa-alaturi-de-doamna-pr        | 2026-05-03 | facebook-post             |            87 |               63 |                55 |       0.873 |             4 |
| 2026-05-04_am-avut-placerea-de-a-ma-intalni-cu-principele-albert-al-ii         | 2026-05-04 | facebook-post             |            62 |               30 |                29 |       0.967 |             3 |
| 2026-05-04_am-organizat-astazi-in-marja-reuniunii-comunitatii-politice         | 2026-05-04 | facebook-post             |            95 |               62 |                60 |       0.968 |             4 |
| 2026-05-04_live-declaratii-de-presa-dupa-participarea-la-reuniunea-comu        | 2026-05-04 | facebook-post             |            16 |               11 |                11 |       1     |             0 |
| 2026-05-04_multumesc-prietenilor-europeni-pentru-participarea-la-discut        | 2026-05-04 | facebook-post             |            71 |               42 |                41 |       0.976 |             4 |
| 2026-05-05_live-declaratii-de-presa-sustinute-la-palatul-cotroceni             | 2026-05-05 | facebook-post             |             8 |                6 |                 6 |       1     |             0 |
| 2026-05-09_sarbatorim-azi-ziua-europei-maine-ziua-independentei-sunt-do        | 2026-05-09 | facebook-post             |           705 |              358 |               200 |       0.559 |            38 |
| 2026-05-12_abordarea-strategica-a-romaniei-in-ceea-ce-priveste-politica        | 2026-05-12 | facebook-post             |           169 |               91 |                62 |       0.681 |             8 |
| 2026-05-12_am-avut-o-discutie-substantiala-cu-presedintele-poloniei-kar        | 2026-05-12 | facebook-post             |           140 |               74 |                62 |       0.838 |             6 |
| 2026-05-12_intalnire-de-lucru-alaturi-de-secretarul-general-al-nato-mar        | 2026-05-12 | facebook-post             |           115 |               77 |                70 |       0.909 |             5 |
| 2026-05-12_live-declaratii-de-presa-comune-cu-presedintele-republicii-p        | 2026-05-12 | facebook-post             |            11 |                9 |                 9 |       1     |             0 |
| 2026-05-12_live-declaratii-de-presa-sustinute-dupa-participarea-la-conf        | 2026-05-12 | facebook-post             |            16 |               13 |                13 |       1     |             0 |
| 2026-05-12_live-participare-la-conferinta-internationala-black-sea-and         | 2026-05-12 | facebook-post             |            11 |               10 |                10 |       1     |             0 |
| 2026-05-12_live-primirea-presedintelui-republicii-polone-karol-nawrocki        | 2026-05-12 | facebook-post             |            10 |                9 |                 9 |       1     |             0 |
| 2026-05-12_live-primirea-secretarului-general-nato-mark-rutte-la-palatu        | 2026-05-12 | facebook-post             |            10 |                9 |                 9 |       1     |             0 |
| 2026-05-13_am-avut-astazi-o-intrevedere-excelenta-cu-presedintele-curti        | 2026-05-13 | facebook-post             |            62 |               39 |                35 |       0.897 |             3 |
| 2026-05-13_b9summit-romania-polonia-ucraina-b92026                             | 2026-05-13 | facebook-post             |             4 |                4 |                 4 |       1     |             0 |
| 2026-05-13_le-am-urat-bun-venit-la-bucuresti-liderilor-statelor-membre         | 2026-05-13 | facebook-post             |           205 |              112 |                93 |       0.83  |             9 |
| 2026-05-13_live-declaratii-de-presa-comune-ale-presedintelui-romaniei-n        | 2026-05-13 | facebook-post             |            33 |               24 |                23 |       0.958 |             0 |
| 2026-05-13_live-primirea-presedintelui-ucrainei-la-palatul-cotroceni-si        | 2026-05-13 | facebook-post             |            12 |                9 |                 9 |       1     |             0 |
| 2026-05-13_o-participare-ampla-astazi-la-bucuresti-a-statelor-din-forma        | 2026-05-13 | facebook-post             |           233 |              127 |               107 |       0.843 |            11 |
| 2026-05-13_presedintele-volodimir-zelenski-a-fost-invitatul-special-al         | 2026-05-13 | facebook-post             |           125 |               74 |                65 |       0.878 |             6 |
| 2026-05-13_summitul-b9-la-palatul-cotroceni-impreuna-suntem-mai-puterni        | 2026-05-13 | facebook-post             |             8 |                5 |                 5 |       1     |             2 |
| 2026-05-13_unitatea-forta-si-coerenta-trebuie-sa-ne-ghideze-in-consolid        | 2026-05-13 | facebook-post             |            20 |               14 |                14 |       1     |             2 |
| 2026-05-13_zi-foarte-importanta-astazi-la-palatul-cotroceni-unde-are-lo        | 2026-05-13 | facebook-post             |            65 |               37 |                35 |       0.946 |             2 |
| 2026-05-14_la-summitul-b9-am-reconfirmat-un-lucru-esential-securitatea         | 2026-05-14 | facebook-post             |            39 |               25 |                25 |       1     |             2 |
| 2026-05-15_investitiile-in-tot-ce-tine-de-apararea-cetatenilor-nostri-a        | 2026-05-15 | facebook-post             |           182 |              102 |                85 |       0.833 |             7 |
| 2026-05-15_live-declaratii-de-presa-sustinute-de-presedintele-romaniei         | 2026-05-15 | facebook-post             |            23 |               19 |                19 |       1     |             0 |
| 2026-05-21_t                                                                   | 2026-05-21 | facebook-post             |           111 |               61 |                51 |       0.836 |             5 |
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

### 2025-02-20 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| oraș              |           1 |
| moldova           |           1 |
| vizita            |           1 |
| recent            |           1 |
| întâlni           |           1 |
| om                |           1 |
| calzi             |           1 |
| inteligente       |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-02-20 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| românia           |           2 |
| aștepta           |           1 |
| schimbare         |           1 |
| real              |           1 |
| puternic          |           1 |
| direcție          |           1 |
| clar              |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-02-21 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| românia       |           3 |
| trebui        |           3 |
| securitate    |           2 |
| europa        |           2 |
| stat          |           2 |
| discuție      |           1 |
| internațional |           1 |
| reconfigurare |           1 |
| prinde        |           1 |
| prost         |           1 |
| moment        |           1 |
| posibil       |           1 |
| anulare       |           1 |
| alegere       |           1 |
| prezentare    |           1 |
| ulterior      |           1 |
| dovadă        |           1 |
| echivoc       |           1 |
| convinge      |           1 |
| român         |           1 |

### 2025-02-21 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| împreună |           1 |
| românia  |           1 |
| onestă   |           1 |

### 2025-02-21 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| societate         |           2 |
| președinte        |           1 |
| trebui            |           1 |
| uni               |           1 |
| energiile         |           1 |
| putea             |           1 |
| dezvolta          |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-02-21 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| urbanism     |           4 |
| oraș         |           4 |
| urbanistic   |           3 |
| pug          |           3 |
| cadru        |           3 |
| vrea         |           3 |
| capitală     |           3 |
| european     |           3 |
| bucurești    |           3 |
| ultim        |           2 |
| studiu       |           2 |
| actualizare  |           2 |
| uauim        |           2 |
| public       |           2 |
| dezvoltare   |           2 |
| an           |           2 |
| urban        |           2 |
| sustenabil   |           2 |
| standard     |           2 |
| fundamentare |           1 |

### 2025-02-21 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |           2 |
| onestă      |           2 |
| parte       |           1 |
| schimbare   |           1 |
| alătură     |           1 |
| echipă      |           1 |
| voluntar    |           1 |
| campanie    |           1 |
| românia     |           1 |
| vino        |           1 |
| alături     |           1 |
| week-end    |           1 |
| februarie   |           1 |
| oraș        |           1 |
| ploiești    |           1 |
| brașov      |           1 |
| târgu       |           1 |
| mureș       |           1 |
| sibiu       |           1 |
| completează |           1 |

### 2025-02-22 — facebook-post

| cuvânt             |   frecvență |
|:-------------------|------------:|
| bucurești          |           3 |
| finalist           |           2 |
| premie             |           1 |
| săptămânii         |           1 |
| european           |           1 |
| mobilității        |           1 |
| proiect            |           1 |
| transformare       |           1 |
| bulevard           |           1 |
| gheorghe           |           1 |
| duca               |           1 |
| întru              |           1 |
| expoziție          |           1 |
| temporar           |           1 |
| interactiv         |           1 |
| organizat          |           1 |
| tpbi               |           1 |
| primărie           |           1 |
| stb                |           1 |
| societatepeacțiuni |           1 |

### 2025-02-22 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| vremuri      |           1 |
| complicat    |           1 |
| singur       |           1 |
| resursă      |           1 |
| rămâne       |           1 |
| discernământ |           1 |
| propriu      |           1 |

### 2025-02-23 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| românia       |           5 |
| om            |           3 |
| sine          |           3 |
| stat          |           3 |
| criză         |           2 |
| intern        |           2 |
| însă          |           2 |
| instituție    |           2 |
| putea         |           2 |
| vrea          |           2 |
| grijă         |           2 |
| discuta       |           1 |
| week-end      |           1 |
| ploiești      |           1 |
| brașov        |           1 |
| sibiu         |           1 |
| târgu-mureș   |           1 |
| traversa      |           1 |
| situație      |           1 |
| internațional |           1 |

### 2025-02-23 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| vrea             |           5 |
| germania         |           3 |
| victorie         |           2 |
| important        |           2 |
| politic          |           2 |
| european         |           2 |
| uniuneaeuropeană |           2 |
| economic         |           2 |
| felicit          |           1 |
| bloc             |           1 |
| centru-dreaptă   |           1 |
| pro-european     |           1 |
| cducsu           |           1 |
| alegere          |           1 |
| general          |           1 |
| actual           |           1 |
| context          |           1 |
| internațional    |           1 |
| atât             |           1 |
| turbulent        |           1 |

### 2025-02-23 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| grup         |           3 |
| femeie       |           2 |
| terapie      |           2 |
| suport       |           1 |
| afecta       |           1 |
| violență     |           1 |
| domestic     |           1 |
| agresiune    |           1 |
| sexual       |           1 |
| discriminare |           1 |
| gen          |           1 |
| primărie     |           1 |
| capitală     |           1 |
| dgasmb       |           1 |
| parteneriat  |           1 |
| asociație    |           1 |
| necuvinte    |           1 |
| invita       |           1 |
| participa    |           1 |
| dedica       |           1 |

### 2025-02-24 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           4 |
| proiect      |           1 |
| politic      |           1 |
| entuziast    |           1 |
| muncitor     |           1 |
| voluntar     |           1 |
| câștiga      |           1 |
| voluntarii   |           1 |
| cheie        |           1 |
| succes       |           1 |
| alegere      |           1 |
| prezidențial |           1 |
| mulțumi      |           1 |
| alătura      |           1 |
| campanie     |           1 |
| românia      |           1 |
| onestă       |           1 |
| îndemn       |           1 |
| implica      |           1 |
| completa     |           1 |

### 2025-02-25 — facebook-post

| cuvânt                                                     |   frecvență |
|:-----------------------------------------------------------|------------:|
| drum                                                       |           2 |
| românia                                                    |           2 |
| cifră                                                      |           1 |
| vorbi                                                      |           1 |
| clar                                                       |           1 |
| bun                                                        |           1 |
| onestă                                                     |           1 |
| șansă                                                      |           1 |
| real                                                       |           1 |
| httpsdrivegooglecomopenidajotnnyxaymfaa-xkteer-auspdrivefs |           1 |
| păstra                                                     |           1 |
| direcție                                                   |           1 |
| corect                                                     |           1 |
| valoare                                                    |           1 |
| occidental                                                 |           1 |
| trebui                                                     |           1 |
| uni                                                        |           1 |
| niciodată                                                  |           1 |
| exista                                                     |           1 |
| loc                                                        |           1 |

### 2025-02-25 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| împreună          |           1 |
| vrea              |           1 |
| reuși             |           1 |
| romaniaonesta     |           1 |
| romaniputernica   |           1 |
| nicusorpresedinte |           1 |

### 2025-02-25 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| târziu       |           1 |
| decât        |           1 |
| niciodată    |           1 |
| alegerile    |           1 |
| trebui       |           1 |
| organiza     |           1 |
| transparent  |           1 |
| profesionist |           1 |

### 2025-02-26 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| vrea              |           3 |
| încredere         |           1 |
| român             |           1 |
| președinte        |           1 |
| activ             |           1 |
| implicat          |           1 |
| folosi            |           1 |
| putere            |           1 |
| constituțional    |           1 |
| determina         |           1 |
| guvern            |           1 |
| pune              |           1 |
| aplicare          |           1 |
| eficient          |           1 |
| soluție           |           1 |
| problemă          |           1 |
| cetățean          |           1 |
| romaniaonesta     |           1 |
| romaniaputernica  |           1 |
| nicusorpresedinte |           1 |

### 2025-02-26 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| semnătură    |           3 |
| sine         |           2 |
| formular     |           2 |
| putea        |           2 |
| aproape      |           1 |
| depunere     |           1 |
| candidaturii |           1 |
| proces       |           1 |
| decurge      |           1 |
| planifica    |           1 |
| voluntarii   |           1 |
| teren        |           1 |
| zilnic       |           1 |
| asigura      |           1 |
| completa     |           1 |
| corect       |           1 |
| respecta     |           1 |
| lege         |           1 |
| adunăm       |           1 |
| om           |           1 |

### 2025-02-27 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| vrea      |           7 |
| familie   |           4 |
| copil     |           3 |
| proiect   |           3 |
| municipi  |           2 |
| bucurești |           2 |
| sector    |           2 |
| separare  |           2 |
| copie     |           2 |
| suport    |           2 |
| direct    |           2 |
| ajutor    |           2 |
| leu       |           2 |
| ajuta     |           1 |
| rămâne    |           1 |
| alături   |           1 |
| direcție  |           1 |
| generale  |           1 |
| asistență |           1 |
| social    |           1 |

### 2025-02-27 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| problemă     |           2 |
| urbanism     |           2 |
| sibiu        |           1 |
| descoperi    |           1 |
| același      |           1 |
| bucurești    |           1 |
| cupolă       |           1 |
| catedrală    |           1 |
| mitropolitan |           1 |
| putea        |           1 |
| ascunsă      |           1 |
| clădire      |           1 |
| urma         |           1 |
| ridica       |           1 |
| privi        |           1 |
| calitate     |           1 |
| vieților     |           1 |
| vrea         |           1 |
| alege        |           1 |
| președinte   |           1 |

### 2025-02-27 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| copilărie         |           1 |
| făgăraș           |           1 |
| dimineață         |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-02-27 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| dimineață         |           1 |
| lansăm            |           1 |
| video             |           1 |
| copilărie         |           1 |
| făgăraș           |           1 |
| aștepta           |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-02-27 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |           2 |
| întâmpla   |           2 |
| românia    |           2 |
| viață      |           1 |
| lupta      |           1 |
| dreptate   |           1 |
| protecție  |           1 |
| vulnerabil |           1 |
| neimaginat |           1 |
| frate      |           1 |
| tate       |           1 |
| acuza      |           1 |
| justiție   |           1 |
| român      |           1 |
| trafic     |           1 |
| persoană   |           1 |
| viol       |           1 |
| formă      |           1 |
| continuat  |           1 |
| tată       |           1 |

### 2025-02-28 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| casă              |           1 |
| bunicii           |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-02-28 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| important         |           2 |
| cred              |           1 |
| ști               |           1 |
| veni              |           1 |
| sine              |           1 |
| părea             |           1 |
| spune             |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-02-28 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| menținere         |           1 |
| legătură          |           1 |
| părinte           |           1 |
| străinătate       |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-02-28 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| românia      |           3 |
| democrație   |           3 |
| român        |           2 |
| fundamental  |           2 |
| retrogradare |           2 |
| alegere      |           2 |
| pune         |           2 |
| plan         |           2 |
| profund      |           1 |
| îngrijorător |           1 |
| retrograda   |           1 |
| index        |           1 |
| democrația   |           1 |
| trece        |           1 |
| statut       |           1 |
| viciat       |           1 |
| regim        |           1 |
| hibrid       |           1 |
| schimbare    |           1 |
| reflecta     |           1 |

### 2025-02-28 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| politică          |           1 |
| extern            |           1 |
| trebui            |           1 |
| pune              |           1 |
| întotdeauna       |           1 |
| loc               |           1 |
| interes           |           1 |
| național          |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |
| romaniaputernica  |           1 |

### 2025-02-28 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| mergeam           |           1 |
| colindat          |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-02-28 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| europa      |           2 |
| trebui      |           2 |
| sustin      |           1 |
| ferm        |           1 |
| ucraina     |           1 |
| luptă       |           1 |
| pace        |           1 |
| justa       |           1 |
| sustenabila |           1 |
| moment      |           1 |
| tensionat   |           1 |
| rămâne      |           1 |
| calmi       |           1 |
| lucid       |           1 |
| apreciez    |           1 |
| reacție     |           1 |
| lider       |           1 |
| european    |           1 |
| pune        |           1 |
| speranță    |           1 |

### 2025-03-01 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| spune             |           1 |
| copie             |           1 |
| oraș              |           1 |
| mic               |           1 |
| românia           |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-01 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| film              |           1 |
| carte             |           1 |
| copilărie         |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-01 — facebook-post

| cuvânt                               |   frecvență |
|:-------------------------------------|------------:|
| whatsapp                             |           2 |
| haideți                              |           1 |
| sta                                  |           1 |
| vorbă                                |           1 |
| aștepta                              |           1 |
| mesaj                                |           1 |
| împreună                             |           1 |
| duce                                 |           1 |
| număr                                |           1 |
| telefon                              |           1 |
| cotroceni                            |           1 |
| urmărește                            |           1 |
| canal                                |           1 |
| nicusor                              |           1 |
| dan                                  |           1 |
| httpswhatsappcomchannelvbtgnombptoql |           1 |
| nicusorpresedinte                    |           1 |
| alegeriromania                       |           1 |
| bucuresti                            |           1 |
| romaniaonesta                        |           1 |

### 2025-03-01 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| rol               |           1 |
| școală            |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-01 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| solidaritate      |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-01 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| trăim        |           1 |
| putea        |           1 |
| provocatoare |           1 |
| vremuri      |           1 |
| ultim        |           1 |
| deceniu      |           1 |
| esențial     |           1 |
| pierdem      |           1 |
| vedere       |           1 |
| mic          |           1 |
| moment       |           1 |
| bucurie      |           1 |
| primăvară    |           1 |
| plin         |           1 |
| speranță     |           1 |

### 2025-03-02 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| vrea           |           8 |
| stație         |           4 |
| denumire       |           2 |
| stb            |           1 |
| primi          |           1 |
| precis         |           1 |
| reflecta       |           1 |
| zonă           |           1 |
| amplasa        |           1 |
| modificare     |           1 |
| implementa     |           1 |
| asociație      |           1 |
| dezvoltare     |           1 |
| intercomunitar |           1 |
| transport      |           1 |
| public         |           1 |
| bucurești      |           1 |
| ilfov          |           1 |
| tpbi           |           1 |
| perioadă       |           1 |

### 2025-03-02 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| entuziast   |           1 |
| echipă      |           1 |
| voluntar    |           1 |
| nivel       |           1 |
| național    |           1 |
| bucurești   |           1 |
| cluj-napoca |           1 |
| iași        |           1 |
| timișoara   |           1 |
| craiova     |           1 |
| constanța   |           1 |
| brașov      |           1 |
| sibiu       |           1 |
| piatră      |           1 |
| neamț       |           1 |
| botoșani    |           1 |
| suceava     |           1 |
| localitate  |           1 |
| țară        |           1 |
| diaspora    |           1 |

### 2025-03-02 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| educație          |           1 |
| primi             |           1 |
| părinte           |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-02 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| mâncare           |           1 |
| bunică            |           1 |
| lapte             |           1 |
| mămăligă          |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-02 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           4 |
| câine        |           3 |
| sine         |           3 |
| cazare       |           2 |
| aspa         |           2 |
| loc          |           2 |
| spațiu       |           2 |
| mărima       |           1 |
| capacitate   |           1 |
| adăpost      |           1 |
| mihăilești   |           1 |
| configurație |           1 |
| putea        |           1 |
| caza         |           1 |
| căță         |           1 |
| față         |           1 |
| adăposti     |           1 |
| țarcuru      |           1 |
| desființat   |           1 |
| noile        |           1 |

### 2025-03-02 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| românia           |           1 |
| loc               |           1 |
| lume              |           1 |
| matematică        |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-02 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| sat               |           1 |
| bunic             |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-03 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| dr         |           3 |
| riad       |           3 |
| general    |           3 |
| dezvoltare |           3 |
| primi      |           2 |
| capitală   |           2 |
| es         |           2 |
| bucurești  |           2 |
| mohammed   |           2 |
| abdulghani |           2 |
| khayat     |           2 |
| arab       |           2 |
| urbanistic |           2 |
| onoare     |           1 |
| sediu      |           1 |
| primărie   |           1 |
| vizită     |           1 |
| oficial    |           1 |
| ambasador  |           1 |
| regat      |           1 |

### 2025-03-03 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| bucuriă           |           1 |
| merge             |           1 |
| școală            |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-03 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| vrea                |           1 |
| alege               |           1 |
| următor             |           1 |
| an                  |           1 |
| uita                |           1 |
| tinerii             |           1 |
| viitor              |           1 |
| românia             |           1 |
| lornicusorpresedint |           1 |
| romaniaonesta       |           1 |
| romaniaputernica    |           1 |
| bucurești           |           1 |
| tânăr               |           1 |

### 2025-03-03 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| pano              |           1 |
| liceu             |           1 |
| radu              |           1 |
| negru             |           1 |
| făgăraș           |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-03 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| vacanțele         |           1 |
| țară              |           1 |
| bunică            |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-04 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| consolidare |           5 |
| afla        |           3 |
| clădire     |           3 |
| leu         |           3 |
| an          |           2 |
| derulare    |           2 |
| stradă      |           2 |
| bloc        |           2 |
| finanțare   |           2 |
| clădirilor  |           2 |
| risc        |           2 |
| seismic     |           2 |
| vrea        |           2 |
| miliard     |           2 |
| sine        |           1 |
| împlini     |           1 |
| cutremur    |           1 |
| devastator  |           1 |
| zgudui      |           1 |
| bucurești   |           1 |

### 2025-03-04 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| român        |           3 |
| rusia        |           2 |
| oficial      |           2 |
| alegere      |           2 |
| serviciu     |           1 |
| informații   |           1 |
| extern       |           1 |
| comunicat    |           1 |
| ataca        |           1 |
| procuror     |           1 |
| ancheta      |           1 |
| călin        |           1 |
| georgescu    |           1 |
| act          |           1 |
| public       |           1 |
| intervine    |           1 |
| sprijin      |           1 |
| candidat     |           1 |
| prezidențial |           1 |
| semnal       |           1 |

### 2025-03-04 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| însemna      |           2 |
| promisiune   |           1 |
| simplu       |           1 |
| esențial     |           1 |
| primărie     |           1 |
| capitală     |           1 |
| trebui       |           1 |
| alături      |           1 |
| bucureșteni  |           1 |
| normalitate  |           1 |
| acces        |           1 |
| restricționa |           1 |
| oficialitate |           1 |
| respect      |           1 |
| instituție   |           1 |
| față         |           1 |
| cetățean     |           1 |

### 2025-03-04 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| viziunea |           1 |
| viitor   |           1 |
| guvern   |           1 |

### 2025-03-05 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| google       |           7 |
| public       |           5 |
| bucurești    |           4 |
| oraș         |           4 |
| serviciu     |           3 |
| putea        |           2 |
| transformare |           2 |
| cetățean     |           2 |
| provocare    |           2 |
| capitală     |           2 |
| trafic       |           2 |
| aglomerat    |           2 |
| succes       |           2 |
| proiect      |           2 |
| sistem       |           2 |
| îmbunătățire |           2 |
| tehnologiu   |           2 |
| digital      |           2 |
| important    |           2 |
| întâlnire    |           1 |

### 2025-03-05 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| intervenție             |           2 |
| președinte              |           2 |
| semn                    |           2 |
| dialog                  |           2 |
| important               |           2 |
| sine                    |           2 |
| românia                 |           2 |
| stateleunitealeamericii |           2 |
| trump                   |           1 |
| azi-noapte              |           1 |
| congres                 |           1 |
| reluare                 |           1 |
| relație                 |           1 |
| volodymyr               |           1 |
| zelenskyy               |           1 |
| speranță                |           1 |
| redeschiderie           |           1 |
| consistent              |           1 |
| ucraina                 |           1 |
| aliat                   |           1 |

### 2025-03-05 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| digital   |           9 |
| sine      |           8 |
| centru    |           7 |
| program   |           4 |
| lume      |           3 |
| senior    |           3 |
| persoană  |           3 |
| dgasmb    |           2 |
| hi        |           2 |
| întru     |           2 |
| desfășura |           2 |
| putea     |           2 |
| telefon   |           2 |
| vrea      |           2 |
| ominis    |           2 |
| vârstnic  |           2 |
| organizăm |           1 |
| curs      |           1 |
| inițiere  |           1 |
| senioare  |           1 |

### 2025-03-06 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| familie           |           3 |
| copil             |           1 |
| iubire            |           1 |
| ține              |           1 |
| ancora            |           1 |
| lume              |           1 |
| salutări          |           1 |
| român             |           1 |
| sper              |           1 |
| mesaj             |           1 |
| ajunge            |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-06 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| cluj              |           4 |
| vedea             |           1 |
| sâmbătă           |           1 |
| vrea              |           1 |
| trimite           |           1 |
| poveste           |           1 |
| oraș              |           1 |
| număr             |           1 |
| whatsapp          |           1 |
| încă              |           1 |
| cere              |           1 |
| comentariu        |           1 |
| vedem             |           1 |
| nicușorpresedinte |           1 |
| alegeripresedinte |           1 |
| româniaonesta     |           1 |

### 2025-03-06 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| muncă      |           2 |
| viitor     |           2 |
| afacere    |           1 |
| familie    |           1 |
| înființa   |           1 |
| bacău      |           1 |
| crește     |           1 |
| sine       |           1 |
| transforma |           1 |
| întru      |           1 |
| companie   |           1 |
| succes     |           1 |
| specializa |           1 |
| producție  |           1 |
| tâmplărie  |           1 |
| pvc        |           1 |
| genera     |           1 |
| loc        |           1 |
| esențial   |           1 |
| susține    |           1 |

### 2025-03-07 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| schimbare  |           2 |
| instituție |           2 |
| lună       |           1 |
| român      |           1 |
| spune      |           1 |
| clar       |           1 |
| sine       |           1 |
| putea      |           1 |
| cere       |           1 |
| întru      |           1 |
| țară       |           1 |
| corupt     |           1 |
| captura    |           1 |
| grup       |           1 |
| interes    |           1 |
| economie   |           1 |
| viziune    |           1 |
| sistem     |           1 |
| sănătate   |           1 |
| educație   |           1 |

### 2025-03-07 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| țară       |           4 |
| diasporă   |           3 |
| românia    |           3 |
| român      |           2 |
| munci      |           2 |
| sine       |           2 |
| stat       |           2 |
| puternic   |           2 |
| candidez   |           1 |
| onesc      |           1 |
| greu       |           1 |
| plăti      |           1 |
| taxă       |           1 |
| bun        |           1 |
| simț       |           1 |
| cer        |           1 |
| autoritate |           1 |
| lucra      |           1 |
| grup       |           1 |
| interes    |           1 |

### 2025-03-07 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |           2 |
| onestă      |           2 |
| parte       |           1 |
| schimbare   |           1 |
| alătură     |           1 |
| echipă      |           1 |
| voluntar    |           1 |
| campanie    |           1 |
| românia     |           1 |
| vino        |           1 |
| alături     |           1 |
| week-end    |           1 |
| martie      |           1 |
| oraș        |           1 |
| cluj-napoca |           1 |
| alba        |           1 |
| iulia       |           1 |
| deva        |           1 |
| completează |           1 |
| formular    |           1 |

### 2025-03-08 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| industrie  |           3 |
| fabrică    |           2 |
| importanță |           2 |
| loc        |           2 |
| muncă      |           2 |
| sector     |           2 |
| plăcere    |           1 |
| oferi      |           1 |
| floare     |           1 |
| doamnelor  |           1 |
| lucra      |           1 |
| confecție  |           1 |
| faberom    |           1 |
| fosta      |           1 |
| apaca      |           1 |
| cândva     |           1 |
| emblemă    |           1 |
| românia    |           1 |
| ciudă      |           1 |
| istoric    |           1 |

### 2025-03-08 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| femeie        |           2 |
| viață         |           1 |
| sărbători     |           1 |
| arăta         |           1 |
| recunoștință  |           1 |
| an            |           1 |
| românia       |           1 |
| romaniaonesta |           1 |

### 2025-03-08 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| femeie     |           3 |
| putea      |           3 |
| sprijin    |           2 |
| număr      |           2 |
| martie     |           1 |
| sărbători  |           1 |
| floare     |           1 |
| compliment |           1 |
| însă       |           1 |
| parte      |           1 |
| gest       |           1 |
| special    |           1 |
| trece      |           1 |
| moment     |           1 |
| dificil    |           1 |
| merita     |           1 |
| direcție   |           1 |
| generală   |           1 |
| asistență  |           1 |
| social     |           1 |

### 2025-03-08 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| pădure      |           2 |
| puiet       |           1 |
| arbor       |           1 |
| forestier   |           1 |
| planta      |           1 |
| parc        |           1 |
| tineret     |           1 |
| week        |           1 |
| end         |           1 |
| alpab       |           1 |
| colaborare  |           1 |
| asociație   |           1 |
| copie       |           1 |
| suprafață   |           1 |
| plantare    |           1 |
| aproximativ |           1 |
| metrupătrat |           1 |
| folosi      |           1 |
| metodă      |           1 |
| inovator    |           1 |

### 2025-03-08 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| voce              |           2 |
| om                |           1 |
| vrea              |           1 |
| conta             |           1 |
| decât             |           1 |
| politicienilor    |           1 |
| cluj              |           1 |
| romaniaonesta     |           1 |
| romaniaputernica  |           1 |
| nicusorpresedinte |           1 |
| clujnapocî        |           1 |

### 2025-03-09 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| conversație   |           1 |
| tinerii       |           1 |
| lecție        |           1 |
| dorință       |           1 |
| schimbare     |           1 |
| putere        |           1 |
| construi      |           1 |
| viitor        |           1 |
| bun           |           1 |
| împreună      |           1 |
| putea         |           1 |
| românia       |           1 |
| onest         |           1 |
| nicusordan    |           1 |
| romaniaonesta |           1 |
| cluj          |           1 |
| tineri        |           1 |

### 2025-03-09 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| șos            |           5 |
| bdul           |           5 |
| cale           |           3 |
| lucrare        |           2 |
| sine           |           2 |
| vrea           |           2 |
| stradă         |           2 |
| intervenții    |           1 |
| reparare       |           1 |
| străze         |           1 |
| administrație  |           1 |
| străzilor      |           1 |
| asb            |           1 |
| începe         |           1 |
| remediere      |           1 |
| grop           |           1 |
| apăru          |           1 |
| cauză          |           1 |
| fenomen        |           1 |
| îngheț-dezgheț |           1 |

### 2025-03-09 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| uita         |           1 |
| niciodată    |           1 |
| depune       |           1 |
| coroană      |           1 |
| floare       |           1 |
| statuile     |           1 |
| ion          |           1 |
| ic           |           1 |
| brătianu     |           1 |
| iuliu        |           1 |
| maniu        |           1 |
| alba         |           1 |
| iulia        |           1 |
| semn         |           1 |
| respect      |           1 |
| recunoștință |           1 |
| jertfă       |           1 |
| suferi       |           1 |
| închisore    |           1 |
| comunist     |           1 |

### 2025-03-11 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           7 |
| parc       |           4 |
| lucrare    |           2 |
| bucurești  |           2 |
| public     |           2 |
| curățenie  |           1 |
| primăvară  |           1 |
| administra |           1 |
| lună       |           1 |
| martie     |           1 |
| aprilie    |           1 |
| toalet     |           1 |
| arborii    |           1 |
| arbuștie   |           1 |
| tunde      |           1 |
| gard       |           1 |
| viu        |           1 |
| îngriji    |           1 |
| rond       |           1 |
| trandafir  |           1 |

### 2025-03-11 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| onest             |           3 |
| însuși            |           1 |
| membru            |           1 |
| familie           |           1 |
| jur               |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-11 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| român      |           3 |
| decizie    |           2 |
| anulare    |           2 |
| alegere    |           2 |
| stat       |           2 |
| slab       |           2 |
| putea      |           2 |
| trebui     |           2 |
| sine       |           2 |
| schimba    |           2 |
| partid     |           1 |
| politic    |           1 |
| corupt     |           1 |
| promova    |           1 |
| incompeten |           1 |
| funcție    |           1 |
| public     |           1 |
| principal  |           1 |
| vinovat    |           1 |
| situație   |           1 |

### 2025-03-11 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| nicușor           |           1 |
| vedea             |           1 |
| învingător        |           1 |
| romaniaonestă     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-11 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| responsabilitate  |           1 |
| tenacitate        |           1 |
| acasă             |           1 |
| societate         |           1 |
| romaniaonestă     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-12 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| asb            |           4 |
| vrea           |           4 |
| gestiona       |           3 |
| platformă      |           2 |
| proiect        |           2 |
| bucurești      |           2 |
| trafic         |           2 |
| semna          |           1 |
| cadru          |           1 |
| an             |           1 |
| administrație  |           1 |
| străzilor      |           1 |
| crea           |           1 |
| bază           |           1 |
| geospațial     |           1 |
| infrastructură |           1 |
| ajuta          |           1 |
| eficient       |           1 |
| stradă         |           1 |
| îmbunătățim    |           1 |

### 2025-03-12 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| întoarce          |           1 |
| franța            |           1 |
| suporta           |           1 |
| nedreptate        |           1 |
| luptă             |           1 |
| continuu          |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| variantă   |           2 |
| domn       |           1 |
| cristian   |           1 |
| tudor      |           1 |
| popescu    |           1 |
| solicita   |           1 |
| final      |           1 |
| intervi    |           1 |
| realiza    |           1 |
| împreună   |           1 |
| cătălin    |           1 |
| striblea   |           1 |
| radio      |           1 |
| europa     |           1 |
| fm         |           1 |
| rezolva    |           1 |
| problemă   |           1 |
| matematică |           1 |
| accepta    |           1 |
| plăcere    |           1 |

### 2025-03-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| revedea    |           1 |
| alba       |           1 |
| iulia      |           1 |
| prieten    |           1 |
| vechi      |           1 |
| alături    |           1 |
| protesta   |           1 |
| exploatăre |           1 |
| cian       |           1 |
| roșiă      |           1 |
| montan     |           1 |
| protest    |           1 |
| arăta      |           1 |
| popor      |           1 |
| putere     |           1 |
| schimba    |           1 |
| destin     |           1 |
| țară       |           1 |
| amenința   |           1 |

### 2025-03-12 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| nicușor           |           1 |
| putea             |           1 |
| românia           |           1 |
| țară              |           1 |
| sine              |           1 |
| pleca             |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-12 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| schimbări         |           1 |
| putere            |           1 |
| exempl            |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-13 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| milion         |           3 |
| euro           |           3 |
| modernizare    |           3 |
| termoficare    |           3 |
| bucurești      |           3 |
| vrea           |           3 |
| fond           |           3 |
| rețea          |           3 |
| sistem         |           2 |
| finanțare      |           2 |
| investiție     |           2 |
| infrastructură |           2 |
| reabilitare    |           2 |
| îmbunătățire   |           2 |
| pas            |           2 |
| continua       |           2 |
| oraș           |           2 |
| semna          |           1 |
| contract       |           1 |
| valoare        |           1 |

### 2025-03-13 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| violent           |           1 |
| problemă          |           1 |
| sine              |           1 |
| confrunta         |           1 |
| familie           |           1 |
| românia           |           1 |
| sărăcie           |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-13 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |           2 |
| lucrurile     |           1 |
| important     |           1 |
| vedea         |           1 |
| suprafață     |           1 |
| schimbare     |           1 |
| real          |           1 |
| produce       |           1 |
| privind       |           1 |
| lucru         |           1 |
| profunzime    |           1 |
| romaniaonesta |           1 |

### 2025-03-13 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| lupta             |           1 |
| an                |           1 |
| instituție        |           1 |
| strâmb            |           1 |
| stat              |           1 |
| mafie             |           1 |
| imobiliar         |           1 |
| pregăti           |           1 |
| deveni            |           1 |
| primar            |           1 |
| capitală          |           1 |
| oră               |           1 |
| invi              |           1 |
| episod            |           1 |
| viață             |           1 |
| luptă             |           1 |
| civic             |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-13 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| nedreptate   |           2 |
| sistem       |           2 |
| civic        |           2 |
| niciodat     |           1 |
| suporta      |           1 |
| lupta        |           1 |
| an           |           1 |
| nedrept      |           1 |
| mafie        |           1 |
| imobiliar    |           1 |
| vorbia       |           1 |
| roșiă        |           1 |
| montan       |           1 |
| patrimoniu   |           1 |
| bucureștean  |           1 |
| spațiu       |           1 |
| verde        |           1 |
| recunoscător |           1 |
| organizație  |           1 |
| activiștilor |           1 |

### 2025-03-13 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| sonic       |           2 |
| analiză     |           2 |
| bucurești   |           2 |
| intervenție |           2 |
| aviz        |           2 |
| toaletare   |           2 |
| defrișare   |           2 |
| specialist  |           2 |
| clar        |           2 |
| tomograful  |           1 |
| picus       |           1 |
| detecta     |           1 |
| non-invaziv |           1 |
| eventual    |           1 |
| problemă    |           1 |
| intern      |           1 |
| copace      |           1 |
| putregaiu   |           1 |
| cavităță    |           1 |
| măsurare    |           1 |

### 2025-03-14 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| vrea           |           5 |
| bd             |           5 |
| infrastructură |           4 |
| tramvai        |           3 |
| oraș           |           3 |
| lucrare        |           3 |
| primărie       |           2 |
| capitală       |           2 |
| porr           |           2 |
| esențial       |           2 |
| reabilitare    |           2 |
| bucurești      |           2 |
| aduce          |           2 |
| semnificativ   |           2 |
| dezvoltare     |           2 |
| întâlnire      |           1 |
| important      |           1 |
| sediu          |           1 |
| membru         |           1 |
| conducere      |           1 |

### 2025-03-14 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| arc           |           2 |
| triumf        |           2 |
| vrea          |           2 |
| permanent     |           2 |
| vizitare      |           2 |
| cultură       |           2 |
| bucurești     |           2 |
| istorie       |           2 |
| moment        |           2 |
| armată        |           2 |
| român         |           2 |
| război        |           2 |
| deschide      |           1 |
| începe        |           1 |
| sâmbătă       |           1 |
| martie        |           1 |
| centru        |           1 |
| palatele      |           1 |
| brâncovenești |           1 |
| porțile       |           1 |

### 2025-03-14 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| spune             |           1 |
| tinerilor         |           1 |
| schimbare         |           1 |
| simți             |           1 |
| romaniaonestă     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-14 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| vrea              |           1 |
| aduce             |           1 |
| român             |           1 |
| plecat            |           1 |
| acasă             |           1 |
| trebui            |           1 |
| oferi             |           1 |
| același           |           1 |
| condiție          |           1 |
| vest              |           1 |
| romaniaonestă     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-14 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| sărut             |           1 |
| mână              |           1 |
| aglaia            |           1 |
| romaniaonestă     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-14 — facebook-post

| cuvânt                     |   frecvență |
|:---------------------------|------------:|
| împreună                   |           2 |
| onestă                     |           2 |
| aștepta                    |           1 |
| sâmbătă                    |           1 |
| martie                     |           1 |
| oraș                       |           1 |
| tulcea                     |           1 |
| constanța                  |           1 |
| sta                        |           1 |
| vorbă                      |           1 |
| plimbare                   |           1 |
| completează                |           1 |
| formular                   |           1 |
| httpsnicusordanrovoluntari |           1 |
| vrea                       |           1 |
| primi                      |           1 |
| detaliu                    |           1 |
| locație                    |           1 |
| oră                        |           1 |
| întâlnire                  |           1 |

### 2025-03-14 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| tinerii           |           1 |
| motiv             |           1 |
| rămâne            |           1 |
| românia           |           1 |
| continua          |           1 |
| crede             |           1 |
| țară              |           1 |
| ascult            |           1 |
| susține           |           1 |
| împreună          |           1 |
| lupta             |           1 |
| viitor            |           1 |
| întru             |           1 |
| românie           |           1 |
| onestă            |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |
| tineri            |           1 |

### 2025-03-15 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| timișoara   |           3 |
| an          |           2 |
| proclamație |           2 |
| fundamental |           2 |
| românia     |           2 |
| societate   |           2 |
| sine        |           1 |
| împlini     |           1 |
| citire      |           1 |
| document    |           1 |
| democrație  |           1 |
| crea        |           1 |
| cale        |           1 |
| liber       |           1 |
| uita        |           1 |
| cere        |           1 |
| celebru     |           1 |
| punct       |           1 |
| lustrare    |           1 |
| servi       |           1 |

### 2025-03-15 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| mal           |           3 |
| dâmboviță     |           3 |
| proiect       |           3 |
| urban         |           3 |
| sine          |           3 |
| alpab         |           2 |
| planta        |           2 |
| zonă          |           2 |
| verde         |           2 |
| pod           |           2 |
| internațional |           1 |
| râurilor      |           1 |
| angajat       |           1 |
| împreună      |           1 |
| nodmakerspace |           1 |
| strânge       |           1 |
| deșe          |           1 |
| arbust        |           1 |
| timpuri       |           1 |
| arbor         |           1 |

### 2025-03-15 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| felicit      |           1 |
| comunitate   |           1 |
| maghiar      |           1 |
| românia      |           1 |
| ocazie       |           1 |
| zilei        |           1 |
| maghiarilor  |           1 |
| pretutindeni |           1 |
| mulțumi      |           1 |
| contribuție  |           1 |
| valoros      |           1 |
| dezvoltare   |           1 |
| țară         |           1 |
| împreună     |           1 |
| construi     |           1 |
| viitor       |           1 |
| prosper      |           1 |
| succes       |           1 |
| comun        |           1 |
| depinde      |           1 |

### 2025-03-15 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| constanța     |           2 |
| economic      |           2 |
| administrație |           2 |
| simți         |           1 |
| om            |           1 |
| vrea          |           1 |
| adevărat      |           1 |
| schimbare     |           1 |
| municipiu     |           1 |
| județ         |           1 |
| potențial     |           1 |
| uriaș         |           1 |
| corupție      |           1 |
| instituție    |           1 |
| stat          |           1 |
| precum        |           1 |
| port          |           1 |
| lipsă         |           1 |
| viziune       |           1 |
| românia       |           1 |

### 2025-03-15 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           4 |
| trebui     |           3 |
| sine       |           3 |
| județ      |           3 |
| dezvolta   |           2 |
| economic   |           2 |
| tulcea     |           2 |
| securitate |           2 |
| cetățean   |           2 |
| putea      |           2 |
| european   |           2 |
| înzestrare |           2 |
| militar    |           2 |
| echilibrat |           1 |
| impulsiona |           1 |
| graniță    |           1 |
| estic      |           1 |
| motiv      |           1 |
| prezent    |           1 |
| dovedi     |           1 |

### 2025-03-16 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| rating      |           3 |
| românia     |           3 |
| vrea        |           3 |
| agenție     |           2 |
| retrograda  |           2 |
| țară        |           2 |
| lucru       |           2 |
| ratings     |           2 |
| atragere    |           2 |
| ban         |           2 |
| reformă     |           2 |
| guvern      |           2 |
| zgomot      |           1 |
| electoral   |           1 |
| trata       |           1 |
| discret     |           1 |
| știre       |           1 |
| moodys      |           1 |
| perspectivă |           1 |
| stabil      |           1 |

### 2025-03-16 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| câine       |           4 |
| capitală    |           2 |
| aspa        |           2 |
| sine        |           2 |
| sterilizare |           2 |
| microcipare |           2 |
| acțiune     |           1 |
| informare   |           1 |
| control     |           1 |
| verificare  |           1 |
| stăpân      |           1 |
| loc         |           1 |
| săptămână   |           1 |
| sector      |           1 |
| participa   |           1 |
| polițist    |           1 |
| local       |           1 |
| angajat     |           1 |
| jandarmeria |           1 |
| bucurești   |           1 |

### 2025-03-16 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| tulcea         |           1 |
| ivan           |           1 |
| patzaichinivan |           1 |
| patzaichin     |           1 |
| model          |           1 |
| modestie       |           1 |
| perseverență   |           1 |
| echilibru      |           1 |
| romaniaonesta  |           1 |

### 2025-03-17 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |           3 |
| fond          |           2 |
| național      |           2 |
| finanțare     |           2 |
| consolidare   |           2 |
| milion        |           2 |
| leu           |           2 |
| bloc          |           1 |
| locuință      |           1 |
| situa         |           1 |
| cale          |           1 |
| victoriei     |           1 |
| număr         |           1 |
| consolida     |           1 |
| nerambursabil |           1 |
| amccrs        |           1 |
| semna         |           1 |
| contract      |           1 |
| minister      |           1 |
| dezvoltării   |           1 |

### 2025-03-17 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| spune       |           2 |
| univea      |           1 |
| considera   |           1 |
| încăpățâna  |           1 |
| vedea       |           1 |
| perseverent |           1 |
| lucru       |           1 |
| om          |           1 |
| tulcea      |           1 |
| constanța   |           1 |
| același     |           1 |
| împărtăși   |           1 |
| dezamăgire  |           1 |
| față        |           1 |
| actual      |           1 |
| clasă       |           1 |
| politic     |           1 |
| moment      |           1 |
| schimbare   |           1 |
| folosi      |           1 |

### 2025-03-18 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           2 |
| țară       |           2 |
| acorda     |           1 |
| interviu   |           1 |
| cotidian   |           1 |
| monde      |           1 |
| vorbi      |           1 |
| alegere    |           1 |
| context    |           1 |
| politic    |           1 |
| actual     |           1 |
| potențial  |           1 |
| europa     |           1 |
| lume       |           1 |
| convingere |           1 |
| putea      |           1 |
| deveni     |           1 |
| valoare    |           1 |
| onestitate |           1 |
| conta      |           1 |

### 2025-03-18 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| palat        |           2 |
| monument     |           2 |
| istoric      |           2 |
| investitor   |           2 |
| clădire      |           2 |
| semna        |           1 |
| autorizație  |           1 |
| construire   |           1 |
| restaurare   |           1 |
| oscar        |           1 |
| maugsch      |           1 |
| cunoaște     |           1 |
| societății   |           1 |
| asigurare    |           1 |
| generală     |           1 |
| vorbă        |           1 |
| situa        |           1 |
| universitate |           1 |
| bd           |           1 |
| bulevard     |           1 |

### 2025-03-18 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| ban           |           3 |
| public        |           3 |
| trebui        |           2 |
| regulă        |           2 |
| românia       |           2 |
| președinte    |           2 |
| transparența  |           1 |
| cheltuirii    |           1 |
| cetățean      |           1 |
| deveni        |           1 |
| inadmisibil   |           1 |
| an            |           1 |
| ști           |           1 |
| cheltuii      |           1 |
| instituție    |           1 |
| desecretizare |           1 |
| cost          |           1 |
| zbor          |           1 |
| decât         |           1 |
| întări        |           1 |

### 2025-03-19 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| stradă        |           8 |
| kilometru     |           5 |
| conduct       |           5 |
| modernizare   |           3 |
| fond          |           3 |
| bd            |           3 |
| șantier       |           2 |
| termoficare   |           2 |
| asigura       |           2 |
| european      |           2 |
| nerambursabil |           2 |
| lungime       |           2 |
| vrea          |           2 |
| zonă          |           2 |
| precum        |           2 |
| șosea         |           2 |
| total         |           2 |
| perioadă      |           2 |
| deschidea     |           1 |
| încă          |           1 |

### 2025-03-19 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| diasporă      |           2 |
| diaspor       |           1 |
| impresiona    |           1 |
| gest          |           1 |
| român         |           1 |
| oferi         |           1 |
| încredere     |           1 |
| mulțumi       |           1 |
| nicusordan    |           1 |
| romaniaonesta |           1 |
| comunitate    |           1 |
| emotii        |           1 |
| fyp           |           1 |

### 2025-03-20 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| pleca       |           4 |
| român       |           2 |
| țară        |           2 |
| românia     |           2 |
| admirație   |           1 |
| acasă       |           1 |
| rost        |           1 |
| străinătate |           1 |
| presupune   |           1 |
| curaj       |           1 |
| capacitate  |           1 |
| adaptare    |           1 |
| forță       |           1 |
| interior    |           1 |
| uriaș       |           1 |
| rezista     |           1 |
| dor         |           1 |
| drag        |           1 |
| casă        |           1 |
| paris       |           1 |

### 2025-03-20 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |           2 |
| stat          |           2 |
| alege         |           1 |
| președinte    |           1 |
| pune          |           1 |
| practică      |           1 |
| experiență    |           1 |
| acumula       |           1 |
| administrație |           1 |
| ultim         |           1 |
| an            |           1 |
| românia       |           1 |
| țară          |           1 |
| eficient      |           1 |
| esențial      |           1 |
| consolida     |           1 |
| instituție    |           1 |
| funcțional    |           1 |
| justiție      |           1 |
| rol           |           1 |

### 2025-03-20 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| vedea             |           1 |
| amintire          |           1 |
| studenție         |           1 |
| paris             |           1 |
| nicusorpresedinte |           1 |

### 2025-03-21 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| calitate   |           5 |
| aer        |           5 |
| mediu      |           3 |
| vrea       |           3 |
| contract   |           2 |
| realizare  |           2 |
| plan       |           2 |
| pica       |           2 |
| oraș       |           2 |
| atmosferic |           2 |
| evaluare   |           2 |
| proiect    |           2 |
| vito       |           2 |
| belgia     |           2 |
| nivel      |           2 |
| atribui    |           1 |
| integrat   |           1 |
| document   |           1 |
| strategic  |           1 |
| esențial   |           1 |

### 2025-03-21 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| economie   |           2 |
| combatere  |           1 |
| ferm       |           1 |
| evaziune   |           1 |
| fiscal     |           1 |
| recuperare |           1 |
| just       |           1 |
| fond       |           1 |
| încălca    |           1 |
| lege       |           1 |
| putea      |           1 |
| aduce      |           1 |
| ban        |           1 |
| esențial   |           1 |
| transforma |           1 |
| obiectiv   |           1 |
| prioritate |           1 |
| absolut    |           1 |
| proiect    |           1 |
| țară       |           1 |

### 2025-03-21 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| sine         |           2 |
| putea        |           2 |
| încredere    |           1 |
| cetățean     |           1 |
| câștiga      |           1 |
| greu         |           1 |
| pierde       |           1 |
| ușor         |           1 |
| alegere      |           1 |
| prezidențial |           1 |
| început      |           1 |
| proces       |           1 |
| recâștigare  |           1 |
| încrederii   |           1 |
| român        |           1 |
| instituție   |           1 |
| stat         |           1 |
| democrație   |           1 |
| discuta      |           1 |
| subiect      |           1 |

### 2025-03-21 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| politicienii      |           1 |
| aleși             |           1 |
| servi             |           1 |
| interes           |           1 |
| cetățean          |           1 |
| responsabilitate  |           1 |
| trebui            |           1 |
| întotdeauna       |           1 |
| prezent           |           1 |
| gândire           |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-22 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| andrei            |           1 |
| întreba           |           1 |
| măsură            |           1 |
| putea             |           1 |
| lua               |           1 |
| reducere          |           1 |
| deficit           |           1 |
| bugetar           |           1 |
| răspunde          |           1 |
| întrebare         |           1 |
| subiect           |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-22 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| echipa   |           1 |
| sine     |           1 |
| susține  |           1 |
| moment   |           1 |
| dificil  |           1 |

### 2025-03-22 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| oral          |           4 |
| copil         |           4 |
| bucurești     |           4 |
| sănătate      |           3 |
| școală        |           3 |
| educațional   |           2 |
| prim          |           2 |
| vrea          |           2 |
| sesiune       |           2 |
| învăța        |           2 |
| oară          |           2 |
| lună          |           1 |
| campanie      |           1 |
| administrație |           1 |
| spitalelor    |           1 |
| serviciilor   |           1 |
| medical       |           1 |
| assmb         |           1 |
| direcție      |           1 |
| medicină      |           1 |

### 2025-03-22 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| poziție           |           1 |
| buletin           |           1 |
| vot               |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |
| nd                |           1 |

### 2025-03-23 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| modernizare   |           2 |
| tramvai       |           2 |
| an            |           1 |
| continuăm     |           1 |
| investiție    |           1 |
| transport     |           1 |
| comun         |           1 |
| achiziționa   |           1 |
| încă          |           1 |
| documentație  |           1 |
| pregăti       |           1 |
| accesare      |           1 |
| fond          |           1 |
| nerambursabil |           1 |
| program       |           1 |
| operațional   |           1 |
| regional      |           1 |
| aștepta       |           1 |
| lansare       |           1 |
| ghid          |           1 |

### 2025-03-23 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| românia          |           3 |
| datorie          |           3 |
| cheltuială       |           3 |
| criză            |           2 |
| miliard          |           2 |
| fiscal           |           2 |
| creștere         |           2 |
| președinte       |           2 |
| sine             |           1 |
| confrunta        |           1 |
| precedent        |           1 |
| datoriu          |           1 |
| jumătate         |           1 |
| produce          |           1 |
| țară             |           1 |
| depăși           |           1 |
| leu              |           1 |
| produsinternbrut |           1 |
| echivalent       |           1 |
| euro             |           1 |

### 2025-03-23 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| energică      |           1 |
| împreună      |           1 |
| românia       |           1 |
| onestă        |           1 |
| voluntarind   |           1 |
| bucuresti     |           1 |
| diasporă      |           1 |
| arad          |           1 |
| lugoj         |           1 |
| craiova       |           1 |
| cluj          |           1 |
| brasov        |           1 |
| ilfov         |           1 |
| iasi          |           1 |
| botoșani      |           1 |
| râmnicuvâlcea |           1 |
| constanța     |           1 |
| slobozia      |           1 |
| prahovă       |           1 |
| suceava       |           1 |

### 2025-03-23 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| week-end          |           1 |
| bucurești         |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |
| nd                |           1 |

### 2025-03-24 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| asociație         |           1 |
| salva             |           1 |
| bucurești         |           1 |
| școală            |           1 |
| urbanism          |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-24 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| ego               |           1 |
| capăt             |           1 |
| opri              |           1 |
| abuzure           |           1 |
| urbanistic        |           1 |
| bucurești         |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-24 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| tramvai    |           2 |
| imperio    |           2 |
| românia    |           2 |
| achiziție  |           2 |
| producător |           2 |
| român      |           2 |
| astra      |           1 |
| arad       |           1 |
| exemplu    |           1 |
| perfect    |           1 |
| produs     |           1 |
| calitate   |           1 |
| bun        |           1 |
| precum     |           1 |
| importate  |           1 |
| reprezenta |           1 |
| investiție |           1 |
| mandat     |           1 |
| prim       |           1 |
| primărie   |           1 |

### 2025-03-24 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| președinte        |           1 |
| inovator          |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-24 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| urbanistic   |           3 |
| princip      |           2 |
| dezvoltare   |           2 |
| corect       |           2 |
| lege         |           2 |
| sine         |           2 |
| important    |           1 |
| luptă        |           1 |
| activitate   |           1 |
| public       |           1 |
| apărare      |           1 |
| bucurești    |           1 |
| preluare     |           1 |
| mandat       |           1 |
| primar       |           1 |
| general      |           1 |
| reglementare |           1 |
| încălca      |           1 |
| constant     |           1 |
| lucru        |           1 |

### 2025-03-25 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| putea             |           1 |
| nicușor           |           1 |
| dan               |           1 |
| președinte        |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-25 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| mergeai           |           1 |
| nicușor           |           1 |
| dan               |           1 |
| acțiune           |           1 |
| stiai             |           1 |
| merita            |           1 |
| lupți             |           1 |
| cauză             |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-25 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| nicușor           |           1 |
| dan               |           1 |
| curaj             |           1 |
| merge             |           1 |
| dincolo           |           1 |
| protest           |           1 |
| activist          |           1 |
| civic             |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-25 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| lucru    |           1 |
| ipotetic |           1 |
| vorbi    |           1 |

### 2025-03-26 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| reformă             |           2 |
| schimbare           |           2 |
| gestiona            |           1 |
| situație            |           1 |
| financiar           |           1 |
| complica            |           1 |
| primărie            |           1 |
| capitală            |           1 |
| lupta               |           1 |
| vrea                |           1 |
| același             |           1 |
| lucru               |           1 |
| românia             |           1 |
| nicusordan          |           1 |
| romaniaonesta       |           1 |
| bucuresti           |           1 |
| alegeriprezidential |           1 |

### 2025-03-26 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| candidez          |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |
| panalacapat       |           1 |

### 2025-03-26 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| modernizare |           5 |
| linie       |           5 |
| tramvai     |           5 |
| stradă      |           3 |
| lucrare     |           3 |
| transport   |           3 |
| public      |           3 |
| bulevard    |           2 |
| expoziție   |           2 |
| strada      |           2 |
| kilometru   |           2 |
| esențial    |           2 |
| necesar     |           2 |
| începem     |           1 |
| adiacent    |           1 |
| demara      |           1 |
| aviator     |           1 |
| popișteanu  |           1 |
| puț         |           1 |
| crăciun     |           1 |

### 2025-03-26 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| schimbare         |           1 |
| profund           |           1 |
| sistem            |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-26 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| buget               |           2 |
| românia             |           1 |
| minus               |           1 |
| urgent              |           1 |
| reformă             |           1 |
| echilibra           |           1 |
| asigura             |           1 |
| stabilitate         |           1 |
| economicănicisordan |           1 |
| romaniaonesta       |           1 |
| cheltuială          |           1 |
| economie            |           1 |
| finant              |           1 |
| fyp                 |           1 |

### 2025-03-26 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| președinte        |           1 |
| onest             |           1 |
| putea             |           1 |
| reforma           |           1 |
| stat              |           1 |
| român             |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-26 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| viziunea          |           1 |
| putere            |           1 |
| cuvânt            |           1 |
| putea             |           1 |
| aduce             |           1 |
| schimbare         |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-27 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| public         |           2 |
| an             |           1 |
| jumătate       |           1 |
| muncă          |           1 |
| bucurești      |           1 |
| funcțional     |           1 |
| prelua         |           1 |
| primărie       |           1 |
| generală       |           1 |
| întru          |           1 |
| oraș           |           1 |
| colaps         |           1 |
| blocaj         |           1 |
| financiar      |           1 |
| serviciu       |           1 |
| prag           |           1 |
| faliment       |           1 |
| infrastructură |           1 |
| blocat         |           1 |
| capitală       |           1 |

### 2025-03-27 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| invita       |           1 |
| mihai        |           1 |
| morar        |           1 |
| podcast      |           1 |
| fain         |           1 |
| simplu       |           1 |
| vorbi        |           1 |
| motiv        |           1 |
| alege        |           1 |
| candidez     |           1 |
| alegere      |           1 |
| prezidențial |           1 |
| trece        |           1 |
| istorie      |           1 |
| aproape      |           1 |
| uita         |           1 |
| liceu        |           1 |
| perioadă     |           1 |
| activism     |           1 |
| civic        |           1 |

### 2025-03-27 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           5 |
| moldova    |           3 |
| moment     |           2 |
| chișinău   |           2 |
| românia    |           2 |
| comun      |           2 |
| aderare    |           2 |
| republicii |           2 |
| uniune     |           2 |
| martie     |           1 |
| marca      |           1 |
| an         |           1 |
| esențial   |           1 |
| istorie    |           1 |
| vot        |           1 |
| sfat       |           1 |
| țării      |           1 |
| unire      |           1 |
| basarabia  |           1 |
| decizie    |           1 |

### 2025-03-27 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| internațional |           1 |
| teatr         |           1 |
| bun           |           1 |
| prilej        |           1 |
| celebra       |           1 |
| talent        |           1 |
| artist        |           1 |
| emoție        |           1 |
| oferi         |           1 |
| teatrul       |           1 |
| uni           |           1 |
| inspi         |           1 |
| vedea         |           1 |
| lume          |           1 |
| perspectivă   |           1 |
| an            |           1 |
| actor         |           1 |
| scenă         |           1 |
| magie         |           1 |
| teatru        |           1 |

### 2025-03-27 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| țelul             |           1 |
| reconstrui        |           1 |
| încredere         |           1 |
| om                |           1 |
| autoritate        |           1 |
| public            |           1 |
| societate         |           1 |
| însuși            |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-03-28 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| acorda        |           1 |
| interviu      |           1 |
| publicație    |           1 |
| politico      |           1 |
| răspunde      |           1 |
| întrebare     |           1 |
| relație       |           1 |
| transatlantic |           1 |
| important     |           1 |
| pace          |           1 |
| ucraina       |           1 |
| condiție      |           1 |
| sine          |           1 |
| încheia       |           1 |
| război        |           1 |
| putea         |           1 |
| amenințare    |           1 |
| garanție      |           1 |
| securitate    |           1 |
| românia       |           1 |

### 2025-03-28 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| funcțiile     |           1 |
| public        |           1 |
| moștenire     |           1 |
| familie       |           1 |
| românia       |           1 |
| profesionist  |           1 |
| real          |           1 |
| om            |           1 |
| competent     |           1 |
| aduce         |           1 |
| schimbare     |           1 |
| necesar       |           1 |
| nicusordan    |           1 |
| romaniaonesta |           1 |
| romania       |           1 |
| dreptate      |           1 |
| coruptie      |           1 |

### 2025-03-28 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| activ         |           2 |
| președinte    |           1 |
| trebui        |           1 |
| sine          |           1 |
| lua           |           1 |
| decizie       |           1 |
| prezent       |           1 |
| alături       |           1 |
| român         |           1 |
| nicusordan    |           1 |
| romaniaonesta |           1 |
| guvern        |           1 |
| romania       |           1 |
| viitor        |           1 |
| lider         |           1 |
| nd            |           1 |

### 2025-03-28 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| stradă      |           5 |
| ghencea     |           3 |
| tramvai     |           3 |
| proiect     |           2 |
| prelungire  |           2 |
| domnești    |           2 |
| cuprinde    |           2 |
| vale        |           2 |
| oltului     |           2 |
| str         |           2 |
| benzi       |           2 |
| linie       |           2 |
| companie    |           2 |
| sens        |           2 |
| intersecție |           2 |
| relua       |           1 |
| lucrare     |           1 |
| finalizare  |           1 |
| ordin       |           1 |
| începere    |           1 |

### 2025-03-29 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           3 |
| uniune       |           2 |
| european     |           2 |
| esențial     |           2 |
| aderare      |           1 |
| republicii   |           1 |
| moldova      |           1 |
| re           |           1 |
| prioritate   |           1 |
| reuși        |           1 |
| pas          |           1 |
| rapid        |           1 |
| atât         |           1 |
| beneficiu    |           1 |
| țară         |           1 |
| valorifica   |           1 |
| oportunitate |           1 |
| unic         |           1 |
| oferi        |           1 |
| întreg       |           1 |

### 2025-03-29 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |           3 |
| campanie    |           2 |
| efort       |           2 |
| comun       |           2 |
| începe      |           2 |
| împreună    |           2 |
| mișcare     |           2 |
| ban         |           2 |
| țară        |           2 |
| sine        |           2 |
| puternic    |           2 |
| român       |           2 |
| deschide    |           1 |
| oficial     |           1 |
| sediu       |           1 |
| candidatură |           1 |
| președinție |           1 |
| moment      |           1 |
| important   |           1 |
| continuare  |           1 |

### 2025-03-29 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| medical        |           6 |
| spital         |           3 |
| transplant     |           2 |
| hepatic        |           2 |
| realiza        |           2 |
| succes         |           2 |
| clinic         |           2 |
| maria          |           2 |
| profesionalism |           2 |
| echipă         |           2 |
| pacient        |           2 |
| an             |           2 |
| sine           |           2 |
| sistem         |           2 |
| sănătate       |           2 |
| sfânta         |           1 |
| unitate        |           1 |
| administra     |           1 |
| primărie       |           1 |
| capitală       |           1 |

### 2025-03-29 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| răspuns           |           1 |
| scurt             |           1 |
| întrebare         |           1 |
| clar              |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-30 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| invitat           |           1 |
| radu              |           1 |
| andrei            |           1 |
| tudor             |           1 |
| the               |           1 |
| news              |           1 |
| man               |           1 |
| podcast           |           1 |
| vorbi             |           1 |
| viziune           |           1 |
| românia           |           1 |
| direcție          |           1 |
| pune              |           1 |
| bucurești         |           1 |
| invi              |           1 |
| urmări            |           1 |
| interviu          |           1 |
| youtube           |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-03-30 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| moldova      |           8 |
| republică    |           7 |
| european     |           4 |
| românia      |           3 |
| cetățean     |           2 |
| român        |           2 |
| aderare      |           2 |
| esențial     |           2 |
| fond         |           2 |
| relație      |           2 |
| oportunitate |           2 |
| energetic    |           2 |
| discuta      |           1 |
| susținător   |           1 |
| chișinău     |           1 |
| importanță   |           1 |
| legătură     |           1 |
| strânge      |           1 |
| moldovan     |           1 |
| apropiat     |           1 |

### 2025-03-30 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| vrea              |           2 |
| român             |           1 |
| schimbare         |           1 |
| alegere           |           1 |
| prezidențial      |           1 |
| deschide          |           1 |
| drum              |           1 |
| etapă             |           1 |
| politic           |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |
| nd                |           1 |

### 2025-03-31 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| economic        |           4 |
| potențial       |           2 |
| turistic        |           2 |
| regiune         |           2 |
| vizita          |           1 |
| chișinău        |           1 |
| cramele         |           1 |
| cricova         |           1 |
| adevărat        |           1 |
| simbol          |           1 |
| vizită          |           1 |
| sublinia        |           1 |
| angajament      |           1 |
| ferm            |           1 |
| promova         |           1 |
| dezvoltare      |           1 |
| românia         |           1 |
| consolidare     |           1 |
| parteneriatelor |           1 |
| cultural        |           1 |

### 2025-03-31 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| obișnui       |           1 |
| spirit        |           1 |
| transparență  |           1 |
| împărtăși     |           1 |
| recent        |           1 |
| fotografie    |           1 |
| moment        |           1 |
| romaniaonesta |           1 |

### 2025-03-31 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| voluntarii        |           1 |
| campanie          |           1 |
| week-end          |           1 |
| prezent           |           1 |
| oraș              |           1 |
| implicare         |           1 |
| entuziasm         |           1 |
| împreună          |           1 |
| vrea              |           1 |
| construi          |           1 |
| românia           |           1 |
| onestă            |           1 |
| nicusorpresedinte |           1 |
| timiș             |           1 |
| olt               |           1 |
| prahova           |           1 |
| botoșani          |           1 |
| bihor             |           1 |
| sibiu             |           1 |
| dolj              |           1 |

### 2025-04-01 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| public       |           3 |
| campanie     |           3 |
| psd          |           2 |
| cheltui      |           2 |
| milion       |           2 |
| euro         |           2 |
| ban          |           2 |
| publică      |           2 |
| ultim        |           1 |
| an           |           1 |
| propagandă   |           1 |
| electoral    |           1 |
| același      |           1 |
| partid       |           1 |
| aloca        |           1 |
| fond         |           1 |
| prezidențial |           1 |
| premier      |           1 |
| ciolacu      |           1 |
| sine         |           1 |

### 2025-04-01 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| același    |           2 |
| situație   |           1 |
| financiar  |           1 |
| actual     |           1 |
| românia    |           1 |
| similar    |           1 |
| găsi       |           1 |
| primărie   |           1 |
| moment     |           1 |
| prelua     |           1 |
| instituție |           1 |
| cont       |           1 |
| blocat     |           1 |
| datoriu    |           1 |
| colosal    |           1 |
| an         |           1 |
| reuși      |           1 |
| reduce     |           1 |
| debloca    |           1 |
| investiție |           1 |

### 2025-04-02 — facebook-post

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

### 2025-04-02 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| finală            |           1 |
| ponta-simion      |           1 |
| rău               |           1 |
| variantă          |           1 |
| românia           |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-04-02 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| cultură       |           2 |
| teatr         |           1 |
| ion           |           1 |
| creangă       |           1 |
| abandona      |           1 |
| istorie       |           1 |
| impact        |           1 |
| incredibil    |           1 |
| reîncepe      |           1 |
| reabilitare   |           1 |
| românia       |           1 |
| onest         |           1 |
| însemna       |           1 |
| respect       |           1 |
| nicusordan    |           1 |
| romaniaonesta |           1 |
| bucuresti     |           1 |
| teatru        |           1 |

### 2025-04-03 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| new                 |           2 |
| york                |           2 |
| român               |           1 |
| trimite             |           1 |
| imagine             |           1 |
| letsdoitromanians   |           1 |
| nicusordanpresedint |           1 |

### 2025-04-03 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| teatr        |           4 |
| subordine    |           2 |
| primărie     |           2 |
| buget        |           2 |
| alocat       |           2 |
| instituție   |           2 |
| cultură      |           2 |
| problemă     |           2 |
| sine         |           2 |
| activitate   |           2 |
| investiție   |           2 |
| fond         |           2 |
| sursă        |           2 |
| finanțare    |           2 |
| întâlnire    |           1 |
| director     |           1 |
| afla         |           1 |
| municipiului |           1 |
| bucurești    |           1 |
| discuta      |           1 |

### 2025-04-03 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |           7 |
| festival      |           5 |
| bucurești     |           3 |
| an            |           3 |
| eveniment     |           3 |
| untold        |           2 |
| internațional |           2 |
| artist        |           2 |
| bucura        |           2 |
| semna         |           1 |
| protocol      |           1 |
| colaborare    |           1 |
| universe      |           1 |
| organizare    |           1 |
| anvergură     |           1 |
| începe        |           1 |
| vară          |           1 |
| arena         |           1 |
| național      |           1 |
| găzdui        |           1 |

### 2025-04-03 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |           3 |
| campanie      |           2 |
| susținător    |           2 |
| schimba       |           2 |
| oră           |           1 |
| începe        |           1 |
| oficial       |           1 |
| electoral     |           1 |
| voluntarii    |           1 |
| trebui        |           1 |
| ști           |           1 |
| regulă        |           1 |
| determinare   |           1 |
| succes        |           1 |
| creare        |           1 |
| redistribuire |           1 |
| conținut      |           1 |
| permite       |           1 |
| singur        |           1 |
| restricție    |           1 |

### 2025-04-03 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| român     |           3 |
| diaspora  |           3 |
| românia   |           2 |
| madrid    |           1 |
| londra    |           1 |
| roma      |           1 |
| paris     |           1 |
| berlin    |           1 |
| bruxelles |           1 |
| new       |           1 |
| york      |           1 |
| milion    |           1 |
| munci     |           1 |
| trăi      |           1 |
| spera     |           1 |
| schimbare |           1 |
| real      |           1 |
| mesaj     |           1 |
| pune      |           1 |
| întrebare |           1 |

### 2025-04-03 — facebook-post

| cuvânt                 |   frecvență |
|:-----------------------|------------:|
| berlin                 |           2 |
| danke                  |           1 |
| schn                   |           1 |
| român                  |           1 |
| trimite                |           1 |
| poză                   |           1 |
| nicusorpresedinte      |           1 |
| deceleefricadediaspora |           1 |
| romaniaonesta          |           1 |

### 2025-04-03 — facebook-post

| cuvânt                   |   frecvență |
|:-------------------------|------------:|
| atinge                   |           2 |
| obiectiv                 |           1 |
| donație                  |           1 |
| deadlin                  |           1 |
| diseară                  |           1 |
| oră                      |           1 |
| ziceti                   |           1 |
| putem                    |           1 |
| romaniaonesta            |           1 |
| nicusorpresedinte        |           1 |
| httpsnicusordanrodoneaza |           1 |

### 2025-04-03 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| împreună          |           1 |
| merge             |           1 |
| capăt             |           1 |
| nd                |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-03 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| vrea      |           4 |
| stat      |           3 |
| comercial |           3 |
| proteja   |           3 |
| trebui    |           2 |
| guvern    |           2 |
| măsură    |           2 |
| românesc  |           2 |
| putea     |           2 |
| față      |           2 |
| românia   |           2 |
| uniune    |           2 |
| european  |           2 |
| economie  |           2 |
| tarifele  |           1 |
| impune    |           1 |
| unit      |           1 |
| afecta    |           1 |
| întreg    |           1 |
| lume      |           1 |

### 2025-04-03 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| apă          |           2 |
| proiect      |           1 |
| începe       |           1 |
| an           |           1 |
| finaliza     |           1 |
| stație       |           1 |
| epurare      |           1 |
| glina        |           1 |
| funcționa    |           1 |
| capacitate   |           1 |
| maxim        |           1 |
| bucurești    |           1 |
| curat        |           1 |
| niciodată    |           1 |
| nicusordan   |           1 |
| bucuresti    |           1 |
| mediu        |           1 |
| epurareglină |           1 |
| pmb          |           1 |

### 2025-04-04 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| românia                         |           5 |
| northatlantictreatyorganization |           4 |
| context                         |           3 |
| rămâne                          |           3 |
| securitate                      |           3 |
| activ                           |           3 |
| industrie                       |           3 |
| an                              |           2 |
| alianță                         |           2 |
| europe                          |           2 |
| țară                            |           2 |
| rusia                           |           2 |
| stat                            |           2 |
| european                        |           2 |
| militar                         |           2 |
| apărare                         |           2 |
| plan                            |           2 |
| român                           |           2 |
| aniversa                        |           1 |
| întru                           |           1 |

### 2025-04-04 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| cred              |           2 |
| românia           |           1 |
| europa            |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-04 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| voluntarii  |           1 |
| începe      |           1 |
| campanie    |           1 |
| electoral   |           1 |
| energie     |           1 |
| determinare |           1 |
| românia     |           1 |
| onestă      |           1 |
| însemna     |           1 |
| mișcare     |           1 |
| sine        |           1 |
| dori        |           1 |
| schimbare   |           1 |
| real        |           1 |
| țară        |           1 |
| bun         |           1 |
| nd          |           1 |
| cluj        |           1 |
| brașov      |           1 |
| iași        |           1 |

### 2025-04-05 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| părinte  |           2 |
| război   |           2 |
| crimă    |           2 |
| imagine  |           2 |
| lung     |           1 |
| madrid   |           1 |
| ajunge   |           1 |
| cameră   |           1 |
| hotel    |           1 |
| știre    |           1 |
| cuvânt   |           1 |
| veni     |           1 |
| ușor     |           1 |
| vedea    |           1 |
| plângâ   |           1 |
| sine     |           1 |
| copil    |           1 |
| ucis     |           1 |
| ucraina  |           1 |
| aduce    |           1 |

### 2025-04-05 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| român           |           3 |
| regiune         |           2 |
| madrid          |           2 |
| antreprenor     |           2 |
| diasporă        |           2 |
| oameni          |           2 |
| serviciu        |           2 |
| muncă           |           2 |
| trebui          |           2 |
| țară            |           2 |
| românia         |           2 |
| forță           |           1 |
| antreprenorilor |           1 |
| discuție        |           1 |
| deschis         |           1 |
| serios          |           1 |
| dinamic         |           1 |
| puternic        |           1 |
| comunitate      |           1 |
| business        |           1 |

### 2025-04-05 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| țară      |           5 |
| românia   |           4 |
| român     |           3 |
| întâlnire |           2 |
| românesc  |           2 |
| arganda   |           2 |
| del       |           2 |
| rey       |           2 |
| regiune   |           2 |
| madrid    |           2 |
| om        |           2 |
| uita      |           2 |
| însemna   |           2 |
| limbă     |           2 |
| veni      |           2 |
| vorbi     |           2 |
| primi     |           1 |
| căldură   |           1 |
| harnic    |           1 |
| demn      |           1 |

### 2025-04-05 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| român        |           8 |
| sine         |           5 |
| diasporă     |           4 |
| vrea         |           4 |
| radio        |           3 |
| real         |           3 |
| românia      |           3 |
| întreg       |           2 |
| țară         |           2 |
| interviu     |           1 |
| alături      |           1 |
| plăcere      |           1 |
| invitat      |           1 |
| jurnalistă   |           1 |
| irina        |           1 |
| sântimbreanu |           1 |
| ascultat     |           1 |
| voce         |           1 |
| românesc     |           1 |
| spania       |           1 |

### 2025-04-05 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| vrea      |           5 |
| parc      |           4 |
| urban     |           3 |
| bucurești |           3 |
| amenaja   |           3 |
| tineret   |           3 |
| capitală  |           3 |
| zonă      |           3 |
| loc       |           3 |
| insulă    |           2 |
| plantă    |           2 |
| faună     |           2 |
| pasăre    |           2 |
| putea     |           2 |
| pajiște   |           1 |
| floare    |           1 |
| câmp      |           1 |
| sălbatic  |           1 |
| demers    |           1 |
| parte     |           1 |

### 2025-04-05 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| putere            |           1 |
| construi          |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-05 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           6 |
| oraș         |           4 |
| străzi       |           3 |
| aprilie      |           2 |
| ediție       |           2 |
| proiect      |           2 |
| deschis      |           2 |
| urban        |           2 |
| cale         |           2 |
| victoria     |           2 |
| arteră       |           2 |
| dedica       |           2 |
| comunitate   |           2 |
| street       |           2 |
| încânta      |           1 |
| anunța       |           1 |
| bucureștenie |           1 |
| începe       |           1 |
| lansa        |           1 |
| bucurești    |           1 |

### 2025-04-05 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| gicu           |           4 |
| micu           |           4 |
| madrid         |           3 |
| român          |           3 |
| vizită         |           2 |
| diasporă       |           2 |
| românesc       |           2 |
| spania         |           2 |
| cubas          |           2 |
| sagra          |           2 |
| început        |           2 |
| pleca          |           2 |
| greutate       |           2 |
| poveste        |           2 |
| antreprenorial |           2 |
| succes         |           2 |
| construi       |           2 |
| regiune        |           1 |
| bucurie        |           1 |
| cunosc         |           1 |

### 2025-04-06 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| românia           |           2 |
| sine              |           1 |
| repara            |           1 |
| întoarce          |           1 |
| mesaj             |           1 |
| pleca             |           1 |
| diasporă          |           1 |
| determinare       |           1 |
| ține              |           1 |
| reconstrui        |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |
| nd                |           1 |
| diasporaconteaza  |           1 |

### 2025-04-06 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| împreună     |           1 |
| vindeca      |           1 |
| românia      |           1 |
| medic        |           1 |
| profesionisc |           1 |
| asistente    |           1 |
| medical      |           1 |
| dedicat      |           1 |
| progres      |           1 |
| depinde      |           1 |
| management   |           1 |
| eficient     |           1 |
| susține      |           1 |
| decizie      |           1 |
| pune         |           1 |
| adevărat     |           1 |
| sănătate     |           1 |
| loc          |           1 |
| putea        |           1 |
| contribui    |           1 |

### 2025-04-06 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| românia           |           1 |
| juca              |           1 |
| ligă              |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-04-06 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| românia           |           2 |
| onest             |           1 |
| prezent           |           1 |
| voluntarii        |           1 |
| acțiune           |           1 |
| weekend           |           1 |
| campanie          |           1 |
| distribui         |           1 |
| pliant            |           1 |
| lipi              |           1 |
| afiș              |           1 |
| aduce             |           1 |
| mesaj             |           1 |
| atât              |           1 |
| țară              |           1 |
| diasporă          |           1 |
| împreună          |           1 |
| bun               |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-04-06 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| român             |           1 |
| spania            |           1 |
| purta             |           1 |
| suflet            |           1 |
| dorință           |           1 |
| arzător           |           1 |
| schimbare         |           1 |
| țară              |           1 |
| vrea              |           1 |
| aducem            |           1 |
| înapoi            |           1 |
| acasă             |           1 |
| trebui            |           1 |
| auzim             |           1 |
| voce              |           1 |
| înțelege          |           1 |
| speranță          |           1 |
| acționa           |           1 |
| împlini           |           1 |
| nicusorpresedinte |           1 |

### 2025-04-06 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| eveniment   |           3 |
| tradiții    |           2 |
| floare      |           2 |
| sărbători   |           2 |
| bucurești   |           2 |
| intrare     |           2 |
| autentic    |           2 |
| românesc    |           2 |
| întru       |           2 |
| meșteșug    |           2 |
| creație     |           2 |
| tradițional |           2 |
| reveni      |           1 |
| primărie    |           1 |
| capitală    |           1 |
| creart      |           1 |
| invita      |           1 |
| -a          |           1 |
| ediție      |           1 |
| oficial     |           1 |

### 2025-04-06 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| aspa        |           2 |
| parc        |           2 |
| sine        |           2 |
| adopta      |           2 |
| animal      |           2 |
| reuși       |           1 |
| târg        |           1 |
| adopții     |           1 |
| carol       |           1 |
| câin        |           1 |
| prezent     |           1 |
| eveniment   |           1 |
| găsi        |           1 |
| familie     |           1 |
| câine       |           1 |
| direct      |           1 |
| adăpost     |           1 |
| bucureștean |           1 |
| trece       |           1 |
| opri        |           1 |

### 2025-04-07 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| adevăr     |           2 |
| clip       |           1 |
| demonta    |           1 |
| minciun    |           1 |
| afirma     |           1 |
| niciodată  |           1 |
| educație   |           1 |
| sexual     |           1 |
| grădiniță  |           1 |
| dovadă     |           1 |
| conta      |           1 |
| manipulare |           1 |
| trebui     |           1 |
| expus      |           1 |
| nicusordan |           1 |
| nd         |           1 |
| romania    |           1 |
| adevar     |           1 |
| fakenews   |           1 |

### 2025-04-07 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| stabilitate |           4 |
| pnrr        |           3 |
| european    |           3 |
| românia     |           3 |
| pierdem     |           2 |
| miliard     |           2 |
| euro        |           2 |
| guvernare   |           2 |
| arăta       |           1 |
| psd-pnl     |           1 |
| risca       |           1 |
| ministru    |           1 |
| fondurilor  |           1 |
| recunoaște  |           1 |
| public      |           1 |
| exista      |           1 |
| risc        |           1 |
| pierdere    |           1 |
| ban         |           1 |
| noutate     |           1 |

### 2025-04-07 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| recăpăta          |           1 |
| încredere         |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-04-07 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           4 |
| român      |           3 |
| bun        |           3 |
| sine       |           3 |
| sănătate   |           3 |
| torrejn    |           2 |
| ardoz      |           2 |
| spania     |           2 |
| pierde     |           2 |
| stat       |           2 |
| temă       |           2 |
| trebui     |           2 |
| mulțumi    |           2 |
| întâlni    |           1 |
| puternic   |           1 |
| comunitate |           1 |
| regiune    |           1 |
| madrid     |           1 |
| trăi       |           1 |
| an         |           1 |

### 2025-04-07 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| marcel     |           3 |
| ciolacu    |           3 |
| românia    |           3 |
| român      |           3 |
| sprânceană |           3 |
| domn       |           3 |
| extern     |           2 |
| oficial    |           2 |
| stat       |           2 |
| emisar     |           2 |
| prim       |           1 |
| ministru   |           1 |
| guvern     |           1 |
| conduce    |           1 |
| politică   |           1 |
| paralelă   |           1 |
| linie      |           1 |
| dragoș     |           1 |
| numi       |           1 |
| premier    |           1 |

### 2025-04-07 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| patriotism        |           1 |
| însemna           |           1 |
| pune              |           1 |
| românia           |           1 |
| valoare           |           1 |
| condamni          |           1 |
| haos              |           1 |
| frică             |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-04-08 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |           3 |
| respect       |           2 |
| casă          |           2 |
| comunitate    |           2 |
| umăr          |           2 |
| nicolae       |           2 |
| gheorghe      |           2 |
| internațional |           1 |
| romilor       |           1 |
| gând          |           1 |
| îndrepta      |           1 |
| valoare       |           1 |
| uman          |           1 |
| ține          |           1 |
| împreună      |           1 |
| unitate       |           1 |
| sincer        |           1 |
| toleranță     |           1 |
| românia       |           1 |
| om            |           1 |

### 2025-04-08 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| dezbatere  |           3 |
| sine       |           2 |
| român      |           2 |
| consider   |           1 |
| propunere  |           1 |
| președinte |           1 |
| interimar  |           1 |
| domn       |           1 |
| ilie       |           1 |
| bolojan    |           1 |
| participa  |           1 |
| electoral  |           1 |
| palat      |           1 |
| cotroceni  |           1 |
| bun        |           1 |
| văd        |           1 |
| locație    |           1 |
| cadru      |           1 |
| neutru     |           1 |
| adecvat    |           1 |

### 2025-04-08 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |           1 |
| declara       |           1 |
| luptători     |           1 |
| anti-sistem   |           1 |
| fapt          |           1 |
| concret       |           1 |
| susține       |           1 |
| afirmațiile   |           1 |
| instanță      |           1 |
| oară          |           1 |
| apăra         |           1 |
| cauză         |           1 |
| om            |           1 |
| romaniaonesta |           1 |
| nicusordan    |           1 |

### 2025-04-09 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| succes            |           1 |
| tati              |           1 |
| aștepta           |           1 |
| antena            |           1 |
| vorbima           |           1 |
| românie           |           1 |
| onest             |           1 |
| puternic          |           1 |
| copil             |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-04-10 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| ponta     |           5 |
| alege     |           5 |
| victor    |           4 |
| sine      |           3 |
| dunăre    |           3 |
| românia   |           3 |
| cetățenie |           3 |
| steven    |           2 |
| seagal    |           2 |
| prim      |           2 |
| ministru  |           2 |
| inunda    |           2 |
| sat       |           2 |
| românesc  |           2 |
| loc       |           2 |
| primi     |           2 |
| produce   |           2 |
| pagubă    |           2 |
| serbia    |           2 |
| român     |           2 |

### 2025-04-10 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| candidat      |           2 |
| pontă         |           1 |
| singur        |           1 |
| autoproclama  |           1 |
| anti-soroșist |           1 |
| întâlnire     |           1 |
| soroș         |           1 |
| sistem        |           1 |
| tupeu         |           1 |
| sine          |           1 |
| pretinde      |           1 |
| anti-sistem   |           1 |

### 2025-04-11 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| cuvânt   |           1 |
| soacră   |           1 |
| emoționa |           1 |
| profund  |           1 |
| lilian   |           1 |

### 2025-04-11 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| persoană     |           2 |
| dizabilitate |           2 |
| capitală     |           2 |
| exprima      |           2 |
| indemnizație |           1 |
| bucurești    |           1 |
| reduce       |           1 |
| guvern       |           1 |
| psd-pnl-udmr |           1 |
| tăiere       |           1 |
| brutal       |           1 |
| buget        |           1 |
| propagandă   |           1 |
| cinic        |           1 |
| înșelător    |           1 |
| adversar     |           1 |
| răspândi     |           1 |
| perioadă     |           1 |
| inacceptabil |           1 |
| ignorare     |           1 |

### 2025-04-11 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| stat          |           6 |
| coaliție      |           4 |
| cheltuială    |           4 |
| crește        |           3 |
| eficiență     |           2 |
| sine          |           2 |
| populism      |           2 |
| final         |           1 |
| an            |           1 |
| trecut        |           1 |
| stabilitate   |           1 |
| psd-pnl       |           1 |
| înființă      |           1 |
| model         |           1 |
| administrație |           1 |
| trump         |           1 |
| departament   |           1 |
| guvernamental |           1 |
| reducere      |           1 |
| rămâne        |           1 |

### 2025-04-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| japonia    |           2 |
| românia    |           2 |
| hanami     |           2 |
| sărbătoare |           2 |
| florilor   |           2 |
| cireș      |           2 |
| parc       |           2 |
| cultură    |           2 |
| popor      |           2 |
| cunoști    |           2 |
| japonez    |           2 |
| trebui     |           2 |
| învățăm    |           2 |
| artă       |           2 |
| onora      |           1 |
| particip   |           1 |
| alături    |           1 |
| es         |           1 |
| katae      |           1 |
| takashi    |           1 |

### 2025-04-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           4 |
| purta      |           3 |
| domn       |           2 |
| ciolacu    |           1 |
| sine       |           1 |
| teme       |           1 |
| obliga     |           1 |
| fust       |           1 |
| ajunge     |           1 |
| cotroceni  |           1 |
| asigur     |           1 |
| prim       |           1 |
| ministru   |           1 |
| liber      |           1 |
| haină      |           1 |
| palat      |           1 |
| victoria   |           1 |
| material   |           1 |
| publicitar |           1 |
| politic    |           1 |

### 2025-04-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| live       |           1 |
| declarații |           1 |
| presă      |           1 |
| sediu      |           1 |
| campanie   |           1 |

### 2025-04-12 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| campanie     |           2 |
| sesizare     |           1 |
| autoritate   |           1 |
| electoral    |           1 |
| permanentă   |           1 |
| solicita     |           1 |
| respectare   |           1 |
| princip      |           1 |
| fair-play    |           1 |
| circumstanță |           1 |
| convenabile  |           1 |
| sine         |           1 |
| putea        |           1 |
| pretinde     |           1 |
| sust         |           1 |
| curat        |           1 |
| onest        |           1 |
| utiliza      |           1 |
| practică     |           1 |
| neloial      |           1 |

### 2025-04-13 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| vedere       |           1 |
| lipsă        |           1 |
| reacție      |           1 |
| instituție   |           1 |
| responsabil  |           1 |
| față         |           1 |
| val          |           1 |
| dezinformare |           1 |
| lansa        |           1 |
| rubric       |           1 |
| dedica       |           1 |
| demontare    |           1 |
| falsurilor   |           1 |
| circula      |           1 |
| online       |           1 |
| simți        |           1 |
| justifica    |           1 |
| însă         |           1 |
| consider     |           1 |
| esențial     |           1 |

### 2025-04-13 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| rusia      |           2 |
| condamn    |           1 |
| fermitate  |           1 |
| atac       |           1 |
| criminal   |           1 |
| lansa      |           1 |
| rachetă    |           1 |
| balistic   |           1 |
| oraș       |           1 |
| sumî       |           1 |
| ucraina    |           1 |
| moment     |           1 |
| om         |           1 |
| biserică   |           1 |
| sărbătoare |           1 |
| florii     |           1 |
| sine       |           1 |
| vedea      |           1 |
| săptămână  |           1 |
| întreg     |           1 |

### 2025-04-13 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| corupție  |           1 |
| motiv     |           1 |
| principal |           1 |
| om        |           1 |
| duce      |           1 |
| greu      |           1 |
| vorbi     |           1 |
| spital    |           1 |
| școală    |           1 |
| nivel     |           1 |
| trai      |           1 |
| conduce   |           1 |
| păcălit   |           1 |
| dezamăgi  |           1 |
| veni      |           1 |
| schimba   |           1 |
| lucru     |           1 |
| temeliu   |           1 |
| începe    |           1 |
| vârf      |           1 |

### 2025-04-13 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| bucurești |           2 |
| urban     |           2 |
| capitală  |           2 |
| vrea      |           2 |
| cale      |           2 |
| victoria  |           2 |
| găzdui    |           2 |
| concert   |           2 |
| atelieră  |           2 |
| street    |           2 |
| week-end  |           1 |
| străzi    |           1 |
| deschis   |           1 |
| promenadă |           1 |
| eveniment |           1 |
| outdoor   |           1 |
| loc       |           1 |
| weekend   |           1 |
| zonă      |           1 |
| sector    |           1 |

### 2025-04-13 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| târg      |           2 |
| paște     |           2 |
| aștepta   |           2 |
| artist    |           2 |
| tradiții  |           1 |
| floare    |           1 |
| sărbători |           1 |
| sine      |           1 |
| deschide  |           1 |
| weekend   |           1 |
| parc      |           1 |
| rege      |           1 |
| mihai     |           1 |
| herăstrău |           1 |
| aprilie   |           1 |
| stand     |           1 |
| plin      |           1 |
| bunătate  |           1 |
| cozonac   |           1 |
| pască     |           1 |

### 2025-04-14 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| cetățean    |           5 |
| politic     |           4 |
| candidat    |           4 |
| electoral   |           3 |
| bec         |           3 |
| libertate   |           3 |
| exprimare   |           3 |
| marcel      |           3 |
| ciolacu     |           3 |
| privi       |           3 |
| funcție     |           2 |
| birou       |           2 |
| liberă      |           2 |
| exprimar    |           2 |
| decizie     |           2 |
| sine        |           2 |
| scrie       |           2 |
| opinie      |           2 |
| conduce     |           2 |
| obligatoriu |           2 |

### 2025-04-14 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| întărire                        |           1 |
| poziție                         |           1 |
| românia                         |           1 |
| northatlantictreatyorganization |           1 |
| uniuneaeuropeană                |           1 |
| începe                          |           1 |
| consultare                      |           1 |
| aliat                           |           1 |
| față                            |           1 |
| amenințare                      |           1 |
| hibrid                          |           1 |
| confrunta                       |           1 |
| romaniaonesta                   |           1 |
| nicusorpresedint                |           1 |

### 2025-04-14 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| dori             |           1 |
| fetiță           |           1 |
| băiețel          |           1 |
| trăi             |           1 |
| românia          |           1 |
| datorie          |           1 |
| lăsa             |           1 |
| țară             |           1 |
| mândru           |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |
| nicusordan       |           1 |

### 2025-04-14 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| corupție   |           2 |
| președinte |           1 |
| absent     |           1 |
| iohannis   |           1 |
| tandem     |           1 |
| psd-pnl    |           1 |
| tolera     |           1 |
| caz        |           1 |
| sprijini   |           1 |
| măsură     |           1 |
| îmbunătăți |           1 |
| capacitate |           1 |
| dna        |           1 |
| diicot     |           1 |
| investiga  |           1 |
| aduce      |           1 |
| justiție   |           1 |
| vrea       |           1 |
| asigura    |           1 |
| proces     |           1 |

### 2025-04-15 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| postare         |           2 |
| număr           |           2 |
| raporta         |           2 |
| activitate      |           1 |
| suspect         |           1 |
| conturilor      |           1 |
| social          |           1 |
| medie           |           1 |
| sine            |           1 |
| extinde         |           1 |
| seară           |           1 |
| facebook        |           1 |
| depăși          |           1 |
| distribuire     |           1 |
| complet         |           1 |
| disproporționat |           1 |
| utilizator      |           1 |
| vizualiza       |           1 |
| situație        |           1 |
| principal       |           1 |

### 2025-04-15 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| an         |           3 |
| scădere    |           2 |
| străin     |           2 |
| față       |           2 |
| același    |           2 |
| perioadă   |           2 |
| capital    |           2 |
| sine       |           2 |
| producție  |           1 |
| industrial |           1 |
| prim       |           1 |
| lună       |           1 |
| investiție |           1 |
| direct     |           1 |
| mic        |           1 |
| trecut     |           1 |
| înscrie    |           1 |
| firm       |           1 |
| înființa   |           1 |
| companie   |           1 |

### 2025-04-15 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| urmăritor     |           3 |
| comentariu    |           3 |
| cont          |           2 |
| instagram     |           2 |
| tiktok        |           2 |
| părea         |           2 |
| ajuta         |           2 |
| specialiștii  |           2 |
| spune         |           2 |
| atac          |           2 |
| -ul           |           2 |
| nicusordanpg  |           1 |
| nicusordanpmb |           1 |
| sine          |           1 |
| întâmpla      |           1 |
| ciudat        |           1 |
| ultim         |           1 |
| oră           |           1 |
| apărea        |           1 |
| distribuire   |           1 |

### 2025-04-15 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| românia          |           1 |
| lăsa             |           1 |
| mână             |           1 |
| nicusorpresedint |           1 |
| romaniaonesta    |           1 |

### 2025-04-16 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| drog       |           4 |
| prevenție  |           3 |
| trafic     |           3 |
| tânăr      |           2 |
| consum     |           2 |
| stat       |           2 |
| rețea      |           2 |
| activ      |           2 |
| program    |           2 |
| risc       |           2 |
| ultim      |           2 |
| bucurești  |           2 |
| veni       |           1 |
| veste      |           1 |
| îngrozitor |           1 |
| moarte     |           1 |
| an         |           1 |
| victimă    |           1 |
| supradoză  |           1 |
| problemă   |           1 |

### 2025-04-16 — facebook-post

| cuvânt                      |   frecvență |
|:----------------------------|------------:|
| ciolacu                     |           2 |
| român                       |           1 |
| cenzurat                    |           1 |
| ritishroadcastingorporation |           1 |
| marcel                      |           1 |
| sine                        |           1 |
| permite                     |           1 |
| ne-                         |           1 |
| satura                      |           1 |
| instituție                  |           1 |
| stat                        |           1 |
| răspunde                    |           1 |
| comenzi                     |           1 |
| politic                     |           1 |
| nicusordan                  |           1 |
| nd                          |           1 |
| romaniaonesta               |           1 |
| dreptate                    |           1 |
| libertate                   |           1 |

### 2025-04-16 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| pasaj       |           6 |
| bucurești   |           3 |
| leu         |           3 |
| vrea        |           2 |
| capitală    |           2 |
| demara      |           2 |
| procedură   |           2 |
| consolidare |           2 |
| reabilitare |           2 |
| lujerului   |           2 |
| obor        |           2 |
| pod         |           2 |
| băneasa     |           2 |
| tehnic      |           2 |
| putea       |           2 |
| investiție  |           2 |
| siguranță   |           2 |
| important   |           1 |
| reabilita   |           1 |
| primărie    |           1 |

### 2025-04-17 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| paov           |           4 |
| bucurești      |           4 |
| apă            |           3 |
| plan           |           2 |
| oraș           |           2 |
| verde          |           2 |
| urban          |           2 |
| strategic      |           2 |
| domeniu        |           2 |
| prioritar      |           2 |
| transport      |           2 |
| calitate       |           2 |
| aer            |           2 |
| infrastructură |           2 |
| digital        |           2 |
| sistem         |           2 |
| lansa          |           1 |
| oficial        |           1 |
| acțiune        |           1 |
| proiect        |           1 |

### 2025-04-17 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| primărie    |           2 |
| treabă      |           2 |
| încerca     |           2 |
| veste       |           1 |
| bun         |           1 |
| capitală    |           1 |
| atrage      |           1 |
| milion      |           1 |
| leu         |           1 |
| obligațiune |           1 |
| plăti       |           1 |
| datorie     |           1 |
| vechi       |           1 |
| lua         |           1 |
| primar      |           1 |
| videanu     |           1 |
| subscriere  |           1 |
| față        |           1 |
| sumă        |           1 |
| dori        |           1 |

### 2025-04-17 — facebook-post

| cuvânt               |   frecvență |
|:---------------------|------------:|
| președintele-împărat |           1 |
| reprezenta           |           1 |
| românia              |           1 |
| schimbare            |           1 |
| nd                   |           1 |
| prezidential         |           1 |
| romaniaonesta        |           1 |

### 2025-04-17 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| ataca               |           1 |
| cibernetic          |           1 |
| cont                |           1 |
| risca               |           1 |
| bloca               |           1 |
| comunicare          |           1 |
| susținere           |           1 |
| voastrănicusordan   |           1 |
| nd                  |           1 |
| alegeriprezidential |           1 |
| romania             |           1 |
| ataccibernetic      |           1 |

### 2025-04-18 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| muncă       |           5 |
| loc         |           3 |
| cozonac     |           2 |
| om          |           2 |
| fiscal      |           2 |
| românia     |           2 |
| vizita      |           1 |
| fabrică     |           1 |
| panificație |           1 |
| prag        |           1 |
| paște       |           1 |
| miros       |           1 |
| proaspet    |           1 |
| forfotă     |           1 |
| angajaților |           1 |
| speranță    |           1 |
| afacere     |           1 |
| succes      |           1 |
| oferi       |           1 |
| stabile     |           1 |

### 2025-04-18 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| românia          |           2 |
| realitate        |           1 |
| simplu           |           1 |
| fura             |           1 |
| frică            |           1 |
| schimbare        |           1 |
| onest            |           1 |
| putea            |           1 |
| manipula         |           1 |
| împreună         |           1 |
| puternic         |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |
| nicusordan       |           1 |

### 2025-04-18 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| președinte       |           1 |
| vrea             |           1 |
| schimbăre        |           1 |
| dori             |           1 |
| om               |           1 |
| nicusorpresedint |           1 |
| romaniaonesta    |           1 |
| nicusordan       |           1 |
| nd               |           1 |

### 2025-04-19 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| speranță |           3 |
| lumină   |           2 |
| sărbător |           2 |
| noapte   |           1 |
| învierii |           1 |
| bină     |           1 |
| puternic |           1 |
| decât    |           1 |
| rău      |           1 |
| adevăr   |           1 |
| învinge  |           1 |
| păstra   |           1 |
| dincolo  |           1 |
| hristos  |           1 |
| înviat   |           1 |
| dori     |           1 |
| liniște  |           1 |

### 2025-04-19 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| paște      |           2 |
| familie    |           2 |
| pregătim   |           1 |
| sărbător   |           1 |
| moment     |           1 |
| alături    |           1 |
| nicusordan |           1 |
| nd         |           1 |
| traditii   |           1 |
| oua        |           1 |

### 2025-04-20 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| paște        |           1 |
| aduce        |           1 |
| împreună     |           1 |
| reaminti     |           1 |
| important    |           1 |
| moment       |           1 |
| petrece      |           1 |
| alături      |           1 |
| drag         |           1 |
| sărbătoare   |           1 |
| familie      |           1 |
| loc          |           1 |
| regăsi       |           1 |
| liniște      |           1 |
| bucurie      |           1 |
| echilibru    |           1 |
| pastefericit |           1 |

### 2025-04-20 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| paște      |           2 |
| sărbători  |           1 |
| lumina     |           1 |
| nicusordan |           1 |
| nd         |           1 |
| romania    |           1 |
| comunitate |           1 |

### 2025-04-21 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| profund      |           1 |
| tristețe     |           1 |
| afla         |           1 |
| veste        |           1 |
| trecere      |           1 |
| veșnic       |           1 |
| sanctității  |           1 |
| papă         |           1 |
| francisc     |           1 |
| lider        |           1 |
| spiritual    |           1 |
| remarcabil   |           1 |
| simbol       |           1 |
| compasiunie  |           1 |
| model        |           1 |
| bunătate     |           1 |
| modestie     |           1 |
| înțelepciune |           1 |
| crea         |           1 |
| punt         |           1 |

### 2025-04-22 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| vrea              |           2 |
| dragi             |           1 |
| român             |           1 |
| diasporă          |           1 |
| țară              |           1 |
| întoarce          |           1 |
| vedea             |           1 |
| vot               |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-22 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| nedreptate        |           1 |
| românia           |           1 |
| vreau             |           1 |
| românie           |           1 |
| om                |           1 |
| cinstit           |           1 |
| pierde            |           1 |
| vedea             |           1 |
| vot               |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-22 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| preț             |           1 |
| apărea           |           1 |
| senin            |           1 |
| exista           |           1 |
| legătură         |           1 |
| clar             |           1 |
| plăti            |           1 |
| factură          |           1 |
| cumpărăt         |           1 |
| decizie          |           1 |
| trimite          |           1 |
| reprezenta       |           1 |
| alegere          |           1 |
| politicienilor   |           1 |
| conta            |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |
| nicusordan       |           1 |
| nd               |           1 |

### 2025-04-22 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| vot               |           1 |
| conta             |           1 |
| enerva            |           1 |
| nicusorpresedinte |           1 |
| nd                |           1 |

### 2025-04-23 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| crin      |           1 |
| antonescu |           1 |
| mafie     |           1 |
| imobiliar |           1 |

### 2025-04-23 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| dragi             |           1 |
| moldovan          |           1 |
| alege             |           1 |
| românie           |           1 |
| onest             |           1 |
| puternic          |           1 |
| susține           |           1 |
| moldova           |           1 |
| european          |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-23 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| profesor    |           1 |
| plătit      |           1 |
| investiție  |           1 |
| instituție  |           1 |
| învățământ  |           1 |
| soluție     |           1 |
| abandon     |           1 |
| școlar      |           1 |
| educație    |           1 |
| rămâne      |           1 |
| promisiune  |           1 |
| hârtie      |           1 |
| trebui      |           1 |
| voinț       |           1 |
| real        |           1 |
| ban         |           1 |
| direcționat |           1 |
| corect      |           1 |
| nicusordan  |           1 |
| nd          |           1 |

### 2025-04-23 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| sănătate    |           2 |
| românia     |           2 |
| onestă      |           2 |
| întru       |           2 |
| acces       |           2 |
| vrea        |           2 |
| stat        |           2 |
| fundamental |           1 |
| construi    |           1 |
| împreună    |           1 |
| om          |           1 |
| locui       |           1 |
| sat         |           1 |
| oraș        |           1 |
| trebui      |           1 |
| real        |           1 |
| serviciu    |           1 |
| medical     |           1 |
| sigur       |           1 |
| rapid       |           1 |

### 2025-04-24 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| românia                         |           4 |
| libertate                       |           4 |
| angajament                      |           3 |
| european                        |           3 |
| societate                       |           3 |
| exprimare                       |           3 |
| sine                            |           3 |
| universitate                    |           2 |
| apartenență                     |           2 |
| uniune                          |           2 |
| northatlantictreatyorganization |           2 |
| precum                          |           2 |
| valoare                         |           2 |
| stat                            |           2 |
| educație                        |           2 |
| știință                         |           2 |
| instituție                      |           2 |
| parteneriat                     |           2 |
| strategic                       |           2 |
| stateleunitealeamericii         |           2 |

### 2025-04-24 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| rămâne                  |           2 |
| crin                    |           1 |
| antonescu               |           1 |
| reprezenta              |           1 |
| garanție                |           1 |
| marcel                  |           1 |
| ciolacu                 |           1 |
| premier                 |           1 |
| partidulnaționalliberal |           1 |
| subordonat              |           1 |
| psd                     |           1 |

### 2025-04-24 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| educație     |           3 |
| românia      |           2 |
| viitor       |           2 |
| temelie      |           1 |
| român        |           1 |
| puternic     |           1 |
| copil        |           1 |
| merita       |           1 |
| șansă        |           1 |
| real         |           1 |
| școală       |           1 |
| sigur        |           1 |
| profesor     |           1 |
| motivat      |           1 |
| sistem       |           1 |
| diferență    |           1 |
| sat          |           1 |
| oraș         |           1 |
| elev         |           1 |
| posibilitate |           1 |

### 2025-04-24 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| sistem       |           2 |
| sănătate     |           2 |
| lipsă        |           2 |
| loc          |           1 |
| cheltuim     |           1 |
| lucru        |           1 |
| bucurești    |           1 |
| alege        |           1 |
| investi      |           1 |
| conta        |           1 |
| adevărat     |           1 |
| medical      |           1 |
| suferi       |           1 |
| medic        |           1 |
| direcție     |           1 |
| clar         |           1 |
| incapacitate |           1 |
| gestiona     |           1 |
| ban          |           1 |
| public       |           1 |

### 2025-04-24 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| trebui            |           2 |
| justiția          |           1 |
| reformă           |           1 |
| real              |           1 |
| corupție          |           1 |
| sistemic          |           1 |
| ține              |           1 |
| loc               |           1 |
| dezvoltare        |           1 |
| nivel             |           1 |
| trai              |           1 |
| influență         |           1 |
| politic           |           1 |
| îndepărtat        |           1 |
| integritate       |           1 |
| regulă            |           1 |
| nicusorpresedinte |           1 |
| nd                |           1 |
| romaniaonesta     |           1 |

### 2025-04-24 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| societate  |           1 |
| justiție   |           1 |
| liber      |           1 |
| curajoasă  |           1 |
| accesibil  |           1 |
| român      |           1 |
| trebui     |           1 |
| putea      |           1 |
| încredere  |           1 |
| lege       |           1 |
| același    |           1 |
| stat       |           1 |
| apăra      |           1 |
| nedreptăți |           1 |

### 2025-04-25 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |          11 |
| etapă        |           4 |
| plan         |           4 |
| urbanistic   |           4 |
| urbanism     |           3 |
| proces       |           3 |
| elaborare    |           3 |
| general      |           3 |
| pug          |           3 |
| studiu       |           3 |
| avizare      |           3 |
| important    |           2 |
| întru        |           2 |
| finaliza     |           2 |
| fundamentare |           2 |
| primărie     |           2 |
| capitală     |           2 |
| public       |           2 |
| bază         |           2 |
| accesa       |           2 |

### 2025-04-25 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| haideți           |           1 |
| alături           |           1 |
| dreptate          |           1 |
| românia           |           1 |
| nd                |           1 |
| nicusorpresedinte |           1 |

### 2025-04-25 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| bebe        |           2 |
| familie     |           2 |
| proiect     |           2 |
| bucurești   |           1 |
| găsi        |           1 |
| haină       |           1 |
| jucărie     |           1 |
| dona        |           1 |
| drag        |           1 |
| copil       |           1 |
| sprijini    |           1 |
| bucureștean |           1 |
| putea       |           1 |
| deveni      |           1 |
| model       |           1 |
| întreg      |           1 |
| țară        |           1 |
| promova     |           1 |
| economie    |           1 |
| circular    |           1 |

### 2025-04-25 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| reconstruim       |           1 |
| demnitate         |           1 |
| colectiv          |           1 |
| printru           |           1 |
| economie          |           1 |
| puternic          |           1 |
| slujbă            |           1 |
| interes           |           1 |
| național          |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-25 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| atacat           |           1 |
| candidat         |           1 |
| frică            |           1 |
| schimbare        |           1 |
| adică            |           1 |
| vot              |           1 |
| nicusordan       |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |
| nd               |           1 |

### 2025-04-26 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| rămâne        |           1 |
| exemplu       |           1 |
| implicare     |           1 |
| civic         |           1 |
| susținere     |           1 |
| dumneavoastră |           1 |
| onora         |           1 |
| mulțumi       |           1 |
| domn          |           1 |
| victor        |           1 |
| rebengiuc     |           1 |

### 2025-04-26 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| întreba           |           1 |
| tânăr             |           1 |
| putea             |           1 |
| campanie          |           1 |
| românia           |           1 |
| onestă            |           1 |
| simplu            |           1 |
| ultim             |           1 |
| weekend           |           1 |
| alegere           |           1 |
| suna              |           1 |
| prietenă          |           1 |
| rudă              |           1 |
| cunoscut          |           1 |
| ieși              |           1 |
| vot               |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-26 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| aspa      |           4 |
| bun       |           3 |
| târg      |           3 |
| adopta    |           2 |
| viață     |           2 |
| veni      |           2 |
| veste     |           1 |
| cățeie    |           1 |
| participa |           1 |
| organiza  |           1 |
| primi     |           1 |
| șansă     |           1 |
| mulțumi   |           1 |
| parklake  |           1 |
| alege     |           1 |
| pleca     |           1 |
| acasă     |           1 |
| prieten   |           1 |
| patruped  |           1 |
| oferi     |           1 |

### 2025-04-26 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| românia           |           1 |
| fapt              |           1 |
| concret           |           1 |
| om                |           1 |
| intenționat       |           1 |
| vorbă             |           1 |
| gol               |           1 |
| politician        |           1 |
| interes           |           1 |
| ascuns            |           1 |
| nicusorpresedinte |           1 |
| nd                |           1 |
| faptenuvorbă      |           1 |

### 2025-04-26 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| românia           |           1 |
| onestă            |           1 |
| singur            |           1 |
| variantă          |           1 |
| schimbare         |           1 |
| dreptate          |           1 |
| vedea             |           1 |
| vot               |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-27 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| om                |           2 |
| loc               |           1 |
| românia           |           1 |
| acces             |           1 |
| medic             |           1 |
| primar            |           1 |
| capitală          |           1 |
| pune              |           1 |
| sănătate          |           1 |
| plan              |           1 |
| președinte        |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-27 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| tinerilor         |           1 |
| bucureștean       |           1 |
| susținere         |           1 |
| vedea             |           1 |
| vot               |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-27 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| aminti        |           1 |
| crin          |           1 |
| antonescu     |           1 |
| candidat      |           1 |
| marcel        |           1 |
| ciolacu       |           1 |
| absent        |           1 |
| parlament     |           1 |
| prieten       |           1 |
| psd           |           1 |
| parte         |           1 |
| mafie         |           1 |
| imobiliar     |           1 |
| an            |           1 |
| om            |           1 |
| aduce         |           1 |
| politică      |           1 |
| klaus         |           1 |
| iohannis      |           1 |
| romaniaonesta |           1 |

### 2025-04-27 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| sine              |           2 |
| viitor            |           2 |
| întreba           |           1 |
| mamă              |           1 |
| sat               |           1 |
| oraș              |           1 |
| mic               |           1 |
| copil             |           1 |
| întru             |           1 |
| românie           |           1 |
| fură              |           1 |
| tinerii           |           1 |
| trăi              |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-04-28 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| dezbatere  |           2 |
| valoare    |           2 |
| președinte |           2 |
| sistem     |           2 |
| sine       |           1 |
| încheia    |           1 |
| percepe    |           1 |
| aștept     |           1 |
| drag       |           1 |
| părere     |           1 |
| impresiil  |           1 |
| comentariu |           1 |
| intra      |           1 |
| palat      |           1 |
| cotroceni  |           1 |
| singur     |           1 |
| gând       |           1 |
| viață      |           1 |
| răspuns    |           1 |
| gest       |           1 |

### 2025-04-28 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| echipă      |           2 |
| începe      |           1 |
| confruntare |           1 |
| candidat    |           1 |
| susținător  |           1 |
| ajunge      |           1 |
| palat       |           1 |
| cotroceni   |           1 |
| gata        |           1 |
| acțiune     |           1 |
| succes      |           1 |
| nicușor     |           1 |
| nd          |           1 |

### 2025-04-28 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           2 |
| mirabela   |           1 |
| președinte |           1 |
| sta        |           1 |
| putere     |           1 |
| românia    |           1 |
| țară       |           1 |
| bun        |           1 |

### 2025-04-28 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| președinte        |           1 |
| asculta           |           1 |
| om                |           1 |
| găsi              |           1 |
| soluție           |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-04-28 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| dezbatere      |           2 |
| participa      |           1 |
| candidat       |           1 |
| alegere        |           1 |
| prezidențial   |           1 |
| organiza       |           1 |
| digi           |           1 |
| tvr            |           1 |
| antena         |           1 |
| cetățen        |           1 |
| român          |           1 |
| ști            |           1 |
| viziune        |           1 |
| țară           |           1 |
| urmări         |           1 |
| confruntare    |           1 |
| idee           |           1 |
| celălalt       |           1 |
| contracandidat |           1 |
| putea          |           1 |

### 2025-04-29 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| adevăr            |           1 |
| vrea              |           1 |
| învinge           |           1 |
| putea             |           1 |
| reuși             |           1 |
| nicusorpresedinte |           1 |
| romaniaonesta     |           1 |

### 2025-04-29 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| apăra       |           2 |
| sine        |           2 |
| veteranilor |           1 |
| război      |           1 |
| cinsti      |           1 |
| curaj       |           1 |
| românia     |           1 |
| preț        |           1 |
| viață       |           1 |
| datorie     |           1 |
| rămâne      |           1 |
| respect     |           1 |
| cuvânt      |           1 |
| investi     |           1 |
| serios      |           1 |
| țară        |           1 |
| onora       |           1 |
| veteran     |           1 |
| investește  |           1 |
| forță       |           1 |

### 2025-04-29 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| teren       |           4 |
| domn        |           2 |
| antonescu   |           2 |
| document    |           2 |
| arăta       |           2 |
| transfer    |           2 |
| btt         |           2 |
| caz         |           2 |
| certificat  |           2 |
| atestare    |           2 |
| proprietate |           2 |
| instanță    |           2 |
| crin        |           1 |
| cere        |           1 |
| dezbatere   |           1 |
| lună        |           1 |
| public      |           1 |
| invi        |           1 |
| judeca      |           1 |
| singur      |           1 |

### 2025-04-29 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| nd                  |           2 |
| sprijin             |           1 |
| dovedi              |           1 |
| bucurești           |           1 |
| reușim              |           1 |
| românia             |           1 |
| romaniaonesta       |           1 |
| nicusordan          |           1 |
| nicusordanpresedint |           1 |

### 2025-04-29 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| sistem           |           1 |
| nume             |           1 |
| an               |           1 |
| lupt             |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |

### 2025-04-29 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| succes   |           1 |
| nicușor  |           1 |
| echipă   |           1 |
| nd       |           1 |

### 2025-04-30 — facebook-post

| cuvânt                                                     |   frecvență |
|:-----------------------------------------------------------|------------:|
| act                                                        |           1 |
| confirma                                                   |           1 |
| spune                                                      |           1 |
| mulțumi                                                    |           1 |
| uita                                                       |           1 |
| dezbatere                                                  |           1 |
| httpsdrivegooglecomdrivefoldersocpalfpmsz-hwhcwdhycrhzijth |           1 |

### 2025-04-30 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| mirabela      |           1 |
| drag          |           1 |
| romaniaonesta |           1 |

### 2025-04-30 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| diaspora      |           1 |
| parte         |           1 |
| viitor        |           1 |
| românia       |           1 |
| romaniaonesta |           1 |

### 2025-05-01 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| disperare |           1 |
| atinge    |           1 |
| cotă      |           1 |
| maxim     |           1 |
| marcel    |           1 |
| ciolacu   |           1 |
| ajunge    |           1 |
| trimite   |           1 |
| mesaj     |           1 |
| direct    |           1 |
| număr     |           1 |
| personal  |           1 |
| cetățean  |           1 |
| cerându   |           1 |
| vota      |           1 |
| crin      |           1 |
| antonescu |           1 |
| singur    |           1 |
| șansă     |           1 |
| sine      |           1 |

### 2025-05-01 — facebook-post

| cuvânt                      |   frecvență |
|:----------------------------|------------:|
| sine                        |           3 |
| spital                      |           3 |
| bolnav                      |           2 |
| sistem                      |           2 |
| construi                    |           2 |
| singur                      |           2 |
| oară                        |           2 |
| privat                      |           2 |
| abuza                       |           2 |
| construire                  |           2 |
| locație                     |           2 |
| ritishroadcastingorporation |           1 |
| incalificabil               |           1 |
| folosi                      |           1 |
| român                       |           1 |
| cancer                      |           1 |
| temă                        |           1 |
| electoral                   |           1 |
| alegere                     |           1 |
| prezidențial                |           1 |

### 2025-05-01 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| minut               |           1 |
| liv                 |           1 |
| lucian              |           1 |
| mîndruță            |           1 |
| material            |           1 |
| publicitar          |           1 |
| politic             |           1 |
| candidat            |           1 |
| nicușor-daniel      |           1 |
| dan                 |           1 |
| email               |           1 |
| contactnicusordanro |           1 |
| adresă              |           1 |
| str                 |           1 |
| bd                  |           1 |
| regina              |           1 |
| elisabeta           |           1 |
| sector              |           1 |
| bucurești           |           1 |
| cmf                 |           1 |

### 2025-05-01 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| vedea         |           1 |
| vot           |           1 |
| pleca         |           1 |
| vacanță       |           1 |
| uita          |           1 |
| buletinu      |           1 |
| acasă         |           1 |
| nd            |           1 |
| romaniaonesta |           1 |

### 2025-05-01 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| poze           |           1 |
| posta          |           1 |
| elena          |           1 |
| lasconi        |           1 |
| fals           |           1 |
| grosolan       |           1 |
| pretins        |           1 |
| întâlnire      |           1 |
| loc            |           1 |
| niciodată      |           1 |
| conferință     |           1 |
| presă          |           1 |
| live           |           1 |
| oră            |           1 |
| material       |           1 |
| publicitar     |           1 |
| politic        |           1 |
| candidat       |           1 |
| nicușor-daniel |           1 |
| dan            |           1 |

### 2025-05-01 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| aminti              |           1 |
| victor              |           1 |
| ponta               |           1 |
| alegeriprezidențial |           1 |

### 2025-05-01 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| candidat      |           1 |
| pro-european  |           1 |
| putea         |           1 |
| învinge       |           1 |
| simion        |           1 |
| romaniaonesta |           1 |
| nd            |           1 |

### 2025-05-02 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| pleca             |           1 |
| localitate        |           1 |
| minivacanță       |           1 |
| putea             |           1 |
| vota              |           1 |
| țară              |           1 |
| romaniaonesta     |           1 |
| nicusorpresedinte |           1 |

### 2025-05-02 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| voce      |           2 |
| viitor    |           2 |
| celebrăm  |           1 |
| energie   |           1 |
| curaj     |           1 |
| vis       |           1 |
| generație |           1 |
| putea     |           1 |
| schimba   |           1 |
| lume      |           1 |
| tinerii   |           1 |
| începe    |           1 |
| alegere   |           1 |
| ieși      |           1 |
| vot       |           1 |
| parte     |           1 |
| schimbare |           1 |
| fă        |           1 |
| auzit     |           1 |
| alege     |           1 |

### 2025-05-02 — facebook-post

| cuvânt             |   frecvență |
|:-------------------|------------:|
| pleca              |           1 |
| românia            |           1 |
| putea              |           1 |
| vota               |           1 |
| țară               |           1 |
| afla               |           1 |
| listă              |           1 |
| secție             |           1 |
| votare             |           1 |
| străinătate        |           1 |
| httpsvotdiasporaro |           1 |
| romaniaonesta      |           1 |
| nicusorpresedinte  |           1 |

### 2025-05-02 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| ciolacu             |           2 |
| dezinformare        |           1 |
| marcă               |           1 |
| coaliție            |           1 |
| spune               |           1 |
| putea               |           1 |
| bate                |           1 |
| simion              |           1 |
| tur                 |           1 |
| fals                |           1 |
| nicusordan          |           1 |
| nd                  |           1 |
| alegeriprezidential |           1 |
| vot                 |           1 |

### 2025-05-02 — facebook-post

| cuvânt             |   frecvență |
|:-------------------|------------:|
| diaspora           |           1 |
| vota               |           1 |
| listă              |           1 |
| secție             |           1 |
| votare             |           1 |
| străinătate        |           1 |
| httpsvotdiasporaro |           1 |
| romaniaonesta      |           1 |
| nicusorpresedinte  |           1 |

### 2025-05-02 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| ieșim             |           1 |
| vot               |           1 |
| românia           |           1 |
| om                |           1 |
| pune              |           1 |
| interes           |           1 |
| țară              |           1 |
| loc               |           1 |
| nicusordan        |           1 |
| nicusorpresedinte |           1 |
| româniaonestă     |           1 |

### 2025-05-02 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| suflet        |           1 |
| voluntarilor  |           1 |
| susținător    |           1 |
| alături       |           1 |
| campanie      |           1 |
| duminică      |           1 |
| decidem       |           1 |
| împreună      |           1 |
| viitor        |           1 |
| dori          |           1 |
| decât         |           1 |
| instrument    |           1 |
| romaniaonesta |           1 |
| nd            |           1 |

### 2025-05-02 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| mulțumim       |           1 |
| bec            |           1 |
| consecvență    |           1 |
| fotografiile   |           1 |
| fals           |           1 |
| vrea           |           1 |
| circula        |           1 |
| liber          |           1 |
| continuare     |           1 |
| celălalt       |           1 |
| fak            |           1 |
| news           |           1 |
| -uri           |           1 |
| material       |           1 |
| publicitar     |           1 |
| politic        |           1 |
| candidat       |           1 |
| nicușor-daniel |           1 |
| dan            |           1 |
| email          |           1 |

### 2025-05-02 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| vot               |           2 |
| român             |           1 |
| diasporă          |           1 |
| merge             |           1 |
| conta             |           1 |
| românie           |           1 |
| bun               |           1 |
| româniaonestă     |           1 |
| nicusorpresedinte |           1 |

### 2025-05-02 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| votați        |           1 |
| inimă         |           1 |
| împăcat       |           1 |
| nicușor       |           1 |
| președinte    |           1 |
| romaniaonesta |           1 |

### 2025-05-03 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vot        |           2 |
| tinerii    |           1 |
| vrea       |           1 |
| rol        |           1 |
| decisiv    |           1 |
| nicusordan |           1 |
| romania    |           1 |
| cafea      |           1 |
| weekend    |           1 |
| fyp        |           1 |

### 2025-05-03 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| cravată             |           1 |
| ieșim               |           1 |
| vot                 |           1 |
| alegeriprezidențial |           1 |

### 2025-05-03 — facebook-post

| cuvânt             |   frecvență |
|:-------------------|------------:|
| pleca              |           1 |
| acasă              |           1 |
| putea              |           1 |
| vota               |           1 |
| secție             |           1 |
| votr               |           1 |
| românia            |           1 |
| diasporă           |           1 |
| buletin            |           1 |
| pașaport           |           1 |
| httpsvotdiasporaro |           1 |
| hailavot           |           1 |

### 2025-05-03 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| pleca               |           1 |
| vacanță             |           1 |
| ruga                |           1 |
| vota                |           1 |
| dimineața           |           1 |
| după-amiaza         |           1 |
| atât                |           1 |
| drum                |           1 |
| secție              |           1 |
| votare              |           1 |
| vrea                |           1 |
| aglomera            |           1 |
| alegeriprezidențial |           1 |

### 2025-05-03 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| diasporă            |           2 |
| oră                 |           2 |
| vota                |           1 |
| ține                |           1 |
| cont                |           1 |
| secție              |           1 |
| sine                |           1 |
| închide             |           1 |
| românia             |           1 |
| vot                 |           1 |
| conta               |           1 |
| alegeriprezidențial |           1 |

### 2025-05-03 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| minut               |           1 |
| putea               |           1 |
| decide              |           1 |
| arăta               |           1 |
| următor             |           1 |
| an                  |           1 |
| românia             |           1 |
| vot                 |           1 |
| conta               |           1 |
| alegeriprezidențial |           1 |
| cumvotez            |           1 |

### 2025-05-03 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| presă         |           2 |
| libertății    |           2 |
| presei        |           2 |
| românia       |           1 |
| onest         |           1 |
| internațional |           1 |
| mulțumi       |           1 |
| jurnalișt     |           1 |
| sine          |           1 |
| onora         |           1 |
| meserie       |           1 |
| servi         |           1 |
| interes       |           1 |
| public        |           1 |
| demasca       |           1 |
| corupție      |           1 |
| minciună      |           1 |
| hoție         |           1 |
| impostură     |           1 |
| asigur        |           1 |

### 2025-05-03 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| viitor              |           1 |
| alegere             |           1 |
| lăsa                |           1 |
| decide              |           1 |
| hai                 |           1 |
| vot                 |           1 |
| nicusordan          |           1 |
| alegeriprezidential |           1 |
| tânăr               |           1 |
| parc                |           1 |
| cismigiu            |           1 |

### 2025-05-04 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| rămâne              |           1 |
| oră                 |           1 |
| alegere             |           1 |
| hailavot            |           1 |
| alegeriprezidential |           1 |
| romania             |           1 |

### 2025-05-04 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| intra         |           1 |
| tur           |           1 |
| foto          |           1 |
| credit        |           1 |
| mihai         |           1 |
| bălănescu     |           1 |
| prezidential  |           1 |
| turul         |           1 |
| romaniaonesta |           1 |

### 2025-05-04 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| vot                 |           2 |
| decidem             |           1 |
| soartă              |           1 |
| românia             |           1 |
| hai                 |           1 |
| alegeriprezidential |           1 |
| romania             |           1 |

### 2025-05-04 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| secție              |           2 |
| oră                 |           1 |
| afla                |           1 |
| votare              |           1 |
| rând                |           1 |
| afara               |           1 |
| pleca               |           1 |
| putea               |           1 |
| vota                |           1 |
| legal               |           1 |
| alegeriprezidential |           1 |

### 2025-05-04 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| energie  |           1 |
| echipă   |           1 |
| hailavot |           1 |

### 2025-05-04 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| mirabela            |           1 |
| vota                |           1 |
| alegeriprezidential |           1 |
| romania             |           1 |
| vot                 |           1 |
| fyp                 |           1 |

### 2025-05-04 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| hai                 |           2 |
| vot                 |           2 |
| arăta               |           1 |
| puternic            |           1 |
| decât               |           1 |
| instrument          |           1 |
| alegeriprezidential |           1 |
| romania             |           1 |
| fyp                 |           1 |

### 2025-05-04 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| drum                |           2 |
| oră                 |           1 |
| închidere           |           1 |
| urn                 |           1 |
| munte               |           1 |
| sine                |           1 |
| aglomera            |           1 |
| evita               |           1 |
| aglomerație         |           1 |
| sect                |           1 |
| vota                |           1 |
| hai                 |           1 |
| vot                 |           1 |
| alegeriprezidențial |           1 |
| romanie             |           1 |

### 2025-05-04 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| secție              |           3 |
| votare              |           2 |
| oră                 |           1 |
| închidere           |           1 |
| drum                |           1 |
| opri                |           1 |
| apropiat            |           1 |
| traseu              |           1 |
| evita               |           1 |
| aglomerație         |           1 |
| risc                |           1 |
| găsi                |           1 |
| închis              |           1 |
| ajunge              |           1 |
| acasă               |           1 |
| alegeriprezidential |           1 |

### 2025-05-04 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| oră                 |           2 |
| profitați           |           1 |
| merge               |           1 |
| vot                 |           1 |
| lăsa                |           1 |
| alege               |           1 |
| alegeriprezidențial |           1 |
| romanie             |           1 |

### 2025-05-04 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| mulțumi     |           2 |
| tare        |           1 |
| sprijin     |           1 |
| vota        |           1 |
| donator     |           1 |
| voluntar    |           1 |
| observatoră |           1 |
| independent |           1 |
| delegat     |           1 |
| secție      |           1 |
| sine        |           1 |
| asigura     |           1 |
| numărare    |           1 |
| raportare   |           1 |
| precis      |           1 |
| rezultat    |           1 |

### 2025-05-04 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vota       |           4 |
| românia    |           3 |
| putea      |           2 |
| prezență   |           1 |
| urne       |           1 |
| strica     |           1 |
| plan       |           1 |
| alegere    |           1 |
| diferență  |           1 |
| încă       |           1 |
| oră        |           1 |
| om         |           1 |
| tăcut      |           1 |
| cinstit    |           1 |
| muncitor   |           1 |
| reprezenta |           1 |
| început    |           1 |
| realism    |           1 |
| trăi       |           1 |
| moment     |           1 |

### 2025-05-05 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| politic      |           2 |
| vot          |           1 |
| român        |           1 |
| sine         |           1 |
| încheia      |           1 |
| epocă        |           1 |
| fac          |           1 |
| apel         |           1 |
| politicienii |           1 |
| partid       |           1 |
| săptămână    |           1 |
| elibera      |           1 |
| spațiu       |           1 |
| mediatic     |           1 |
| dezbatere    |           1 |
| societal     |           1 |
| om           |           1 |
| loc          |           1 |
| optimist     |           1 |
| societate    |           1 |

### 2025-05-05 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| putea       |           4 |
| românia     |           3 |
| viitor      |           2 |
| fapt        |           2 |
| sine        |           2 |
| sta         |           2 |
| românie     |           2 |
| vorbă       |           2 |
| împreună    |           2 |
| șansă       |           1 |
| mulțumi     |           1 |
| vota        |           1 |
| speranță    |           1 |
| încredere   |           1 |
| intra       |           1 |
| tur         |           1 |
| arăta       |           1 |
| decent      |           1 |
| muncitoare  |           1 |
| responsabil |           1 |

### 2025-05-06 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| român     |           3 |
| țară      |           3 |
| prut      |           2 |
| inimă     |           2 |
| republică |           2 |
| moldova   |           2 |
| simți     |           2 |
| sine      |           2 |
| pod       |           1 |
| flori     |           1 |
| uni       |           1 |
| despărți  |           1 |
| moment    |           1 |
| simbolic  |           1 |
| arăta     |           1 |
| graniță   |           1 |
| dispărea  |           1 |
| românia   |           1 |
| deveni    |           1 |
| puternic  |           1 |

### 2025-05-06 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| femeie         |           3 |
| viață          |           3 |
| sine           |           2 |
| centru         |           2 |
| curaj          |           1 |
| putere         |           1 |
| alege          |           1 |
| pleca          |           1 |
| relație        |           1 |
| toxic          |           1 |
| reconstruiască |           1 |
| extraordinar   |           1 |
| întru          |           1 |
| dedica         |           1 |
| victimă        |           1 |
| violență       |           1 |
| domestic       |           1 |
| loc            |           1 |
| durere         |           1 |
| transforma     |           1 |

### 2025-05-07 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| putea       |           3 |
| trebui      |           3 |
| românia     |           2 |
| stat        |           2 |
| fiscal      |           2 |
| ban         |           2 |
| vorbi       |           1 |
| cadru       |           1 |
| eveniment   |           1 |
| organiza    |           1 |
| romanian    |           1 |
| business    |           1 |
| leaders     |           1 |
| viziune     |           1 |
| dezvoltare  |           1 |
| cred        |           1 |
| progresa    |           1 |
| respecta    |           1 |
| protejăm    |           1 |
| proprietate |           1 |

### 2025-05-07 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| aventură       |           2 |
| deosebi        |           1 |
| contracandidat |           1 |
| vrea           |           1 |
| duce           |           1 |
| țară           |           1 |
| permite        |           1 |
| viață          |           1 |
| cetățean       |           1 |
| putea          |           1 |
| depinde        |           1 |
| experiment     |           1 |
| izolaționist   |           1 |
| romaniaonesta  |           1 |

### 2025-05-07 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| dezbatere |           1 |
| tur       |           1 |
| merge     |           1 |
| seară     |           1 |
| euronews  |           1 |
| aștepta   |           1 |
| george    |           1 |
| simion    |           1 |
| lună      |           1 |
| marți     |           1 |
| miercuri  |           1 |
| joi       |           1 |
| vineri    |           1 |
| săptămână |           1 |
| viitor    |           1 |
| vrea      |           1 |
| curs      |           1 |
| invitațai |           1 |
| primit    |           1 |

### 2025-05-08 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| clasă    |           1 |
| politic  |           1 |
| ignora   |           1 |
| trăda    |           1 |
| cetățean |           1 |
| răspuns  |           1 |
| putea    |           1 |
| ură      |           1 |
| justiție |           1 |

### 2025-05-08 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| fapte               |           1 |
| vorbă               |           1 |
| alege               |           1 |
| întelept            |           1 |
| alegeriprezidențial |           1 |

### 2025-05-08 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| sine      |           2 |
| opinie    |           2 |
| susține   |           2 |
| ipocrizie |           1 |
| george    |           1 |
| simion    |           1 |
| clar      |           1 |
| asuma     |           1 |
| călin     |           1 |
| georgescu |           1 |
| giorgia   |           1 |
| meloni    |           1 |
| dezica    |           1 |
| vrea      |           1 |
| putea     |           1 |
| om        |           1 |
| interes   |           1 |
| românia   |           1 |
| capăt     |           1 |
| curaj     |           1 |

### 2025-05-08 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| dezbatere      |           1 |
| contracandidat |           1 |
| susținere      |           1 |
| energie        |           1 |
| încredere      |           1 |

### 2025-05-08 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| salut      |           1 |
| alegere    |           1 |
| papă       |           1 |
| leon       |           1 |
| xiv        |           1 |
| -lea       |           1 |
| alături    |           1 |
| comunitate |           1 |
| catolic    |           1 |
| românia    |           1 |
| bucurie    |           1 |
| început    |           1 |
| lume       |           1 |
| mesager    |           1 |
| pace       |           1 |
| echilibru  |           1 |
| călăuză    |           1 |
| moral      |           1 |
| baza       |           1 |
| valoare    |           1 |

### 2025-05-09 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| alegere             |           2 |
| legătură            |           1 |
| fact                |           1 |
| plăti               |           1 |
| creștere            |           1 |
| curs                |           1 |
| schimb              |           1 |
| iată                |           1 |
| alegeriprezidențial |           1 |

### 2025-05-09 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| potențial           |           1 |
| uriaș               |           1 |
| romaniaonesta       |           1 |
| nicusorpresedint    |           1 |
| nicusordan          |           1 |
| alegeriprezidențial |           1 |

### 2025-05-09 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| european         |           8 |
| europa           |           4 |
| românia          |           4 |
| an               |           2 |
| proiect          |           2 |
| valoare          |           2 |
| uniune           |           2 |
| întru            |           2 |
| sine             |           2 |
| primi            |           2 |
| român            |           2 |
| uniuneaeuropeană |           2 |
| direcție         |           2 |
| celebrăm         |           1 |
| politic          |           1 |
| comunitate       |           1 |
| democrație       |           1 |
| libertate        |           1 |
| sta              |           1 |
| solidaritate     |           1 |

### 2025-05-09 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| an       |           1 |
| europa   |           1 |
| foto     |           1 |
| inquam   |           1 |
| photos   |           1 |
| octav    |           1 |
| ganea    |           1 |

### 2025-05-09 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| om                  |           1 |
| sine                |           1 |
| uita                |           1 |
| fapt                |           1 |
| alegeriprezidențial |           1 |

### 2025-05-09 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| pace          |           1 |
| sine          |           1 |
| obține        |           1 |
| descurajare   |           1 |
| război        |           1 |
| romaniaonesta |           1 |

### 2025-05-09 — facebook-post

| cuvânt               |   frecvență |
|:---------------------|------------:|
| ucraina              |           1 |
| trebui               |           1 |
| parte                |           1 |
| pace                 |           1 |
| justă                |           1 |
| securitatenațional   |           1 |
| securitatecibernetic |           1 |

### 2025-05-10 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| românia      |           3 |
| independență |           3 |
| independența |           2 |
| proclamație  |           2 |
| față         |           2 |
| apăra        |           2 |
| construi     |           2 |
| românie      |           2 |
| puternic     |           2 |
| unit         |           2 |
| celebrăm     |           1 |
| stat         |           1 |
| moment       |           1 |
| definitoriu  |           1 |
| istorie      |           1 |
| național     |           1 |
| parlament    |           1 |
| vota         |           1 |
| unanimitate  |           1 |
| imperiu      |           1 |

### 2025-05-10 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| sine                    |           1 |
| bucura                  |           1 |
| simion                  |           1 |
| pierdere                |           1 |
| român                   |           1 |
| călătorie               |           1 |
| viză                    |           1 |
| stateleunitealeamericii |           1 |

### 2025-05-10 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| român      |           2 |
| george     |           1 |
| simion     |           1 |
| sine       |           1 |
| dezvălui   |           1 |
| adevărat   |           1 |
| față       |           1 |
| suveranist |           1 |
| fațadă     |           1 |
| slugarnic  |           1 |
| înșala     |           1 |
| lume       |           1 |
| putere     |           1 |
| bucuri     |           1 |
| mulțumi    |           1 |
| cetățean   |           1 |
| rămâne     |           1 |
| program    |           1 |
| scuti      |           1 |
| viză       |           1 |

### 2025-05-10 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| țară         |           2 |
| dori         |           2 |
| instituție   |           2 |
| valoare      |           2 |
| vrea         |           2 |
| sine         |           1 |
| sigur        |           1 |
| lege         |           1 |
| respecta     |           1 |
| aplica       |           1 |
| princip      |           1 |
| integrităție |           1 |
| loialităție  |           1 |
| față         |           1 |
| jurământ     |           1 |
| reafirma     |           1 |
| esențial     |           1 |
| important    |           1 |
| românia      |           1 |
| ne-          |           1 |

### 2025-05-10 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| diasporă         |           2 |
| prere            |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |

### 2025-05-10 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |           2 |
| sine        |           1 |
| permite     |           1 |
| experiment  |           1 |
| vedea       |           1 |
| pas         |           1 |
| înapoi      |           1 |
| alegere     |           1 |
| speranță    |           1 |
| perfecționa |           1 |
| sistem      |           1 |
| aduce       |           1 |
| experiență  |           1 |
| demonstra   |           1 |
| performanță |           1 |
| mediu       |           1 |
| privat      |           1 |
| haos        |           1 |
| promite     |           1 |
| minune      |           1 |

### 2025-05-11 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| simion      |           2 |
| atacurile   |           1 |
| boță        |           1 |
| continuu    |           1 |
| întâmplător |           1 |
| viza        |           1 |
| postările   |           1 |
| încerca     |           1 |
| arăta       |           1 |
| român       |           1 |
| adevărat    |           1 |
| față        |           1 |
| george      |           1 |
| încercare   |           1 |
| manipulare  |           1 |
| opinie      |           1 |
| public      |           1 |
| precedent   |           1 |
| autoritate  |           1 |
| privință    |           1 |

### 2025-05-11 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| araicu        |           1 |
| alege         |           1 |
| voce          |           1 |
| față          |           1 |
| român         |           1 |
| reuni         |           1 |
| piață         |           1 |
| victoria      |           1 |
| întru         |           1 |
| moment        |           1 |
| tăcere        |           1 |
| opțiune       |           1 |
| romaniaonesta |           1 |

### 2025-05-11 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| suflet          |           2 |
| geluduminică    |           1 |
| urca            |           1 |
| scenă           |           1 |
| romaniainlumina |           1 |
| vorbi           |           1 |
| om              |           1 |
| încredere       |           1 |
| respect         |           1 |
| bunul-simț      |           1 |
| solidaritate    |           1 |
| putea           |           1 |
| temelie         |           1 |
| românii         |           1 |
| romaniaonesta   |           1 |

### 2025-05-11 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| putea          |           2 |
| simion         |           2 |
| om             |           2 |
| sine           |           2 |
| trece          |           1 |
| vedere         |           1 |
| fapt           |           1 |
| george         |           1 |
| speranță       |           1 |
| fals           |           1 |
| uita           |           1 |
| ochi           |           1 |
| promisiune     |           1 |
| ști            |           1 |
| îndeplini      |           1 |
| românia        |           1 |
| conduce        |           1 |
| nicusordan     |           1 |
| alegeriromania |           1 |
| fyp            |           1 |

### 2025-05-11 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| vremuri     |           2 |
| uni         |           2 |
| românie     |           2 |
| putea       |           2 |
| sine        |           2 |
| românia     |           1 |
| trăim       |           1 |
| pune        |           1 |
| încercare   |           1 |
| oferi       |           1 |
| șansă       |           1 |
| reconstrui  |           1 |
| solidar     |           1 |
| rămâne      |           1 |
| optimisc    |           1 |
| proiecta    |           1 |
| speranță    |           1 |
| generațiile |           1 |
| veni        |           1 |
| onest       |           1 |

### 2025-05-11 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| școală           |           1 |
| trebui           |           1 |
| ajuta            |           1 |
| copil            |           1 |
| sine             |           1 |
| dezvolta         |           1 |
| gândire          |           1 |
| critic           |           1 |
| romaniaonesta    |           1 |
| nicusordan       |           1 |
| nicusorpresedint |           1 |

### 2025-05-11 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| aștepta        |           1 |
| piață          |           1 |
| victoria       |           1 |
| începe         |           1 |
| oră            |           1 |
| romaniacorecta |           1 |
| romaniaunită   |           1 |
| romaniaonesta  |           1 |

### 2025-05-12 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| diploma           |           1 |
| bacalaureat       |           1 |
| original          |           1 |
| varianta          |           1 |
| circula           |           1 |
| social            |           1 |
| medie             |           1 |
| fals              |           1 |
| grosolan          |           1 |
| lăsa              |           1 |
| induși            |           1 |
| eroare            |           1 |
| informație        |           1 |
| fabricat          |           1 |
| diplomabacalaurea |           1 |
| diplomanicusordan |           1 |

### 2025-05-12 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| credem           |           1 |
| românia          |           1 |
| ultim            |           1 |
| efort            |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |

### 2025-05-12 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| echilibru        |           1 |
| schimbare        |           1 |
| haos             |           1 |
| social           |           1 |
| dezastru         |           1 |
| economic         |           1 |
| depinde          |           1 |
| viitor           |           1 |
| românia          |           1 |
| hai              |           1 |
| duce             |           1 |
| mesaj            |           1 |
| votez            |           1 |
| prezidential     |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |

### 2025-05-12 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| construi      |           2 |
| românie       |           2 |
| împreună      |           1 |
| putea         |           1 |
| copil         |           1 |
| rămâne        |           1 |
| obligație     |           1 |
| oferi         |           1 |
| sine          |           1 |
| dezvolta      |           1 |
| putem         |           1 |
| dezbinare     |           1 |
| ură           |           1 |
| nicusordan    |           1 |
| româniaonestă |           1 |
| piatavictorie |           1 |
| emotii        |           1 |

### 2025-05-12 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| om          |           2 |
| întotdeauna |           1 |
| primar      |           1 |
| președinte  |           1 |
| vrea        |           1 |
| printre     |           1 |
| cred        |           1 |
| întru       |           1 |
| românie     |           1 |
| conducere   |           1 |
| însemna     |           1 |
| distanță    |           1 |
| apropiere   |           1 |
| voce        |           1 |
| conta       |           1 |
| construcție |           1 |
| românia     |           1 |
| sine        |           1 |
| împreună    |           1 |
| jur         |           1 |

### 2025-05-12 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| mic             |           1 |
| deopotrivă      |           1 |
| același         |           1 |
| gând            |           1 |
| româniaînlumină |           1 |

### 2025-05-12 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| medeleanumelania |           1 |
| explica          |           1 |
| miză             |           1 |
| moment           |           1 |
| prezidential     |           1 |
| votultaucontează |           1 |

### 2025-05-12 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| românia          |           1 |
| președinte       |           1 |
| curajos          |           1 |
| sine             |           1 |
| prezenta         |           1 |
| confruntare      |           1 |
| contracandidație |           1 |
| george           |           1 |
| simion           |           1 |
| veni             |           1 |
| echipă           |           1 |
| nd               |           1 |

### 2025-05-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           1 |
| onestă     |           1 |
| schimbare  |           1 |
| uni        |           1 |
| nicusordan |           1 |

### 2025-05-13 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| contracandidat |           1 |
| încă           |           1 |
| dator          |           1 |
| explica        |           1 |
| paraziție      |           1 |
| sistem         |           1 |
| bugetar        |           1 |
| georgesimion   |           1 |

### 2025-05-13 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| mulțumi           |           1 |
| delia             |           1 |
| grigore           |           1 |
| voce              |           1 |
| rome              |           1 |
| românia           |           1 |
| lupta             |           1 |
| acces             |           1 |
| educație          |           1 |
| societate         |           1 |
| diversitate       |           1 |
| recunoaște        |           1 |
| respectat         |           1 |
| romaniaonesta     |           1 |
| romaniapentrutoti |           1 |

### 2025-05-13 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| învăța        |           1 |
| domn          |           1 |
| victor        |           1 |
| rebengiuc     |           1 |
| mulțumi       |           1 |
| inimă         |           1 |
| alături       |           1 |
| unsingurgand  |           1 |
| romaniaonesta |           1 |

### 2025-05-13 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| niciodată           |           1 |
| suporta             |           1 |
| nedreptate          |           1 |
| an                  |           1 |
| lupt                |           1 |
| moștenire           |           1 |
| istoric             |           1 |
| patrimoniu          |           1 |
| nicusordanpresedint |           1 |

### 2025-05-13 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| românie             |           1 |
| bun                 |           1 |
| român               |           1 |
| țară                |           1 |
| diasporă            |           1 |
| republică           |           1 |
| moldova             |           1 |
| uni                 |           1 |
| reușima             |           1 |
| romaniaonesta       |           1 |
| nicusordanpresedint |           1 |

### 2025-05-13 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| oana      |           1 |
| gheorghiu |           1 |
| om        |           1 |
| strânge   |           1 |
| milion    |           1 |
| român     |           1 |
| jur       |           1 |
| cauză     |           1 |
| național  |           1 |
| spital    |           1 |
| uni       |           1 |
| reușim    |           1 |
| onora     |           1 |
| alături   |           1 |
| românia   |           1 |
| onestă    |           1 |

### 2025-05-13 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| pleca    |           1 |
| educație |           1 |
| popor    |           1 |
| puternic |           1 |
| profesor |           1 |
| pregăti  |           1 |
| plătit   |           1 |

### 2025-05-13 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| dintru        |           2 |
| vin           |           1 |
| familie       |           1 |
| simplu        |           1 |
| oraș          |           1 |
| mic           |           1 |
| românia       |           1 |
| învăța        |           1 |
| părinte       |           1 |
| munci         |           1 |
| rezultatele   |           1 |
| olimpiadă     |           1 |
| posibil       |           1 |
| profesor      |           1 |
| dedicat       |           1 |
| îndruma       |           1 |
| romaniaonesta |           1 |

### 2025-05-13 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |           2 |
| redresa       |           1 |
| economie      |           1 |
| pune          |           1 |
| ordine        |           1 |
| cheltuială    |           1 |
| stat          |           1 |
| măsură        |           1 |
| potrivit      |           1 |
| taxă          |           1 |
| rămâne        |           1 |
| neschimbat    |           1 |
| romaniaonesta |           1 |

### 2025-05-14 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| dezbatere           |           1 |
| consecutiv          |           1 |
| oară                |           1 |
| george              |           1 |
| simion              |           1 |
| lipsi               |           1 |
| politician          |           1 |
| evita               |           1 |
| confruntare         |           1 |
| propriu             |           1 |
| popor               |           1 |
| dovadă              |           1 |
| lașitate            |           1 |
| dezbater            |           1 |
| alegeriprezidențial |           1 |
| nicusordan          |           1 |
| georgesimion        |           1 |

### 2025-05-14 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| mesaj        |           2 |
| om           |           2 |
| politic      |           2 |
| primi        |           1 |
| emoție       |           1 |
| recunoștința |           1 |
| președintă   |           1 |
| republicii   |           1 |
| moldova      |           1 |
| maia         |           1 |
| sandu        |           1 |
| admir        |           1 |
| profund      |           1 |
| curaj        |           1 |
| onestitat    |           1 |
| demnitat     |           1 |
| lider        |           1 |
| arăta        |           1 |
| sine         |           1 |
| putea        |           1 |

### 2025-05-14 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| ban             |           2 |
| folosi          |           1 |
| stat            |           1 |
| rețet           |           1 |
| compensa        |           1 |
| vrea            |           1 |
| niciodată       |           1 |
| irosi           |           1 |
| răspuns         |           1 |
| george          |           1 |
| simion          |           1 |
| denotă          |           1 |
| decât           |           1 |
| ignoranță       |           1 |
| față            |           1 |
| român           |           1 |
| îngrijire       |           1 |
| medical         |           1 |
| retetecompensat |           1 |
| bugetulstat     |           1 |

### 2025-05-14 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| george         |           1 |
| simion         |           1 |
| fugi           |           1 |
| dezbatere      |           1 |
| propri         |           1 |
| susținător     |           1 |
| nicusordan     |           1 |
| alegeriromania |           1 |
| presedint      |           1 |

### 2025-05-14 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| român      |           2 |
| gicu       |           1 |
| micu       |           1 |
| spania     |           1 |
| milioan    |           1 |
| demonstra  |           1 |
| întru      |           1 |
| stat       |           1 |
| coerent    |           1 |
| instituție |           1 |
| slujbă     |           1 |
| om         |           1 |
| reuși      |           1 |

### 2025-05-14 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| adevărat   |           2 |
| român      |           2 |
| alegere    |           2 |
| mulțumi    |           1 |
| prim       |           1 |
| ministru   |           1 |
| polonie    |           1 |
| donald     |           1 |
| tusk       |           1 |
| mesaj      |           1 |
| emoționant |           1 |
| susținere  |           1 |
| respect    |           1 |
| european   |           1 |
| trata      |           1 |
| cetățean   |           1 |
| efort      |           1 |
| sine       |           1 |
| adresa     |           1 |
| limbă      |           1 |

### 2025-05-14 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| om             |           2 |
| simion         |           2 |
| însuși         |           1 |
| sine           |           1 |
| clădi          |           1 |
| campanie       |           1 |
| george         |           1 |
| spune          |           1 |
| sistem         |           1 |
| putea          |           1 |
| permite        |           1 |
| român          |           1 |
| manipula       |           1 |
| nicusordan     |           1 |
| alegeriromania |           1 |
| goergescu      |           1 |
| romaniaonesta  |           1 |

### 2025-05-14 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| lapte    |           1 |
| mămăligă |           1 |
| amintire |           1 |
| radacin  |           1 |

### 2025-05-14 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| voce          |           1 |
| femeie        |           1 |
| trebui        |           1 |
| auzit         |           1 |
| inimă         |           1 |
| adagales      |           1 |
| romaniaonesta |           1 |

### 2025-05-15 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| simion    |           2 |
| georgescu |           2 |
| marketing |           2 |
| lua       |           1 |
| mână      |           1 |
| împarte   |           1 |
| george    |           1 |
| părere    |           1 |
| călin     |           1 |
| alia      |           1 |
| probabil  |           1 |
| strategie |           1 |

### 2025-05-15 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| casă           |           2 |
| contracandidat |           1 |
| minte          |           1 |
| gazetă         |           1 |
| rusesc         |           1 |
| exista         |           1 |
| decizie        |           1 |
| procedură      |           1 |
| suspendare     |           1 |
| fond           |           1 |
| european       |           1 |
| românia        |           1 |
| salva          |           1 |
| bruxelles      |           1 |
| fugi           |           1 |
| dezbatere      |           1 |
| declarație     |           1 |
| complet        |           1 |
| iresponsabil   |           1 |
| privire        |           1 |

### 2025-05-15 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| autist      |           3 |
| românia     |           3 |
| copil       |           2 |
| vrea        |           2 |
| președinte  |           2 |
| intolerabil |           1 |
| jigni       |           1 |
| adult       |           1 |
| tulburare   |           1 |
| spectru     |           1 |
| familiile   |           1 |
| nevoi       |           1 |
| special     |           1 |
| sine        |           1 |
| zbat        |           1 |
| viață       |           1 |
| firesc      |           1 |
| întru       |           1 |
| stat        |           1 |
| umili       |           1 |

### 2025-05-15 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| mulțumi         |           1 |
| star            |           1 |
| imsebastianstan |           1 |
| câștiga         |           1 |
| globul          |           1 |
| aur             |           1 |
| nominaliza      |           1 |
| oscar           |           1 |
| categorie       |           1 |
| bun             |           1 |
| actor           |           1 |
| rol             |           1 |
| masculin        |           1 |
| susținere       |           1 |
| explicit        |           1 |
| emoționat       |           1 |
| hai             |           1 |
| vot             |           1 |
| hailavot        |           1 |
| romaniaonesta   |           1 |

### 2025-05-15 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| românia        |           1 |
| speranță       |           1 |
| drum           |           1 |
| stabilitate    |           1 |
| cere           |           1 |
| seriozitat     |           1 |
| voință         |           1 |
| mulțumi        |           1 |
| domn           |           1 |
| președinte     |           1 |
| ilie           |           1 |
| bolojan        |           1 |
| ura            |           1 |
| succes         |           1 |
| dezbatere      |           1 |
| organiza       |           1 |
| tvr            |           1 |
| palat          |           1 |
| cotroceni      |           1 |
| contracandidat |           1 |

### 2025-05-15 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| simion         |           3 |
| interlop       |           2 |
| spune          |           2 |
| umblu          |           1 |
| esc            |           1 |
| george         |           1 |
| valida         |           1 |
| interacțiune   |           1 |
| prietenos      |           1 |
| om             |           1 |
| problemă       |           1 |
| lege           |           1 |
| susținător     |           1 |
| clanure        |           1 |
| putea          |           1 |
| președinte     |           1 |
| nicusordan     |           1 |
| alegeriromania |           1 |
| wow            |           1 |
| fyp            |           1 |

### 2025-05-15 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| simion         |           3 |
| femeie         |           3 |
| om             |           2 |
| trebui         |           2 |
| partid         |           1 |
| bărbat         |           1 |
| atât           |           1 |
| politic        |           1 |
| vorbi          |           1 |
| spune          |           1 |
| ști            |           1 |
| george         |           1 |
| arăta          |           1 |
| sine           |           1 |
| înconjura      |           1 |
| atitudine      |           1 |
| românia        |           1 |
| putea          |           1 |
| nicusordan     |           1 |
| alegeriromania |           1 |

### 2025-05-15 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| familie      |           1 |
| copil        |           1 |
| minunat      |           1 |
| clădi        |           1 |
| iubire       |           1 |
| respect      |           1 |
| familia      |           1 |
| celebrăm     |           1 |
| legătură     |           1 |
| uni          |           1 |
| bucurie      |           1 |
| împreună     |           1 |
| ziuafamiliei |           1 |

### 2025-05-15 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| mulțumi             |           1 |
| sutele              |           1 |
| mesaj               |           1 |
| spune               |           1 |
| convinge            |           1 |
| apropiat            |           1 |
| nehotărâți          |           1 |
| vota                |           1 |
| nicușor             |           1 |
| dan                 |           1 |
| apreciez            |           1 |
| sincer              |           1 |
| efort               |           1 |
| important           |           1 |
| continuăm           |           1 |
| ales                |           1 |
| ieșim               |           1 |
| vot                 |           1 |
| alegeriprezidential |           1 |
| nicusordan          |           1 |

### 2025-05-16 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| însoți            |           1 |
| grup              |           1 |
| lucrător          |           1 |
| dintru            |           1 |
| depozit           |           1 |
| ieșire            |           1 |
| tură              |           1 |
| asculta           |           1 |
| românia           |           1 |
| onestă            |           1 |
| începe            |           1 |
| munci             |           1 |
| romaniaonesta     |           1 |
| nicusorpresedint  |           1 |
| faravotpierdemtot |           1 |

### 2025-05-16 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| cireșe            |           1 |
| bujor             |           1 |
| om                |           1 |
| vrednic           |           1 |
| plin              |           1 |
| românia           |           1 |
| lupta             |           1 |
| oamenivrednică    |           1 |
| romaniaonesta     |           1 |
| hailavot          |           1 |
| faravotpierdemtot |           1 |

### 2025-05-16 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| sine           |           3 |
| credință       |           2 |
| campanie       |           2 |
| spune          |           1 |
| minciune       |           1 |
| deveni         |           1 |
| păcat          |           1 |
| instrument     |           1 |
| politic        |           1 |
| lume           |           1 |
| părea          |           1 |
| uita           |           1 |
| striga         |           1 |
| arăta          |           1 |
| deget          |           1 |
| nicusordan     |           1 |
| alegeriromania |           1 |
| respect        |           1 |
| religie        |           1 |
| fyp            |           1 |

### 2025-05-16 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| campanie       |           3 |
| onest          |           2 |
| vot            |           2 |
| final          |           1 |
| românie        |           1 |
| mulțumi        |           1 |
| susținere      |           1 |
| putea          |           1 |
| mobiliza       |           1 |
| lume           |           1 |
| ieși           |           1 |
| nicusordan     |           1 |
| alegeriromania |           1 |
| comunitate     |           1 |

### 2025-05-16 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| franța         |           3 |
| președinte     |           2 |
| contracandidat |           1 |
| jigne          |           1 |
| popor          |           1 |
| francez        |           1 |
| acasă          |           1 |
| dialog         |           1 |
| domn           |           1 |
| emmanuel       |           1 |
| macron         |           1 |
| alegere        |           1 |
| românia        |           1 |
| extrem         |           1 |
| important      |           1 |
| viitor         |           1 |
| întreg         |           1 |
| uniuni         |           1 |
| european       |           1 |
| puncta         |           1 |

### 2025-05-16 — facebook-post

| cuvânt              |   frecvență |
|:--------------------|------------:|
| andreeamarinromania |           1 |
| romaniaonesta       |           1 |
| faravotpierdemtot   |           1 |

### 2025-05-16 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| horiateca         |           1 |
| romaniaonesta     |           1 |
| faravotpierdemtot |           1 |

### 2025-05-16 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| om               |           2 |
| mihaimorar       |           2 |
| vrea             |           1 |
| vota             |           1 |
| perfect          |           1 |
| votez            |           1 |
| onest            |           1 |
| gând             |           1 |
| înțelept         |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |
| nicusordan       |           1 |

### 2025-05-16 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| românia   |           3 |
| munci     |           3 |
| merita    |           1 |
| respect   |           1 |
| susținere |           1 |
| fermă     |           1 |
| căpșune   |           1 |
| om        |           1 |
| dimineață |           1 |
| seara     |           1 |
| duce      |           1 |
| afacere   |           1 |
| curat     |           1 |
| cinstit   |           1 |
| trudă     |           1 |
| stat      |           1 |
| sprijini  |           1 |
| muncă     |           1 |
| român     |           1 |
| produce   |           1 |

### 2025-05-16 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| românia           |           1 |
| vânzător          |           1 |
| iluzie            |           1 |
| romaniaonesta     |           1 |
| nicusorpresedint  |           1 |
| faravotpierdemtot |           1 |

### 2025-05-16 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| asculta       |           1 |
| certa         |           1 |
| uni           |           1 |
| împreună      |           1 |
| românia       |           1 |
| onest         |           1 |
| romaniaonesta |           1 |
| romaniaunită  |           1 |

### 2025-05-16 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| om               |           1 |
| duce             |           1 |
| românia          |           1 |
| europa           |           1 |
| ploaie           |           1 |
| ninsoare         |           1 |
| sărbătoare       |           1 |
| familie          |           1 |
| muncă            |           1 |
| greu             |           1 |
| responsabilitat  |           1 |
| uriaș            |           1 |
| recunoaștere     |           1 |
| romaniaonesta    |           1 |
| nicusorpresedint |           1 |

### 2025-05-16 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| tractor       |           1 |
| porni         |           1 |
| câmp          |           1 |
| arde          |           1 |
| motorin       |           1 |
| leu           |           1 |
| porumb        |           1 |
| om            |           1 |
| brezoaele     |           1 |
| bunăstarea    |           1 |
| trebui        |           1 |
| ajunge        |           1 |
| milioan       |           1 |
| român         |           1 |
| țară          |           1 |
| romaniaonesta |           1 |
| nicusordan    |           1 |
| hailavot      |           1 |

### 2025-05-16 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| inimă             |           2 |
| voluntarii        |           1 |
| campanie          |           1 |
| bate              |           1 |
| tare              |           1 |
| mulțumi           |           1 |
| dragiu            |           1 |
| romaniaonesta     |           1 |
| faravotpierdemtot |           1 |

### 2025-05-17 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| invita     |           1 |
| studenție  |           1 |
| grozăvești |           1 |
| lecție     |           1 |
| bachat     |           1 |
| ne-        |           1 |
| ieși       |           1 |

### 2025-05-17 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| continuați |           1 |
| crede      |           1 |
| românia    |           1 |
| ieși       |           1 |
| vot        |           1 |
| alegere    |           1 |
| an         |           1 |
| decizie    |           1 |
| trasa      |           1 |
| direcție   |           1 |
| viitor     |           1 |

### 2025-05-17 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| dragi    |           1 |
| român    |           1 |
| diasporă |           1 |
| alegere  |           1 |
| vrea     |           1 |
| putea    |           1 |
| românia  |           1 |
| loc      |           1 |
| merita   |           1 |
| rămâe    |           1 |
| dori     |           1 |
| întorc   |           1 |
| hai      |           1 |
| vot      |           1 |

### 2025-05-17 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| gust         |           1 |
| românesc     |           1 |
| sine         |           1 |
| compara      |           1 |
| legumă       |           1 |
| proaspăt     |           1 |
| producător   |           1 |
| local        |           1 |
| nicusordan   |           1 |
| producatoare |           1 |
| afacere      |           1 |
| food         |           1 |
| fyp          |           1 |

### 2025-05-17 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| important |           1 |
| românia   |           1 |
| trebui    |           1 |
| continuăm |           1 |
| mobiliză  |           1 |
| lume      |           1 |
| ieși      |           1 |
| vot       |           1 |

### 2025-05-17 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| românia   |           1 |
| putea     |           1 |
| loc       |           1 |
| femeie    |           1 |
| alege     |           1 |
| rămâne    |           1 |
| obligație |           1 |
| trebui    |           1 |
| copil     |           1 |

### 2025-05-18 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| vot           |           2 |
| sine          |           2 |
| mobilizare    |           1 |
| precedent     |           1 |
| victorie      |           1 |
| român         |           1 |
| ieși          |           1 |
| voce          |           1 |
| auzit         |           1 |
| lupta         |           1 |
| crede         |           1 |
| țară          |           1 |
| vrea          |           1 |
| dori          |           1 |
| trăi          |           1 |
| începem       |           1 |
| reconstrucție |           1 |
| românia       |           1 |
| românie       |           1 |
| unit          |           1 |

### 2025-05-18 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| țară        |           3 |
| pleca       |           1 |
| făgăraș     |           1 |
| mic         |           1 |
| vot         |           1 |
| decidem     |           1 |
| vrea        |           1 |
| speranță    |           1 |
| dialog      |           1 |
| construcție |           1 |
| unit        |           1 |
| divizată    |           1 |

### 2025-05-18 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vota       |           4 |
| oraș       |           3 |
| trebui     |           2 |
| românia    |           2 |
| schimbare  |           2 |
| aduce      |           2 |
| țară       |           2 |
| vot        |           2 |
| făgăraș    |           1 |
| natal      |           1 |
| școală     |           1 |
| învăța     |           1 |
| esențial   |           1 |
| ținem      |           1 |
| minte      |           1 |
| pleca      |           1 |
| rădăcinile |           1 |
| realiză    |           1 |
| exista     |           1 |
| român      |           1 |

### 2025-05-18 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| întorci  |           1 |
| acasă    |           1 |
| ști      |           1 |
| rădăcină |           1 |
| porți    |           1 |
| datorie  |           1 |

### 2025-05-18 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| nostalgie   |           1 |
| încredere   |           1 |
| generațiile |           1 |
| tânăr       |           1 |
| invi        |           1 |
| vota        |           1 |
| alegere     |           1 |

### 2025-05-18 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| vot      |           2 |
| conta    |           1 |
| ieșim    |           1 |
| regreta  |           1 |

### 2025-05-18 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| secție    |           2 |
| vota      |           2 |
| important |           1 |
| oră       |           1 |
| prinde    |           1 |
| votare    |           1 |
| sine      |           1 |
| vrea      |           1 |
| închide   |           1 |
| lume      |           1 |
| așteptare |           1 |

### 2025-05-18 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| vedea    |           1 |
| minut    |           1 |
| cișmigiu |           1 |

### 2025-05-18 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| putem     |           1 |
| schimba   |           1 |
| lume      |           1 |
| rând      |           1 |
| implicare |           1 |

### 2025-05-18 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| vot          |           2 |
| rămân        |           1 |
| recunoscător |           1 |
| român        |           1 |
| alege        |           1 |
| sine         |           1 |
| exercita     |           1 |

### 2025-05-18 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| româniaonestă |           1 |
| aproape       |           1 |
| sine          |           1 |
| împlini       |           1 |
| aștepta       |           1 |
| numărătoare   |           1 |
| final         |           1 |
| voturilor     |           1 |

### 2025-05-18 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| gând         |           1 |
| special      |           1 |
| recunoștință |           1 |
| mulțumire    |           1 |
| cetățean     |           1 |
| român        |           1 |
| republică    |           1 |
| moldova      |           1 |
| împreună     |           1 |
| încredere    |           1 |
| speranță     |           1 |
| vrea         |           1 |
| continua     |           1 |
| drum         |           1 |
| european     |           1 |
| doamnă       |           1 |
| președintă   |           1 |
| maia         |           1 |
| sandu        |           1 |
| mesaj        |           1 |

### 2025-05-18 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| vota     |           1 |
| părea    |           1 |
| rău      |           1 |

### 2025-05-18 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| vot              |           1 |
| responsabilitate |           1 |
| deciza           |           1 |
| românia          |           1 |

### 2025-05-21 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| prim       |           1 |
| discuție   |           1 |
| informal   |           1 |
| președintă |           1 |
| parlament  |           1 |
| european   |           1 |
| roberta    |           1 |
| metsola    |           1 |
| românia    |           1 |
| sprijin    |           1 |
| perioadă   |           1 |
| următor    |           1 |

### 2025-05-21 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| public       |           2 |
| prioritate   |           1 |
| principal    |           1 |
| perioadă     |           1 |
| corectare    |           1 |
| deficit      |           1 |
| bugetar      |           1 |
| dialog       |           1 |
| partid       |           1 |
| politic      |           1 |
| sine         |           1 |
| vrea         |           1 |
| axa          |           1 |
| exclusiv     |           1 |
| identificare |           1 |
| soluțiilor   |           1 |
| sens         |           1 |
| elaborare    |           1 |
| plan         |           1 |
| concret      |           1 |

### 2025-05-22 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| repatriot  |           2 |
| român      |           2 |
| mediu      |           2 |
| stat       |           2 |
| bucuros    |           1 |
| particip   |           1 |
| gală       |           1 |
| eveniment  |           1 |
| dedicat    |           1 |
| diasporă   |           1 |
| afacere    |           1 |
| trebui     |           1 |
| sprijini   |           1 |
| încurca    |           1 |
| reveni     |           1 |
| acasă      |           1 |
| previzibil |           1 |
| economic   |           1 |
| competitiv |           1 |
| încuraja   |           1 |

### 2025-05-22 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| președinte      |           2 |
| democrație      |           2 |
| primi           |           1 |
| validare        |           1 |
| mandat          |           1 |
| românia         |           1 |
| onoare          |           1 |
| responsabilitat |           1 |
| vot             |           1 |
| masiv           |           1 |
| arăta           |           1 |
| român           |           1 |
| crede           |           1 |
| schimbare       |           1 |
| cer             |           1 |
| reformare       |           1 |
| instituție      |           1 |
| dezamăgi        |           1 |
| promit          |           1 |
| apăra           |           1 |

### 2025-05-23 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| oraș          |           3 |
| general       |           3 |
| om            |           2 |
| trebui        |           2 |
| bucurești     |           2 |
| esențial      |           2 |
| viitor        |           2 |
| modernizare   |           2 |
| public        |           2 |
| tramvai       |           2 |
| urbanism      |           2 |
| vrea          |           2 |
| dragi         |           1 |
| bucureștean   |           1 |
| aparține      |           1 |
| funcție       |           1 |
| muncă         |           1 |
| administrație |           1 |
| începe        |           1 |
| sine          |           1 |

### 2025-05-24 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| educație    |           3 |
| vrea        |           3 |
| trebui      |           3 |
| tinerilor   |           2 |
| societate   |           2 |
| românia     |           2 |
| universitar |           2 |
| deveni      |           2 |
| civic       |           2 |
| investiția  |           1 |
| ajuta       |           1 |
| crește      |           1 |
| feri        |           1 |
| pericolă    |           1 |
| deschide    |           1 |
| congres     |           1 |
| studenț     |           1 |
| sublinia    |           1 |
| direcție    |           1 |
| esențial    |           1 |

### 2025-05-24 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| vrea          |           5 |
| românia       |           3 |
| țară          |           3 |
| înțelege      |           3 |
| pune          |           3 |
| sine          |           3 |
| speranță      |           2 |
| viitor        |           2 |
| împreună      |           2 |
| român         |           2 |
| presus        |           2 |
| întreg        |           2 |
| arăta         |           2 |
| comunitate    |           2 |
| continuăm     |           1 |
| drum          |           1 |
| democratic    |           1 |
| pro-european  |           1 |
| transatlantic |           1 |
| bun           |           1 |

### 2025-05-25 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| prim     |           2 |
| ajunge   |           1 |
| varșovia |           1 |
| discuție |           1 |
| ministru |           1 |
| donald   |           1 |
| tusk     |           1 |

### 2025-05-25 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| român        |           3 |
| european     |           2 |
| poliție      |           2 |
| frontieră    |           2 |
| frontex      |           2 |
| misiune      |           2 |
| discuție     |           1 |
| util         |           1 |
| plăcut       |           1 |
| parte        |           1 |
| angajat      |           1 |
| agenție      |           1 |
| garda        |           1 |
| coastă       |           1 |
| sediu        |           1 |
| varșovia     |           1 |
| contribui    |           1 |
| zilnic       |           1 |
| protejare    |           1 |
| frontierelor |           1 |

### 2025-05-25 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| polonia    |           2 |
| valoare    |           2 |
| românia    |           2 |
| tydzie     |           2 |
| caa        |           2 |
| participa  |           1 |
| emoție     |           1 |
| speranță   |           1 |
| marș       |           1 |
| milion     |           1 |
| inim       |           1 |
| varșovia   |           1 |
| veni       |           1 |
| prieten    |           1 |
| împărtășim |           1 |
| același    |           1 |
| crede      |           1 |
| democrație |           1 |
| libertate  |           1 |
| putere     |           1 |

### 2025-05-25 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| românia      |           2 |
| român        |           2 |
| ocazie       |           1 |
| zilei        |           1 |
| românilor    |           1 |
| pretutindeni |           1 |
| gând         |           1 |
| sine         |           1 |
| îndrepta     |           1 |
| trăi         |           1 |
| hotare       |           1 |
| voce         |           1 |
| implicare    |           1 |
| rol          |           1 |
| președinte   |           1 |
| țară         |           1 |
| creez        |           1 |
| punt         |           1 |
| idee         |           1 |
| proiect      |           1 |

### 2025-05-26 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |           3 |
| președinte  |           2 |
| depune      |           1 |
| jurământ    |           1 |
| față        |           1 |
| parlament   |           1 |
| țară        |           1 |
| deschide    |           1 |
| voce        |           1 |
| societate   |           1 |
| partener    |           1 |
| implica     |           1 |
| dezbate     |           1 |
| arăta       |           1 |
| viu         |           1 |
| stat        |           1 |
| eficient    |           1 |
| responsabil |           1 |
| deficit     |           1 |
| afecta      |           1 |

### 2025-05-28 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| președinte |           2 |
| trump      |           2 |
| strategic  |           2 |
| interes    |           2 |
| onora      |           1 |
| port       |           1 |
| discuție   |           1 |
| donald     |           1 |
| mulțumi    |           1 |
| mesaj      |           1 |
| felicitare |           1 |
| adresa     |           1 |
| stat       |           1 |
| unit       |           1 |
| america    |           1 |
| reprezenta |           1 |
| aliat      |           1 |
| extrem     |           1 |
| apropiat   |           1 |
| românia    |           1 |

### 2025-05-29 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| decizie        |           2 |
| principiu      |           2 |
| public         |           2 |
| surprinzător   |           1 |
| curte          |           1 |
| constituțional |           1 |
| anunța         |           1 |
| contradicție   |           1 |
| esențial       |           1 |
| democrație     |           1 |
| transparență   |           1 |
| exercitare     |           1 |
| funcție        |           1 |
| acces          |           1 |
| cetățen        |           1 |
| informație     |           1 |
| privind        |           1 |
| declarație     |           1 |
| avere          |           1 |
| demnitarilor   |           1 |

### 2025-05-29 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| afecta      |           2 |
| moment      |           2 |
| autoritate  |           2 |
| rapid       |           2 |
| climatic    |           2 |
| gândurile   |           1 |
| sine        |           1 |
| îndrepta    |           1 |
| familie     |           1 |
| lovi        |           1 |
| inundație   |           1 |
| puternic    |           1 |
| localitate  |           1 |
| județ       |           1 |
| împărtășesc |           1 |
| îngrijorare |           1 |
| trece       |           1 |
| greu        |           1 |
| informa     |           1 |
| real        |           1 |

### 2025-05-31 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| grav          |           2 |
| trebui        |           2 |
| prevenție     |           2 |
| comună        |           1 |
| băcel         |           1 |
| afecta        |           1 |
| inundație     |           1 |
| vorbi         |           1 |
| om            |           1 |
| autoritate    |           1 |
| local         |           1 |
| echipă        |           1 |
| intervenție   |           1 |
| situație      |           1 |
| cunoscut      |           1 |
| an            |           1 |
| sine          |           1 |
| stat          |           1 |
| disfuncțional |           1 |
| domeniu       |           1 |

### 2025-05-31 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           6 |
| praid      |           2 |
| comunitate |           2 |
| om         |           2 |
| putea      |           2 |
| măsură     |           2 |
| apă        |           2 |
| sine       |           2 |
| alături    |           1 |
| profund    |           1 |
| afecta     |           1 |
| inundație  |           1 |
| mii        |           1 |
| suferi     |           1 |
| cauză      |           1 |
| dezastru   |           1 |
| preveni    |           1 |
| solicita   |           1 |
| premier    |           1 |
| trimitere  |           1 |

### 2025-06-01 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| copil     |           4 |
| viitor    |           2 |
| crește    |           2 |
| trebui    |           2 |
| românia   |           2 |
| iunie     |           1 |
| celebrăm  |           1 |
| inocență  |           1 |
| bucurie   |           1 |
| speranță  |           1 |
| aduce     |           1 |
| viață     |           1 |
| aminti    |           1 |
| prețios   |           1 |
| important |           1 |
| oferi     |           1 |
| putea     |           1 |
| demnitate |           1 |
| educație  |           1 |
| sănătate  |           1 |

### 2025-06-02 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| summit                          |           3 |
| important                       |           2 |
| flanc                           |           2 |
| estic                           |           2 |
| stat                            |           2 |
| colectiv                        |           2 |
| apărare                         |           2 |
| încheia                         |           1 |
| vilnius                         |           1 |
| alături                         |           1 |
| partener                        |           1 |
| discuție                        |           1 |
| constitui                       |           1 |
| pas                             |           1 |
| pregătire                       |           1 |
| northatlantictreatyorganization |           1 |
| haga                            |           1 |
| ghida                           |           1 |
| convingere                      |           1 |
| comun                           |           1 |

### 2025-06-04 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| românia          |           5 |
| iunie            |           5 |
| sine             |           4 |
| extern           |           3 |
| prezenta         |           2 |
| intern           |           2 |
| proces           |           2 |
| participare      |           2 |
| deficit          |           2 |
| rămâne           |           2 |
| activitate       |           2 |
| seriozitate      |           2 |
| angaja           |           2 |
| european         |           2 |
| summit           |           2 |
| responsabilitate |           2 |
| principal        |           1 |
| temă             |           1 |
| afla             |           1 |
| agendă           |           1 |

### 2025-06-08 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| cristina    |           2 |
| românia     |           1 |
| celebra     |           1 |
| sportiv     |           1 |
| istorie     |           1 |
| neagu       |           1 |
| bun         |           1 |
| handbalistă |           1 |
| lume        |           1 |
| inspira     |           1 |
| dăruire     |           1 |
| curaj       |           1 |
| performanță |           1 |
| excepțional |           1 |
| mulțumim    |           1 |
| oferi       |           1 |
| tricolor    |           1 |
| vrea        |           1 |
| rămâne      |           1 |
| simbol      |           1 |

### 2025-06-10 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           2 |
| majestății |           2 |
| rege       |           2 |
| spania     |           2 |
| legătură   |           2 |
| spaniei    |           2 |
| puternic   |           2 |
| i-         |           1 |
| ura        |           1 |
| călduros   |           1 |
| bun        |           1 |
| veni       |           1 |
| felipe     |           1 |
| -lea       |           1 |
| afla       |           1 |
| întru      |           1 |
| vizită     |           1 |
| arăta      |           1 |
| profunde   |           1 |
| țară       |           1 |

### 2025-06-10 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| împreună         |           1 |
| puternic         |           1 |
| republicamoldova |           1 |
| românia          |           1 |

### 2025-06-10 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |           3 |
| republică   |           2 |
| moldova     |           2 |
| european    |           2 |
| bucura      |           1 |
| afla        |           1 |
| chișinău    |           1 |
| vizită      |           1 |
| oficial     |           1 |
| calitate    |           1 |
| președinte  |           1 |
| reconfirm   |           1 |
| sprijin     |           1 |
| cuprinzător |           1 |
| sincer      |           1 |
| constant    |           1 |
| întru       |           1 |
| moment      |           1 |
| crucial     |           1 |
| parcurs     |           1 |

### 2025-06-10 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| republicii  |           2 |
| moldova     |           2 |
| participare |           1 |
| eveniment   |           1 |
| viitor      |           1 |
| european    |           1 |
| comun       |           1 |
| românia     |           1 |
| alături     |           1 |
| președinte  |           1 |
| maia        |           1 |
| sandu       |           1 |

### 2025-06-11 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| român        |           3 |
| ucraina      |           2 |
| sine         |           2 |
| românia      |           2 |
| constant     |           2 |
| odesa        |           1 |
| discuție     |           1 |
| bun          |           1 |
| reprezentant |           1 |
| comunitate   |           1 |
| românesc     |           1 |
| sud          |           1 |
| aborda       |           1 |
| problemă     |           1 |
| important    |           1 |
| confrunta    |           1 |
| redeschidere |           1 |
| consulat     |           1 |
| acces        |           1 |
| educație     |           1 |

### 2025-06-11 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| ucraina    |           4 |
| trilateral |           2 |
| românia    |           2 |
| moldova    |           2 |
| precum     |           2 |
| securitate |           2 |
| european   |           2 |
| odesa      |           1 |
| marjă      |           1 |
| summit     |           1 |
| europa     |           1 |
| sud-est    |           1 |
| loc        |           1 |
| reuniune   |           1 |
| format     |           1 |
| înalt      |           1 |
| nivel      |           1 |
| republică  |           1 |
| împreună   |           1 |
| președinte |           1 |

### 2025-06-13 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| justiția         |           2 |
| mineriadă        |           1 |
| iunie            |           1 |
| rămâne           |           1 |
| dureroa          |           1 |
| moment           |           1 |
| istorie          |           1 |
| post-decembristă |           1 |
| an               |           1 |
| pronunța         |           1 |
| hotărâre         |           1 |
| definitiv        |           1 |
| dosar            |           1 |
| mineriada        |           1 |
| lipsește         |           1 |
| verdict          |           1 |
| închide          |           1 |
| atât             |           1 |
| traumă           |           1 |
| suferință        |           1 |

### 2025-06-16 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| vrea         |           2 |
| esențial     |           2 |
| i-           |           1 |
| invita       |           1 |
| palat        |           1 |
| cotroceni    |           1 |
| reprezentant |           1 |
| sindicat     |           1 |
| schimb       |           1 |
| deschide     |           1 |
| idee         |           1 |
| soluție      |           1 |
| genera       |           1 |
| echilibru    |           1 |
| fiscal       |           1 |
| românia      |           1 |
| sine         |           1 |
| afla         |           1 |
| întru        |           1 |
| moment       |           1 |

### 2025-06-18 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| violență     |           6 |
| sine         |           5 |
| femeie       |           4 |
| victimă      |           3 |
| niciuna      |           3 |
| confrunta    |           2 |
| an           |           2 |
| caz          |           2 |
| domestic     |           2 |
| societate    |           2 |
| putea        |           2 |
| trata        |           2 |
| măsură       |           2 |
| construi     |           2 |
| românia      |           1 |
| nivel        |           1 |
| îngrijorător |           1 |
| prim         |           1 |
| lună         |           1 |
| pierde       |           1 |

### 2025-06-20 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| domn          |           2 |
| ilie          |           2 |
| bolojan       |           2 |
| românia       |           2 |
| esențial      |           2 |
| vrea          |           2 |
| dura          |           2 |
| putea         |           2 |
| necesar       |           2 |
| administrație |           2 |
| eficient      |           2 |
| desemna       |           1 |
| funcție       |           1 |
| prim          |           1 |
| ministru      |           1 |
| guvern        |           1 |
| sprijini      |           1 |
| majoritate    |           1 |
| solid         |           1 |
| stabil        |           1 |

### 2025-06-25 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| regat                           |           2 |
| unit                            |           2 |
| northatlantictreatyorganization |           2 |
| real                            |           1 |
| onoare                          |           1 |
| întâlni                         |           1 |
| prim                            |           1 |
| ministru                        |           1 |
| keir                            |           1 |
| starmer                         |           1 |
| marja                           |           1 |
| summit                          |           1 |
| haga                            |           1 |
| reconfirma                      |           1 |
| relație                         |           1 |
| bilateral                       |           1 |
| solid                           |           1 |
| românia                         |           1 |
| calitate                        |           1 |
| partener                        |           1 |

### 2025-06-25 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| comun       |           3 |
| strategic   |           2 |
| regiune     |           2 |
| întâlnire   |           1 |
| productiv   |           1 |
| consistent  |           1 |
| președinte  |           1 |
| turcia      |           1 |
| recep       |           1 |
| tayyip      |           1 |
| erdoan      |           1 |
| haga        |           1 |
| discuta     |           1 |
| parteneriat |           1 |
| româno-turc |           1 |
| cooperare   |           1 |
| țară        |           1 |
| baza        |           1 |
| prietenie   |           1 |
| lung        |           1 |

### 2025-06-25 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| românia                         |           2 |
| republică                       |           2 |
| european                        |           2 |
| ucraina                         |           2 |
| northatlantictreatyorganization |           2 |
| întrevedere                     |           1 |
| bun                             |           1 |
| președinte                      |           1 |
| petr                            |           1 |
| pavel                           |           1 |
| haga                            |           1 |
| discuta                         |           1 |
| relație                         |           1 |
| bilateral                       |           1 |
| excelent                        |           1 |
| cehă                            |           1 |
| precum                          |           1 |
| cooperare                       |           1 |
| plan                            |           1 |
| domeniu                         |           1 |

### 2025-06-25 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| natosummit     |           1 |
| usa            |           1 |
| presidenttrump |           1 |
| romania        |           1 |

### 2025-06-26 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           3 |
| românia    |           3 |
| prim       |           1 |
| întâlnire  |           1 |
| membru     |           1 |
| român      |           1 |
| parlament  |           1 |
| discuta    |           1 |
| prioritate |           1 |
| agendă     |           1 |
| conveni    |           1 |
| menține    |           1 |
| coordonare |           1 |
| strâns     |           1 |
| împreună   |           1 |
| promova    |           1 |
| interes    |           1 |
| profil     |           1 |
| solid      |           1 |
| plan       |           1 |

### 2025-06-26 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| european    |           3 |
| re          |           1 |
| dialog      |           1 |
| bun         |           1 |
| președinte  |           1 |
| consiliu    |           1 |
| antnio      |           1 |
| costa       |           1 |
| reuniuni    |           1 |
| bruxelles   |           1 |
| reitera     |           1 |
| angajament  |           1 |
| ferm        |           1 |
| românia     |           1 |
| colabora    |           1 |
| strânge     |           1 |
| instituție  |           1 |
| stat        |           1 |
| membră      |           1 |
| consolidare |           1 |

### 2025-07-02 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| mihai        |           2 |
| leu          |           2 |
| sport        |           2 |
| afla         |           1 |
| profundă     |           1 |
| tristețe     |           1 |
| veste        |           1 |
| dispariție   |           1 |
| românia      |           1 |
| pierde       |           1 |
| campion      |           1 |
| excepțional  |           1 |
| palmares     |           1 |
| impresionant |           1 |
| om           |           1 |
| integru      |           1 |
| inspira      |           1 |
| curaj        |           1 |
| pasiune      |           1 |
| bun-simț     |           1 |

### 2025-07-08 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| administrativ  |           5 |
| dragoș         |           3 |
| dacian         |           2 |
| cosmin         |           2 |
| judecător      |           2 |
| românia        |           2 |
| personalitate  |           2 |
| recunoaște     |           2 |
| domeniu        |           2 |
| european       |           2 |
| profesor       |           2 |
| facultate      |           2 |
| proiect        |           2 |
| cod            |           2 |
| public         |           2 |
| stat           |           2 |
| numi           |           1 |
| funcție        |           1 |
| curte          |           1 |
| constituțional |           1 |

### 2025-07-14 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| declarație    |           2 |
| avere         |           2 |
| promite       |           1 |
| publica       |           1 |
| sită          |           1 |
| -ul           |           1 |
| administrație |           1 |
| prezidențial  |           1 |
| convingere    |           1 |
| ferm          |           1 |
| asumare       |           1 |
| transparență  |           1 |
| necesar       |           1 |
| funcție       |           1 |
| demnitate     |           1 |
| public        |           1 |
| conține       |           1 |
| inclusiv      |           1 |
| împrumut      |           1 |
| donațiil      |           1 |

### 2025-07-14 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           7 |
| măsură     |           3 |
| piață      |           3 |
| financiar  |           3 |
| românia    |           3 |
| sine       |           3 |
| tva        |           3 |
| situație   |           2 |
| trece      |           2 |
| perioadă   |           2 |
| an         |           2 |
| intra      |           2 |
| buget      |           2 |
| guvern     |           2 |
| putea      |           2 |
| fiscal     |           1 |
| adopta     |           1 |
| reprezenta |           1 |
| provizorie |           1 |
| economie   |           1 |

### 2025-07-18 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| germania  |           3 |
| industrie |           2 |
| românia   |           2 |
| țară      |           2 |
| întâlnire |           1 |
| bun       |           1 |
| cancelar  |           1 |
| federal   |           1 |
| friedrich |           1 |
| merz      |           1 |
| semna     |           1 |
| împreună  |           1 |
| plan      |           1 |
| comun     |           1 |
| acțiune   |           1 |
| reflecta  |           1 |
| dorință   |           1 |
| ferm      |           1 |
| consolida |           1 |
| cooperare |           1 |

### 2025-07-21 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| stat                            |           3 |
| inclusiv                        |           3 |
| sine                            |           2 |
| interferență                    |           2 |
| rusia                           |           2 |
| alegere                         |           2 |
| noiembrie                       |           2 |
| românia                         |           2 |
| jos                             |           2 |
| northatlantictreatyorganization |           2 |
| european                        |           2 |
| trebui                          |           2 |
| îndemn                          |           1 |
| încă                            |           1 |
| îndoii                          |           1 |
| comunicat                       |           1 |
| încercările                     |           1 |
| implicare                       |           1 |
| forță                           |           1 |
| statal                          |           1 |

### 2025-07-22 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| trecut       |           3 |
| profund      |           2 |
| român        |           2 |
| lipsă        |           2 |
| încredere    |           2 |
| om           |           2 |
| viitor       |           2 |
| imagine      |           2 |
| dezinformare |           2 |
| putea        |           2 |
| cetățean     |           2 |
| construi     |           2 |
| îngrijora    |           1 |
| rezultat     |           1 |
| studiu       |           1 |
| prezenta     |           1 |
| inscop       |           1 |
| iicmer       |           1 |
| opinie       |           1 |
| principal    |           1 |

### 2025-07-24 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| mediu        |           2 |
| romsilva     |           2 |
| reformă      |           2 |
| instituție   |           2 |
| guvern       |           2 |
| întâlnire    |           1 |
| ministru     |           1 |
| diana        |           1 |
| buzoianu     |           1 |
| discuta      |           1 |
| propunere    |           1 |
| reorganizare |           1 |
| demers       |           1 |
| susține      |           1 |
| campanie     |           1 |
| electoral    |           1 |
| vorbi        |           1 |
| întru        |           1 |
| păcat        |           1 |
| asocia       |           1 |

### 2025-07-25 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| economic       |           2 |
| interes        |           2 |
| românia        |           2 |
| austriac       |           2 |
| întâlnire      |           1 |
| constructiv    |           1 |
| reprezentant   |           1 |
| mediu          |           1 |
| afacere        |           1 |
| austria        |           1 |
| cadru          |           1 |
| salzburg       |           1 |
| summit         |           1 |
| discuta        |           1 |
| oportunitățile |           1 |
| cooperare      |           1 |
| sublinia       |           1 |
| consolidare    |           1 |
| relație        |           1 |
| bilateral      |           1 |

### 2025-07-25 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| austria    |           3 |
| românia    |           2 |
| intra      |           1 |
| întru      |           1 |
| capitol    |           1 |
| relație    |           1 |
| bilateral  |           1 |
| reveni     |           1 |
| dialog     |           1 |
| deschis    |           1 |
| cooperare  |           1 |
| investitor |           1 |
| dori       |           1 |
| crește     |           1 |
| prezență   |           1 |
| sprijinim  |           1 |
| extindere  |           1 |
| firmă      |           1 |
| românesc   |           1 |

### 2025-07-26 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| austria          |           2 |
| încurajăm        |           2 |
| regiune          |           2 |
| cadru            |           1 |
| întâlnire        |           1 |
| cancelar         |           1 |
| federal          |           1 |
| christian        |           1 |
| stocker          |           1 |
| agrea            |           1 |
| lucra            |           1 |
| împreună         |           1 |
| impuls           |           1 |
| cooperare        |           1 |
| româno-austriece |           1 |
| atât             |           1 |
| nivel            |           1 |
| bilateral        |           1 |
| european         |           1 |
| românia          |           1 |

### 2025-07-27 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| austria     |           2 |
| parteneriat |           2 |
| alături     |           1 |
| investitor  |           1 |
| românia     |           1 |
| intra       |           1 |
| întru       |           1 |
| etapă       |           1 |
| consolidare |           1 |
| dialog      |           1 |
| cooperare   |           1 |
| discuție    |           1 |
| constructiv |           1 |
| viitor      |           1 |
| economic    |           1 |
| nicusordan  |           1 |
| romania     |           1 |
| fyp         |           1 |

### 2025-07-28 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| plăcere    |           1 |
| primi      |           1 |
| palat      |           1 |
| cotroceni  |           1 |
| președinte |           1 |
| adunare    |           1 |
| național   |           1 |
| republicii |           1 |
| coreea     |           1 |
| domn       |           1 |
| woo        |           1 |
| won-shik   |           1 |
| afla       |           1 |
| vizită     |           1 |
| oficial    |           1 |
| românia    |           1 |
| context    |           1 |
| marcăre    |           1 |
| an         |           1 |
| relație    |           1 |

### 2025-07-29 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| sine         |           4 |
| familie      |           2 |
| afla         |           2 |
| profund      |           1 |
| afecta       |           1 |
| pierdere     |           1 |
| viață        |           1 |
| omenesc      |           1 |
| distrugere   |           1 |
| produce      |           1 |
| comunitate   |           1 |
| întreg       |           1 |
| urmă         |           1 |
| inundațiilor |           1 |
| devastatoare |           1 |
| moldova      |           1 |
| gândurile    |           1 |
| îndrepta     |           1 |
| îndoliat     |           1 |
| nevoi        |           1 |

### 2025-07-30 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| victimă       |           3 |
| internațional |           2 |
| trafic        |           2 |
| persoană      |           2 |
| rețea         |           2 |
| comemora      |           1 |
| luptă         |           1 |
| datorie       |           1 |
| recunoaștem   |           1 |
| realitate     |           1 |
| dur           |           1 |
| românia       |           1 |
| păcat         |           1 |
| principal     |           1 |
| țară          |           1 |
| origine       |           1 |
| europa        |           1 |
| mii           |           1 |
| femeie        |           1 |
| bărbat        |           1 |

### 2025-07-30 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| magistrat |           5 |
| sistem    |           4 |
| pensie    |           3 |
| lege      |           3 |
| prevedere |           2 |
| justiție  |           2 |
| sine      |           2 |
| respecta  |           2 |
| clar      |           2 |
| regulă    |           2 |
| continua  |           2 |
| total     |           1 |
| aberant   |           1 |
| lua       |           1 |
| egal      |           1 |
| salariu   |           1 |
| actual    |           1 |
| încuraja  |           1 |
| om        |           1 |
| ieși      |           1 |

### 2025-07-31 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| holocaustului    |           2 |
| comunitate       |           2 |
| trebui           |           2 |
| societate        |           2 |
| putea            |           2 |
| european         |           1 |
| comemorare       |           1 |
| romilor          |           1 |
| reamintim        |           1 |
| responsabilitate |           1 |
| capitol          |           1 |
| dureros          |           1 |
| istorie          |           1 |
| datorie          |           1 |
| cunoaște         |           1 |
| asuma            |           1 |
| trecut           |           1 |
| repeta           |           1 |
| greșelile        |           1 |
| marca            |           1 |

### 2025-08-10 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| drumeție   |           1 |
| natură     |           1 |
| copil      |           1 |
| încântat   |           1 |
| nicusordan |           1 |

### 2025-08-10 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| orhei        |           1 |
| vechi        |           1 |
| răsuna       |           1 |
| muzică       |           1 |
| folk         |           1 |
| festival     |           1 |
| lupilor      |           1 |
| weekend      |           1 |
| moldovenilor |           1 |
| primire      |           1 |
| călduros     |           1 |
| nicusordan   |           1 |

### 2025-08-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| petrece    |           1 |
| dincolo    |           1 |
| prut       |           1 |
| reaminti   |           1 |
| puternic   |           1 |
| legătură   |           1 |
| românia    |           1 |
| republică  |           1 |
| moldova    |           1 |
| rămâne     |           1 |
| unit       |           1 |
| prețui     |           1 |
| apropia    |           1 |
| privi      |           1 |
| încredere  |           1 |
| viitor     |           1 |
| european   |           1 |
| nicusordan |           1 |

### 2025-08-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| ucraina    |           3 |
| european   |           3 |
| construi   |           2 |
| pace       |           2 |
| împreună   |           2 |
| sine       |           2 |
| viitor     |           2 |
| salut      |           1 |
| efort      |           1 |
| președinte |           1 |
| donald     |           1 |
| trump      |           1 |
| contribui  |           1 |
| încheiere  |           1 |
| război     |           1 |
| ilegal     |           1 |
| declanșa   |           1 |
| rusia      |           1 |
| soluție    |           1 |
| just       |           1 |

### 2025-08-13 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| pace                    |           4 |
| președinte              |           3 |
| ucraina                 |           3 |
| poziție                 |           2 |
| trump                   |           2 |
| securitate              |           2 |
| participa               |           1 |
| videoconferință         |           1 |
| coaliție                |           1 |
| voință                  |           1 |
| coordona                |           1 |
| întâlnire               |           1 |
| bilateral               |           1 |
| stateleunitealeamericii |           1 |
| donald                  |           1 |
| federației              |           1 |
| rus                     |           1 |
| salutăm                 |           1 |
| determinare             |           1 |
| pune                    |           1 |

### 2025-08-17 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| ucraina         |           8 |
| rusia           |           5 |
| securitate      |           4 |
| putea           |           3 |
| sprijin         |           3 |
| pace            |           3 |
| cadru           |           2 |
| coaliție        |           2 |
| trebui          |           2 |
| arăta           |           2 |
| proces          |           2 |
| consolidare     |           2 |
| însemna         |           2 |
| garanție        |           2 |
| propriu         |           2 |
| videoconferință |           1 |
| voință          |           1 |
| discuta         |           1 |
| coordona        |           1 |
| efort           |           1 |

### 2025-08-17 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| loc        |           1 |
| vizita     |           1 |
| familie    |           1 |
| românia    |           1 |
| drumeție   |           1 |
| sâmbătă    |           1 |
| rămâne     |           1 |
| favorit    |           1 |
| nicusordan |           1 |

### 2025-08-18 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| rating      |           4 |
| românia     |           4 |
| agenție     |           2 |
| confirma    |           2 |
| bbb-        |           2 |
| perspectivă |           2 |
| negativ     |           2 |
| față        |           2 |
| an          |           2 |
| veste       |           1 |
| bun         |           1 |
| fitch       |           1 |
| vineri      |           1 |
| amintesc    |           1 |
| standard    |           1 |
| and         |           1 |
| poors       |           1 |
| iulie       |           1 |
| reafirm     |           1 |
| seriozitate |           1 |

### 2025-08-18 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| rusia      |           2 |
| sine       |           1 |
| dori       |           1 |
| pace       |           1 |
| cadru      |           1 |
| coaliție   |           1 |
| voință     |           1 |
| discuta    |           1 |
| important  |           1 |
| oferi      |           1 |
| sprijin    |           1 |
| ucraina    |           1 |
| exercita   |           1 |
| presiune   |           1 |
| economic   |           1 |
| negociere  |           1 |
| vrea       |           1 |
| urma       |           1 |
| echitabile |           1 |
| nicusordan |           1 |

### 2025-08-19 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| ucraina         |           2 |
| videoconferință |           1 |
| coaliție        |           1 |
| voință          |           1 |
| consiliu        |           1 |
| european        |           1 |
| sublinia        |           1 |
| pace            |           1 |
| trebui          |           1 |
| just            |           1 |
| durabil         |           1 |
| românia         |           1 |
| continua        |           1 |
| încuraja        |           1 |
| sancțiune       |           1 |
| rusia           |           1 |
| sprijini        |           1 |
| garanție        |           1 |
| fermă           |           1 |
| securitate      |           1 |

### 2025-08-19 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| securitate        |           4 |
| ucraina           |           4 |
| pace              |           4 |
| trebui            |           4 |
| europa            |           3 |
| românia           |           3 |
| vrea              |           3 |
| rusia             |           2 |
| videoconferințele |           1 |
| coaliție          |           1 |
| voință            |           1 |
| consiliu          |           1 |
| european          |           1 |
| aborda            |           1 |
| rezultat          |           1 |
| discuție          |           1 |
| important         |           1 |
| asear             |           1 |
| washington        |           1 |
| privind           |           1 |

### 2025-08-20 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| respect                         |           1 |
| recunoștință                    |           1 |
| militare                        |           1 |
| comandament                     |           1 |
| forță                           |           1 |
| operație                        |           1 |
| special                         |           1 |
| mulțumim                        |           1 |
| profesionalism                  |           1 |
| loialitate                      |           1 |
| contribui                       |           1 |
| siguranță                       |           1 |
| respectare                      |           1 |
| angajamentă                     |           1 |
| românia                         |           1 |
| cadru                           |           1 |
| northatlantictreatyorganization |           1 |
| uniuneaeuropeană                |           1 |
| nicusordan                      |           1 |

### 2025-08-21 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| parte        |           1 |
| primire      |           1 |
| călduros     |           1 |
| roșiă        |           1 |
| montan       |           1 |
| trebui       |           1 |
| valorifica   |           1 |
| sit          |           1 |
| unesco       |           1 |
| unic         |           1 |
| putea        |           1 |
| aduce        |           1 |
| milion       |           1 |
| turist       |           1 |
| oportunitate |           1 |
| dezvoltare   |           1 |
| comunitate   |           1 |
| local        |           1 |
| nicusordan   |           1 |

### 2025-08-26 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |           5 |
| trebui      |           4 |
| român       |           3 |
| românia     |           3 |
| sine        |           3 |
| obiectiv    |           3 |
| economic    |           3 |
| împreună    |           2 |
| extern      |           2 |
| securitate  |           2 |
| necesar     |           2 |
| relansa     |           2 |
| economie    |           2 |
| rămâne      |           2 |
| parteneriat |           2 |
| strategic   |           2 |
| cooperare   |           2 |
| lucru       |           2 |
| prioritate  |           2 |
| țară        |           2 |

### 2025-08-28 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| muncă      |           2 |
| sine       |           2 |
| ură        |           2 |
| român      |           2 |
| condamn    |           1 |
| fermitate  |           1 |
| agresiune  |           1 |
| tânăr      |           1 |
| veni       |           1 |
| bucurești  |           1 |
| lovi       |           1 |
| umili      |           1 |
| naște      |           1 |
| fapt       |           1 |
| intolerabe |           1 |
| ultim      |           1 |
| săptămână  |           1 |
| propaga    |           1 |
| spațiu     |           1 |
| public     |           1 |

### 2025-08-31 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| român      |           4 |
| limbă      |           3 |
| republică  |           2 |
| moldova    |           2 |
| limbii     |           2 |
| românia    |           2 |
| onoare     |           1 |
| prezent    |           1 |
| dictare    |           1 |
| național   |           1 |
| organiza   |           1 |
| ocazie     |           1 |
| zilei      |           1 |
| doamnă     |           1 |
| președinte |           1 |
| maia       |           1 |
| sandu      |           1 |
| invitație  |           1 |
| exemplu    |           1 |
| oferi      |           1 |

### 2025-08-31 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| național    |           2 |
| participare |           1 |
| alături     |           1 |
| președinte  |           1 |
| republicii  |           1 |
| moldova     |           1 |
| maia        |           1 |
| sandu       |           1 |
| eveniment   |           1 |
| dictare     |           1 |
| piață       |           1 |
| marii       |           1 |
| adunări     |           1 |
| chișinău    |           1 |

### 2025-09-01 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| european         |           3 |
| militar          |           3 |
| importanță       |           2 |
| securitate       |           2 |
| uniuneaeuropeană |           2 |
| neagră           |           2 |
| ura              |           1 |
| bun              |           1 |
| veni             |           1 |
| țărm             |           1 |
| negru            |           1 |
| doamnă           |           1 |
| președinte       |           1 |
| comisie          |           1 |
| ursula           |           1 |
| von              |           1 |
| der              |           1 |
| leyen            |           1 |
| țară             |           1 |
| strategic        |           1 |

### 2025-09-01 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           2 |
| mulțumi    |           1 |
| manfred    |           1 |
| weber      |           1 |
| vizită     |           1 |
| cotroceni  |           1 |
| discuție   |           1 |
| consistent |           1 |
| președinte |           1 |
| partid     |           1 |
| popular    |           1 |
| prioritate |           1 |
| comun      |           1 |
| uniune     |           1 |
| sigur      |           1 |
| stabil     |           1 |
| economie   |           1 |
| competitiv |           1 |
| continua   |           1 |
| lucra      |           1 |

### 2025-09-02 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| solidaritate |           2 |
| european     |           2 |
| securitate   |           2 |
| mal          |           1 |
| negru        |           1 |
| întâmpina    |           1 |
| ursula       |           1 |
| von          |           1 |
| der          |           1 |
| leyen        |           1 |
| trăim        |           1 |
| perioadă     |           1 |
| complica     |           1 |
| presiune     |           1 |
| parte        |           1 |
| rusia        |           1 |
| important    |           1 |
| românia      |           1 |
| rămâne       |           1 |
| pilon        |           1 |

### 2025-09-03 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| coposu       |           4 |
| steluță      |           3 |
| doamnă       |           2 |
| semna        |           1 |
| respect      |           1 |
| considerație |           1 |
| decret       |           1 |
| decorare     |           1 |
| post-mortem  |           1 |
| lucia        |           1 |
| rodica       |           1 |
| ordin        |           1 |
| național     |           1 |
| serviciu     |           1 |
| credincios   |           1 |
| grad         |           1 |
| cavaler      |           1 |
| ultim        |           1 |
| descendent   |           1 |
| direct       |           1 |

### 2025-09-03 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| energie    |           5 |
| nuclear    |           4 |
| securitate |           3 |
| energetic  |           3 |
| românia    |           3 |
| investiție |           3 |
| viitor     |           3 |
| important  |           2 |
| cernavodă  |           2 |
| pas        |           2 |
| consolida  |           2 |
| economie   |           2 |
| pilon      |           2 |
| național   |           2 |
| pregăti    |           2 |
| domeniu    |           2 |
| românesc   |           2 |
| însemna    |           2 |
| marca      |           1 |
| moment     |           1 |

### 2025-09-03 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           4 |
| prioritate |           2 |
| agendă     |           2 |
| ucraina    |           2 |
| bucura     |           1 |
| primi      |           1 |
| palat      |           1 |
| cotroceni  |           1 |
| președinte |           1 |
| consiliu   |           1 |
| antnio     |           1 |
| costa      |           1 |
| discuta    |           1 |
| nivel      |           1 |
| lună       |           1 |
| următor    |           1 |
| axa        |           1 |
| securitate |           1 |
| apărare    |           1 |
| precum     |           1 |

### 2025-09-10 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| românia      |           3 |
| american     |           2 |
| strategic    |           2 |
| economic     |           2 |
| investiție   |           2 |
| întâlnire    |           1 |
| important    |           1 |
| reprezentant |           1 |
| investitor   |           1 |
| reitera      |           1 |
| parteneriat  |           1 |
| stat         |           1 |
| unit         |           1 |
| rămâne       |           1 |
| esențial     |           1 |
| întărire     |           1 |
| componentă   |           1 |
| prioritate   |           1 |
| comun        |           1 |
| comunitate   |           1 |

### 2025-09-15 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| ocde        |           4 |
| românia     |           3 |
| aderare     |           3 |
| vrea        |           3 |
| dezvoltat   |           2 |
| țară        |           2 |
| discuție    |           1 |
| excelent    |           1 |
| secretar    |           1 |
| general     |           1 |
| mathias     |           1 |
| cormann     |           1 |
| organizație |           1 |
| reuni       |           1 |
| economie    |           1 |
| consolidat  |           1 |
| democrații  |           1 |
| lume        |           1 |
| totodată    |           1 |
| stabili     |           1 |

### 2025-09-16 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| general      |           3 |
| cercetare    |           2 |
| prezenta     |           2 |
| ultim        |           2 |
| an           |           2 |
| chestiune    |           2 |
| invi         |           2 |
| parchet      |           2 |
| public       |           2 |
| sine         |           2 |
| procuror     |           1 |
| reprezenta   |           1 |
| dovadă       |           1 |
| consistent   |           1 |
| acțiune      |           1 |
| dezinformare |           1 |
| sistematic   |           1 |
| rusia        |           1 |
| românia      |           1 |
| influențăre  |           1 |

### 2025-09-17 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| lege           |           4 |
| proprietate    |           3 |
| stat           |           3 |
| teren          |           3 |
| curte          |           2 |
| constituțional |           2 |
| sesizare       |           2 |
| privind        |           2 |
| prevedea       |           2 |
| transfer       |           2 |
| respecta       |           2 |
| constituție    |           2 |
| exista         |           2 |
| vrea           |           2 |
| interes        |           2 |
| clar           |           2 |
| sine           |           2 |
| oară           |           2 |
| admite         |           1 |
| lună           |           1 |

### 2025-09-23 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| coaliție    |           3 |
| guvernare   |           3 |
| lider       |           2 |
| dialog      |           2 |
| economic    |           2 |
| întâlnire   |           1 |
| palat       |           1 |
| cotroceni   |           1 |
| cadru       |           1 |
| media       |           1 |
| necesar     |           1 |
| constructiv |           1 |
| consolidare |           1 |
| stabilitate |           1 |
| politic     |           1 |
| țară        |           1 |
| sublinia    |           1 |
| importanță  |           1 |
| menținere   |           1 |
| unitate     |           1 |

### 2025-09-24 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| european       |           4 |
| industrie      |           3 |
| apărare        |           2 |
| întâlnire      |           1 |
| bun            |           1 |
| palat          |           1 |
| cotroceni      |           1 |
| reprezentant   |           1 |
| companie       |           1 |
| airbus         |           1 |
| alături        |           1 |
| ambasadorii    |           1 |
| franța         |           1 |
| germania       |           1 |
| spaniei        |           1 |
| bucurești      |           1 |
| discuta        |           1 |
| oportunitățile |           1 |
| colaborare     |           1 |
| domeniu        |           1 |

### 2025-09-24 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| moldova     |           3 |
| legătură    |           2 |
| românia     |           2 |
| republică   |           2 |
| istoric     |           1 |
| viu         |           1 |
| construi    |           1 |
| om          |           1 |
| familie     |           1 |
| valoare     |           1 |
| comun       |           1 |
| alegere     |           1 |
| parlamentar |           1 |
| vrea        |           1 |
| loc         |           1 |
| duminică    |           1 |
| septembrie  |           1 |
| reprezenta  |           1 |
| moment      |           1 |
| crucial     |           1 |

### 2025-09-26 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| spital     |           3 |
| sine       |           3 |
| românia    |           3 |
| infecție   |           3 |
| copil      |           2 |
| viață      |           2 |
| anchetă    |           2 |
| control    |           2 |
| putea      |           2 |
| nosocomial |           2 |
| pune       |           2 |
| sănătate   |           2 |
| profund    |           1 |
| îndurera   |           1 |
| tragedie   |           1 |
| petrece    |           1 |
| copie      |           1 |
| sfântă     |           1 |
| maria      |           1 |
| iași       |           1 |

### 2025-09-28 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| dragi      |           1 |
| basaraban  |           1 |
| românia    |           1 |
| important  |           1 |
| viitor     |           1 |
| republicii |           1 |
| moldova    |           1 |
| încă       |           1 |
| vota       |           1 |
| vot        |           1 |
| conta      |           1 |
| putea      |           1 |
| înclina    |           1 |
| balanță    |           1 |
| parcurs    |           1 |
| democratic |           1 |
| stabil     |           1 |

### 2025-09-29 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| an         |           4 |
| cipru      |           4 |
| alianță    |           3 |
| românilor  |           2 |
| gând       |           2 |
| sine       |           2 |
| îndrepta   |           2 |
| român      |           2 |
| atașament  |           2 |
| românesc   |           2 |
| viu        |           2 |
| românia    |           2 |
| comunitate |           2 |
| ocazie     |           1 |
| împlinire  |           1 |
| înființare |           1 |
| aproape    |           1 |
| trăi       |           1 |
| munci      |           1 |
| construii  |           1 |

### 2025-09-29 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| moldova       |           3 |
| republicii    |           2 |
| felicit       |           1 |
| cetățen       |           1 |
| mobilizare    |           1 |
| vot           |           1 |
| ferm          |           1 |
| direcție      |           1 |
| continuare    |           1 |
| parcurs       |           1 |
| european      |           1 |
| țară          |           1 |
| dumneavoastră |           1 |
| scrie         |           1 |
| pagină        |           1 |
| istorie       |           1 |
| ști           |           1 |
| ușor          |           1 |
| v-            |           1 |
| voce          |           1 |

### 2025-09-30 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| timișoara   |           2 |
| real        |           2 |
| românia     |           2 |
| stat        |           2 |
| vizita      |           1 |
| companie    |           1 |
| folosi      |           1 |
| inteligență |           1 |
| artificial  |           1 |
| concret     |           1 |
| ajuta       |           1 |
| medic       |           1 |
| depista     |           1 |
| cancer      |           1 |
| repede      |           1 |
| celălalt    |           1 |
| dezvolt     |           1 |
| sistem      |           1 |
| inteligent  |           1 |
| analiză     |           1 |

### 2025-09-30 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| administrație |           3 |
| prezidențială |           3 |
| efort         |           3 |
| stat          |           3 |
| reducere      |           2 |
| buget         |           2 |
| gest          |           2 |
| bugetar       |           2 |
| om            |           2 |
| lună          |           1 |
| iulie         |           1 |
| spune         |           1 |
| vrea          |           1 |
| contribui     |           1 |
| austerita     |           1 |
| printru       |           1 |
| real          |           1 |
| propriu       |           1 |
| simbolic      |           1 |
| rectificare   |           1 |

### 2025-09-30 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| european      |           6 |
| oraș          |           2 |
| primar        |           2 |
| cadru         |           2 |
| proces        |           2 |
| stat          |           2 |
| uniune        |           2 |
| motoar        |           1 |
| dezvoltare    |           1 |
| însă          |           1 |
| oară          |           1 |
| primi         |           1 |
| recunoaștere  |           1 |
| resursă       |           1 |
| merita        |           1 |
| resimți       |           1 |
| direct        |           1 |
| dificultate   |           1 |
| perioadă      |           1 |
| bucureștiului |           1 |

### 2025-10-01 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| fiscal    |           4 |
| lege      |           3 |
| efort     |           3 |
| sine      |           3 |
| introduce |           3 |
| măsură    |           2 |
| recent    |           2 |
| bugetar   |           2 |
| impozit   |           2 |
| cere      |           2 |
| venit     |           2 |
| corect    |           2 |
| clar      |           2 |
| trimite   |           1 |
| înapoi    |           1 |
| parlament |           1 |
| anula     |           1 |
| lua       |           1 |
| guvern    |           1 |
| reduce    |           1 |

### 2025-10-01 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           3 |
| copenhaga  |           1 |
| participa  |           1 |
| reuniune   |           1 |
| informal   |           1 |
| consiliu   |           1 |
| summit     |           1 |
| comunitate |           1 |
| politic    |           1 |
| cadru      |           1 |
| vrea       |           1 |
| discuta    |           1 |
| modalitate |           1 |
| concret    |           1 |
| coordona   |           1 |
| consolida  |           1 |
| apărare    |           1 |
| reziliență |           1 |
| precum     |           1 |
| sprijin    |           1 |

### 2025-10-02 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| european      |           2 |
| vizită        |           1 |
| copenhaga     |           1 |
| dedica        |           1 |
| participăr    |           1 |
| summit        |           1 |
| comunitate    |           1 |
| politic       |           1 |
| întru         |           1 |
| perioadă      |           1 |
| securitate    |           1 |
| continent     |           1 |
| pune          |           1 |
| încercare     |           1 |
| trebui        |           1 |
| intensifica   |           1 |
| efort         |           1 |
| național      |           1 |
| cooperare     |           1 |
| internațional |           1 |

### 2025-10-02 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| suedia      |           3 |
| european    |           2 |
| discuție    |           1 |
| productiv   |           1 |
| premier     |           1 |
| ulf         |           1 |
| kristersson |           1 |
| marja       |           1 |
| summit      |           1 |
| comunitate  |           1 |
| politic     |           1 |
| românia     |           1 |
| cooperare   |           1 |
| bilateral   |           1 |
| strânge     |           1 |
| context     |           1 |
| alianță     |           1 |
| concentra   |           1 |
| dezvoltare  |           1 |
| continuare  |           1 |

### 2025-10-02 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| declarație |           1 |
| presă      |           1 |
| susține    |           1 |
| participăr |           1 |
| reuniune   |           1 |
| comunitate |           1 |
| politic    |           1 |
| european   |           1 |

### 2025-10-02 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| european     |           3 |
| public       |           2 |
| le-          |           1 |
| prezenta     |           1 |
| coleg        |           1 |
| principal    |           1 |
| concluzie    |           1 |
| raport       |           1 |
| procurorului |           1 |
| general      |           1 |
| privind      |           1 |
| alegere      |           1 |
| an           |           1 |
| trecut       |           1 |
| accent       |           1 |
| rețea        |           1 |
| social       |           1 |
| folosi       |           1 |
| federație    |           1 |
| rus          |           1 |

### 2025-10-02 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| european    |           3 |
| românia     |           1 |
| sine        |           1 |
| alătura     |           1 |
| inițiativă  |           1 |
| lansa       |           1 |
| președinte  |           1 |
| emmanuel    |           1 |
| macron      |           1 |
| premier     |           1 |
| giorgia     |           1 |
| meloni      |           1 |
| privind     |           1 |
| coaliție    |           1 |
| drogurilor  |           1 |
| urgent      |           1 |
| abordare    |           1 |
| cuprinzător |           1 |
| nivel       |           1 |
| răspunde    |           1 |

### 2025-10-02 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           3 |
| moldova    |           2 |
| sprijin    |           1 |
| republică  |           1 |
| sine       |           1 |
| opri       |           1 |
| discuta    |           1 |
| doamnă     |           1 |
| președinte |           1 |
| maia       |           1 |
| sandu      |           1 |
| partener   |           1 |
| pas        |           1 |
| concreț    |           1 |
| accelerare |           1 |
| proces     |           1 |
| integrare  |           1 |
| loc        |           1 |
| republicii |           1 |
| familie    |           1 |

### 2025-10-03 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| privind      |           3 |
| lege         |           2 |
| activitate   |           2 |
| anre         |           2 |
| asf          |           2 |
| ancom        |           2 |
| funcționa    |           2 |
| public       |           2 |
| întru        |           2 |
| trebui       |           2 |
| reglementare |           2 |
| instituție   |           2 |
| sine         |           2 |
| promulga     |           1 |
| important    |           1 |
| pachet       |           1 |
| reformă      |           1 |
| asuma        |           1 |
| guvern       |           1 |
| act          |           1 |

### 2025-10-06 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| consilier     |          18 |
| începe        |          17 |
| prezidențial  |          13 |
| octombrie     |          11 |
| stat          |           8 |
| noiembrie     |           7 |
| administrație |           4 |
| numire        |           3 |
| onorific      |           3 |
| vrea          |           3 |
| relație       |           3 |
| cadru         |           2 |
| societate     |           2 |
| politică      |           2 |
| român         |           2 |
| pretutinden   |           2 |
| problemă      |           2 |
| diană         |           2 |
| public        |           2 |
| secretariat   |           2 |

### 2025-10-09 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| memorie       |           3 |
| victimă       |           2 |
| românia       |           2 |
| istorie       |           2 |
| om            |           2 |
| sine          |           2 |
| suferi        |           2 |
| etnic         |           2 |
| întru         |           2 |
| tensiune      |           2 |
| social        |           2 |
| discurs       |           2 |
| păstra        |           2 |
| participa     |           1 |
| ceremonie     |           1 |
| dedicat       |           1 |
| comemorare    |           1 |
| holocaustului |           1 |
| eveniment     |           1 |
| tragic        |           1 |

### 2025-10-12 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| an          |           5 |
| sine        |           4 |
| stat        |           3 |
| ușă         |           2 |
| inimă       |           2 |
| cuiva       |           2 |
| trebui      |           2 |
| bun         |           2 |
| limbă       |           2 |
| iad         |           2 |
| rai         |           2 |
| spune       |           2 |
| suflet      |           2 |
| ruga        |           1 |
| năvălim     |           1 |
| ciocăni     |           1 |
| mișca       |           1 |
| dori        |           1 |
| încetinitor |           1 |
| țăran       |           1 |

### 2025-10-13 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| australia        |           3 |
| românia          |           3 |
| sine             |           2 |
| primi            |           1 |
| palat            |           1 |
| cotroceni        |           1 |
| delegație        |           1 |
| conduce          |           1 |
| milton           |           1 |
| dick             |           1 |
| președinte       |           1 |
| cameră           |           1 |
| reprezentanților |           1 |
| actual           |           1 |
| context          |           1 |
| global           |           1 |
| marca            |           1 |
| transformare     |           1 |
| provocare        |           1 |
| esențial         |           1 |

### 2025-10-13 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| electronic   |           3 |
| sine         |           3 |
| legislativ   |           2 |
| monitorizare |           2 |
| persoană     |           2 |
| românia      |           2 |
| respecta     |           2 |
| alertă       |           2 |
| apropiere    |           2 |
| frontieră    |           2 |
| prevedere    |           2 |
| promulga     |           1 |
| lege         |           1 |
| aprobare     |           1 |
| ordonanță    |           1 |
| urgență      |           1 |
| actualiza    |           1 |
| cadru        |           1 |
| domeniu      |           1 |
| inculpa      |           1 |

### 2025-10-14 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| trebui         |           2 |
| fenomen        |           1 |
| corupție       |           1 |
| ataca          |           1 |
| frontal        |           1 |
| flagel         |           1 |
| afecta         |           1 |
| societate      |           1 |
| deveni         |           1 |
| preocupare     |           1 |
| serviciu       |           1 |
| român          |           1 |
| informație     |           1 |
| mecanism       |           1 |
| deplin         |           1 |
| constituțional |           1 |
| defini         |           1 |
| punct          |           1 |
| vedere         |           1 |
| juridic        |           1 |

### 2025-10-16 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| lege          |           3 |
| străin        |           3 |
| ocde          |           3 |
| vrea          |           3 |
| sancționa     |           2 |
| corupere      |           2 |
| funcționar    |           2 |
| economic      |           2 |
| aderare       |           2 |
| românia       |           2 |
| aduce         |           2 |
| sine          |           2 |
| promulga      |           1 |
| publică       |           1 |
| cadru         |           1 |
| operațiune    |           1 |
| internațional |           1 |
| alinia        |           1 |
| standard      |           1 |
| apropia       |           1 |

### 2025-10-17 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| sine             |           3 |
| tragedie         |           2 |
| trebui           |           2 |
| românia          |           2 |
| an               |           2 |
| cetățen          |           2 |
| neglijență       |           2 |
| responsabilitate |           2 |
| instituție       |           2 |
| moarte           |           2 |
| putea            |           2 |
| aștepta          |           2 |
| explozie         |           1 |
| produce          |           1 |
| întru            |           1 |
| bloc             |           1 |
| cale             |           1 |
| rahova           |           1 |
| bucurești        |           1 |
| cutremurător     |           1 |

### 2025-10-20 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |           4 |
| european    |           3 |
| comisar     |           2 |
| brunner     |           2 |
| țară        |           2 |
| securitate  |           2 |
| regiune     |           2 |
| sine        |           2 |
| uniune      |           2 |
| acționa     |           2 |
| schengen    |           2 |
| palat       |           1 |
| cotroceni   |           1 |
| dialog      |           1 |
| constructiv |           1 |
| afacere     |           1 |
| intern      |           1 |
| migrație    |           1 |
| magnus      |           1 |
| vizită      |           1 |

### 2025-10-20 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| pensie      |           4 |
| magistrațe  |           3 |
| reformă     |           2 |
| decizie     |           2 |
| vrea        |           2 |
| rămâne      |           1 |
| prioritate  |           1 |
| poziționare |           1 |
| corectare   |           1 |
| prevedere   |           1 |
| anormal     |           1 |
| egal        |           1 |
| salariu     |           1 |
| clasă       |           1 |
| politic     |           1 |
| reglementa  |           1 |
| defectuos   |           1 |
| an          |           1 |
| partid      |           1 |
| coaliție    |           1 |

### 2025-10-21 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| față        |           3 |
| înalt       |           2 |
| trebui      |           2 |
| sine        |           2 |
| semna       |           1 |
| decret      |           1 |
| trecere     |           1 |
| rezervă     |           1 |
| doamnă      |           1 |
| general     |           1 |
| florentina  |           1 |
| ioniță      |           1 |
| armat       |           1 |
| puternic    |           1 |
| însemna     |           1 |
| dotare      |           1 |
| modern      |           1 |
| capacitate  |           1 |
| tehnic      |           1 |
| integritate |           1 |

### 2025-10-22 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| pacient      |           5 |
| medical      |           5 |
| vrea         |           4 |
| sistem       |           3 |
| lege         |           2 |
| grad         |           2 |
| personal     |           2 |
| unitate      |           2 |
| destinat     |           2 |
| promulga     |           1 |
| aduce        |           1 |
| reglementare |           1 |
| domeniu      |           1 |
| sănătate     |           1 |
| crește       |           1 |
| protecție    |           1 |
| deopotrivă   |           1 |
| sanitar      |           1 |
| public       |           1 |
| privat       |           1 |

### 2025-10-22 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| drum      |           1 |
| bruxelles |           1 |
| reuniune  |           1 |
| consiliu  |           1 |
| european  |           1 |

### 2025-10-23 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| lege       |           6 |
| vrea       |           5 |
| public     |           3 |
| promulga   |           2 |
| reformă    |           2 |
| domeniu    |           2 |
| pachet     |           2 |
| guvern     |           2 |
| medic      |           2 |
| serviciu   |           2 |
| săptămână  |           1 |
| permite    |           1 |
| consistent |           1 |
| sănătate   |           1 |
| proiect    |           1 |
| parte      |           1 |
| sine       |           1 |
| angaja     |           1 |
| răspundere |           1 |
| parlament  |           1 |

### 2025-10-23 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| securitate       |           2 |
| proiect          |           2 |
| apărare          |           2 |
| temă             |           2 |
| important        |           2 |
| acces            |           2 |
| locuință         |           2 |
| extrem           |           1 |
| încărca          |           1 |
| reuniune         |           1 |
| lider            |           1 |
| uniuneaeuropeană |           1 |
| bruxelles        |           1 |
| discutăm         |           1 |
| europa           |           1 |
| domeniu          |           1 |
| zid              |           1 |
| dronă            |           1 |
| sancțiune        |           1 |
| rusia            |           1 |

### 2025-10-24 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| universitate |           4 |
| an           |           3 |
| național     |           3 |
| educație     |           3 |
| românia      |           3 |
| decizie      |           3 |
| tradiție     |           2 |
| universitar  |           2 |
| iași         |           2 |
| alexandru    |           2 |
| ioan         |           2 |
| cuza         |           2 |
| arte         |           2 |
| george       |           2 |
| enescu       |           2 |
| cultură      |           2 |
| cunoaștere   |           2 |
| trebui       |           2 |
| academic     |           2 |
| iașul        |           2 |

### 2025-10-24 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| românesc    |           3 |
| antibiotic  |           2 |
| iași        |           2 |
| farmaceutic |           2 |
| producție   |           2 |
| simbol      |           1 |
| industrie   |           1 |
| lider       |           1 |
| mondial     |           1 |
| nistatină   |           1 |
| demonstra   |           1 |
| an          |           1 |
| tradiție    |           1 |
| muncă       |           1 |
| viziune     |           1 |
| putea       |           1 |
| transforma  |           1 |
| brand       |           1 |
| întru       |           1 |
| reper       |           1 |

### 2025-10-25 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |           4 |
| apăra       |           2 |
| pace        |           2 |
| armată      |           2 |
| an          |           2 |
| onora       |           1 |
| brigada     |           1 |
| mecanizată  |           1 |
| podu        |           1 |
| înalt       |           1 |
| iași        |           1 |
| curaj       |           1 |
| sacrificiu  |           1 |
| suficient   |           1 |
| dori        |           1 |
| trebui      |           1 |
| pregăti     |           1 |
| modernizare |           1 |
| rămâne      |           1 |
| prioritate  |           1 |

### 2025-10-25 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| proiect     |           3 |
| avansat     |           3 |
| artificial  |           2 |
| complet     |           2 |
| implantabil |           2 |
| dezvolta    |           2 |
| cercetător  |           2 |
| student     |           2 |
| sine        |           2 |
| afla        |           2 |
| vrea        |           2 |
| românia     |           2 |
| mic         |           1 |
| inimă       |           1 |
| aplicație   |           1 |
| atât        |           1 |
| adult       |           1 |
| copil       |           1 |
| grup        |           1 |
| ieșan       |           1 |

### 2025-10-26 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| participa   |           1 |
| alături     |           1 |
| familie     |           1 |
| sfințire    |           1 |
| pictură     |           1 |
| catedrală   |           1 |
| național    |           1 |
| construcție |           1 |
| născut      |           1 |
| vis         |           1 |
| credință    |           1 |
| român       |           1 |
| aminti      |           1 |
| important   |           1 |
| răbdare     |           1 |
| încredere   |           1 |
| speranță    |           1 |
| clădi       |           1 |
| împreună    |           1 |

### 2025-10-26 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| sfințire  |           1 |
| pictură   |           1 |
| catedrală |           1 |
| național  |           1 |

### 2025-10-28 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| vrea           |           5 |
| românia        |           3 |
| reformă        |           3 |
| asigura        |           3 |
| sine           |           3 |
| comisar        |           2 |
| european       |           2 |
| economie       |           2 |
| deficit        |           2 |
| redresa        |           2 |
| reduce         |           2 |
| discuție       |           1 |
| constructiv    |           1 |
| valdis         |           1 |
| dombrovskis    |           1 |
| productivitate |           1 |
| implementare   |           1 |
| simplificare   |           1 |
| discuta        |           1 |
| special        |           1 |

### 2025-10-28 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| domn         |           3 |
| rus          |           3 |
| război       |           2 |
| an           |           2 |
| profund      |           1 |
| respect      |           1 |
| semn         |           1 |
| recunoaștere |           1 |
| devotament   |           1 |
| curaj        |           1 |
| contribuție  |           1 |
| apărare      |           1 |
| țară         |           1 |
| semna        |           1 |
| decret       |           1 |
| privind      |           1 |
| acordare     |           1 |
| grad         |           1 |
| general      |           1 |
| brigadă      |           1 |

### 2025-10-29 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| românia        |           4 |
| vrea           |           4 |
| american       |           3 |
| continua       |           3 |
| forță          |           2 |
| prezență       |           2 |
| flanc          |           2 |
| estic          |           2 |
| echipament     |           2 |
| militar        |           2 |
| deplin         |           2 |
| strategic      |           2 |
| redimensionare |           1 |
| rotațional     |           1 |
| operă          |           1 |
| trupă          |           1 |
| reveni         |           1 |
| fapt           |           1 |
| nivel          |           1 |
| război         |           1 |

### 2025-10-30 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| sine           |          10 |
| rămâne         |           5 |
| an             |           4 |
| tragedie       |           3 |
| românia        |           3 |
| putea          |           3 |
| oglindă        |           3 |
| viață          |           2 |
| încă           |           2 |
| acțiune        |           2 |
| deveni         |           2 |
| lua            |           2 |
| supraviețuitor |           2 |
| om             |           2 |
| stat           |           2 |
| același        |           2 |
| grav           |           2 |
| reformă        |           2 |
| împlini        |           1 |
| schimba        |           1 |

### 2025-11-04 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| român       |           2 |
| sine        |           2 |
| familie     |           2 |
| afla        |           1 |
| profundă    |           1 |
| tristețe    |           1 |
| veste       |           1 |
| prinde      |           1 |
| dărâmăture  |           1 |
| turn        |           1 |
| medieval    |           1 |
| roma        |           1 |
| stinge      |           1 |
| azi-noapte  |           1 |
| spital      |           1 |
| transmit    |           1 |
| condoleanță |           1 |
| apropiat    |           1 |
| gândurile   |           1 |
| îndrepta    |           1 |

### 2025-11-05 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| românia                         |           6 |
| northatlantictreatyorganization |           6 |
| apărare                         |           4 |
| rutte                           |           3 |
| secretar                        |           3 |
| general                         |           3 |
| țară                            |           3 |
| securitate                      |           3 |
| vrea                            |           3 |
| i-                              |           2 |
| domn                            |           2 |
| mark                            |           2 |
| context                         |           2 |
| industrie                       |           2 |
| transmite                       |           2 |
| zonă                            |           2 |
| spațiu                          |           2 |
| euroatlantic                    |           2 |
| vorbi                           |           2 |
| estic                           |           2 |

### 2025-11-05 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| emeric    |           5 |
| ienei     |           5 |
| fotbal    |           3 |
| sport     |           2 |
| generație |           2 |
| echipă    |           2 |
| românia   |           2 |
| mulțumim  |           1 |
| bucurie   |           1 |
| aduce     |           1 |
| atât      |           1 |
| oară      |           1 |
| mândru    |           1 |
| românesc  |           1 |
| pierde    |           1 |
| figură    |           1 |
| legendar  |           1 |
| însă      |           1 |
| memorie   |           1 |
| vrea      |           1 |

### 2025-11-06 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| apărare                         |           5 |
| industrie                       |           4 |
| aliat                           |           3 |
| românia                         |           2 |
| apăra                           |           2 |
| pregăti                         |           2 |
| sine                            |           2 |
| asuma                           |           2 |
| puternic                        |           2 |
| estic                           |           2 |
| securitate                      |           2 |
| northatlantictreatyorganization |           2 |
| rusia                           |           2 |
| angaja                          |           2 |
| militar                         |           2 |
| consolida                       |           2 |
| precum                          |           2 |
| exista                          |           2 |
| neagră                          |           2 |
| rol                             |           1 |

### 2025-11-07 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| stat            |           5 |
| economic        |           3 |
| mediu           |           3 |
| trebui          |           3 |
| românia         |           2 |
| dezvoltare      |           2 |
| moment          |           2 |
| politică        |           2 |
| piață           |           2 |
| competitivitate |           1 |
| creștere        |           1 |
| cuvânt          |           1 |
| cheie           |           1 |
| temă            |           1 |
| discuta         |           1 |
| cadru           |           1 |
| eveniment       |           1 |
| dialog          |           1 |
| summit          |           1 |
| inteligent      |           1 |

### 2025-11-07 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| ghyka        |           3 |
| public       |           3 |
| grigore      |           2 |
| alexandru    |           2 |
| pământesc    |           2 |
| acces        |           2 |
| dreptate     |           2 |
| societate    |           2 |
| nume         |           2 |
| sine         |           2 |
| român        |           2 |
| domnitor     |           2 |
| semn         |           1 |
| profund      |           1 |
| respect      |           1 |
| considerație |           1 |
| memorie      |           1 |
| ultim        |           1 |
| domn         |           1 |
| moldova      |           1 |

### 2025-11-09 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| ghyka     |           4 |
| istorie   |           4 |
| domnitor  |           3 |
| moldova   |           3 |
| românia   |           3 |
| modern    |           3 |
| unire     |           2 |
| grigore   |           2 |
| alexandru |           2 |
| începe    |           2 |
| încă      |           2 |
| moment    |           2 |
| trebui    |           2 |
| aminti    |           2 |
| limbă     |           2 |
| veni      |           2 |
| aboli     |           2 |
| sprijini  |           2 |
| pune      |           2 |
| om        |           2 |

### 2025-11-10 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| mediu          |           6 |
| european       |           4 |
| lege           |           3 |
| evaluare       |           3 |
| românia        |           3 |
| energetic      |           3 |
| sesizare       |           2 |
| constituțional |           2 |
| ariilor        |           2 |
| natural        |           2 |
| protejat       |           2 |
| impact         |           2 |
| obligație      |           2 |
| stat           |           2 |
| uniune         |           2 |
| permite        |           2 |
| proiect        |           2 |
| sănătos        |           2 |
| garanta        |           2 |
| protecție      |           2 |

### 2025-11-10 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           4 |
| apărare    |           4 |
| industrie  |           3 |
| producție  |           2 |
| privind    |           2 |
| industrial |           2 |
| germania   |           2 |
| dezvolta   |           2 |
| economie   |           2 |
| vrea       |           2 |
| tip        |           2 |
| deveni     |           1 |
| hub        |           1 |
| inovație   |           1 |
| domeniu    |           1 |
| europa     |           1 |
| sud-est    |           1 |
| mesaj      |           1 |
| transmite  |           1 |
| cadru      |           1 |

### 2025-11-11 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| corneliu   |           4 |
| coposu     |           4 |
| politic    |           3 |
| democrație |           3 |
| om         |           2 |
| păstra     |           2 |
| seniorului |           2 |
| libertate  |           2 |
| istorie    |           2 |
| rămâne     |           2 |
| exemplu    |           2 |
| putea      |           2 |
| față       |           2 |
| urmă       |           1 |
| deceniu    |           1 |
| trece      |           1 |
| veșnic     |           1 |
| semn       |           1 |
| omagiu     |           1 |
| depune     |           1 |

### 2025-11-12 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| apărare         |           6 |
| strategie       |           5 |
| sine            |           5 |
| național        |           4 |
| societate       |           3 |
| administrație   |           3 |
| public          |           3 |
| vrea            |           3 |
| românia         |           3 |
| corupție        |           3 |
| dezbatere       |           2 |
| corectare       |           2 |
| inclusiv        |           2 |
| economic        |           2 |
| parte           |           2 |
| acțiune         |           2 |
| sens            |           2 |
| social          |           2 |
| principal       |           2 |
| vulnerabilitate |           2 |

### 2025-11-13 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| militar                         |           8 |
| northatlantictreatyorganization |           6 |
| nivel                           |           5 |
| aliat                           |           4 |
| sine                            |           3 |
| exercițiu                       |           3 |
| securitate                      |           3 |
| românia                         |           3 |
| efort                           |           3 |
| important                       |           2 |
| stat                            |           2 |
| franța                          |           2 |
| politic                         |           2 |
| război                          |           2 |
| descurajare                     |           2 |
| apărare                         |           2 |
| flanc                           |           2 |
| estic                           |           2 |
| împreună                        |           2 |
| capacitate                      |           2 |

### 2025-11-13 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| republicii |           3 |
| moldova    |           3 |
| integrare  |           2 |
| european   |           2 |
| primi      |           1 |
| palat      |           1 |
| cotroceni  |           1 |
| vizită     |           1 |
| extern     |           1 |
| preluare   |           1 |
| mandat     |           1 |
| prim       |           1 |
| ministru   |           1 |
| alexandru  |           1 |
| munteanu   |           1 |
| românia    |           1 |
| rămâne     |           1 |
| sincer     |           1 |
| ferm       |           1 |
| susținător |           1 |

### 2025-11-17 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           4 |
| letta      |           3 |
| viitor     |           3 |
| românia    |           3 |
| raport     |           2 |
| pieței     |           2 |
| putea      |           2 |
| dezvoltare |           2 |
| sine       |           2 |
| domn       |           2 |
| discuta    |           2 |
| industrie  |           2 |
| primi      |           1 |
| palat      |           1 |
| cotroceni  |           1 |
| enrico     |           1 |
| premier    |           1 |
| italia     |           1 |
| autor      |           1 |
| much       |           1 |

### 2025-11-18 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| energie       |           5 |
| românia       |           4 |
| putea         |           4 |
| organizație   |           3 |
| aderare       |           3 |
| european      |           3 |
| birol         |           2 |
| agenție       |           2 |
| internațional |           2 |
| cooperare     |           2 |
| dezvoltare    |           2 |
| economic      |           2 |
| ocde          |           2 |
| parte         |           2 |
| lume          |           2 |
| discuta       |           2 |
| energetic     |           2 |
| global        |           2 |
| investiție    |           2 |
| necesar       |           2 |

### 2025-11-18 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| bloc        |           3 |
| ne-         |           1 |
| părăsi      |           1 |
| dumitru     |           1 |
| lupescu     |           1 |
| președinte  |           1 |
| asociație   |           1 |
| începe      |           1 |
| construcție |           1 |
| parc        |           1 |
| tineret     |           1 |
| față        |           1 |
| curaj       |           1 |
| sine        |           1 |
| lupta       |           1 |
| instanță    |           1 |
| cunoaște    |           1 |
| membru      |           1 |
| fondator    |           1 |
| usb         |           1 |

### 2025-11-18 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| ilie          |           3 |
| ilașcu        |           3 |
| libertate     |           2 |
| erou          |           2 |
| sine          |           2 |
| luăm          |           1 |
| rămas-bun     |           1 |
| patriot       |           1 |
| crede         |           1 |
| acționa       |           1 |
| niciun        |           1 |
| ezitare       |           1 |
| vis           |           1 |
| unire         |           1 |
| exemplu       |           1 |
| verticalitate |           1 |
| curaj         |           1 |
| aminti        |           1 |
| luptă         |           1 |
| identitate    |           1 |

### 2025-11-19 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| boală          |           4 |
| lege           |           3 |
| viață          |           3 |
| sesiza         |           2 |
| constituțional |           2 |
| exista         |           2 |
| privat         |           2 |
| trebui         |           2 |
| curte          |           1 |
| legătură       |           1 |
| aprobare       |           1 |
| ordonanță      |           1 |
| urgență        |           1 |
| introduce      |           1 |
| registru       |           1 |
| unic           |           1 |
| electronic     |           1 |
| transmisibile  |           1 |
| prevedea       |           1 |
| păstrare       |           1 |

### 2025-11-20 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| potra          |           2 |
| operațiune     |           1 |
| readucere      |           1 |
| țară           |           1 |
| escortă        |           1 |
| horațiu        |           1 |
| dorian         |           1 |
| alexandru      |           1 |
| confirma       |           1 |
| angajament     |           1 |
| ferm           |           1 |
| stat           |           1 |
| român          |           1 |
| ordine         |           1 |
| constituțional |           1 |
| sine           |           1 |
| apăra          |           1 |
| suspecta       |           1 |
| acțiune        |           1 |
| ajunge         |           1 |

### 2025-11-20 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| ocde         |           5 |
| integritate  |           5 |
| public       |           4 |
| românia      |           3 |
| aderare      |           3 |
| lege         |           3 |
| funcție      |           3 |
| stat         |           3 |
| perioadă     |           3 |
| putea        |           3 |
| pas          |           2 |
| regulă       |           2 |
| instituție   |           2 |
| lună         |           2 |
| atribuție    |           2 |
| sine         |           2 |
| transparență |           2 |
| legislativ   |           2 |
| standard     |           2 |
| aproape      |           2 |

### 2025-11-21 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| uniune           |           5 |
| uniuneaeuropeană |           5 |
| cadru            |           5 |
| european         |           4 |
| coeziune         |           4 |
| important        |           3 |
| necesitate       |           3 |
| sublinia         |           3 |
| convergență      |           3 |
| creștere         |           3 |
| eficient         |           3 |
| obiectiv         |           3 |
| competitivitate  |           3 |
| executiv         |           2 |
| fitto            |           2 |
| stimula          |           2 |
| consolidare      |           2 |
| viitor           |           2 |
| buget            |           2 |
| evidenția        |           2 |

### 2025-11-21 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           4 |
| economie   |           3 |
| securitate |           3 |
| țară       |           3 |
| românia    |           2 |
| uniune     |           2 |
| zonă       |           2 |
| dezvoltat  |           2 |
| trebui     |           2 |
| sine       |           2 |
| moment     |           1 |
| maturitate |           1 |
| expertiza  |           1 |
| adevărat   |           1 |
| parte      |           1 |
| proces     |           1 |
| decizie    |           1 |
| strategie  |           1 |
| direcție   |           1 |
| an         |           1 |

### 2025-11-23 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| lege           |           2 |
| promulga       |           1 |
| săptămână      |           1 |
| introduce      |           1 |
| amendare       |           1 |
| comerciant     |           1 |
| sumă           |           1 |
| cuprinde       |           1 |
| leu            |           1 |
| nerespectare   |           1 |
| obligație      |           1 |
| înlocui        |           1 |
| produs         |           1 |
| achiziționat   |           1 |
| fizic          |           1 |
| online         |           1 |
| cumpărător     |           1 |
| constata       |           1 |
| neconformitate |           1 |
| termen         |           1 |

### 2025-11-25 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| stat         |           3 |
| digitalizare |           2 |
| instrument   |           2 |
| permite      |           2 |
| deveni       |           2 |
| anumit       |           2 |
| vrea         |           2 |
| românia      |           2 |
| putea        |           2 |
| sine         |           2 |
| cibernetic   |           2 |
| încredere    |           2 |
| onoare       |           1 |
| găzduii      |           1 |
| palat        |           1 |
| cotroceni    |           1 |
| summit       |           1 |
| guvernanță   |           1 |
| digital      |           1 |
| acorda       |           1 |

### 2025-11-26 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| strategie    |           3 |
| național     |           3 |
| cetățean     |           3 |
| stat         |           3 |
| român        |           3 |
| vrea         |           3 |
| apărare      |           2 |
| țară         |           2 |
| document     |           2 |
| instituție   |           2 |
| apăra        |           2 |
| independență |           2 |
| lume         |           2 |
| identitate   |           2 |
| față         |           2 |
| parlament    |           1 |
| românia      |           1 |
| vota         |           1 |
| prezenta     |           1 |
| plen         |           1 |

### 2025-12-01 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| an       |           5 |
| românia  |           3 |
| prilej   |           2 |
| război   |           2 |
| ion      |           2 |
| vasile   |           2 |
| banu     |           2 |
| militar  |           2 |
| țară     |           2 |
| conferi  |           2 |
| gest     |           2 |
| viață    |           2 |
| zilei    |           1 |
| național |           1 |
| decora   |           1 |
| veteran  |           1 |
| colonel  |           1 |
| ordin    |           1 |
| virtute  |           1 |
| grad     |           1 |

### 2025-12-01 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| român      |           5 |
| trăi       |           2 |
| afla       |           2 |
| românia    |           2 |
| țară       |           2 |
| național   |           1 |
| sărbătoare |           1 |
| om         |           1 |
| arc        |           1 |
| triumf     |           1 |
| impresiona |           1 |
| bucurie    |           1 |
| număr      |           1 |
| atât       |           1 |
| veni       |           1 |
| împreună   |           1 |
| emoție     |           1 |
| paradă     |           1 |
| privire    |           1 |
| vedea      |           1 |

### 2025-12-02 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| lege           |           5 |
| parlamentar    |           3 |
| pas            |           2 |
| proces         |           2 |
| legislativ     |           2 |
| ocde           |           2 |
| românia        |           2 |
| registru       |           2 |
| ruti           |           2 |
| public         |           2 |
| reprezentant   |           2 |
| prevedere      |           2 |
| întâlnirilor   |           2 |
| terț           |           2 |
| oră            |           2 |
| constituțional |           2 |
| promulga       |           1 |
| recent         |           1 |
| modificare     |           1 |
| statutului     |           1 |

### 2025-12-03 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| european         |           4 |
| uniuneaeuropeană |           3 |
| românia          |           3 |
| substanțial      |           2 |
| consolidare      |           2 |
| apărare          |           2 |
| actual           |           2 |
| importanță       |           2 |
| necesitate       |           2 |
| continua         |           2 |
| consiliu         |           2 |
| discuție         |           1 |
| ambasadorii      |           1 |
| stat             |           1 |
| membră           |           1 |
| bucurești        |           1 |
| reafirma         |           1 |
| angajament       |           1 |
| ferm             |           1 |
| parcurs          |           1 |

### 2025-12-03 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| trebui      |           4 |
| stat        |           3 |
| sine        |           3 |
| situație    |           2 |
| paltinu     |           2 |
| putea       |           2 |
| obligatoriu |           2 |
| vrea        |           2 |
| dezastruos  |           1 |
| barajul     |           1 |
| genera      |           1 |
| criză       |           1 |
| proporție   |           1 |
| om          |           1 |
| județ       |           1 |
| prahova     |           1 |
| dâmbovița   |           1 |
| arăta       |           1 |
| grav        |           1 |
| deveni      |           1 |

### 2025-12-04 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| domn        |           4 |
| rebengiuc   |           4 |
| românia     |           3 |
| european    |           3 |
| important   |           3 |
| sine        |           3 |
| asociație   |           2 |
| dori        |           2 |
| față        |           2 |
| onoare      |           1 |
| felicit     |           1 |
| victor      |           1 |
| cadru       |           1 |
| ceremonie   |           1 |
| decernare   |           1 |
| premiu      |           1 |
| oferi       |           1 |
| inițiativă  |           1 |
| cultură     |           1 |
| democratică |           1 |

### 2025-12-04 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| lege        |           4 |
| putea       |           3 |
| extremism   |           2 |
| stat        |           2 |
| datorie     |           2 |
| clar        |           2 |
| material    |           2 |
| transmite   |           1 |
| parlament   |           1 |
| cerere      |           1 |
| reexaminare |           1 |
| modifica    |           1 |
| oug         |           1 |
| privind     |           1 |
| combatere   |           1 |
| român       |           1 |
| acționa     |           1 |
| ferm        |           1 |
| ură         |           1 |
| xenofobie   |           1 |

### 2025-12-05 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| lege          |           4 |
| locuință      |           3 |
| sine          |           3 |
| regulă        |           2 |
| construcție   |           2 |
| imobiliar     |           2 |
| vrea          |           2 |
| putea         |           2 |
| viitor        |           2 |
| maximum       |           2 |
| scop          |           2 |
| semna         |           1 |
| decret        |           1 |
| promulgare    |           1 |
| introduce     |           1 |
| clar          |           1 |
| strict        |           1 |
| domeniu       |           1 |
| tranzacțiilor |           1 |
| proteja       |           1 |

### 2025-12-07 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| vot         |           2 |
| dragi       |           1 |
| bucureștean |           1 |
| invi        |           1 |
| merge       |           1 |
| indiferent  |           1 |
| opțiune     |           1 |
| proces      |           1 |
| democratic  |           1 |
| important   |           1 |
| primar      |           1 |
| alege       |           1 |
| număr       |           1 |
| legitim     |           1 |
| decizie     |           1 |
| lua         |           1 |
| cunosc      |           1 |
| bucurești   |           1 |
| vota        |           1 |
| sigur       |           1 |

### 2025-12-08 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| felicitări       |           2 |
| succes           |           2 |
| vot              |           2 |
| cetățean         |           2 |
| oraș             |           2 |
| complex          |           2 |
| primar           |           2 |
| general          |           2 |
| responsabilitate |           2 |
| aleș             |           1 |
| local            |           1 |
| confirma         |           1 |
| regulă           |           1 |
| bază             |           1 |
| democrație       |           1 |
| întotdeauna      |           1 |
| dreptate         |           1 |
| opinie           |           1 |
| exprima          |           1 |
| ciprian          |           1 |

### 2025-12-09 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| franța      |           4 |
| românia     |           3 |
| președinte  |           2 |
| francez     |           2 |
| macron      |           2 |
| militar     |           2 |
| rol         |           2 |
| real        |           1 |
| plăcere     |           1 |
| întâlni     |           1 |
| republicii  |           1 |
| emmanuel    |           1 |
| reafirma    |           1 |
| prietenie   |           1 |
| profund     |           1 |
| lega        |           1 |
| angajament  |           1 |
| comun       |           1 |
| consolida   |           1 |
| parteneriat |           1 |

### 2025-12-09 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           4 |
| apărare    |           3 |
| tehnologie |           3 |
| franța     |           2 |
| domeniu    |           2 |
| emergent   |           2 |
| vrea       |           2 |
| dori       |           2 |
| producție  |           2 |
| companie   |           2 |
| investiție |           2 |
| securitate |           2 |
| colaborare |           2 |
| industrie  |           2 |
| solid      |           2 |
| putea      |           2 |
| europa     |           2 |
| thales     |           2 |
| tehnologiu |           2 |
| întâlnire  |           1 |

### 2025-12-09 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| paris          |           4 |
| cooperare      |           3 |
| numeros        |           2 |
| româno-francez |           2 |
| economie       |           2 |
| educație       |           2 |
| românesc       |           2 |
| capitală       |           2 |
| franța         |           2 |
| legătură       |           2 |
| dezvoltare     |           2 |
| român          |           2 |
| important      |           2 |
| nicolae        |           2 |
| titulescu      |           2 |
| loc            |           2 |
| agresiune      |           2 |
| excelent       |           1 |
| întrevedere    |           1 |
| primar         |           1 |

### 2025-12-10 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| justiție  |          10 |
| problemă  |           7 |
| sine      |           5 |
| sistem    |           5 |
| trebui    |           5 |
| fapt      |           4 |
| interior  |           4 |
| rând      |           3 |
| politic   |           3 |
| vorbi     |           3 |
| vedea     |           2 |
| recorder  |           2 |
| încă      |           2 |
| aduce     |           2 |
| public    |           2 |
| vrea      |           2 |
| probă     |           2 |
| raport    |           2 |
| vorbim    |           2 |
| magistrat |           2 |

### 2025-12-11 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| decembrie   |           3 |
| problemă    |           2 |
| sistem      |           2 |
| justiție    |           2 |
| vrea        |           2 |
| oră         |           2 |
| adresă      |           2 |
| trimite     |           2 |
| material    |           2 |
| nominal     |           2 |
| magistrat   |           1 |
| spune       |           1 |
| integritate |           1 |
| lucru       |           1 |
| serios      |           1 |
| invit       |           1 |
| magistrație |           1 |
| reclama     |           1 |
| discuție    |           1 |
| limită      |           1 |

### 2025-12-15 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| stat        |           4 |
| justiție    |           2 |
| interior    |           2 |
| sine        |           2 |
| plec        |           1 |
| summit      |           1 |
| helsinki    |           1 |
| lua         |           1 |
| îngrijorăre |           1 |
| societate   |           1 |
| lega        |           1 |
| funcționare |           1 |
| împărtăși   |           1 |
| problemă    |           1 |
| semnala     |           1 |
| spațiu      |           1 |
| public      |           1 |
| grav        |           1 |
| rezolvare   |           1 |
| limită      |           1 |

### 2025-12-16 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| securitate                      |           4 |
| regiune                         |           2 |
| estic                           |           2 |
| european                        |           2 |
| apărare                         |           2 |
| uniuneaeuropeană                |           2 |
| northatlantictreatyorganization |           2 |
| republică                       |           2 |
| moldova                         |           2 |
| acțiune                         |           1 |
| rusia                           |           1 |
| reprezenta                      |           1 |
| amenințare                      |           1 |
| majoră                          |           1 |
| reuniune                        |           1 |
| helsinki                        |           1 |
| evidenția                       |           1 |
| rol                             |           1 |
| central                         |           1 |
| flancului                       |           1 |

### 2025-12-16 — facebook-post

| cuvânt                |   frecvență |
|:----------------------|------------:|
| sportiv               |           6 |
| lege                  |           4 |
| european              |           4 |
| național              |           2 |
| formare               |           2 |
| constituție           |           2 |
| românia               |           2 |
| cetățenie             |           2 |
| trimite               |           1 |
| curte                 |           1 |
| constituțional        |           1 |
| sesizare              |           1 |
| neconstituționalitate |           1 |
| impune                |           1 |
| minimum               |           1 |
| evolua                |           1 |
| întru                 |           1 |
| echipă                |           1 |
| competițiă            |           1 |
| oficial               |           1 |

### 2025-12-16 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| industrie   |           4 |
| finlandez   |           3 |
| apărare     |           3 |
| discuție    |           2 |
| organizație |           2 |
| cercetare   |           2 |
| european    |           2 |
| proiect     |           2 |
| oferi       |           2 |
| comun       |           2 |
| relevant    |           2 |
| companie    |           2 |
| cooperare   |           2 |
| vrea        |           2 |
| util        |           1 |
| aplicat     |           1 |
| purta       |           1 |
| prestigiu   |           1 |
| domeniu     |           1 |
| vizita      |           1 |

### 2025-12-17 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           3 |
| economic   |           2 |
| afacere    |           2 |
| român      |           2 |
| regat      |           2 |
| unit       |           2 |
| mediu      |           2 |
| susținere  |           2 |
| dezvoltare |           2 |
| inovare    |           2 |
| britanic   |           2 |
| comercial  |           2 |
| încuraja   |           2 |
| continuare |           2 |
| țară       |           2 |
| londra     |           1 |
| întru      |           1 |
| competitiv |           1 |
| ecosistemă |           1 |
| lume       |           1 |

### 2025-12-17 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| majestății |           1 |
| rege       |           1 |
| charles    |           1 |
| -lea       |           1 |
| primire    |           1 |
| palat      |           1 |
| buckingham |           1 |

### 2025-12-17 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| întâlnire    |           1 |
| extraordinar |           1 |
| bun          |           1 |
| cald         |           1 |
| comunitate   |           1 |
| român        |           1 |
| regat        |           1 |
| unit         |           1 |
| marii        |           1 |
| britania     |           1 |
| irlandei     |           1 |
| nord         |           1 |
| diasporă     |           1 |
| românesc     |           1 |
| resursă      |           1 |
| neprețuit    |           1 |
| păstra       |           1 |
| identitate   |           1 |
| viu          |           1 |
| duce         |           1 |

### 2025-12-18 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| european  |           3 |
| uniune    |           3 |
| an        |           2 |
| important |           2 |
| discuție  |           2 |
| buget     |           2 |
| vrea      |           2 |
| politică  |           2 |
| începe    |           1 |
| ultim     |           1 |
| reuniune  |           1 |
| consiliu  |           1 |
| moment    |           1 |
| definire  |           1 |
| direcție  |           1 |
| strategic |           1 |
| perioadă  |           1 |
| următor   |           1 |
| românia   |           1 |
| subiect   |           1 |

### 2025-12-18 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| dialog      |           1 |
| antreprenor |           1 |
| român       |           1 |
| britanică   |           1 |
| întâlnire   |           1 |
| om          |           1 |
| comunitate  |           1 |
| românesc    |           1 |
| moment      |           1 |
| deosebit    |           1 |
| alături     |           1 |
| majestate   |           1 |
| rege        |           1 |
| charles     |           1 |
| -lea        |           1 |
| scurt       |           1 |
| vizită      |           1 |
| londra      |           1 |
| construim   |           1 |
| punt        |           1 |

### 2025-12-19 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| european         |           2 |
| încheia          |           1 |
| turneu           |           1 |
| ultim            |           1 |
| consiliu         |           1 |
| an               |           1 |
| discuta          |           1 |
| temă             |           1 |
| esențial         |           1 |
| viitor           |           1 |
| uniune           |           1 |
| românia          |           1 |
| buget            |           1 |
| competitivitate  |           1 |
| economic         |           1 |
| extindere        |           1 |
| uniuneaeuropeană |           1 |
| sprijin          |           1 |
| ucraina          |           1 |

### 2025-12-20 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           5 |
| discuție   |           3 |
| magistrat  |           2 |
| final      |           2 |
| lună       |           2 |
| primi      |           1 |
| pagină     |           1 |
| material   |           1 |
| relevant   |           1 |
| problemă   |           1 |
| justiție   |           1 |
| promite    |           1 |
| parcurge   |           1 |
| weekend    |           1 |
| reveni     |           1 |
| concluzie  |           1 |
| sine       |           1 |
| înscrie    |           1 |
| audiență   |           1 |
| consultăre |           1 |

### 2025-12-20 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| constituțional |           3 |
| curte          |           2 |
| lege           |           2 |
| decide         |           1 |
| recent         |           1 |
| schimbare      |           1 |
| esențial       |           1 |
| președinte     |           1 |
| românia        |           1 |
| sine           |           1 |
| recâștiga      |           1 |
| sesiza         |           1 |
| ccr            |           1 |
| privire        |           1 |
| motiv          |           1 |
| inclusiv       |           1 |
| fond           |           1 |
| reexamina      |           1 |
| parlament      |           1 |
| revenire       |           1 |

### 2025-12-21 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| sine      |           6 |
| libertate |           4 |
| revoluție |           4 |
| decembrie |           3 |
| românia   |           3 |
| comunism  |           3 |
| uman      |           3 |
| strigăt   |           2 |
| român     |           2 |
| trăi      |           2 |
| izolare   |           2 |
| frică     |           2 |
| trebui    |           2 |
| demnitate |           2 |
| ști       |           2 |
| putea     |           2 |
| curaj     |           2 |
| regim     |           2 |
| construi  |           2 |
| viață     |           2 |

### 2025-12-21 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| interes       |           7 |
| acționa       |           4 |
| public        |           4 |
| magistrat     |           4 |
| vrea          |           4 |
| consiliu      |           3 |
| superior      |           3 |
| grup          |           3 |
| sine          |           3 |
| imediat       |           2 |
| sistem        |           2 |
| spune         |           2 |
| magistraturii |           2 |
| legislativ    |           2 |
| majoritate    |           2 |
| csm           |           2 |
| chestiune     |           2 |
| justiție      |           2 |
| conducere     |           2 |
| instanțelor   |           2 |

### 2025-12-25 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| crăciun    |           2 |
| aproape    |           2 |
| viață      |           2 |
| naștere    |           1 |
| hristos    |           1 |
| creștin    |           1 |
| sărbătoare |           1 |
| speranță   |           1 |
| lumină     |           1 |
| adevăr     |           1 |
| credință   |           1 |
| afla       |           1 |
| aminti     |           1 |
| acasă      |           1 |
| magie      |           1 |
| copilărie  |           1 |
| readuce    |           1 |
| esență     |           1 |
| valoare    |           1 |
| sens       |           1 |

### 2025-12-26 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| românia       |           3 |
| lume          |           3 |
| om            |           2 |
| tenis         |           2 |
| virginia      |           2 |
| ruzici        |           2 |
| sportiv       |           2 |
| turneu        |           2 |
| cadru         |           1 |
| vizitelor     |           1 |
| extern        |           1 |
| ultim         |           1 |
| săptămână     |           1 |
| bucurie       |           1 |
| reîntâlnire   |           1 |
| special       |           1 |
| drag          |           1 |
| personalitate |           1 |
| aduce         |           1 |
| contribuție   |           1 |

### 2025-12-26 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| corneliu         |           2 |
| porumboiu        |           2 |
| nume             |           2 |
| româniîndiaspora |           2 |
| întâlnire        |           1 |
| special          |           1 |
| paris            |           1 |
| regizor          |           1 |
| scenarist        |           1 |
| marcă            |           1 |
| cinematografie   |           1 |
| contemporan      |           1 |
| public           |           1 |
| asociază         |           1 |
| polițist         |           1 |
| adjectiv         |           1 |
| film             |           1 |
| rămâne           |           1 |
| reper            |           1 |
| memorie          |           1 |

### 2025-12-27 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| aștept   |           1 |
| nerbdare |           1 |
| afla     |           1 |
| spune    |           1 |
| mirabela |           1 |
| emisiune |           1 |
| vrea     |           1 |
| difuzat  |           1 |
| oră      |           1 |
| digi     |           1 |

### 2025-12-27 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| profesor      |           2 |
| martin        |           2 |
| andler        |           2 |
| prilej        |           2 |
| revedea       |           1 |
| emoție        |           1 |
| paris         |           1 |
| emeri         |           1 |
| universitate  |           1 |
| versailles    |           1 |
| saint-quentin |           1 |
| domn          |           1 |
| matematician  |           1 |
| juriu         |           1 |
| concurs       |           1 |
| selecționa    |           1 |
| cole          |           1 |
| normale       |           1 |
| suprieure     |           1 |
| reaminti      |           1 |

### 2025-12-27 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| rațiu      |           3 |
| nicolae    |           2 |
| român      |           2 |
| ion        |           1 |
| revedea    |           1 |
| londra     |           1 |
| familie    |           1 |
| mijloc     |           1 |
| comunitate |           1 |
| reper      |           1 |
| implicare  |           1 |
| civic      |           1 |
| susținere  |           1 |
| parcurs    |           1 |
| democratic |           1 |
| țară       |           1 |
| fundație   |           1 |
| conduce    |           1 |
| sprijin    |           1 |
| deceniu    |           1 |

### 2025-12-28 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| george      |           2 |
| iacobescu   |           2 |
| veritabil   |           1 |
| plăcere     |           1 |
| revăd       |           1 |
| londra      |           1 |
| sir         |           1 |
| respectat   |           1 |
| apreciat    |           1 |
| român       |           1 |
| britanie    |           1 |
| profesie    |           1 |
| inginer     |           1 |
| constructor |           1 |
| nume        |           1 |
| sine        |           1 |
| lega        |           1 |
| dezvoltare  |           1 |
| celebr      |           1 |
| centru      |           1 |

### 2025-12-28 — facebook-post

| cuvânt                         |   frecvență |
|:-------------------------------|------------:|
| britishbroadcastingcorporation |           2 |
| christian                      |           2 |
| mititelu                       |           2 |
| redacție                       |           1 |
| român                          |           1 |
| rămâne                         |           1 |
| reper                          |           1 |
| jurnalism                      |           1 |
| înalt                          |           1 |
| standard                       |           1 |
| felicita                       |           1 |
| performanță                    |           1 |
| jurnalist                      |           1 |
| conduce                        |           1 |
| românia                        |           1 |
| cadru                          |           1 |
| întâlnire                      |           1 |
| comunitate                     |           1 |
| românesc                       |           1 |
| londra                         |           1 |

### 2026-01-01 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| an          |           7 |
| viitor      |           3 |
| încredere   |           2 |
| adevărat    |           2 |
| împreună    |           2 |
| provocăre   |           1 |
| curaj       |           1 |
| renunța     |           1 |
| față        |           1 |
| încercăre   |           1 |
| greu        |           1 |
| pas         |           1 |
| cere        |           1 |
| determinare |           1 |
| răbdar      |           1 |
| întru       |           1 |
| bun         |           1 |
| campanie    |           1 |
| complex     |           1 |
| vizită      |           1 |

### 2026-01-04 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| spera         |           1 |
| ultim         |           1 |
| clipă         |           1 |
| întru         |           1 |
| deznodământ   |           1 |
| diferit       |           1 |
| însă          |           1 |
| afla          |           1 |
| profundă      |           1 |
| tristețe      |           1 |
| pierdere      |           1 |
| tânăr         |           1 |
| român         |           1 |
| incendiu      |           1 |
| crans-montana |           1 |
| transmit      |           1 |
| sincere       |           1 |
| condoleanță   |           1 |
| familie       |           1 |
| îndoliat      |           1 |

### 2026-01-05 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| cheltuielile  |           1 |
| administrație |           1 |
| prezidențial  |           1 |
| reduce        |           1 |
| adică         |           1 |
| milion        |           1 |
| leu           |           1 |
| decât         |           1 |
| angaja        |           1 |
| iulie         |           1 |

### 2026-01-06 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| începe   |           1 |
| reuniune |           1 |
| lider    |           1 |
| stat     |           1 |
| guverne  |           1 |
| palat    |           1 |
| lyse     |           1 |

### 2026-01-06 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| plăcere    |           1 |
| reîntâlni  |           1 |
| președinte |           1 |
| emmanuel   |           1 |
| macron     |           1 |
| deschidere |           1 |
| reuniuni   |           1 |
| stat       |           1 |
| membră     |           1 |
| coaliție   |           1 |
| voință     |           1 |

### 2026-01-07 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| ajunge        |           1 |
| bucurești     |           1 |
| parcurs       |           1 |
| zbor          |           1 |
| spațiu        |           1 |
| aerian        |           1 |
| elveția       |           1 |
| aeronavă      |           1 |
| escorta       |           1 |
| avion         |           1 |
| f-            |           1 |
| gest          |           1 |
| apreciere     |           1 |
| sprijin       |           1 |
| acorda        |           1 |
| transport     |           1 |
| internațional |           1 |
| victimă       |           1 |
| incendi       |           1 |
| crans-montana |           1 |

### 2026-01-08 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| român        |           3 |
| aeronavă     |           2 |
| gest         |           2 |
| reprezenta   |           2 |
| stat         |           2 |
| respecta     |           2 |
| putea        |           1 |
| asculta      |           1 |
| înregistrare |           1 |
| convorbire   |           1 |
| pilot        |           1 |
| spartan      |           1 |
| controlor    |           1 |
| trafic       |           1 |
| zrich        |           1 |
| comunica     |           1 |
| decizie      |           1 |
| escortare    |           1 |
| românesc     |           1 |
| semn         |           1 |

### 2026-01-09 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| vrea             |           9 |
| românia          |           8 |
| european         |           8 |
| uniuneaeuropeană |           7 |
| produs           |           6 |
| vamal            |           6 |
| sector           |           5 |
| putea            |           5 |
| mercosur         |           4 |
| agricol          |           4 |
| important        |           4 |
| taxă             |           4 |
| importa          |           4 |
| comercial        |           3 |
| oportunitate     |           3 |
| produce          |           3 |
| stat             |           2 |
| negocia          |           2 |
| suplimentar      |           2 |
| producător       |           2 |

### 2026-01-13 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| sine        |           5 |
| program     |           5 |
| românia     |           3 |
| flex        |           3 |
| educație    |           3 |
| liceen      |           3 |
| american    |           3 |
| strategic   |           2 |
| stat        |           2 |
| unit        |           2 |
| perspectivă |           2 |
| bun         |           2 |
| lume        |           2 |
| succes      |           2 |
| român       |           2 |
| vrea        |           2 |
| dorință     |           2 |
| tinerilor   |           2 |
| parteneriat |           1 |
| america     |           1 |

### 2026-01-15 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |          11 |
| românia    |           7 |
| sine       |           5 |
| politică   |           4 |
| securitate |           4 |
| extern     |           3 |
| măsură     |           3 |
| urmări     |           3 |
| național   |           3 |
| putea      |           3 |
| uniune     |           3 |
| european   |           3 |
| șef        |           2 |
| misiune    |           2 |
| diplomatic |           2 |
| acredita   |           2 |
| lucru      |           2 |
| an         |           2 |
| prioritate |           2 |
| rămâne     |           2 |

### 2026-01-15 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| cultură     |           8 |
| sine        |           3 |
| an          |           3 |
| spațiu      |           2 |
| viitor      |           2 |
| contemporan |           2 |
| cultural    |           2 |
| pune        |           2 |
| valoare     |           2 |
| deschide    |           2 |
| tânăr       |           2 |
| dedica      |           2 |
| creator     |           2 |
| român       |           2 |
| vrea        |           2 |
| sală        |           2 |
| teatru      |           2 |
| cotroceni   |           2 |
| național    |           1 |
| reaminti    |           1 |

### 2026-01-16 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| românia          |           3 |
| investiție       |           3 |
| securitate       |           3 |
| european         |           2 |
| instrument       |           2 |
| safe             |           2 |
| vrea             |           2 |
| bun              |           2 |
| proiect          |           2 |
| esențial         |           2 |
| uniuneaeuropeană |           2 |
| reprezenta       |           2 |
| contribui        |           2 |
| actual           |           2 |
| sine             |           2 |
| decizie          |           1 |
| comisie          |           1 |
| aproba           |           1 |
| aplicație        |           1 |
| finanțare        |           1 |

### 2026-01-17 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| local            |           5 |
| public           |           5 |
| lege             |           2 |
| permite          |           2 |
| sistem           |           2 |
| putea            |           2 |
| vrea             |           2 |
| promulga         |           1 |
| polițișt         |           1 |
| utiliza          |           1 |
| cameră           |           1 |
| foto-video-audio |           1 |
| portabil         |           1 |
| exercitare       |           1 |
| atribuție        |           1 |
| serviciu         |           1 |
| reglementare     |           1 |
| stabili          |           1 |
| clar             |           1 |
| situație         |           1 |

### 2026-01-17 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| medical      |           3 |
| periodic     |           3 |
| acces        |           2 |
| hpv          |           2 |
| serviciu     |           2 |
| gratuit      |           2 |
| testare      |           2 |
| cancer       |           2 |
| tip          |           2 |
| viață        |           2 |
| femeie       |           2 |
| control      |           2 |
| sănătate     |           2 |
| promulga     |           1 |
| lege         |           1 |
| adoptare     |           1 |
| ordonanță    |           1 |
| guvern       |           1 |
| asigura      |           1 |
| continuitate |           1 |

### 2026-01-19 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| românia                         |           6 |
| general                         |           4 |
| grynkewich                      |           4 |
| neagră                          |           3 |
| inclusiv                        |           3 |
| forță                           |           2 |
| saceur                          |           2 |
| comandament                     |           2 |
| sine                            |           2 |
| dialog                          |           2 |
| strategic                       |           2 |
| pace                            |           2 |
| spațiu                          |           2 |
| aerian                          |           2 |
| obiectiv                        |           2 |
| northatlantictreatyorganization |           2 |
| primi                           |           1 |
| palat                           |           1 |
| cotroceni                       |           1 |
| alexus                          |           1 |

### 2026-01-23 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| stat          |           6 |
| european      |           5 |
| uniune        |           3 |
| relație       |           2 |
| transatlantic |           2 |
| importanță    |           2 |
| membră        |           2 |
| inclusiv      |           2 |
| românia       |           2 |
| discuție      |           2 |
| informal      |           2 |
| consiliu      |           2 |
| unit          |           2 |
| esențial      |           2 |
| securitate    |           2 |
| abordare      |           2 |
| exista        |           2 |
| continuare    |           2 |
| zonă          |           2 |
| pace          |           2 |

### 2026-01-24 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| unire      |           5 |
| românia    |           5 |
| român      |           4 |
| trebui     |           4 |
| viitor     |           4 |
| întru      |           4 |
| sine       |           4 |
| moment     |           3 |
| prezent    |           3 |
| construi   |           3 |
| marca      |           2 |
| om         |           2 |
| față       |           2 |
| act        |           2 |
| interes    |           2 |
| națiune    |           2 |
| societate  |           2 |
| însemna    |           2 |
| putea      |           2 |
| capacitate |           2 |

### 2026-01-24 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| elev       |           5 |
| valoare    |           3 |
| societate  |           3 |
| esențial   |           2 |
| profesor   |           2 |
| formare    |           2 |
| sine       |           2 |
| întru      |           2 |
| crede      |           2 |
| împlinire  |           1 |
| an         |           1 |
| înființare |           1 |
| acorda     |           1 |
| colegi     |           1 |
| național   |           1 |
| unire      |           1 |
| focșani    |           1 |
| ordin      |           1 |
| merit      |           1 |
| învțmânt   |           1 |

### 2026-01-24 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| moment           |           4 |
| patriotism       |           4 |
| an               |           3 |
| însemna          |           3 |
| față             |           3 |
| sărbătoare       |           2 |
| trebui           |           2 |
| om               |           2 |
| ideal            |           2 |
| responsabilitate |           2 |
| pas              |           2 |
| românia          |           2 |
| trăim            |           1 |
| complicat        |           1 |
| întru            |           1 |
| crede            |           1 |
| bucura           |           1 |
| reflecta         |           1 |
| religios         |           1 |
| miracol          |           1 |

### 2026-01-26 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| holocaustului |           3 |
| memorie       |           3 |
| întru         |           3 |
| sine          |           3 |
| comemorare    |           2 |
| tragedie      |           2 |
| istorie       |           2 |
| alături       |           2 |
| victimă       |           2 |
| deveni        |           2 |
| lume          |           2 |
| formă         |           2 |
| adevăr        |           2 |
| internațional |           1 |
| victimelor    |           1 |
| dedica        |           1 |
| reflecție     |           1 |
| umanitate     |           1 |
| regim         |           1 |
| nazist        |           1 |

### 2026-02-04 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| european        |           8 |
| energie         |           4 |
| consiliu        |           3 |
| românia         |           3 |
| antonio         |           2 |
| costa           |           2 |
| președinte      |           2 |
| cadru           |           2 |
| creștere        |           2 |
| competitivitate |           2 |
| stat            |           2 |
| rând            |           2 |
| susținem        |           2 |
| uniune          |           2 |
| consolidare     |           2 |
| sine            |           2 |
| convorbire      |           1 |
| consistent      |           1 |
| privind         |           1 |
| temă            |           1 |

### 2026-02-04 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| românia   |           5 |
| raport    |           5 |
| sine      |           4 |
| electoral |           4 |
| singur    |           3 |
| platformă |           3 |
| tiktok    |           3 |
| decizie   |           3 |
| campanie  |           3 |
| european  |           3 |
| referire  |           2 |
| document  |           2 |
| țară      |           2 |
| strict    |           2 |
| amplu     |           2 |
| libertate |           2 |
| exprimare |           2 |
| alegere   |           2 |
| juridic   |           2 |
| cont      |           2 |

### 2026-02-05 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| sine                            |           3 |
| militar                         |           2 |
| smârdan                         |           2 |
| american                        |           2 |
| stat                            |           2 |
| unit                            |           2 |
| northatlantictreatyorganization |           2 |
| exercițiil                      |           1 |
| desfășura                       |           1 |
| ultim                           |           1 |
| forță                           |           1 |
| românesc                        |           1 |
| antrena                         |           1 |
| alături                         |           1 |
| arăta                           |           1 |
| parteneriat                     |           1 |
| strategic                       |           1 |
| românia                         |           1 |
| america                         |           1 |
| puternic                        |           1 |

### 2026-02-08 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| consiliu                |           4 |
| pace                    |           4 |
| românia                 |           4 |
| invitație               |           2 |
| vrea                    |           2 |
| februarie               |           2 |
| stat                    |           2 |
| primi                   |           1 |
| participa               |           1 |
| reuniune                |           1 |
| loc                     |           1 |
| washington              |           1 |
| spune                   |           1 |
| saluta                  |           1 |
| efort                   |           1 |
| administrație           |           1 |
| stateleunitealeamericii |           1 |
| promovare               |           1 |
| primire                 |           1 |
| alătura                 |           1 |

### 2026-02-11 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| american    |           5 |
| românia     |           3 |
| sine        |           3 |
| țară        |           2 |
| exista      |           2 |
| economic    |           2 |
| discuție    |           1 |
| lider       |           1 |
| companie    |           1 |
| reuni       |           1 |
| umbrelă     |           1 |
| cameră      |           1 |
| comerț      |           1 |
| amcham      |           1 |
| mesaj       |           1 |
| companiilor |           1 |
| dori        |           1 |
| investi     |           1 |
| continuare  |           1 |
| premi       |           1 |

### 2026-02-12 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| sine         |           5 |
| energie      |           5 |
| vrea         |           4 |
| european     |           3 |
| competitiv   |           3 |
| companie     |           3 |
| putea        |           2 |
| piață        |           2 |
| trebui       |           2 |
| reglementare |           2 |
| europa       |           2 |
| românia      |           2 |
| țară         |           2 |
| dezvoltat    |           2 |
| important    |           1 |
| dezbatere    |           1 |
| particip     |           1 |
| belgia       |           1 |
| alături      |           1 |
| celălalt     |           1 |

### 2026-02-13 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| economie      |           4 |
| românia       |           3 |
| politic       |           3 |
| echilibru     |           2 |
| sine          |           2 |
| reduce        |           2 |
| consum        |           2 |
| diminuare     |           2 |
| economic      |           2 |
| deficit       |           2 |
| privat        |           2 |
| vrea          |           2 |
| genera        |           2 |
| dezvoltare    |           2 |
| structural    |           2 |
| problemă      |           2 |
| dumneavoastră |           2 |
| același       |           2 |
| invi          |           1 |
| privi         |           1 |

### 2026-02-15 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| participa  |           2 |
| consiliu   |           2 |
| unit       |           2 |
| america    |           2 |
| românia    |           2 |
| vrea       |           2 |
| sprijin    |           2 |
| proces     |           2 |
| fâșie      |           2 |
| gaza       |           2 |
| sptmână    |           1 |
| viitor     |           1 |
| reuniune   |           1 |
| pcii       |           1 |
| washington |           1 |
| rspunza    |           1 |
| invitație  |           1 |
| președinte |           1 |
| statelor   |           1 |
| donald     |           1 |

### 2026-02-18 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| pensie         |           2 |
| salut          |           1 |
| decizie        |           1 |
| curte          |           1 |
| constituțional |           1 |
| privind        |           1 |
| reformă        |           1 |
| magistrațe     |           1 |
| recalibrare    |           1 |
| calcul         |           1 |
| gest           |           1 |
| echitate       |           1 |
| aștepta        |           1 |
| societate      |           1 |
| asigur         |           1 |
| magistrație    |           1 |
| muncă          |           1 |
| respecta       |           1 |
| importanță     |           1 |
| arhitectură    |           1 |

### 2026-02-19 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| putea                   |           8 |
| contribui               |           4 |
| rând                    |           4 |
| pace                    |           3 |
| românia                 |           3 |
| oferi                   |           3 |
| intervenție             |           2 |
| consiliu                |           2 |
| stat                    |           2 |
| stateleunitealeamericii |           2 |
| internațional           |           2 |
| situație                |           2 |
| gaza                    |           2 |
| copil                   |           2 |
| sistem                  |           2 |
| precum                  |           2 |
| reconstrucție           |           2 |
| palestinian             |           2 |
| relație                 |           2 |
| tradițional             |           2 |

### 2026-02-20 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| pace        |           2 |
| securitate  |           2 |
| washington  |           2 |
| românia     |           2 |
| sine        |           2 |
| temelie     |           1 |
| țară        |           1 |
| prosper     |           1 |
| politică    |           1 |
| extern      |           1 |
| important   |           1 |
| partener    |           1 |
| diferit     |           1 |
| format      |           1 |
| ales        |           1 |
| materie     |           1 |
| consolida   |           1 |
| aprofundăme |           1 |
| parteneriat |           1 |
| stat        |           1 |

### 2026-02-24 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| premier    |           2 |
| bolojan    |           2 |
| bruxelles  |           2 |
| vrea       |           2 |
| european   |           2 |
| economic   |           2 |
| românia    |           2 |
| țară       |           2 |
| discuție   |           1 |
| aplicat    |           1 |
| ilie       |           1 |
| vizită     |           1 |
| joi        |           1 |
| sine       |           1 |
| semna      |           1 |
| declarație |           1 |
| privind    |           1 |
| lansare    |           1 |
| mecanism   |           1 |
| eastinvest |           1 |

### 2026-02-24 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| ucraina    |           5 |
| vrea       |           3 |
| pace       |           3 |
| an         |           2 |
| europa     |           2 |
| deveni     |           2 |
| rusia      |           2 |
| război     |           2 |
| sine       |           2 |
| securitate |           2 |
| ucrainean  |           2 |
| uniune     |           2 |
| european   |           2 |
| trebui     |           2 |
| urmă       |           1 |
| teribile   |           1 |
| scenarii   |           1 |
| realitate  |           1 |
| ataca      |           1 |
| declanșa   |           1 |

### 2026-02-27 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| pensie         |           2 |
| aștepta        |           2 |
| societate      |           2 |
| stat           |           2 |
| sine           |           2 |
| promulga       |           1 |
| dimineață      |           1 |
| lege           |           1 |
| privind        |           1 |
| magistrață     |           1 |
| urmă           |           1 |
| publicare      |           1 |
| monitor        |           1 |
| oficial        |           1 |
| decizie        |           1 |
| curte          |           1 |
| constituțional |           1 |
| recalibrare    |           1 |
| calcul         |           1 |
| gest           |           1 |

### 2026-02-27 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |           4 |
| plângere   |           3 |
| penal      |           3 |
| campanie   |           3 |
| vedea      |           3 |
| aep        |           2 |
| știre      |           2 |
| instituție |           2 |
| același    |           2 |
| anula      |           2 |
| instanță   |           2 |
| întâmpla   |           2 |
| funcționar |           2 |
| referitor  |           1 |
| informație |           1 |
| privind    |           1 |
| legătură   |           1 |
| electoral  |           1 |
| preluare   |           1 |
| aprilie    |           1 |

### 2026-03-01 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| sine       |           4 |
| afla       |           3 |
| securitate |           3 |
| român      |           3 |
| rămâne     |           3 |
| românia    |           2 |
| siguranță  |           2 |
| mijlociu   |           2 |
| stat       |           2 |
| extern     |           2 |
| zonă       |           2 |
| deplin     |           1 |
| niciun     |           1 |
| amenințare |           1 |
| direct     |           1 |
| actual     |           1 |
| context    |           1 |
| regional   |           1 |
| orientul   |           1 |
| degrada    |           1 |

### 2026-03-03 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| nirenberg   |           2 |
| ambasador   |           2 |
| stat        |           2 |
| bun         |           2 |
| bucura      |           1 |
| primi       |           1 |
| palat       |           1 |
| cotroceni   |           1 |
| darryl      |           1 |
| unit        |           1 |
| america     |           1 |
| românia     |           1 |
| prim        |           1 |
| dialog      |           1 |
| putea       |           1 |
| parteneriat |           1 |
| strategic   |           1 |
| deveni      |           1 |
| puternic    |           1 |
| convinge    |           1 |

### 2026-03-05 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| premier     |           2 |
| polonez     |           2 |
| donald      |           2 |
| tusk        |           2 |
| securitate  |           2 |
| viitor      |           2 |
| proiect     |           2 |
| european    |           2 |
| dezvoltare  |           2 |
| domeniu     |           2 |
| dialog      |           1 |
| substanțial |           1 |
| subiect     |           1 |
| vital       |           1 |
| românia     |           1 |
| polonia     |           1 |
| important   |           1 |
| coordonăm   |           1 |
| precum      |           1 |
| consolidare |           1 |

### 2026-03-05 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| polonia                         |           5 |
| românia                         |           3 |
| important                       |           3 |
| securitate                      |           3 |
| președinte                      |           2 |
| nawrocki                        |           2 |
| context                         |           2 |
| legătură                        |           2 |
| dezvolta                        |           2 |
| parteneriat                     |           2 |
| comun                           |           2 |
| țară                            |           2 |
| economic                        |           2 |
| perspectivă                     |           2 |
| european                        |           2 |
| sine                            |           2 |
| northatlantictreatyorganization |           2 |
| răspunde                        |           1 |
| plăcere                         |           1 |
| invitație                       |           1 |

### 2026-03-06 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| polonia       |           2 |
| martie        |           1 |
| ocazie        |           1 |
| zilei         |           1 |
| solidarității |           1 |
| româno-polon  |           1 |
| sărbătorita   |           1 |
| săptămână     |           1 |
| efectua       |           1 |
| vizită        |           1 |
| oficial       |           1 |
| întâlni       |           1 |
| președinte    |           1 |
| karol         |           1 |
| nawrocki      |           1 |
| premier       |           1 |
| donald        |           1 |
| tusk          |           1 |
| șef           |           1 |
| cameră        |           1 |

### 2026-03-08 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| ctre          |           4 |
| femeie        |           3 |
| sine          |           3 |
| continua      |           2 |
| an            |           1 |
| doamnelor     |           1 |
| domnișoarelor |           1 |
| internațional |           1 |
| femeii        |           1 |
| mulțumi       |           1 |
| familie       |           1 |
| dumneavoastră |           1 |
| comunitate    |           1 |
| des           |           1 |
| uitm          |           1 |
| datorm        |           1 |
| puternic      |           1 |
| curajos       |           1 |
| pcat          |           1 |
| îns           |           1 |

### 2026-03-09 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| european        |           8 |
| competitivitate |           4 |
| costa           |           3 |
| cadru           |           3 |
| românia         |           3 |
| energie         |           3 |
| asigura         |           3 |
| antonio         |           2 |
| președinte      |           2 |
| temă            |           2 |
| vrea            |           2 |
| sine            |           2 |
| piață           |           2 |
| tranziție       |           2 |
| verde           |           2 |
| buget           |           2 |
| uniune          |           2 |
| dori            |           2 |
| perspectivă     |           2 |
| trebui          |           2 |

### 2026-03-09 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| putea         |           3 |
| sine          |           3 |
| curaj         |           2 |
| regim         |           2 |
| demnitate     |           2 |
| rămâne        |           2 |
| liber         |           2 |
| libertate     |           2 |
| păstra        |           2 |
| deținuților   |           1 |
| politic       |           1 |
| anticomuniști |           1 |
| marca         |           1 |
| an            |           1 |
| martie        |           1 |
| aminti        |           1 |
| înfrunta      |           1 |
| abuzure       |           1 |
| comunist      |           1 |
| transforma    |           1 |

### 2026-03-10 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| european        |           6 |
| preț            |           3 |
| lider           |           2 |
| energie         |           2 |
| competitivitate |           2 |
| industrie       |           2 |
| reduce          |           2 |
| trebui          |           2 |
| sector          |           2 |
| energetic       |           2 |
| sine            |           2 |
| seară           |           1 |
| dialog          |           1 |
| aplica          |           1 |
| cadru           |           1 |
| reuniuni        |           1 |
| videoconferință |           1 |
| grup            |           1 |
| stat            |           1 |
| prieten         |           1 |

### 2026-03-11 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| românia                 |           6 |
| echipament              |           5 |
| situație                |           2 |
| orientul                |           2 |
| mijlociu                |           2 |
| război                  |           2 |
| român                   |           2 |
| țară                    |           2 |
| om                      |           2 |
| stat                    |           2 |
| forță                   |           2 |
| militar                 |           2 |
| vrea                    |           2 |
| exista                  |           2 |
| stateleunitealeamericii |           2 |
| convoca                 |           1 |
| ședință                 |           1 |
| csat                    |           1 |
| analiză                 |           1 |
| evoluție                |           1 |

### 2026-03-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           4 |
| vrea       |           4 |
| energetic  |           3 |
| deveni     |           3 |
| proiect    |           2 |
| producție  |           2 |
| apărare    |           2 |
| securitate |           2 |
| ucraina    |           2 |
| semna      |           1 |
| președinte |           1 |
| zelenski   |           1 |
| document   |           1 |
| oficial    |           1 |
| pune       |           1 |
| bază       |           1 |
| dezvoltare |           1 |
| major      |           1 |
| reciproc   |           1 |
| avantajos  |           1 |

### 2026-03-12 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| ucraina     |           6 |
| românia     |           5 |
| sine        |           4 |
| relație     |           3 |
| român       |           3 |
| i-          |           2 |
| luptă       |           2 |
| duce        |           2 |
| neîncredere |           2 |
| țară        |           2 |
| război      |           2 |
| asuma       |           2 |
| încredere   |           2 |
| putea       |           2 |
| continua    |           2 |
| minorităție |           2 |
| limbă       |           2 |
| reafirma    |           2 |
| susținere   |           2 |
| uniune      |           2 |

### 2026-03-16 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| românia     |           3 |
| organizație |           3 |
| țară        |           3 |
| ocde        |           3 |
| dezvoltare  |           2 |
| economic    |           2 |
| reformă     |           2 |
| membru      |           2 |
| secretar    |           2 |
| general     |           2 |
| cormann     |           2 |
| studiu      |           2 |
| economie    |           2 |
| elaborare   |           2 |
| politică    |           2 |
| aderare     |           1 |
| cooperare   |           1 |
| obiectiv    |           1 |
| strategic   |           1 |
| asuma       |           1 |

### 2026-03-16 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| vrea        |           6 |
| energetic   |           4 |
| românia     |           4 |
| omv         |           3 |
| petrom      |           3 |
| discuta     |           2 |
| proiect     |           2 |
| neptun      |           2 |
| deep        |           2 |
| gaz         |           2 |
| investiție  |           2 |
| securitate  |           2 |
| situație    |           2 |
| termen      |           2 |
| scurt       |           2 |
| mediu       |           2 |
| preț        |           2 |
| combustibil |           2 |
| major       |           2 |
| alfred      |           1 |

### 2026-03-17 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| sânge      |           5 |
| putea      |           5 |
| donare     |           3 |
| medical    |           2 |
| transfuzie |           2 |
| sine       |           2 |
| centru     |           2 |
| salva      |           1 |
| viață      |           1 |
| împreună   |           1 |
| gest       |           1 |
| simplu     |           1 |
| acțiune    |           1 |
| ușor       |           1 |
| realiza    |           1 |
| diferență  |           1 |
| seman      |           1 |
| trece      |           1 |
| experiență |           1 |
| traume     |           1 |

### 2026-03-19 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| declarații |           1 |
| presă      |           1 |
| susține    |           1 |
| bruxelles  |           1 |
| regat      |           1 |
| belgia     |           1 |

### 2026-03-19 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| românia                         |           4 |
| northatlantictreatyorganization |           4 |
| mark                            |           3 |
| rutte                           |           3 |
| vrea                            |           3 |
| an                              |           3 |
| sine                            |           3 |
| american                        |           2 |
| întâlnire                       |           2 |
| secretar                        |           2 |
| general                         |           2 |
| dialog                          |           2 |
| țară                            |           2 |
| discuta                         |           2 |
| summit                          |           2 |
| sprijin                         |           2 |
| echipament                      |           2 |
| apăra                           |           1 |
| parte                           |           1 |
| parteneriat                     |           1 |

### 2026-03-20 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| internațional |           3 |
| românia       |           2 |
| sine          |           2 |
| decide        |           1 |
| alătura       |           1 |
| declarație    |           1 |
| regat         |           1 |
| unit          |           1 |
| franța        |           1 |
| germania      |           1 |
| italia        |           1 |
| olanda        |           1 |
| japonia       |           1 |
| privind       |           1 |
| asigurare     |           1 |
| strâmtoare    |           1 |
| ormuz         |           1 |
| libertții     |           1 |
| navigație     |           1 |
| principiu     |           1 |

### 2026-03-20 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| onoare     |           1 |
| bucurie    |           1 |
| întâlni    |           1 |
| bruxelles  |           1 |
| majestate  |           1 |
| rege       |           1 |
| philippe   |           1 |
| împreună   |           1 |
| discuție   |           1 |
| bun        |           1 |
| apropia    |           1 |
| viziune    |           1 |
| comun      |           1 |
| dezvolta   |           1 |
| relație    |           1 |
| românia    |           1 |
| belgia     |           1 |
| i-         |           1 |
| mulțumi    |           1 |
| majestății |           1 |

### 2026-03-21 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           7 |
| expoziție  |           5 |
| brâncuși   |           5 |
| cultural   |           5 |
| român      |           4 |
| muzeu      |           4 |
| constantin |           3 |
| an         |           3 |
| berlin     |           3 |
| artă       |           3 |
| europa     |           2 |
| președinte |           2 |
| germania   |           2 |
| patronaj   |           2 |
| eveniment  |           2 |
| valoare    |           2 |
| parte      |           2 |
| institut   |           2 |
| lucrare    |           2 |
| european   |           2 |

### 2026-03-22 — facebook-post

| cuvânt            |   frecvență |
|:------------------|------------:|
| stat              |           4 |
| român             |           2 |
| reformă           |           2 |
| companiilor       |           2 |
| serviciu          |           2 |
| public            |           2 |
| trebui            |           2 |
| putea             |           2 |
| puternic          |           2 |
| trecut            |           1 |
| bruxelles         |           1 |
| discuție          |           1 |
| oana              |           1 |
| gheorghiu         |           1 |
| viceprim-ministru |           1 |
| digitalizare      |           1 |
| conveni           |           1 |
| an                |           1 |
| crucial           |           1 |
| finalizare        |           1 |

### 2026-03-23 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| internațional |           4 |
| francofonie   |           4 |
| țară          |           3 |
| francofonia   |           2 |
| promova       |           2 |
| parte         |           2 |
| românia       |           2 |
| zilei         |           2 |
| dacian        |           2 |
| cioloș        |           2 |
| funcție       |           2 |
| nivel         |           2 |
| an            |           2 |
| francofon     |           2 |
| valoare       |           1 |
| identitate    |           1 |
| istoric       |           1 |
| limbă         |           1 |
| francez       |           1 |
| rezonanță     |           1 |

### 2026-03-26 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| sine          |           4 |
| informațional |           3 |
| medical       |           3 |
| românia       |           3 |
| spune         |           3 |
| om            |           3 |
| război        |           2 |
| afecta        |           2 |
| medic         |           2 |
| an            |           2 |
| reclamă       |           2 |
| internet      |           2 |
| supune        |           2 |
| parte         |           2 |
| zonă          |           2 |
| societate     |           2 |
| adevăr        |           2 |
| profesie      |           1 |
| mesaj         |           1 |
| ține          |           1 |

### 2026-03-27 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| slovacia      |           3 |
| european      |           3 |
| conflict      |           2 |
| securitate    |           2 |
| român         |           2 |
| primi         |           1 |
| palat         |           1 |
| cotroceni     |           1 |
| prim          |           1 |
| ministru      |           1 |
| robert        |           1 |
| fico          |           1 |
| discuta       |           1 |
| agendă        |           1 |
| analiza       |           1 |
| împreună      |           1 |
| impact        |           1 |
| criză         |           1 |
| internațional |           1 |
| actual        |           1 |

### 2026-03-27 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| parteneriat |           3 |
| românia     |           3 |
| turcia      |           3 |
| reconfirma  |           2 |
| strategic   |           2 |
| neagră      |           2 |
| discuție    |           2 |
| cooperare   |           2 |
| comunitate  |           2 |
| întâlni     |           1 |
| palat       |           1 |
| cotroceni   |           1 |
| numan       |           1 |
| kurtulmuș   |           1 |
| președinte  |           1 |
| marii       |           1 |
| adunări     |           1 |
| național    |           1 |
| turciei     |           1 |
| dialog      |           1 |

### 2026-03-30 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| european     |           4 |
| investiție   |           3 |
| social       |           3 |
| proiect      |           2 |
| om           |           2 |
| muncă        |           2 |
| mînzatu      |           2 |
| nivel        |           2 |
| trebui       |           1 |
| sine         |           1 |
| concentra    |           1 |
| loc          |           1 |
| calitate     |           1 |
| educație     |           1 |
| sănătate     |           1 |
| protejare    |           1 |
| cetatean     |           1 |
| problematică |           1 |
| esențial     |           1 |
| depinde      |           1 |

### 2026-03-31 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| românia    |           7 |
| european   |           5 |
| țară       |           5 |
| uniune     |           4 |
| economic   |           4 |
| sine       |           4 |
| important  |           3 |
| lucru      |           3 |
| trebui     |           3 |
| integrare  |           3 |
| aderare    |           2 |
| decalaj    |           2 |
| an         |           2 |
| continua   |           2 |
| dezvoltare |           2 |
| major      |           2 |
| instituție |           2 |
| obiectiv   |           2 |
| vrea       |           2 |
| piață      |           2 |

### 2026-03-31 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| moldova    |           4 |
| munteanu   |           3 |
| prim       |           2 |
| ministru   |           2 |
| republicii |           2 |
| alexandru  |           2 |
| republică  |           2 |
| românia    |           2 |
| uniune     |           2 |
| european   |           2 |
| creștere   |           2 |
| proiect    |           2 |
| discuție   |           1 |
| aplica     |           1 |
| sine       |           1 |
| axa        |           1 |
| prioritate |           1 |
| comun      |           1 |
| urgent     |           1 |
| trebui     |           1 |

### 2026-03-31 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| european       |           5 |
| transport      |           4 |
| românia        |           3 |
| fond           |           3 |
| ucraina        |           3 |
| țară           |           3 |
| autostradă     |           3 |
| moldova        |           3 |
| marfă          |           2 |
| atât           |           2 |
| apostolos      |           2 |
| tzitzikostas   |           2 |
| comisar        |           2 |
| coridoară      |           2 |
| esențial       |           2 |
| inclusiv       |           2 |
| infrastructură |           2 |
| europa         |           2 |
| republică      |           2 |
| asigurare      |           1 |

### 2026-04-02 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| român       |           2 |
| parte       |           2 |
| istoric     |           2 |
| însemna     |           2 |
| bucura      |           1 |
| brățăre     |           1 |
| dacic       |           1 |
| coif        |           1 |
| coțofenești |           1 |
| recupera    |           1 |
| felicit     |           1 |
| procuror    |           1 |
| olandez     |           1 |
| echipă      |           1 |
| comun       |           1 |
| anchetă     |           1 |
| apreciez    |           1 |
| totodată    |           1 |
| sprijin     |           1 |
| agenție     |           1 |

### 2026-04-05 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| celebra     |           2 |
| înviere     |           2 |
| dori        |           2 |
| valoare     |           2 |
| credincioșe |           1 |
| sfânt       |           1 |
| sărbător    |           1 |
| prilej      |           1 |
| bucurie     |           1 |
| alături     |           1 |
| drag        |           1 |
| speranță    |           1 |
| liniște     |           1 |
| sufletesc   |           1 |
| cristos     |           1 |
| învia       |           1 |
| mesaj       |           1 |
| esențial    |           1 |
| reconfirma  |           1 |
| încredere   |           1 |

### 2026-04-07 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| an            |           4 |
| sine          |           4 |
| om            |           3 |
| românia       |           3 |
| unitate       |           2 |
| medical       |           2 |
| fond          |           2 |
| european      |           2 |
| mondial       |           1 |
| sănătate      |           1 |
| transmite     |           1 |
| gând          |           1 |
| recunoștință  |           1 |
| sistem        |           1 |
| sanitar       |           1 |
| medic         |           1 |
| asistent      |           1 |
| tehnician     |           1 |
| administrator |           1 |
| rol           |           1 |

### 2026-04-07 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| declarațiile |           1 |
| presă        |           1 |
| susține      |           1 |
| final        |           1 |
| vizită       |           1 |
| centru       |           1 |
| arde         |           1 |
| spital       |           1 |
| clinic       |           1 |
| județean     |           1 |
| urgență      |           1 |
| pius         |           1 |
| brînzeu      |           1 |
| timișoara    |           1 |

### 2026-04-08 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| occidental     |           3 |
| fbi            |           2 |
| partener       |           2 |
| cibernetic     |           2 |
| informație     |           2 |
| împreună       |           1 |
| printre        |           1 |
| sri            |           1 |
| anunța         |           1 |
| destructurare  |           1 |
| atac           |           1 |
| informatic     |           1 |
| prelungi       |           1 |
| infrastructură |           1 |
| sensibil       |           1 |
| stat           |           1 |
| actori         |           1 |
| asociat        |           1 |
| gru            |           1 |
| serviciu       |           1 |

### 2026-04-12 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| an          |           2 |
| putere      |           2 |
| hristos     |           1 |
| înviat      |           1 |
| certitudine |           1 |
| reaminti    |           1 |
| triumf      |           1 |
| speranță    |           1 |
| renașterii  |           1 |
| moment      |           1 |
| întoarce    |           1 |
| valoare     |           1 |
| defini      |           1 |
| încredere   |           1 |
| putea       |           1 |
| iubire      |           1 |
| bunătate    |           1 |
| față        |           1 |
| seman       |           1 |
| sărbătorile |           1 |

### 2026-04-20 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| reformă      |           2 |
| final        |           2 |
| proiect      |           2 |
| program      |           2 |
| trece        |           1 |
| revistă      |           1 |
| împreună     |           1 |
| ministru     |           1 |
| dragoș       |           1 |
| pâslaru      |           1 |
| stadiu       |           1 |
| implementare |           1 |
| pnrr         |           1 |
| investiție   |           1 |
| trebui       |           1 |
| duce         |           1 |
| bun          |           1 |
| sfârșit      |           1 |
| încă         |           1 |
| asigura      |           1 |

### 2026-04-22 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| politic        |           6 |
| partid         |           4 |
| sine           |           4 |
| pro-occidental |           3 |
| consultare     |           2 |
| coaliție       |           2 |
| criză          |           2 |
| diferență      |           2 |
| opinie         |           2 |
| discuție       |           2 |
| vrea           |           2 |
| forță          |           2 |
| românia        |           2 |
| actual         |           1 |
| informal       |           1 |
| moment         |           1 |
| constituție    |           1 |
| președinte     |           1 |
| atribuție      |           1 |
| însă           |           1 |

### 2026-04-22 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| partid                  |           2 |
| consultări              |           1 |
| formațiune              |           1 |
| politic                 |           1 |
| parlamentar             |           1 |
| național                |           1 |
| liberal                 |           1 |
| partidulnaționalliberal |           1 |

### 2026-04-22 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| live        |           1 |
| consultări  |           1 |
| partid      |           1 |
| formațiune  |           1 |
| politic     |           1 |
| parlamentar |           1 |
| uniune      |           1 |
| salvați     |           1 |
| românia     |           1 |
| usr         |           1 |

### 2026-04-22 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| live        |           1 |
| consultare  |           1 |
| partid      |           1 |
| formațiune  |           1 |
| politic     |           1 |
| parlamentar |           1 |
| uniune      |           1 |
| democrată   |           1 |
| maghiar     |           1 |
| românia     |           1 |
| udmr        |           1 |

### 2026-04-22 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| parlamentar   |           2 |
| live          |           1 |
| consultări    |           1 |
| partid        |           1 |
| formațiune    |           1 |
| politic       |           1 |
| grup          |           1 |
| minorităților |           1 |
| național      |           1 |

### 2026-04-22 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| partid      |           2 |
| live        |           1 |
| consultare  |           1 |
| formațiune  |           1 |
| politic     |           1 |
| parlamentar |           1 |
| social      |           1 |
| democrat    |           1 |
| psd         |           1 |

### 2026-04-22 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| live       |           1 |
| declarație |           1 |
| presă      |           1 |
| susținut   |           1 |
| palat      |           1 |
| cotroceni  |           1 |

### 2026-04-23 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| violență     |           4 |
| lege         |           3 |
| femeie       |           3 |
| prevenire    |           2 |
| femicid      |           2 |
| necesar      |           2 |
| înțelege     |           2 |
| promulga     |           1 |
| combatere    |           1 |
| violențu     |           1 |
| preceda      |           1 |
| înjositor    |           1 |
| degradant    |           1 |
| comportament |           1 |
| tip          |           1 |
| agresiune    |           1 |
| ignora       |           1 |
| insuficient  |           1 |
| abordat      |           1 |
| consecință   |           1 |

### 2026-04-23 — facebook-post

| cuvânt           |   frecvență |
|:-----------------|------------:|
| european         |           5 |
| uniune           |           5 |
| trebui           |           4 |
| resursă          |           4 |
| informal         |           3 |
| consiliu         |           3 |
| important        |           3 |
| buget            |           3 |
| cipru            |           2 |
| reuniune         |           2 |
| asigurare        |           2 |
| românia          |           2 |
| viitor           |           2 |
| uniuneaeuropeană |           2 |
| vrea             |           2 |
| coeziune         |           2 |
| pilon            |           2 |
| competitivitate  |           2 |
| securitate       |           2 |
| politic          |           2 |

### 2026-04-24 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| live         |           1 |
| declarațiile |           1 |
| presă        |           1 |
| susține      |           1 |
| final        |           1 |
| reuniuni     |           1 |
| informal     |           1 |
| consiliu     |           1 |
| european     |           1 |
| nicosia      |           1 |
| republică    |           1 |
| cipru        |           1 |

### 2026-04-24 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| european   |           4 |
| românia    |           3 |
| ban        |           3 |
| sine       |           3 |
| adică      |           2 |
| dori       |           2 |
| vrea       |           2 |
| fond       |           2 |
| an         |           2 |
| subiect    |           1 |
| important  |           1 |
| aborda     |           1 |
| consiliu   |           1 |
| informal   |           1 |
| cipru      |           1 |
| viitor     |           1 |
| cadru      |           1 |
| financiar  |           1 |
| multianual |           1 |
| destinat   |           1 |

### 2026-04-25 — facebook-post

| cuvânt          |   frecvență |
|:----------------|------------:|
| lider           |           2 |
| semna           |           1 |
| asear           |           1 |
| demisiile       |           1 |
| miniștrilor     |           1 |
| social-democrat |           1 |
| propunere       |           1 |
| miniștru        |           1 |
| interimar       |           1 |
| transmite       |           1 |
| guvern          |           1 |
| vrea            |           1 |
| exercita        |           1 |
| continuare      |           1 |
| rol             |           1 |
| mediator        |           1 |
| invita          |           1 |
| lună            |           1 |
| partid          |           1 |
| politic         |           1 |

### 2026-04-28 — facebook-post

| cuvânt         |   frecvență |
|:---------------|------------:|
| vrea           |           5 |
| inițiativa     |           2 |
| românia        |           2 |
| dezvoltare     |           2 |
| economie       |           2 |
| constanța      |           2 |
| port           |           2 |
| strategic      |           2 |
| european       |           2 |
| transport      |           2 |
| fond           |           2 |
| infrastructură |           2 |
| investiție     |           2 |
| dubrovnik      |           1 |
| marja          |           1 |
| summit         |           1 |
| înregistra     |           1 |
| pas            |           1 |
| important      |           1 |
| consolidare    |           1 |

### 2026-04-28 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| austria     |           2 |
| parteneriat |           2 |
| precum      |           2 |
| marjă       |           1 |
| summit      |           1 |
| inițiativa  |           1 |
| dubrovnik   |           1 |
| plăcere     |           1 |
| discuta     |           1 |
| christian   |           1 |
| stocker     |           1 |
| cancelaru   |           1 |
| federal     |           1 |
| european    |           1 |
| economic    |           1 |
| investitor  |           1 |
| economie    |           1 |
| românia     |           1 |
| colaborare  |           1 |
| continua    |           1 |

### 2026-04-28 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| live       |           1 |
| declarații |           1 |
| presă      |           1 |
| susține    |           1 |
| marja      |           1 |
| summit     |           1 |
| inițiativa |           1 |
| dubrovnik  |           1 |
| republică  |           1 |
| croația    |           1 |

### 2026-04-28 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| românia                 |           3 |
| efort                   |           3 |
| diplomatic              |           2 |
| intelligence            |           2 |
| schimb                  |           2 |
| autoritate              |           2 |
| român                   |           2 |
| sri                     |           2 |
| partener                |           2 |
| acțiune                 |           2 |
| moldova                 |           2 |
| participa               |           1 |
| activ                   |           1 |
| succes                  |           1 |
| transatlantic           |           1 |
| coordonat               |           1 |
| departament             |           1 |
| stat                    |           1 |
| stateleunitealeamericii |           1 |
| presupune               |           1 |

### 2026-04-29 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| participa  |           1 |
| sesiune    |           1 |
| special    |           1 |
| forumului  |           1 |
| afaceri    |           1 |
| inițiativa |           1 |
| format     |           1 |
| relevant   |           1 |
| reuni      |           1 |
| țară       |           1 |
| comunist   |           1 |
| dezvoltare |           1 |
| similar    |           1 |
| același    |           1 |
| aspirație  |           1 |
| interior   |           1 |
| uniune     |           1 |
| european   |           1 |
| urmări     |           1 |
| obiectiv   |           1 |

### 2026-04-29 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| live         |           1 |
| declarațiile |           1 |
| presă        |           1 |
| susține      |           1 |
| participare  |           1 |
| forum        |           1 |
| afaceri      |           1 |
| inițiativa   |           1 |
| dubrovnik    |           1 |
| republică    |           1 |
| croația      |           1 |

### 2026-05-03 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| câștiga                 |           5 |
| loc                     |           4 |
| echipa                  |           4 |
| național                |           3 |
| campionat               |           2 |
| mondial                 |           2 |
| first                   |           2 |
| tech                    |           2 |
| challenge               |           2 |
| internațional           |           2 |
| liceu                   |           2 |
| colegiu                 |           2 |
| felicită                |           1 |
| elev                    |           1 |
| român                   |           1 |
| lot                     |           1 |
| robotic                 |           1 |
| participa               |           1 |
| houston                 |           1 |
| stateleunitealeamericii |           1 |

### 2026-05-03 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| vrea       |           4 |
| participa  |           2 |
| alături    |           2 |
| grup       |           2 |
| moldova    |           2 |
| regional   |           2 |
| drum       |           1 |
| armenia    |           1 |
| doamnă     |           1 |
| președintă |           1 |
| maia       |           1 |
| sandu      |           1 |
| republică  |           1 |
| sine       |           1 |
| desfășura  |           1 |
| cadru      |           1 |
| reuniuni   |           1 |
| comunitate |           1 |
| politic    |           1 |
| european   |           1 |

### 2026-05-04 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| monaco        |           2 |
| plăcere       |           1 |
| întâlni       |           1 |
| principe      |           1 |
| albert        |           1 |
| -lea          |           1 |
| summit        |           1 |
| erevan        |           1 |
| românia       |           1 |
| împărtăși     |           1 |
| bun           |           1 |
| relație       |           1 |
| bilateral     |           1 |
| preocupare    |           1 |
| constant      |           1 |
| cooperare     |           1 |
| multilateral  |           1 |
| ordine        |           1 |
| internațional |           1 |
| baza          |           1 |

### 2026-05-04 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| energetic   |           2 |
| aduce       |           2 |
| organiza    |           1 |
| marja       |           1 |
| reuniuni    |           1 |
| comunitate  |           1 |
| politic     |           1 |
| european    |           1 |
| erevan      |           1 |
| eveniment   |           1 |
| nivel       |           1 |
| înalt       |           1 |
| dedicat     |           1 |
| coridor     |           1 |
| vertical    |           1 |
| gaze        |           1 |
| rol         |           1 |
| consolidare |           1 |
| securitate  |           1 |
| regional    |           1 |

### 2026-05-04 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| live        |           1 |
| declarații  |           1 |
| presă       |           1 |
| participare |           1 |
| reuniune    |           1 |
| comunitate  |           1 |
| politic     |           1 |
| european    |           1 |
| erevan      |           1 |
| republică   |           1 |
| armenia     |           1 |

### 2026-05-04 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| european      |           2 |
| prieten       |           1 |
| participare   |           1 |
| discuție      |           1 |
| dezinformare  |           1 |
| amenințri     |           1 |
| hibrid        |           1 |
| co-prezidat   |           1 |
| împreun       |           1 |
| președinte    |           1 |
| muntenegru    |           1 |
| jakov         |           1 |
| milatovic     |           1 |
| dezinformarea |           1 |
| atac          |           1 |
| cibernetic    |           1 |
| ingerință     |           1 |
| extern        |           1 |
| amenințare    |           1 |
| interconectat |           1 |

### 2026-05-05 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| live       |           1 |
| declarații |           1 |
| presă      |           1 |
| susține    |           1 |
| palat      |           1 |
| cotroceni  |           1 |

### 2026-05-09 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| românia   |          18 |
| european  |          16 |
| uniune    |          12 |
| sine      |          12 |
| europa    |          10 |
| an        |           6 |
| vrea      |           6 |
| moment    |           5 |
| duce      |           5 |
| dezbatere |           5 |
| greșeală  |           5 |
| adevărat  |           4 |
| decât     |           4 |
| loc       |           4 |
| exista    |           4 |
| lozincă   |           4 |
| politică  |           4 |
| interior  |           4 |
| pace      |           3 |
| oară      |           3 |

### 2026-05-12 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| românia                         |           5 |
| northatlantictreatyorganization |           5 |
| puternic                        |           4 |
| pilon                           |           3 |
| european                        |           3 |
| exista                          |           3 |
| strategic                       |           2 |
| politică                        |           2 |
| extern                          |           2 |
| discuție                        |           2 |
| intern                          |           2 |
| niciun                          |           2 |
| uniune                          |           2 |
| stateleunitealeamericii         |           2 |
| relație                         |           2 |
| corect                          |           2 |
| europa                          |           2 |
| atât                            |           2 |
| abordare                        |           1 |
| privi                           |           1 |

### 2026-05-12 — facebook-post

| cuvânt       |   frecvență |
|:-------------|------------:|
| polonia      |           5 |
| românia      |           3 |
| președinte   |           2 |
| nawrocki     |           2 |
| partener     |           2 |
| zonă         |           2 |
| cooperare    |           2 |
| oportunitate |           2 |
| discuție     |           1 |
| substanțial  |           1 |
| karol        |           1 |
| primi        |           1 |
| palat        |           1 |
| cotroceni    |           1 |
| summit       |           1 |
| strategic    |           1 |
| agendă       |           1 |
| întâlnire    |           1 |
| viza         |           1 |
| modalitate   |           1 |

### 2026-05-12 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| northatlantictreatyorganization |           3 |
| summit                          |           3 |
| securitate                      |           3 |
| apărare                         |           2 |
| întâlnire                       |           1 |
| lucru                           |           1 |
| alături                         |           1 |
| secretar                        |           1 |
| general                         |           1 |
| mark                            |           1 |
| rutte                           |           1 |
| președinte                      |           1 |
| polonia                         |           1 |
| karol                           |           1 |
| nawrocki                        |           1 |
| pregătire                       |           1 |
| vrea                            |           1 |
| găzdui                          |           1 |
| palat                           |           1 |
| cotroceni                       |           1 |

### 2026-05-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| live       |           1 |
| declarații |           1 |
| presă      |           1 |
| comun      |           1 |
| președinte |           1 |
| republicii |           1 |
| polone     |           1 |
| karol      |           1 |
| nawrocki   |           1 |

### 2026-05-12 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| live          |           1 |
| declarații    |           1 |
| presă         |           1 |
| susține       |           1 |
| participare   |           1 |
| conferință    |           1 |
| internațional |           1 |
| black         |           1 |
| sea           |           1 |
| and           |           1 |
| balkans       |           1 |
| security      |           1 |
| forum         |           1 |

### 2026-05-12 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| live          |           1 |
| participare   |           1 |
| conferință    |           1 |
| internațional |           1 |
| black         |           1 |
| sea           |           1 |
| and           |           1 |
| balkans       |           1 |
| security      |           1 |
| forum         |           1 |

### 2026-05-12 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| live       |           1 |
| primire    |           1 |
| președinte |           1 |
| republicii |           1 |
| polone     |           1 |
| karol      |           1 |
| nawrocki   |           1 |
| palat      |           1 |
| cotroceni  |           1 |

### 2026-05-12 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| live                            |           1 |
| primire                         |           1 |
| secretar                        |           1 |
| general                         |           1 |
| northatlantictreatyorganization |           1 |
| mark                            |           1 |
| rutte                           |           1 |
| palat                           |           1 |
| cotroceni                       |           1 |

### 2026-05-13 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| european    |           2 |
| om          |           2 |
| românia     |           2 |
| curte       |           2 |
| întrevedere |           1 |
| excelent    |           1 |
| președinte  |           1 |
| curtie      |           1 |
| echrcedh    |           1 |
| mattias     |           1 |
| guyomar     |           1 |
| reafirma    |           1 |
| sprijin     |           1 |
| ferm        |           1 |
| sistem      |           1 |
| convenție   |           1 |
| rol         |           1 |
| esențial    |           1 |
| protejare   |           1 |
| fundamental |           1 |

### 2026-05-13 — facebook-post

| cuvânt   |   frecvență |
|:---------|------------:|
| bsummit  |           1 |
| romania  |           1 |
| polonia  |           1 |
| ucraina  |           1 |

### 2026-05-13 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| northatlantictreatyorganization |           5 |
| securitate                      |           5 |
| ucraina                         |           3 |
| summit                          |           3 |
| transatlantic                   |           3 |
| bucurești                       |           2 |
| aliat                           |           2 |
| exista                          |           2 |
| prioritate                      |           2 |
| oferi                           |           2 |
| le-                             |           1 |
| ura                             |           1 |
| bun                             |           1 |
| veni                            |           1 |
| lider                           |           1 |
| stat                            |           1 |
| membră                          |           1 |
| invitațe                        |           1 |
| prieten                         |           1 |
| nordică                         |           1 |

### 2026-05-13 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| președinte                      |           2 |
| live                            |           1 |
| declarații                      |           1 |
| presă                           |           1 |
| comun                           |           1 |
| românia                         |           1 |
| nicușor                         |           1 |
| dan                             |           1 |
| republicii                      |           1 |
| polone                          |           1 |
| karol                           |           1 |
| nawrocki                        |           1 |
| secretar                        |           1 |
| general                         |           1 |
| northatlantictreatyorganization |           1 |
| mark                            |           1 |
| rutte                           |           1 |
| final                           |           1 |
| summit                          |           1 |
| formatului                      |           1 |

### 2026-05-13 — facebook-post

| cuvânt      |   frecvență |
|:------------|------------:|
| live        |           1 |
| primire     |           1 |
| președinte  |           1 |
| ucraina     |           1 |
| palat       |           1 |
| cotroceni   |           1 |
| participare |           1 |
| summit      |           1 |
| bucurești   |           1 |

### 2026-05-13 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| comun                           |           4 |
| întru                           |           3 |
| declarație                      |           3 |
| țară                            |           3 |
| northatlantictreatyorganization |           3 |
| bucurești                       |           2 |
| format                          |           2 |
| exista                          |           2 |
| amenințare                      |           2 |
| rusia                           |           2 |
| discuție                        |           2 |
| summit                          |           2 |
| important                       |           2 |
| putea                           |           2 |
| participare                     |           1 |
| amplu                           |           1 |
| stat                            |           1 |
| aliat                           |           1 |
| zonă                            |           1 |
| nordic                          |           1 |

### 2026-05-13 — facebook-post

| cuvânt     |   frecvență |
|:-----------|------------:|
| președinte |           2 |
| zelenski   |           2 |
| special    |           2 |
| continua   |           2 |
| românia    |           2 |
| securitate |           2 |
| apărare    |           2 |
| ucraina    |           2 |
| tehnologiu |           2 |
| volodîmîr  |           1 |
| invitat    |           1 |
| summit     |           1 |
| palat      |           1 |
| cotroceni  |           1 |
| ocazie     |           1 |
| consultare |           1 |
| bilateral  |           1 |
| excelent   |           1 |
| dialog     |           1 |
| începe     |           1 |

### 2026-05-13 — facebook-post

| cuvânt    |   frecvență |
|:----------|------------:|
| summit    |           1 |
| palat     |           1 |
| cotroceni |           1 |
| împreună  |           1 |
| puternic  |           1 |

### 2026-05-13 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| unitate                         |           1 |
| forță                           |           1 |
| coerență                        |           1 |
| trebui                          |           1 |
| ghida                           |           1 |
| consolidare                     |           1 |
| flancului                       |           1 |
| estic                           |           1 |
| împreună                        |           1 |
| siguranță                       |           1 |
| cetățen                         |           1 |
| summitulb                       |           1 |
| flanculestic                    |           1 |
| northatlantictreatyorganization |           1 |

### 2026-05-13 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| securitate    |           2 |
| stat          |           2 |
| important     |           1 |
| palat         |           1 |
| cotroceni     |           1 |
| loc           |           1 |
| -a            |           1 |
| ediție        |           1 |
| summit        |           1 |
| formatului    |           1 |
| bucurești     |           1 |
| temă          |           1 |
| central       |           1 |
| oferi         |           1 |
| transatlantic |           1 |
| urma          |           1 |
| discuție      |           1 |
| aplica        |           1 |
| comun         |           1 |
| zonă          |           1 |

### 2026-05-14 — facebook-post

| cuvânt                          |   frecvență |
|:--------------------------------|------------:|
| summit                          |           1 |
| reconfirma                      |           1 |
| lucru                           |           1 |
| esențial                        |           1 |
| securitate                      |           1 |
| europa                          |           1 |
| forță                           |           1 |
| northatlantictreatyorganization |           1 |
| depinde                         |           1 |
| unitate                         |           1 |
| relație                         |           1 |
| transatlantic                   |           1 |
| hotărâți                        |           1 |
| investi                         |           1 |
| apărare                         |           1 |
| sprijinim                       |           1 |
| flanc                           |           1 |
| estic                           |           1 |
| consolida                       |           1 |
| capacitate                      |           1 |

### 2026-05-15 — facebook-post

| cuvânt                  |   frecvență |
|:------------------------|------------:|
| apărare                 |           4 |
| bsda                    |           4 |
| bucurești               |           3 |
| industrie               |           3 |
| securitate              |           3 |
| context                 |           2 |
| expoziție               |           2 |
| internațional           |           2 |
| an                      |           2 |
| stateleunitealeamericii |           2 |
| investițiile            |           1 |
| ține                    |           1 |
| cetățean                |           1 |
| deveni                  |           1 |
| prioritate              |           1 |
| actual                  |           1 |
| global                  |           1 |
| multiplu                |           1 |
| conflict                |           1 |
| militar                 |           1 |

### 2026-05-15 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| live          |           1 |
| declarații    |           1 |
| presă         |           1 |
| susține       |           1 |
| președinte    |           1 |
| românia       |           1 |
| nicușor       |           1 |
| dan           |           1 |
| final         |           1 |
| vizită        |           1 |
| expoziție     |           1 |
| internațional |           1 |
| black         |           1 |
| sea           |           1 |
| defense       |           1 |
| aerospace     |           1 |
| and           |           1 |
| security      |           1 |
| bsda          |           1 |

### 2026-05-21 — facebook-post

| cuvânt        |   frecvență |
|:--------------|------------:|
| societate     |           3 |
| ong           |           3 |
| -urilor       |           3 |
| măsură        |           3 |
| civil         |           2 |
| față          |           2 |
| ță            |           1 |
| sugerez       |           1 |
| dezbatere     |           1 |
| cameră        |           1 |
| decizional    |           1 |
| invita        |           1 |
| organizație   |           1 |
| reprezentativ |           1 |
| transparența  |           1 |
| stat          |           1 |
| persoană      |           1 |
| juridic       |           1 |
| necesar       |           1 |
| sine          |           1 |

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
| vrea          |        4884 |
| sine          |        4168 |
| românia       |        3142 |
| spune         |        2854 |
| putea         |        2522 |
| trebui        |        2079 |
| președinte    |        1734 |
| vedea         |        1696 |
| moment        |        1669 |
| domn          |        1660 |
| om            |        1447 |
| an            |        1367 |
| stat          |        1347 |
| parte         |        1299 |
| exista        |        1192 |
| lucru         |        1171 |
| ști           |        1131 |
| european      |        1130 |
| discuție      |        1122 |
| partid        |        1103 |
| crede         |        1054 |
| țară          |        1050 |
| român         |        1031 |
| ăă            |        1024 |
| bun           |        1012 |
| important     |         927 |
| veni          |         909 |
| dumneavoastră |         854 |
| vorbi         |         806 |
| guvern        |         798 |

## Stopwords folosite

Listă **stopwordsiso RO** (438 cuvinte) + domain extras (cardinali, câteva auxiliare nestockate).


## Note metodologice

- **Tokenizare + lemmatizare**: spaCy `ro_core_news_sm`. Token-ele sunt reduse la lemma (formă canonică): `românia/româniei/român/români` → `românia`/`român`, `anunț/anunțul` → `anunța`, `săptămânile` → `săptămână`.
- **Stopwords**: `stopwordsiso` (RO) + extensii pentru cardinali și conjuncții scurte.
- **Numerele și punctuația** sunt eliminate; diacriticele cedilă (ş, ţ) sunt normalizate la virgulă-below (ș, ț).
- **TTR** (type-token ratio) e biased de lungime — discursurile scurte au TTR mai mare. Util doar comparativ pe lungimi similare.