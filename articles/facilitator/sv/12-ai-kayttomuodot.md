---
article_id: 12-ai-kayttomuodot
concept: ai-kayttomuodot
register: facilitator
lang: sv
source_lang: fi
translations:
- en
- fi
title: AI-användningslägen och kostnader
order: 11
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

# AI-användningslägen och kostnader

I Pronoia är AI ett kompletterande verktyg, inte ett beroende: varje Delfi fungerar helt utan AI, och alla AI-funktioner faller tillbaka på ett regelbaserat reservsystem. Den här artikeln beskriver hur du väljer AI-användning medvetet, vilka tjänster som finns och hur kostnaderna hålls under kontroll.

## De tre lägena

AI-användningen väljs med en enda inställning, graderad efter hur mycket data som exponeras för AI:n:

- **Ingen AI (off)** — inget skickas till en AI-tjänst; hela processen körs regelbaserat.
- **Metodhjälp (assist)** — standard; endast stöd till facilitatorn (Fråga Pronoia, profiler, översättning). Panelisternas innehåll skickas inte ut.
- **Full** — dessutom panelinnehåll: AI-panelister, Runda 0-chatt, PIRE-fördjupning, kodningsförslag.

Innan studien går över till processen (att öppna den första rundan) måste du **välja läget medvetet**. "Ingen AI" är där ett fullt likvärdigt alternativ. Nivån kan senare höjas men inte sänkas under det som panelisterna redan deltagit i.

## Tjänster

**Metodhjälp (assist räcker, inget panelinnehåll):** Fråga Pronoia (metodrådgivning), profilgenerering (AI-panelisternas profiler från fenomenbeskrivningen), översättning.

**Panelinnehåll (kräver full-läget):** AI-panelister (syntetiska perspektivargument), Runda 0-intake-chatt, PIRE-fördjupning, kodningsförslag.

Den största men mest förutsägbara posten är AI-panelister (kostnad = panelister × teser × rundor). Runda 0-chatten är den minsta men mest oförutsägbara eftersom den är interaktiv.

## Kostnader och tak

AI:ns bakgrundskostnad omvandlas till fasta **krediter**, så du ser bara en omvandling (t.ex. 100 krediter = 1 €). Före varje körning visas en **pre-flight-uppskattning** ("≈ 390 krediter ≈ 3,90 €") baserat på panelens storlek.

Utgifterna kan begränsas med tre tak, av vilka det minsta gäller: **plånbokssaldo**, **tak per studie** och **tak per facilitator/månad**. När ett tak nås överskrider AI:n det inte utan faller kontrollerat tillbaka på den regelbaserade funktionen — processen fortsätter utan extra kostnad.

Det finns tre betalningsmodeller: plattformskrediter, egen API-nyckel (BYO) eller värdnyckel. Obs: "eget Claude-konto" avser en Anthropic **API-nyckel** (console.anthropic.com), inte ett claude.ai-abonnemang.

## När används vad — exempel

- **Känslig mänsklig panel** (t.ex. som berör patientdata) → **off**. Starkast integritetsskydd: inget skickas till en AI-tjänst.
- **En enskild forskare som behöver metodstöd** → **assist**. Fråga Pronoia + översättning; panelinnehållet stannar på maskinen.
- **En pilot utan en riktig panel** → **full**. AI-panelister simulerar argumentation (Route B) för att testa teserna.
- **En hybridpanel som saknar ett perspektiv** → **full, selektivt**. Några AI-panelister fyller luckan; människorna utgör stommen.
- **En stor flerspråkig panel** → **full + tak**. Runda 0 + översättning; sätt ett tak per studie i förväg.
- **En organisation som kör flera studier** → **full + egen API-nyckel**. Kostnaderna på egen faktura, data under egna villkor (datasuveränitet).

## Facilitatorns checklista

1. Välj läget medvetet — off är ett fullt likvärdigt alternativ.
2. I full-läget, granska pre-flight-uppskattningen och sätt vid behov ett tak per studie före generering.
3. Se till att panelisterna får informationen om AI-användning (inbjudan + /privacy).
4. Håll antalet AI-panelister motiverat — de kompletterar, de ersätter inte, verklig expertis.
