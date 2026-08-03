---
article_id: 08-aikakysymykset
concept: aikakysymykset
register: facilitator
lang: sv
source_lang: fi
translations:
- en
- fi
title: 'Tidsfrågor: tidsfönster och tidsserie'
order: 8
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

# Tidsfrågor: tidsfönster och tidsserie

En vanlig skaltes frågar *hur sannolikt eller önskvärt* något är. Tidsfrågor frågar *när* och *hur mycket*. Pronoia har två tidsfrågetyper, utformade särskilt för framsynsstudier.

## Tidsfönster — när?

Panelisten uppskattar tidpunkten för en händelse som ett **fönster**: den tidigaste och den senaste tidpunkten. I stället för en punktprognos får man ett spann som också uttrycker svarandens osäkerhet — ett smalt fönster är en säker ståndpunkt, ett brett en osäker.

**Kriterium.** När tesen skapas väljer facilitatorn om panelisterna uppskattar den **möjliga** eller den **sannolika** tidpunkten. Möjlig ger bredare fönster (vad som över huvud taget är tänkbart), sannolik smalare (vad man bör förbereda sig på). Kriteriet visas för panelisten som frågans instruktion — att blanda de två gör svaren ojämförbara, så välj ett.

**"Kommer aldrig att ske".** En klassisk lärdom från tidsättnings-Delfi: tvingas en skeptiker ange ett årtal snedvrids fördelningen. Aldrig-alternativet (på som standard) låter tvivlet synas ärligt. Aldrig-svar rapporteras som en **andel** och ingår inte i tidskvartilerna — 30 % aldrig plus ett smalt medianfönster är ett annat fynd än enbart ett smalt fönster.

**Resultat.** Panelens svar ritas som fönsterband med **medianfönstret** markerat ovanpå (från medianen av tidigast-uppskattningarna till medianen av senast-uppskattningarna). Konsensus (0–1) beräknas ur kvartilavstånden för tidigast- och senast-uppskattningarna i förhållande till svarslinjen: ju tätare panelisterna landar på samma år, desto högre konsensus. Samma tal visas i konvergenstabellen.

## Tidsserie — hur mycket?

Facilitatorn matar in en **realiserad historisk serie** (t.ex. elförbrukning 2010–2025), och panelisten fortsätter den med minst tre jämnt fördelade framtidspunkter. Historiken förankrar uppskattningarna: alla ser samma utgångsläge och tar ställning till samma storhets fortsättning.

**Parametrar.** Storhetens namn och enhet (y-axeln), intervallet i år (jämn fördelning på x-axeln) och antalet skattningspunkter (minst 3). Åren som ska uppskattas härleds automatiskt ur historikens sista år.

**Resultat.** Panelens uppskattningar sammanfattas i en **mediankurva** och ett **kvartilband** (Q1–Q3) som förlänger historiken; enskilda uppskattningar syns som svaga linjer. Ett brett band signalerar dissensus, och särskilt intressant är *bandets breddning över tid* — paneler är ofta mer eniga om nära år än om avlägsna.

## Systertyp: tidsuppskattning

Pronoia har också en lättare **tidsuppskattning** (`temporal`): panelisten anger **ett enda år** (eller "inte inom denna horisont"), och resultatet är ett årshistogram + median. Arbetsfördelning: **temporal** när en snabb punktuppskattning räcker och fördelningen fångar osäkerheten; **tidsfönster** när man vill att *varje panelist* uttrycker sin egen osäkerhet (fönstrets bredd) och kriteriet (möjlig/sannolik) — analytiskt rikare men tyngre att besvara.

## Vilken när?

**Tidsfönster**, när frågan gäller tidpunkten för en händelse eller övergång ("när blir X vanligt / möjligt"). **Tidsserie**, när fenomenet har en mätbar volym och historiska data ("hur utvecklas mängden X"). I båda är motiveringen lika viktig som siffrorna — dialog och revideringar fungerar som i andra testyper, och konvergensen mellan rundor beräknas även för tidsfrågor.
