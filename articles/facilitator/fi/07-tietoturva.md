---
article_id: 07-tietoturva
concept: tietosuoja
register: facilitator
lang: fi
source_lang: fi
translations:
- en
- sv
title: Tietoturva ja läpinäkyvyys
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

# Tietoturva ja läpinäkyvyys

Fasilitoija on tutkimuksen **rekisterinpitäjä**: vastaat siitä, mitä dataa kerätään,
miten panelisteja informoidaan ja miten heidän oikeutensa toteutuvat. Tämä artikkeli
kokoaa olennaisen; täysi seloste on `docs/SECURITY-TRANSPARENCY.md`.

## Missä data on

Aineisto sijaitsee **EU-alueella olevalla palvelimella** ja sitä käsitellään EU:n
tietosuojasäädösten mukaisesti. Liikenne on salattua, panelistien pääsy tapahtuu
kertakäyttöisillä kutsulinkeillä ilman salasanoja, varmuuskopiot pysyvät EU-alueella,
ja ohjelmiston muutokset kulkevat automaattitarkistusten ja staging-ympäristön kautta
ennen tuotantoa. Ajantasaiset tiedot käsittelijöistä ja säilytysajoista ovat julkisessa
selosteessa: /privacy.

Aineisto ei lähde palvelusta automaattisesti. Kaksi tilannetta, joissa se lähtee, ovat
molemmat sinun päätöksiäsi: **AI-ominaisuuksien käyttö** ja **aineiston vienti** (CSV,
DAE-handoff, raportit).

> Rekisterinpitäjänä huomaa: palvelininfrastruktuurin tarjoaja ja tekoälypalvelu ovat
> henkilötietojen käsittelijöitä. Ajantasainen luettelo on selosteessa.

## AI ja Anthropic

Kun AI-ominaisuudet ovat päällä, osa datasta käsitellään Anthropicin API:lla:
helpdesk lähettää kysymyksesi + metodikirjaston, syventämisehdotukset lähettävät teesit
ja **panelistien argumentit pseudonyymeillä** (P-NN), AI-panelistit teesit + profiilin.
**Nimiä tai sähköposteja ei lähetetä koskaan** — vain pseudonyymejä ja sisältöä.

**Valitse tutkimuksen AI-taso** asetuksista ("Tekoälyn käyttö tutkimuksessa"):
*Ei tekoälyä* (mitään ei lähetetä tekoälypalveluun), *Vain ohjeapu* (oletus; vain metodiapu, ei paneelin
sisältöä), tai *Täysi* (myös AI-panelistit, R0-chat, syventäminen, koodaus). Valinta
portittaa jokaisen AI-kutsun.

Jos et halua lähettää mitään tekoälypalveluun millään tutkimuksella: **älä aseta
`ANTHROPIC_API_KEY`:tä** (isäntäkytkin). Silloin AI-ominaisuudet degradoituvat siististi
ja Pronoia toimii ilman tekoälypalvelua riippumatta tutkimuksen AI-tasosta. Kytkin ei
koske aineiston sijaintia eikä vientejä.

## Anonymiteetti

Panelistit näkevät toisensa vain pseudonyymeillä. **Facilitator-blind** -tila piilottaa
nimet ja sähköpostit myös sinulta. **Suositus arkaluonteisiin paneeleihin: aja
facilitator-blind.** DAE-handoff ja CSV-vienti eivät sisällä nimiä tai sähköposteja
**koskaan** — riippumatta blind-asetuksesta (07/2026 alkaen). Muista: vapaateksti voi
paljastaa henkilön sisällön kautta, vaikka tunniste on piilossa.

## Anonymisointi tutkimuksen päättyessä (07/2026)

Kun tutkimus on valmis, anonymisoi se: **Panelistit-välilehden 🔒 Anonymisoi tutkimus**
-nappi poistaa nimet ja sähköpostit pysyvästi ja mitätöi kutsulinkit. Jäljelle jäävä
aineisto on aidosti anonyymiä tutkimusdataa — pseudonyymejä ilman avainta henkilöön.
Toiminto on **peruuttamaton** (kaksivaiheinen varmistus) ja kirjautuu aikaleimalla.
Avoimen tutkimuksen anonymisointi katkaisee panelistien pääsyn — tee se vasta lopuksi.

## Pienten solujen sääntö (n < 3)

Paneelimatriisin solu, jossa on alle kolme ihmistä, voi yksilöidä henkilön ilman
nimeäkin. Matriisin terveyskortti varoittaa tällaisista soluista (🔒), ja ne kulkevat
koneluettavana `small_cells`-listana analyysivientiin. **Älä julkaise solutason lukuja
alle kolmen hengen soluista ilman asianomaisten suostumusta.**

## Pääsyavain (tuotantoympäristö)

Tuotannossa fasilitaattoriympäristö on suojattu pääsyavaimella: selain kysyy avainta
ensimmäisellä kerralla ja muistaa sen. Avaimen saat ylläpitäjältä. Panelistien
vastauslinkit toimivat ilman avainta. (Paikallisessa kehitysajossa avainta ei kysytä.)

## Julkinen tietosuojaseloste

Osoitteessa **/privacy** on julkinen tietosuoja- ja AI-seloste (fi/en/sv). Linkki
liitetään automaattisesti jokaiseen kutsuviestiin ja panelistin kotinäkymään.
AI-läpinäkyvyydestä tarkemmin: artikkeli *AI-läpinäkyvyys ja tekoälypanelistit*.

## Panelistin oikeudet

Informoi panelisteja ennen R0:aa: mitä kerätään ja miksi, käytetäänkö AI:ta, miten
anonymiteetti toimii, säilytysaika ja oikeudet (tarkastus, oikaisu, **poisto**).
Poisto on tuettu: voit poistaa tutkimuksen, panelistin, teesin ja kommentin.

## Pikatarkistus ennen julkaisua

1. AI päällä vai ei? Sopiiko aineiston arkaluonteisuuteen?
2. Arkaluonteinen paneeli → facilitator-blind.
3. Panelistit informoitu? Kutsussa kulkee automaattisesti AI-maininta ja /privacy-linkki.
4. AI-mallin versio pinnattu (reprodusoitavuus, ks. AI-mallit-dokumentti)?
5. Vienti käsitellään luottamuksellisena; säilytys ja lopuksi poisto sovittu.
6. Matriisin pienet solut (n < 3) tarkistettu — ei solutason lukuja raportteihin ilman suostumusta.
7. Tutkimuksen päätyttyä: 🔒 Anonymisoi tutkimus.
