---
article_id: 09-kysymystyypit
concept: kysymystyypit
register: facilitator
lang: sv
source_lang: fi
translations:
- en
- fi
title: 'Frågetyper: en urvalsguide med exempel'
order: 9
version: '1.0'
last_updated: '2026-08-02'
license: CC-BY-4.0
authors:
- Metodix Oy
status: published
public: false
kb_include: true
original_source: Delphi-Pronoia frontend/help
---

# Frågetyper: en urvalsguide med exempel

Pronoia har tio frågetyper (+ kriterievariabler). Valet av typ avgör *vad panelen kan lära dig*: samma ämne ger olika kunskap som skalbedömning, tidsuppskattning eller resursfördelning. Tumregel: välj den lättaste typ som besvarar din forskningsfråga — och be alltid om motiveringen.

## Grundtyper

### Skala (scale)
**Vad:** panelisten bedömer ett påstående på en numerisk skala (standard 1–9); valfria **kriterievariabler** (t.ex. sannolikhet × önskvärdhet) ger flera bedömningar av samma tes.
**Använd när:** du vill mäta stöd, sannolikhet eller önskvärdhet och följa konsensus över rundor. Delfis arbetshäst.
**Exempel:** *"Generell AI sköter mer än hälften av kommunernas kundservice till 2035."* Kriterier: sannolikhet + önskvärdhet.
**Resultat:** fördelning, centralmått, IQR, tyngdpunkt på skalan; P×D-gapet avslöjar hot/önskan-spänningar.

### Öppen (open)
**Vad:** endast textsvar, ingen numerisk bedömning.
**Använd när:** du kartlägger ett fenomen som ännu inte kan formuleras som påståenden — idégenerering i runda 0/1, svaga signaler, begreppsinsamling.
**Exempel:** *"Vilken är den viktigaste förändringen i expertarbetet som ingen ännu tar på allvar?"*
**Resultat:** kvalitativt material för argumentanalys; ofta råmaterial för nästa rundas teser.

### Rangordning (ranking)
**Vad:** panelisten sätter de givna alternativen i prioritetsordning.
**Använd när:** du behöver en prioritetsordning över en avgränsad mängd — men intensiteten spelar ingen roll (jfr. satsning).
**Exempel:** *"Rangordna drivkrafterna efter deras inverkan på distansundervisningens kvalitet: lärarnas kompetens · verktyg · pedagogiska modeller · elevernas självstyrning."*
**Resultat:** genomsnittlig placering per alternativ; spridningen visar de mest omstridda.

### Flerval (multichoice)
**Vad:** val bland givna alternativ (ett eller flera).
**Använd när:** frågan är en klassificering eller "vilka av dessa" — ingen ordning, ingen intensitet.
**Exempel:** *"Vilka hinder bromsar AI-införandet i din organisation mest? (välj 1–3)"*
**Resultat:** valandelar; en snabb karta att bygga följdfrågor på.

## Strukturerings- och prioriteringstyper

### Gruppering (grouping)
**Vad:** panelisten sorterar objekt i facilitatorns korgar genom att dra (card-sort).
**Använd när:** du vill att panelen klassificerar en mängd fenomen — t.ex. signaler efter mognad, teser efter acceptans eller åtgärder efter brådska.
**Exempel:** objekt = 8 svaga signaler; korgar = *Heta · Svala · Kalla*. Eller: åtgärder i korgarna *Nu · 3 år · 10 år · Aldrig*.
**Resultat:** korgfördelning + modalkorg per objekt; oenighet syns som spridning mellan korgar.

### Satsning (allocation)
**Vad:** panelisten fördelar en fast summa (standard 100 poäng) mellan alternativen.
**Använd när:** ordning inte räcker utan du behöver *hur mycket* — resursfördelning eller fördelning av sannolikhetsmassa över ömsesidigt uteslutande scenarier.
**Exempel:** *"Fördela 100 poäng på hur kommunen bör vikta klimatåtgärder: transport · byggnader · energi · mat · kompensationer."* Eller: *"Fördela 100 % på fyra scenarier efter sannolikhet."*
**Resultat:** genomsnittlig fördelning + spridning per alternativ; normaliserad läses den direkt som sannolikheter.

### 2×2-placering (xy)
**Vad:** panelisten placerar ämnet som en punkt på ett tvåaxligt plan genom att dra.
**Använd när:** två dimensioner ska bedömas *i förhållande till varandra* — klassiskt påverkan × osäkerhet (härledning av scenarioaxlar) eller sannolikhet × önskvärdhet som en karta.
**Exempel:** tes = *"Kvantdatorer knäcker dagens kryptering"*; axlar = påverkan (x) × osäkerhet (y).
**Resultat:** spridningsdiagram + tyngdpunkt + kvadrantfördelning; två läger i olika hörn är i sig ett fynd och en kandidat till scenarioaxel.

## Tidstyper

### Tidsuppskattning (temporal)
**Vad:** panelisten anger **ett enda år** då påståendet förverkligas — eller "inte inom denna horisont".
**Använd när:** du vill ha en snabb tidsbedömning för en stor tesmängd; fördelningen uttrycker panelens osäkerhet.
**Exempel:** *"Vilket år görs mer än hälften av studentproven med AI-stöd?"* (spann 2026–2050).
**Resultat:** årshistogram + median + beyond-andel. En tvåtoppig fördelning = oenighet om tidpunkten.

### Tidsfönster (timewindow)
**Vad:** panelisten anger **två år** (tidigast–senast) enligt valt kriterium (*möjlig* eller *sannolik*); alternativet "aldrig" finns.
**Använd när:** varje panelists *egen osäkerhet* är en del av datan — ett smalt fönster är en säker ståndpunkt, ett brett en osäker. Analytiskt rikare än temporal, tyngre att besvara.
**Exempel:** *"Ett fusionskraftverk matar in el i Finlands nät."* Kriterium: sannolik; spann 2030–2070; aldrig tillåtet.
**Resultat:** fönsterband + medianfönster + tidigast/senast-kvartiler + aldrig-andel; konsensus ur IQR-bredden.

### Tidsserie (timeseries)
**Vad:** facilitatorn matar in en realiserad historisk serie; panelisten fortsätter den med ≥3 jämnt fördelade skattningspunkter (dra i diagrammet eller skriv i fälten).
**Använd när:** fenomenet har en mätbar volym och historiska data — kvantitativ framsyn där alla förankras i samma utgångsläge.
**Exempel:** *"Distansarbetets andel av expertarbetsdagar (%)"*: historik 2010–2025, skattningar 2030/2035/2040.
**Resultat:** mediankurva + kvartilband som förlänger historiken; bandets breddning visar hur långt panelens blick bär.

## Snabbval

Stöd/sannolikhet → **skala** · idégenerering → **öppen** · ordning → **rangordning** · kategorier → **flerval** eller **gruppering** · hur mycket → **satsning** · två dimensioner → **2×2** · när (snabbt) → **tidsuppskattning** · när + osäkerhet → **tidsfönster** · hur mycket i framtiden → **tidsserie**. Och i alla: motiveringen är det som Delfi lever på.
