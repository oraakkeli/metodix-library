---
article_id: 07-tietoturva
concept: tietosuoja
register: facilitator
lang: sv
source_lang: fi
translations:
- en
- fi
title: Säkerhet och transparens
order: 7
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

# Säkerhet och transparens

Facilitatorn är studiens **personuppgiftsansvarig**: du ansvarar för vilka uppgifter som samlas in, hur panelister informeras och hur deras rättigheter tillgodoses. Den här artikeln samlar det väsentliga; den fullständiga redogörelsen finns i `docs/SECURITY-TRANSPARENCY.md`.

## Var data finns

Materialet finns på en **server inom EU** och behandlas i enlighet med EU:s dataskyddslagstiftning. Trafiken är krypterad, panelisterna når studien via engångslänkar utan lösenord, säkerhetskopior stannar inom EU, och ändringar i programvaran går genom automatiska kontroller och en staging-miljö före produktion. Aktuella personuppgiftsbiträden och lagringstider finns i det offentliga uttalandet: /privacy.

Materialet lämnar inte tjänsten automatiskt. De två situationer där det gör det är båda ditt beslut: **användning av AI-funktionerna** och **export av materialet** (CSV, DAE-handoff, rapporter).

> Som personuppgiftsansvarig: infrastrukturleverantören och AI-tjänsten är personuppgiftsbiträden. Den aktuella förteckningen finns i uttalandet.

## AI och Anthropic

När AI-funktioner är på behandlas en del data av Anthropics API: hjälpdesken skickar din fråga + metodbiblioteket, fördjupningsförslagen skickar teser och **panelisternas argument med pseudonymer** (P-NN), AI-panelisterna teser + profil. **Namn eller e-post skickas aldrig** — endast pseudonymer och innehåll.

**Välj studiens AI-nivå** i inställningarna (”AI-användning i denna studie”): *Ingen AI* (inget skickas till AI-tjänsten), *Endast hjälp* (standard; endast metodhjälp, inget panelinnehåll), eller *Full* (även AI-panelister, R0-chatt, fördjupning, kodning). Valet grindar varje AI-anrop.

Om du inte vill skicka något till en AI-tjänst i någon studie: **sätt inte `ANTHROPIC_API_KEY`** (huvudströmbrytare). Då degraderas AI-funktionerna prydligt och Pronoia körs utan AI-tjänst oavsett studiens AI-nivå. Strömbrytaren påverkar varken var materialet finns eller exporter.

## Anonymitet

Panelister ser bara varandra med pseudonymer. **Facilitator-blind**-läget döljer namn och e-post även för dig. **Rekommendation för känsliga paneler: kör facilitator-blind.** DAE-handoffen och CSV-exporten innehåller **aldrig** namn eller e-post — oavsett blind-inställningen (fr.o.m. 07/2026). Kom ihåg: fritext kan röja en person via innehållet, även om identifieraren är dold.

## Anonymisering när studien avslutas (07/2026)

När studien är klar, anonymisera den: knappen **🔒 Anonymisera studien** på fliken Panelister raderar namn och e-post permanent och spärrar inbjudningslänkarna. Kvarvarande material är genuint anonym forskningsdata — pseudonymer utan nyckel till en person. Åtgärden är **oåterkallelig** (tvåstegsbekräftelse) och registreras med tidsstämpel. Anonymisering av en öppen studie bryter panelisternas åtkomst — gör det först i slutet.

## Regeln om små celler (n < 3)

En matriscell med färre än tre människor kan identifiera en person även utan namn. Matrisens hälsokort varnar för sådana celler (🔒), och de följer med som en maskinläsbar `small_cells`-lista i analysexporten. **Publicera inte siffror på cellnivå för celler med färre än tre personer utan deras samtycke.**

## Åtkomstnyckel (produktion)

I produktion är facilitatormiljön skyddad med en åtkomstnyckel: webbläsaren frågar efter den första gången och kommer ihåg den. Nyckeln fås av administratören. Panelisternas svarslänkar fungerar utan nyckel. (I lokal utveckling frågas ingen nyckel.)

## Offentlig dataskyddsinformation

På **/privacy** finns en offentlig dataskydds- och AI-information (fi/en/sv). Länken bifogas automatiskt i varje inbjudan och på panelistens hemvy. Mer om AI-transparens: artikeln *AI-transparens och AI-panelister*.

## Panelistens rättigheter

Informera panelister före R0: vad som samlas in och varför, om AI används, hur anonymiteten fungerar, lagringstid och rättigheter (tillgång, rättelse, **radering**). Radering stöds: du kan ta bort en studie, en panelist, en tes och en kommentar.

## Snabbkontroll före publicering

1. AI på eller av? Passar det materialets känslighet?
2. Känslig panel → facilitator-blind.
3. Panelister informerade? Inbjudan innehåller automatiskt AI-meddelandet och /privacy-länken.
4. AI-modellens version fastnaglad (reproducerbarhet, se AI-modeller-dokumentet)?
5. Export behandlas konfidentiellt; lagring och slutlig radering överenskommen.
6. Små matrisceller (n < 3) kontrollerade — inga siffror på cellnivå i rapporter utan samtycke.
7. När studien avslutas: 🔒 Anonymisera studien.
