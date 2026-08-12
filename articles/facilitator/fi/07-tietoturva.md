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
version: '1.1'
last_updated: '2026-08-12'
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

## Oma tili ja kirjautuminen

Fasilitaattorilla on **henkilökohtainen tili**: sähköposti ja salasana. Jaettuja
tunnuksia ei käytetä, koska jaetusta tunnuksesta ei jälkikäteen näe kuka teki mitä —
eikä pääsyä voi poistaa yhdeltä ihmiseltä kerrallaan.

- **Uusi tili syntyy kutsusta.** Avoin rekisteröityminen on suljettu ensimmäisen
  ylläpitäjän jälkeen. Kutsulinkki on kertakäyttöinen ja vanhenee.
- **Salasanan voi palauttaa itse** kirjautumissivun linkistä, jos palvelimelle on
  määritetty sähköpostilähetys. Ylläpitäjä voi myös nollata sen.
- **Kaksivaiheinen tunnistautuminen** on kaikille vapaaehtoinen ja **ylläpitäjille
  pakollinen**. Se otetaan käyttöön omalta profiilisivulta autentikaattorisovelluksella
  (esim. Google Authenticator puhelimessa tai Applen Salasanat Macilla). Ota
  varakoodit talteen käyttöönoton yhteydessä — niitä ei näytetä toista kertaa.
- **Istunnot näet itse.** Profiilisivu listaa laitteet joilla olet kirjautuneena, ja
  voit katkaista minkä tahansa niistä tai kaikki muut kuin nykyisen.

Ylläpitäjä voi tarvittaessa katkaista käyttäjän istunnot sulkematta tiliä. Hän **ei**
näe kenenkään muun istuntolistaa eikä voi purkaa toisen kaksivaiheista.

## Kuka näkee tutkimuksesi

Tutkimuksella on kolme roolia:

| Rooli | Näkee | Voi muuttaa | Henkilötiedot |
|---|---|---|---|
| **Omistaja** | kaiken | kaiken, ml. jäsenet, AI-moodi, sokkous, poisto | kyllä (paitsi blind-tilassa) |
| **Fasilitaattori** | kaiken | tutkimuksen sisällön | kyllä (paitsi blind-tilassa) |
| **Katselija** | tulokset | ei mitään | **ei koskaan** |

Katselija on rooli jonka annat rahoittajalle tai arvioijalle: lukuoikeus tuloksiin ei
ole oikeus niiden takana oleviin ihmisiin.

Tutkimus voi kuulua **organisaatiolle** (yliopisto, kunta, yritys). Silloin
organisaation ylläpitäjä on omistaja myös silloin kun tekijä lähtee talosta, ja
tekoälykulut menevät organisaation kukkarosta. Ilman organisaatiota tutkimus on
henkilökohtainen — se on oletus ja täysin tuettu.

**Omistajuus on siirrettävissä** (Tiimi ja oikeudet -sivu). Tee se ennen kuin lähdet
projektista: tutkimus jonka ainoa omistaja on poistunut, on jumissa.

## Oikeushistoria

Jokainen oikeusmuutos kirjautuu muuttumattomaan lokiin: kuka lisäsi kenet, mikä rooli
oli ennen ja mikä nyt, milloin kutsu lähetettiin, peruttiin tai hyväksyttiin, milloin
tutkimus liitettiin organisaatioon ja milloin sokkous purettiin. Loki löytyy
tutkimuksen **Tiimi ja oikeudet** -sivulta ja on omistajatason tieto.

Tämä on se vastaus jonka laitos kysyy: *kenellä on ollut pääsy tähän paneeliin ja mistä
alkaen*. Rivejä ei muokata eikä poisteta, ja ne säilyvät vaikka tutkimus tai käyttäjä
poistettaisiin.

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
**koskaan** — riippumatta blind-asetuksesta. Muista: vapaateksti voi
paljastaa henkilön sisällön kautta, vaikka tunniste on piilossa.

Sokkous on **itsensä sokeuttamista**, ei tiiminhallintaa: se piilottaa henkilöllisyydet
kaikilta, myös omistajalta joka kytki sen päälle. Sen purkaminen paljastaa jokaisen
panelistin koko tiimille, ja **purku kirjautuu oikeushistoriaan**.

## Anonymisointi tutkimuksen päättyessä

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

Sama raja toteutuu myös ohjelmassa: ryhmätason tuloksia ei näytetä alle kolmen hengen
ryhmistä, pienet ryhmät niputetaan "Muut"-ryhmään, ja jos sekin jää alle kolmen, koko
ryhmäjako jätetään näyttämättä — muuten pienen ryhmän luvut voisi laskea
kokonaisuudesta vähentämällä.

## Julkinen tietosuojaseloste

Osoitteessa **/privacy** on julkinen tietosuoja- ja AI-seloste (fi/en/sv). Linkki
liitetään automaattisesti jokaiseen kutsuviestiin ja panelistin kotinäkymään.
AI-läpinäkyvyydestä tarkemmin: artikkeli *AI-läpinäkyvyys ja tekoälypanelistit*.

## Panelistin oikeudet

Informoi panelisteja ennen R0:aa: mitä kerätään ja miksi, käytetäänkö AI:ta, miten
anonymiteetti toimii, säilytysaika ja oikeudet (tarkastus, oikaisu, **poisto**).
Poisto on tuettu: voit poistaa tutkimuksen, panelistin, teesin ja kommentin, ja
ylläpitäjä voi poistaa käyttäjätilin kokonaan.

## Pikatarkistus ennen julkaisua

1. AI päällä vai ei? Sopiiko aineiston arkaluonteisuuteen?
2. Arkaluonteinen paneeli → facilitator-blind.
3. Panelistit informoitu? Kutsussa kulkee automaattisesti AI-maininta ja /privacy-linkki.
4. Tiimin roolit tarkistettu — onko katselija oikea rooli sille joka vain seuraa?
5. AI-mallin versio pinnattu (reprodusoitavuus, ks. AI-mallit-dokumentti)?
6. Vienti käsitellään luottamuksellisena; säilytys ja lopuksi poisto sovittu.
7. Matriisin pienet solut (n < 3) tarkistettu — ei solutason lukuja raportteihin ilman suostumusta.
8. Tutkimuksen päätyttyä: 🔒 Anonymisoi tutkimus.
