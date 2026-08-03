---
article_id: 10-ai-lapinakyvyys
concept: ai-lapinakyvyys
register: facilitator
lang: fi
source_lang: fi
translations:
- en
- sv
title: AI-läpinäkyvyys ja tekoälypanelistit
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

# AI-läpinäkyvyys ja tekoälypanelistit

Pronoia käyttää tekoälyä kahdessa roolissa: **tekoälypanelistit** osallistuvat paneeliin synteettisinä näkökulmina, ja **AI-generointitoiminnot** avustavat fasilitoijaa (esim. teesiluonnokset, yhteenvedot). Tämä artikkeli kuvaa, miten tekoälyn käyttö tehdään näkyväksi — sekä siksi, että EU:n AI-asetus (2024/1689, art. 50) sitä edellyttää 2.8.2026 alkaen, että ennen kaikkea siksi, että Delfoi-tutkimuksen validiteetti vaatii synteettisen ja inhimillisen argumentin erottamista kaikissa vaiheissa.

## Mitä panelisti näkee

Kun tutkimuksessa on tekoälypanelisteja, panelistille näytetään **AI-ilmoitus** kotinäkymässä ennen vastaamisen aloittamista. Ilmoitus kertoo tekoälypanelistien läsnäolon, määrän ja merkintätavan. Ilmoitusta ei voi piilottaa. Voit täydentää vakiotekstiä tutkimuskohtaisella huomautuksella (genai-huomautus tutkimuksen asetuksissa) — esimerkiksi kertomalla, miksi tekoälypanelisteja käytetään juuri tässä tutkimuksessa.

Dialogissa ja tuloksissa tekoälypanelistien sisältö on aina merkitty 🤖-tunnisteella. Panelistit näkevät tekoälypanelisteista pseudonyymin tunnisteen kuten ihmisistäkin — mutta AI-alkuisena.

## Mitä fasilitoija näkee

Fasilitaattorinäkymässä tekoälypanelistit erottuvat muodossa **AI · rooli** (esim. "AI · ilmastotutkija"). Paneelin osallistujakortti näyttää ihmisten ja tekoälypanelistien määrät erikseen (👤 / 🤖).

## Koneluettava merkintä exporteissa

Kaikki analyysiin lähtevä data kantaa eksplisiittisen AI-merkinnän:

- **DAE Handoff (JSON)**: jokainen panelisti-, argumentti-, dialogi- ja revisiotietue sisältää `ai_generated`-kentän (true/false). Payloadin `ai_provenance`-lohko kokoaa yhteenvedon: tekoälypanelistien määrä, käytetty oletusmalli ja merkintäkentät.
- **CSV-export**: `ai_generated`-sarake jokaisella rivillä.

DAE-analyysiputki hyödyntää näitä merkintöjä pitääkseen synteettiset ja inhimilliset argumentit erillään — merkintä ei siis ole vain sääntelyvaatimus vaan analyysin laadun edellytys.

## Tietosuoja AI-toiminnoissa

AI-generointi käyttää Anthropicin Claude-API:a. Panelistien avovastaukset lähetetään API:in **ilman identiteettitietoja** (vain pseudonyymi). API-dataa ei käytetä mallien koulutukseen. Kaikilla AI-toiminnoilla on sääntöpohjainen varajärjestelmä, joten tutkimus toimii myös kokonaan ilman tekoälyä.

## Fasilitoijan muistilista

1. Kerro tekoälypanelistien käytöstä jo kutsuviestissä — älä anna sen tulla yllätyksenä.
2. Kirjoita tutkimuskohtainen genai-huomautus: miksi AI-panelisteja käytetään ja mihin niiden profiilit perustuvat.
3. Älä poista AI-merkintöjä raporteista tai julkaisuista — merkintä on sekä lakisääteinen että menetelmällinen vaatimus.
