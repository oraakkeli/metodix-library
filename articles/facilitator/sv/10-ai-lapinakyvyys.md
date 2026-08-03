---
article_id: 10-ai-lapinakyvyys
concept: ai-lapinakyvyys
register: facilitator
lang: sv
source_lang: fi
translations:
- en
- fi
title: AI-transparens och AI-panelister
order: 10
version: '1.0'
last_updated: '2026-07-11'
license: CC-BY-4.0
authors:
- Metodix Oy
status: published
public: false
kb_include: true
original_source: Delphi-Pronoia frontend/help
---

# AI-transparens och AI-panelister

Pronoia använder AI i två roller: **AI-panelister** deltar i panelen som syntetiska perspektiv, och **AI-genereringsfunktioner** hjälper facilitatorn (t.ex. tesutkast, sammanfattningar). Den här artikeln beskriver hur AI-användningen görs synlig — både för att EU:s AI-förordning (2024/1689, art. 50) kräver det från och med 2.8.2026, och framför allt för att en Delfistudies validitet kräver att syntetiska och mänskliga argument kan skiljas åt i alla skeden.

## Vad panelisten ser

När en studie innehåller AI-panelister visas ett **AI-meddelande** i hemvyn innan panelisten börjar svara. Meddelandet anger AI-panelisternas närvaro, antal och märkning. Det kan inte döljas. Du kan komplettera standardtexten med en studiespecifik anmärkning (genai-anmärkningen i studiens inställningar) — till exempel varför AI-panelister används i just den här studien.

I dialog och resultat är innehåll från AI-panelister alltid markerat med 🤖-symbolen. Panelisterna ser AI-panelister under en pseudonym kod precis som människor — men med AI-prefix.

## Vad facilitatorn ser

I facilitatorvyn visas AI-panelister som **AI · roll** (t.ex. "AI · klimatforskare"). Panelens deltagarkort visar antalet människor och AI-panelister separat (👤 / 🤖).

## Maskinläsbar märkning i exporter

All data som går till analys bär en explicit AI-märkning:

- **DAE Handoff (JSON)**: varje panelist-, argument-, dialog- och revisionspost innehåller fältet `ai_generated` (true/false). Payloadens `ai_provenance`-block sammanfattar proveniensen: antal AI-panelister, standardmodell och de märkta fälten.
- **CSV-export**: en `ai_generated`-kolumn på varje rad.

DAE-analyspipelinen använder märkningarna för att hålla syntetiska och mänskliga argument åtskilda — märkningen är inte bara ett regulatoriskt krav utan en förutsättning för analysens kvalitet.

## Dataskydd i AI-funktioner

AI-genereringen använder Anthropics Claude-API. Panelisternas öppna svar skickas till API:et **utan identitetsuppgifter** (endast pseudonym). API-data används inte för modellträning. Alla AI-funktioner har ett regelbaserat reservsystem, så en studie fungerar även helt utan AI.

## Facilitatorns checklista

1. Berätta om AI-panelisterna redan i inbjudan — låt det inte komma som en överraskning.
2. Skriv en studiespecifik genai-anmärkning: varför AI-panelister används och vad deras profiler bygger på.
3. Ta aldrig bort AI-märkningar från rapporter eller publikationer — märkningen är både ett rättsligt och ett metodologiskt krav.
