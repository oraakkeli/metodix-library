---
article_id: 12-ai-kayttomuodot
concept: ai-kayttomuodot
register: facilitator
lang: fi
source_lang: fi
translations:
- en
- sv
title: Tekoälyn käyttömuodot ja kustannukset
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

# Tekoälyn käyttömuodot ja kustannukset

Pronoiassa tekoäly on täydentävä työkalu, ei riippuvuus: jokainen Delfoi toimii täysin ilman tekoälyä, ja kaikki AI-toiminnot degradoituvat sääntöpohjaiseen varajärjestelmään. Tämä artikkeli kertoo, miten valitset tekoälyn käytön tietoisesti, mitä palveluita on tarjolla ja miten kustannukset pysyvät hallinnassa.

## Kolme moodia

Tekoälyn käyttö valitaan yhdellä asetuksella, joka on porrastettu sen mukaan, kuinka paljon dataa tekoälylle altistetaan:

- **Ei tekoälyä (off)** — mitään ei lähetetä tekoälypalveluun; koko prosessi ajetaan sääntöpohjaisesti.
- **Menetelmäapu (assist)** — oletus; vain fasilitoijan tuki (Kysy Pronoialta, profiilit, käännös). Panelistien tuottamaa sisältöä ei lähetetä ulos.
- **Täysi (full)** — lisäksi panelistisisältö: tekoälypanelistit, Kierros 0 -chat, PIRE-syvennys, koodausehdotukset.

Ennen kuin tutkimus siirtyy prosessiin (ensimmäisen kierroksen avaaminen), sinun on **valittava moodi tietoisesti**. "Ei tekoälyä" on siinä täysin yhdenvertainen vaihtoehto. Tasoa voi myöhemmin nostaa, mutta ei laskea sen alle, mihin panelistit ovat jo osallistuneet.

## Palvelut

**Menetelmäapu (assist riittää, ei panelistisisältöä):** Kysy Pronoialta (menetelmäneuvonta), profiiligenerointi (AI-panelistien profiilit ilmiökuvauksesta), käännös.

**Panelistisisältö (vaatii full-moodin):** tekoälypanelistit (synteettiset näkökulma-argumentit), Kierros 0 -intake-chat, PIRE-syvennys, koodausehdotukset.

Suurin mutta ennakoitavin erä ovat tekoälypanelistit (kustannus = panelistit × teesit × kierrokset). Kierros 0 -chat on pienin mutta arvaamattomin, koska se on interaktiivinen.

## Kustannukset ja katot

Tekoälyn taustakustannus muunnetaan kiinteiksi **krediiteiksi**, joten näet vain yhden muunnoksen (esim. 100 krediittiä = 1 €). Ennen jokaista ajoa näytetään **pre-flight-arvio** ("≈ 390 krediittiä ≈ 3,90 €") paneelin koon perusteella.

Kuluja voi rajata kolmella katolla, joista pienin sitoo: **kukkarosaldo**, **per-tutkimus-katto** ja **per-fasilitoija/kuukausi-katto**. Katon täytyttyä tekoäly ei ylitä sitä vaan putoaa hallitusti sääntöpohjaiseen toimintoon — prosessi jatkuu ilman lisäkuluja.

Maksumalleja on kolme: alustan kreditit, oma API-avain (BYO) tai isäntäavain. Huom: "oma Claude-tili" tarkoittaa Anthropicin **API-avainta** (console.anthropic.com), ei claude.ai-tilausta.

## Milloin mikäkin — esimerkkejä

- **Arkaluontoinen ihmispaneeli** (esim. potilastietoja sivuava) → **off**. Vahvin tietosuoja: mitään ei lähetetä tekoälypalveluun.
- **Yksittäinen tutkija, joka kaipaa menetelmätukea** → **assist**. Kysy Pronoialta + käännös; panelistisisältö pysyy koneella.
- **Pilotti ilman aitoa paneelia** → **full**. Tekoälypanelistit simuloivat argumentointia (Route B) teesien testaamiseksi.
- **Hybridipaneeli, jossa puuttuu näkökulma** → **full valikoidusti**. Muutama tekoälypanelisti täydentää katvealueen; ihmiset muodostavat rungon.
- **Iso monikielinen paneeli** → **full + katot**. Kierros 0 + käännös; aseta per-tutkimus-katto etukäteen.
- **Organisaatio, joka ajaa useita tutkimuksia** → **full + oma API-avain**. Kulut omalle laskulle, data omiin sopimusehtoihin (datasuvereniteetti).

## Fasilitoijan muistilista

1. Valitse moodi tietoisesti — off on täysveroinen vaihtoehto.
2. Full-moodissa katso pre-flight-arvio ja aseta tarvittaessa per-tutkimus-katto ennen generointia.
3. Varmista, että panelistit saavat paljastuksen tekoälyn käytöstä (kutsu + /privacy).
4. Pidä tekoälypanelistien määrä perusteltuna — ne täydentävät, eivät korvaa aitoa asiantuntemusta.
