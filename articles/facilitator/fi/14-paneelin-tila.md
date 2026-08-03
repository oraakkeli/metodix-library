---
article_id: 14-paneelin-tila
concept: paneelin-tila
register: facilitator
lang: fi
source_lang: fi
translations:
- en
- sv
title: Paneelin tila — mitä mitataan ja miten sitä luetaan
order: 13
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

# Paneelin tila — mitä mitataan ja miten sitä luetaan

Kun kierros sulkeutuu, fasilitoijan ensimmäinen kysymys on aina sama: **missä paneeli nyt on?** Vastaus ei ole yksi luku vaan kolme kysymystä, jotka menevät helposti sekaisin.

- **Missä paneeli on?** Yhden teesin jakauma yhdellä kierroksella.
- **Pysyykö se siellä?** Kahden kierroksen välinen muutos — vakaus.
- **Onko siellä ketään?** Kuinka moni vastasi ja kuinka moni palasi — kattavuus.

Kolmas unohtuu useimmin, ja se on ratkaiseva. **Puuttuvaa ulottuvuutta ei voi korvata toisella.** Vakaa yksimielisyys, jonka tuotti kuusi jäljelle jäänyttä panelistia, ei ole vahvempi tulos kuin liikkuva erimielisyys neljälläkymmenellä. Siksi ekosysteemin kokoavat indikaattorit lasketaan **geometrisena** keskiarvona: jos yksi aliosa on nolla, koko luku on nolla eikä sitä voi kompensoida.

## Kolme mittaria, joita ei saa sekoittaa

**Yksimielisyys teesitasolla — Agreement A.** Perusmittari on van der Eijkin *Agreement A*, joka on tehty juuri järjestysasteikoille (1–5, 1–7, pakotettu ±3). Se kulkee välillä **−1 … +1**: +1 on täysi yksimielisyys, 0 tasainen hajonta, −1 paneelin jakautuminen asteikon kahteen päähän. Lasketaan yhdestä jakaumasta, ei tarvitse toista kierrosta.

**Prosessi — vakaus ja konvergenssi.** Kahden kierroksen välillä katsotaan, paljonko jakauma muuttui ja kapenivatko kvartiilit. Vakiintunut nyrkkisääntö on **15 %:n sääntö**: sitä pienempi muutos lasketaan vakaaksi. Suunta ja vakaus ovat eri asioita — jakauma voi kaventua ja silti heilua, tai pysyä leveänä ja täysin paikallaan. Jälkimmäinen on usein arvokkaampi löydös.

**Tutkimuksen tila — johtava indikaattori.** Teesitason luvut kootaan yhdeksi tilaksi, joka riippuu variaatiosta: **CDI, CCI, RCI tai BCI**.

Sekaannus näiden välillä on tavallisin virhe: "paneeli on yksimielinen" voi tarkoittaa mitä tahansa kolmesta, ja ne johtavat eri toimenpiteisiin.

## Miksi kynnys lasketaan eikä valita

Tämä on mittariston metodinen ydin, ja se muuttaa sitä miten lukuja luetaan.

A:lla on **voimakas positiivinen pienen otoksen harha**. Kahdeksan panelistin täysin satunnaisesta jakaumasta A on keskimäärin noin 0,20, ja joka kahdeskymmenes tuottaa jopa 0,55. Kiinteä kynnys — vaikkapa "yli 0,40 on konsensus" — saa pienen paneelin siis näyttämään yksimieliseltä silloinkin kun sen vastaukset ovat puhdasta kohinaa. Juuri tämä oli syy siihen, että testipaneelit näyttivät aina yhtenäisiltä.

Ratkaisu ei ole valita parempi kynnys vaan **johtaa se joka kerta**: ekosysteemi arpoo tuhansia satunnaispaneeleja, joilla on sama koko ja sama asteikko kuin teesilläsi, ja lukee kohinan ylärajan niistä. Viisiportaisella tai pidemmällä asteikolla katto noudattaa muotoa **≈ 1,55 / √n** — kolmellakymmenellä panelistilla noin 0,28, kahdeksalla yli 0,50. Lyhyemmällä asteikolla kerroin on suurempi: myös asteikon pituus vaikuttaa, ei vain vastaajamäärä.

Kaksi käytännön sääntöä:

- **Älä vertaa eri teesien A-lukuja ilman niiden kynnyksiä.** Myöhemmin syntynyt teesi, johon vastasi 12 ihmistä, ei ole yksimielisempi kuin 40 vastaajan teesi, vaikka luku olisi korkeampi.
- **Jokainen luku kertoo oman kriteerinsä.** Tuloksessa on aina käytetty kynnys ja sen peruste. Jos kriteeriä ei näy, lukua ei ole tarkoitettu raportoitavaksi.

Sama kuri koskee kuoppatestiä, nelikentän rakennetta ja ryhmäjaon selitysvoimaa. Yksikään kynnys ei ole käsivaraisesti valittu.

## Neljä paikkaa, joista erimielisyys löytyy

Yksimielinen luku ei ole todiste yksimielisyydestä. Paneeli voi olla erimielinen neljällä tavalla, joista vain ensimmäinen näkyy suoraan A:ssa.

**1. Negatiivinen A.** Klassinen kahtiajako, massaa asteikon molemmissa päissä. Selvin ja harvinaisin.

**2. Kuoppa jakaumassa.** Paneeli jakautuu kahtia niin lähelle toisiaan, että A jää positiiviseksi. Näin kävi CoWup-delfoin selvimmälle jakolinjalle: 43 % vastaan 54 % kuopan yli, A silti +0,16. Ilman erillistä kuoppatestiä paneelin kiinnostavin jako ei olisi päätynyt jännitekartalle. Testi on nollakalibroitu ja **vaatii ihmisvahvistuksen** — se on havainto, ei luokitus.

**3. Nelikentän antidiagonaali.** Kumpikin kriteerimuuttuja erikseen voi olla yksimielinen, ja paneeli silti jakautuu. Seuraava luku.

**4. Ryhmien välinen hajonta.** Kohtalainen A ei tarkoita, ettei kysymystä ymmärretty, vaan voi tarkoittaa **kahta sisäisesti johdonmukaista tulevaisuuskuvaa**, joiden summa näyttää hajanaiselta. Oppimisanalytiikka-delfoin teesi "Menetetty lupaus" sai aggregaatissa A = 0,39 — "kohtalaista yksimielisyyttä" — mutta tulevaisuuskuvan sisällä A oli 0,81. Tämä on Petri Tapion Disaggregative Policy Delphin lähtökohta, ja siitä seuraa sääntö: **matala A on kysymys, ei vastaus.**

## Kaksi kriteerimuuttujaa — nelikenttä ei ole kahden luvun summa

Teesiä arvioidaan tyypillisesti kahdella kriteerillä: todennäköinen ja toivottava (tai vaikuttava, tai toteutettavissa oleva). Näiden **yhteisjakauma on oma tietonsa**, ei reunajakaumien johdannainen.

Todiste on yksinkertainen. Paneeli, joka asettuu ruutuihin "epätodennäköinen & ei-toivottava" + "todennäköinen & toivottava", ja paneeli, joka asettuu ruutuihin "epätodennäköinen & toivottava" + "todennäköinen & ei-toivottava", tuottavat **täsmälleen samat reunajakaumat** — molemmilla akseleilla identtiset luvut. Silti ensimmäinen on sopusointuinen ja toinen repeää.

Nelikenttää luetaan akselit tuntien. Todennäköisyys × toivottavuus positiivisella yhteydellä on **toiveajattelua**: mitä toivon, pidän myös todennäköisenä — ja mitä en toivo, arvioin epätodennäköiseksi. Todennäköisyys × vaikuttavuus samalla yhteydellä ei ole sitä vaan toteamus "mitä todennäköisempi, sitä merkittävämpi". Ekosysteemi kieltäytyy nimeämästä ilmiötä, jos akseleita ei ole ilmoitettu.

## Variaatio ratkaisee, mitä luku tarkoittaa

Sama jakauma tarkoittaa eri asiaa eri variaatiossa. Siksi kullakin on **oma johtava indikaattorinsa** ja portti, joka on läpäistävä ennen kuin pääluku on luettavissa.

| Variaatio | Indikaattori | Aliosat | Portti — mitä ilman pääluku ei kelpaa |
|---|---|---|---|
| **Classical** | CCI | yksimielisyys × vakaus × kattavuus | **Vakaus.** Ilman sitä konsensusta ei tulkita lainkaan. |
| **Argument** | CDI | polarisaatio × vakaus × argumentaatio | **Argumentaatio.** Vakaa jakautuma ilman perusteluja ei ole tulos. |
| **Real-Time** | RCI | positio × asettuminen × altistus | **Asettuminen, sitten altistus.** Kanta ei kelpaa, jos vastaaja ei ole nähnyt ryhmän tilaa. |
| **Barometer** | BCI | muutoksen suuruus × jatkuvuusluottamus | **Vertailukelpoisuus.** Jos teesit tai paneeli vaihtuivat, muutos on artefakti. |

**Classical (CCI):** *eksploraatio → konvergenssi → kiteytyminen*, tai *dissensus*. Jos jakauma heiluu, ollaan yhä eksploraatiossa riippumatta siitä miten kapea se juuri nyt on. Vakaa kahtiajako ei ole epäonnistunut konsensus vaan **dissensus** — se siirtyy jänniteanalyysiin.

**Argument (CDI):** *eksploraatio → artikulaatio → kiteytyminen*, sivupolkuina *romahdus*, *divergenssi* ja *kohina*. Tässä hyvä uutinen on **korkea** CDI: perusteltuja, vakaita, kilpailevia tulevaisuuksia. Erimielisyyden katoaminen ei ole voitto vaan syy epäillä keinotekoista konsensusta. Vakaa mutta aliperusteltu jakautuma on *artikulaatio* — pyydä perustelut, älä uutta ääntä. Jos jakauma yhä liikkuu, ratkaisevaa on onko liike jäsentynyttä (*divergenssi*) vai ei (*kohina* — tarkista teesin muotoilu).

**Real-Time (RCI):** *kylvö → virtaus → asettuminen → asettunut → vahvistettu*. Kierroksettomassa asetelmassa vakaus tarkoittaa tasapainoa, ei kierrosten välistä eroa. Paneeli voi näyttää asettuneelta vain siksi, ettei osa ole palannut katsomaan — siksi altistus on oma porttinsa.

**Barometer (BCI):** *perustaso → vakaa → signaali → hälytys*, epäonnistumistilana *artefakti*. Tässä **muutos on löydös**, ei virhe — päinvastoin kuin muissa. Mutta se on luettavissa vasta kun aaltojen vertailukelpoisuus on todettu: hiljaa muokattu teesi tuottaa muutosta, joka kertoo teesistä eikä maailmasta.

**Ensimmäinen kierros on kaikissa erikoistapaus.** Vakautta ei ole, kun vertailukohtaa ei ole. Silloin indikaattori on määrittelemätön — ei nolla eikä arvaus. Yhden kierroksen "konsensus" on jakauman kuvaus, ei prosessin tulos.

## Puhuuko paneeli toisilleen?

Delfoi **olettaa** vuorovaikutusta: asiantuntijat näkevät toistensa perustelut ja kehittävät kantojaan. Ekosysteemi mittaa nyt myös tämän oletuksen, koska se osoittautui pettäväksi.

Kahden aidon delfoin kaikki 783 argumenttia seulottiin panelistien välisten viittausten varalta. Aitoja vertaisviitteitä löytyi **kaksi** — noin 0,5 %. Samaan aikaan fasilitoijalle suunnattu puhe (muokkausehdotukset, termihuomiot, kysymyksenasettelun kritiikki) oli yhdellä kierroksella yli neljännes kaikesta. Panelistit kirjoittivat aktiivisesti — yhteen suuntaan.

**Tämä ei ole paneelin vika.** Kummassakaan asetelmassa ei ollut kanavaa, jossa panelisti olisi voinut puhua toiselle: he eivät jättäneet keskustelematta, heille ei avattu keskustelua. Siksi sääntö on tiukka — monologista aineistoa **ei saa raportoida paneelin ominaisuutena** ("paneeli ei sitoutunut", "keskustelu jäi ohueksi") ennen kuin on selvitetty, oliko kanavaa olemassa. Se on asetelman tieto: kysyttävä, ei pääteltävä.

Sama koskee **ilmapiiriä**, joka johdetaan dialogiliikkeistä: jos liikkeitä ei ole rakenteellisesta syystä, ilmapiiriä ei raportoida lainkaan — ei myöskään "neutraalina". Tyhjästä jakaumasta ei lueta tunneilmastoa.

Pronoiassa kanava on olemassa: **dialogivaihe**, jossa panelisti näkee pseudonyymin vertaisnäkymän ja voi vastata toisten perusteluihin. Se on ainoa kohta, jossa vertaisviittaus voi syntyä — kierros 0:n valmisteleva chat käydään Kastalian kanssa, joten se on panelistin ja apurin välinen, ei panelistien. Mitattu 0,5 % on siis sekä dialogivaiheen menetelmällinen perustelu että lähtötaso, jota vasten sen vaikutus voidaan todeta.

## Missä mikäkin lasketaan

**Pronoiassa** PIRE tekee kierrosten välissä nopean triagen: mediaani, kvartiiliväli ja säädettävä kynnys → signaali ja ehdotettu operaatio. Se on **tarkoituksella karkea** ja tehty seuraavan kierroksen rakentamiseen, ei raportointiin; luettavuusmerkki palvelee samaa: se kertoo onko tulos luettavissa, ei onko paneeli yksimielinen. **DAE-analyysissä** lasketaan kalibroitu mittaristo — agreement A omine kynnyksineen, kuoppatesti, nelikenttä, ryhmäjaon selitysvoima ja variaation johtava indikaattori. Sieltä tulevat raportin luvut.

Kaksi rajaa pätee molemmissa:

- **Indikaattorit lasketaan vain ihmisäänistä.** Tekoälyn tuottama kanta ei ole panelistin ääni. AI-paneelin voi ajaa rinnalla vertailukohdaksi, mutta se raportoidaan erikseen — vertaillaan, ei sekoiteta.
- **Kone laskee, ihminen tulkitsee.** Kuoppatesti, ryhmien nimeäminen ja vertaisviittausten vahvistus ovat ihmisen työtä. Kone kertoo mistä katsoa, ei mitä nähdä.

## Fasilitoijan muistilista

- Kysy kolme kysymystä erikseen: missä paneeli on, pysyykö se siellä, onko siellä ketään.
- Älä lue yhden kierroksen konsensusta prosessin tuloksena — vakaus alkaa toisesta kierroksesta.
- Älä vertaa A-lukuja teesien välillä ilman kynnyksiä; pieni n nostaa lukua ilman että mikään muuttui.
- Kun A on kohtalainen, kysy onko hajonta jäsentymätöntä vai ryhmien välistä. Eri johtopäätös, eri toimenpide.
- Katso nelikenttää, älä kahta reunajakaumaa. Samat kaksi lukua kertovat kahdesta eri paneelista.
- Argumentti-delfoissa erimielisyyden katoaminen on epäilyttävää, ei onnistunutta.
- Ennen kuin luonnehdit paneelia hiljaiseksi, tarkista oliko sillä kanava puhua.

*Ks. myös "Konsensus vs. dissensus", "Orientaatiot N/S/R/E/D", "PIRE — kierrosväliapuri" ja "Pronoia ↔ DAE".*
