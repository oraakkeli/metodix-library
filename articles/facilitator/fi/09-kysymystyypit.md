---
article_id: 09-kysymystyypit
concept: kysymystyypit
register: facilitator
lang: fi
source_lang: fi
translations:
- en
- sv
title: 'Kysymystyypit: valintaopas esimerkein'
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

# Kysymystyypit: valintaopas esimerkein

Pronoiassa on kymmenen kysymystyyppiä (+ kriteerimuuttujat). Tyypin valinta ratkaisee, *mitä paneelilta voi oppia*: sama aihe tuottaa eri tiedon asteikkona, ajoituksena tai resurssijakona. Nyrkkisääntö: valitse kevyin tyyppi, joka vastaa tutkimuskysymykseesi — ja pyydä aina perustelu.

## Perustyypit

### Asteikko (scale)
**Mikä:** panelisti arvioi väitettä numeroasteikolla (oletus 1–9); valinnaiset **kriteerimuuttujat** (esim. todennäköisyys × toivottavuus) tuottavat useita arvioita samasta teesistä.
**Käytä kun:** haluat mitata kannatusta, todennäköisyyttä tai toivottavuutta ja seurata konsensusta kierrosten yli. Delfoin työjuhta.
**Esimerkki:** *"Yleiskäyttöinen tekoäly hoitaa yli puolet kuntien asiakaspalvelusta vuoteen 2035 mennessä."* Kriteerit: todennäköisyys + toivottavuus.
**Tulos:** jakauma, keskiluvut, IQR, painopiste asteikolla; P×D-kuilu paljastaa uhka/toive-jännitteet.

### Avoin (open)
**Mikä:** pelkkä tekstivastaus, ei numeroarviota.
**Käytä kun:** kartoitat ilmiötä, jota et vielä osaa väittämiksi — kierroksen 0/1 ideointi, hiljaiset signaalit, käsitteiden keruu.
**Esimerkki:** *"Mikä on tärkein asiantuntijatyön muutos, jota kukaan ei vielä ota vakavasti?"*
**Tulos:** laadullinen aineisto argumenttianalyysiin; usein seuraavan kierroksen teesien raaka-aine.

### Järjestys (ranking)
**Mikä:** panelisti panee annetut vaihtoehdot paremmuusjärjestykseen.
**Käytä kun:** haluat prioriteettijärjestyksen rajatusta joukosta — mutta intensiteetillä ei ole väliä (vrt. panostus).
**Esimerkki:** *"Järjestä ajurit sen mukaan, mikä vaikuttaa eniten etäopetuksen laatuun: opettajien osaaminen · välineet · pedagogiset mallit · oppilaiden itseohjautuvuus."*
**Tulos:** keskimääräinen sijaluku per vaihtoehto; hajonta kertoo kiistanalaisimmat kohteet.

### Monivalinta (multichoice)
**Mikä:** valinta annetuista vaihtoehdoista (yksi tai useita).
**Käytä kun:** kysymys on luokittelu tai "mitkä näistä" — ei järjestystä eikä intensiteettiä.
**Esimerkki:** *"Mitkä esteet hidastavat tekoälyn käyttöönottoa organisaatiossasi eniten? (valitse 1–3)"*
**Tulos:** valintaosuudet; hyvä nopea kartta jatkokysymysten pohjaksi.

## Rakenne- ja priorisointityypit

### Ryhmittely (grouping)
**Mikä:** panelisti lajittelee aihiot fasilitoijan määrittelemiin koreihin raahaamalla (card-sort).
**Käytä kun:** haluat luokitella joukon ilmiöitä paneelin silmin — esim. signaalit kypsyyden, teesit hyväksyttävyyden tai toimet kiireellisyyden mukaan.
**Esimerkki:** aihiot = 8 heikkoa signaalia; korit = *Kuumat · Viileät · Kylmät*. Tai: toimenpiteet koreihin *Nyt · 3 v · 10 v · Ei koskaan*.
**Tulos:** per aihio korijakauma + modaalikori; erimielisyys näkyy hajontana korien välillä.

### Panostus (allocation)
**Mikä:** panelisti jakaa kiinteän summan (oletus 100 pistettä) vaihtoehtojen kesken.
**Käytä kun:** järjestys ei riitä vaan tarvitaan *kuinka paljon* — resurssien jako tai todennäköisyysmassan jako toisensa poissulkeville skenaarioille.
**Esimerkki:** *"Jaa 100 pistettä sen mukaan, miten kunnan pitäisi painottaa ilmastotoimia: liikenne · rakennukset · energia · ruoka · kompensaatiot."* Tai: *"Jaa 100 % neljälle skenaariolle todennäköisyyden mukaan."*
**Tulos:** keskimääräinen jako + hajonta per vaihtoehto; normalisoituna suora todennäköisyystulkinta.

### 2×2-sijoittelu (xy)
**Mikä:** panelisti sijoittaa aiheen pisteeksi kaksiakseliselle tasolle raahaamalla.
**Käytä kun:** kaksi ulottuvuutta pitää arvioida *suhteessa toisiinsa* — klassisesti vaikuttavuus × epävarmuus (skenaarioakselien johtaminen) tai todennäköisyys × toivottavuus yhtenä karttana.
**Esimerkki:** teesi = *"Kvanttilaskenta murtaa nykysalauksen"*; akselit = vaikuttavuus (x) × epävarmuus (y).
**Tulos:** sirontakuvio + keskipiste + kvadranttijakauma; kahden leirin hajonta eri kulmiin on itsessään löydös ja skenaarioakseliehdokas.

## Aikatyypit

### Aikaestimaatti (temporal)
**Mikä:** panelisti antaa **yhden vuoden**, jolloin väite toteutuu — tai "ei tässä aikaikkunassa".
**Käytä kun:** haluat nopean ajoitusarvion isolle teesijoukolle; jakauma kuvaa paneelin epävarmuuden.
**Esimerkki:** *"Minä vuonna yli puolet ylioppilaskirjoituksista tehdään tekoälyavusteisesti?"* (haarukka 2026–2050).
**Tulos:** vuosihistogrammi + mediaani + beyond-osuus. Kaksihuippuinen jakauma = ajoituserimielisyys.

### Aikaikkuna (timewindow)
**Mikä:** panelisti antaa **kaksi vuotta** (aikaisin–viimeistään) valitulla kriteerillä (*mahdollinen* tai *todennäköinen*); "ei koskaan" -vaihtoehto saatavilla.
**Käytä kun:** yksittäisen panelistin *oma epävarmuus* on osa dataa — kapea ikkuna on varma kanta, leveä epävarma. Analyyttisesti rikkaampi kuin temporal, raskaampi vastata.
**Esimerkki:** *"Fuusiovoimala syöttää sähköä Suomen verkkoon."* Kriteeri: todennäköinen; jana 2030–2070; never sallittu.
**Tulos:** ikkunajanat + mediaani-ikkuna + earliest/latest-kvartiilit + never-osuus; konsensus IQR-leveydestä.

### Aikasarja (timeseries)
**Mikä:** fasilitoija syöttää toteutuneen historia-aikasarjan, panelisti jatkaa sitä ≥3 tasavälisellä arviopisteellä (raahaus graafissa tai numerokentät).
**Käytä kun:** ilmiöllä on mitattava volyymi ja historiadataa — määrällinen ennakointi, jossa kaikki ankkuroituvat samaan lähtötilanteeseen.
**Esimerkki:** *"Etätyön osuus asiantuntijatyöpäivistä (%)"*: historia 2010–2025, arviot 2030/2035/2040.
**Tulos:** mediaanikäyrä + kvartiilivyöhyke historian jatkeena; vyöhykkeen leveneminen kertoo mihin asti paneelin näkymä kantaa.

## Pikavalinta

Kannatus/todennäköisyys → **asteikko** · ideointi → **avoin** · järjestys → **ranking** · luokat → **monivalinta** tai **ryhmittely** · kuinka paljon → **panostus** · kaksi ulottuvuutta → **2×2** · milloin (nopea) → **aikaestimaatti** · milloin + epävarmuus → **aikaikkuna** · paljonko tulevaisuudessa → **aikasarja**. Ja kaikissa: perustelu on se, mistä Delfoi elää.
