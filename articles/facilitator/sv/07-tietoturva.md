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
version: '1.4'
last_updated: '2026-08-17'
license: CC-BY-4.0
authors:
- Metodix Oy
status: published
public: false
kb_include: true
original_source: Delphi-Pronoia frontend/help
---

# Säkerhet och transparens

Som facilitator är du studiens **personuppgiftsansvarig**: du ansvarar för vilka data
som samlas in, hur panelisterna informeras och hur deras rättigheter tillgodoses. Den
här artikeln samlar det väsentliga; den fullständiga redogörelsen finns i
`docs/SECURITY-TRANSPARENCY.md`.

## Var data finns

Materialet ligger på en **server inom EU** och behandlas enligt EU:s dataskyddsregler.
Trafiken är krypterad, panelisterna kommer in via personliga, tidsbegränsade
inbjudningslänkar utan lösenord,
säkerhetskopiorna stannar inom EU, och ändringar i programvaran passerar automatiska
kontroller och en stagingmiljö före produktion. Aktuella uppgifter om biträden och
lagringstider finns i den offentliga informationen: /privacy.

Data lämnar inte tjänsten av sig själv. De två situationer där det sker är båda dina
beslut: **användning av AI-funktionerna** och **export av materialet** (CSV,
DAE-handoff, rapporter).

> Som personuppgiftsansvarig, notera: infrastrukturleverantören och AI-tjänsten är
> personuppgiftsbiträden. Den aktuella förteckningen finns i informationen.

## Ditt konto och inloggning

En facilitator har ett **personligt konto**: e-post och lösenord. Delade inloggningar
används inte, eftersom en delad inloggning gör det omöjligt att i efterhand se vem som
gjorde vad — och omöjligt att ta bort åtkomsten för en person i taget.

- **Ett nytt konto uppstår ur en inbjudan.** Öppen registrering är stängd efter den
  första administratören. Kontoinbjudan är av engångstyp och går ut. (Panelistens
  inbjudningslänk är något annat: den är personlig och **återanvändbar** — samma adress
  bär hen från runda till runda — men även den går ut, och du kan förnya eller
  återkalla den på fliken Panelister. En förnyelse dödar den gamla länken, så det finns
  alltid exakt en giltig länk per panelist.)
- **Du kan återställa ditt lösenord själv** från inloggningssidan om e-postutskick är
  konfigurerat på servern. En administratör kan också återställa det.
- **Tvåstegsverifiering** är frivillig för alla och **obligatorisk för
  administratörer**. Du slår på den från din profilsida med en autentiseringsapp
  (Google Authenticator i telefonen, Apple Lösenord på en Mac, med flera). Spara
  reservkoderna vid aktiveringen — de visas inte en andra gång.
- **Du ser dina egna misslyckade inloggningsförsök.** Profilsidan berättar hur många
  misslyckade försök som hann samlas innan du senast kom in. Ett är vardag; flera i rad är
  skäl att byta lösenord och slå på tvåstegsverifiering. Enskilda försök loggas inte — det
  skulle bli ett register över IP- och e-postadresser — utan siffran är ett aggregat, och
  den är **din** uppgift, inte administratörens övervakningsvy.
- **Du ser dina egna sessioner.** Profilsidan listar de enheter där du är inloggad, och
  du kan avsluta vilken som helst av dem eller alla utom den nuvarande.

En administratör kan avsluta en användares sessioner utan att stänga kontot. Hen kan
**inte** se någon annans sessionslista och kan inte stänga av någon annans
tvåstegsverifiering.

## Vem ser din studie

En studie har tre roller:

| Roll | Ser | Kan ändra | Personuppgifter |
|---|---|---|---|
| **Ägare** | allt | allt, inkl. medlemmar, AI-läge, blindläge, radering | ja (utom i blindläge) |
| **Facilitator** | allt | studiens innehåll | ja (utom i blindläge) |
| **Betraktare** | resultat | ingenting | **aldrig** |

Betraktare är rollen du ger en finansiär eller en utvärderare: läsrätt till resultaten
är inte rätt till människorna bakom dem.

En studie kan tillhöra en **organisation** (universitet, kommun, företag). Då är
organisationens administratör ägare även när forskaren lämnar huset, och AI-kostnaderna
tas från organisationens plånbok. Utan organisation är studien personlig — det är
standard och fullt stött.

**Ägarskapet kan överföras** (sidan Team och behörigheter). Gör det innan du lämnar ett
projekt: en studie vars enda ägare är borta står stilla.

## Behörighetshistorik

Varje behörighetsändring skrivs till en oföränderlig logg: vem som lade till vem, vilken
roll som gällde före och efter, när en inbjudan skickades, återkallades eller
accepterades, när studien kopplades till en organisation och när blindläget stängdes av.
Loggen finns på studiens sida **Team och behörigheter** och är information på ägarnivå.

Det är det svar en institution frågar efter: *vem har haft åtkomst till den här panelen
och sedan när*. Rader redigeras eller raderas aldrig, och de överlever att studien eller
användaren tas bort.

## AI och Anthropic

När AI-funktionerna är på behandlas en del av datan via Anthropics API: helpdesken
skickar din fråga + metodbiblioteket, fördjupningsförslagen skickar teserna och
**panelisternas argument under pseudonymer** (P-NN), AI-panelisterna teser + profil.
**Namn och e-postadresser skickas aldrig** — bara pseudonymer och innehåll.

**Välj studiens AI-nivå** i inställningarna ("AI-användning i studien"): *Ingen AI*
(inget skickas till AI-tjänsten), *Endast metodhjälp* (standard; metodstöd, inget
panelinnehåll) eller *Full* (även AI-panelister, R0-chatt, fördjupning, kodning). Valet
grindar varje AI-anrop.

Vill du inte skicka något till AI-tjänsten i någon studie: **sätt inte
`ANTHROPIC_API_KEY`** (värdomkopplaren). AI-funktionerna degraderas då prydligt och
Pronoia fungerar utan AI-tjänsten oavsett studiens AI-nivå. Omkopplaren påverkar varken
var data finns eller exporterna.

## Anonymitet

Panelisterna ser varandra endast under pseudonymer. Läget **facilitator-blind** döljer
namn och e-postadresser även för dig. **Rekommendation för känsliga paneler: kör
facilitator-blind.** DAE-handoff och CSV-export innehåller **aldrig** namn eller
e-postadresser — oavsett blindinställningen. Kom ihåg: fritext kan avslöja en person
genom sitt innehåll även när identifieraren är dold.

Blindläget är att **göra sig själv blind**, inte teamhantering: det döljer identiteterna
för alla, även för den ägare som slog på det. Att stänga av det avslöjar varje panelist
för hela teamet, och **den handlingen skrivs till behörighetshistoriken**.

## Anonymisering när studien avslutas

När studien är klar, anonymisera den: knappen **🔒 Anonymisera studien** på fliken
Panelister tar permanent bort namn och e-postadresser och ogiltigförklarar
inbjudningslänkarna. Det som återstår är genuint anonyma forskningsdata — pseudonymer
utan nyckel till en person. Åtgärden är **oåterkallelig** (tvåstegsbekräftelse) och
tidsstämplas. Att anonymisera en öppen studie bryter panelisternas åtkomst — gör det
först på slutet.

## Regeln om små celler (n < 3)

En cell i panelmatrisen med färre än tre personer kan identifiera en person även utan
namn. Matrisens hälsokort varnar för sådana celler (🔒) och de följer med till
analysexporten som en maskinläsbar `small_cells`-lista. **Publicera inte siffror på
cellnivå från celler med färre än tre personer utan de berördas samtycke.**

Samma gräns upprätthålls i programmet: resultat på gruppnivå visas inte för grupper med
färre än tre, små grupper slås ihop till en "Övriga"-grupp, och om även den understiger
tre visas hela gruppindelningen inte alls — annars kunde en liten grupps siffror räknas
fram genom subtraktion från helheten.

## Meddelanden till panelister

Ett meddelande som skickas från kommunikationscentralen går till panelistens **e-post**
och till hens egen vy. Tre saker är värda att veta:

- **En panelist som dragit sig ur utesluts automatiskt.** Hen får varken meddelandet
  eller e-posten, och ingen ny länk kan skapas. Sammanfattningen visar hur många som
  hoppades över på den grunden.
- **Svarsadressen är studiens kontaktperson**, inte en automat. Panelisten kan svara
  direkt — och det är också ett skäl att svara: ett besvarat meddelande är en signal
  till e-postservrar om att avsändaren är äkta.
- **Du väljer vad som färdas i e-posten.** Den fullständiga formen bär med sig texten du
  skrev; aviseringsformen säger bara att det finns ett meddelande i panelen och länkar
  till hens egen sida. Välj aviseringsformen när meddelandet innehåller panelinnehåll
  som inte är avsett för inkorgar.

En påminnelse kan bära med sig **lägesuppgifter** (egen framfart, gruppens och panelens
framfart). Siffrorna räknas ut för varje mottagare separat och på hens eget språk, och
grupprad följer samma regel om färre än tre som alla andra gruppresultat.

## Offentlig dataskyddsinformation

På **/privacy** finns en offentlig dataskydds- och AI-information (fi/en/sv). Länken
läggs automatiskt till i varje inbjudan och i panelistens hemvy. Mer om AI-transparens:
artikeln *AI-transparens och AI-panelister*.

## Panelistens rättigheter

Informera panelisterna före R0: vad som samlas in och varför, om AI används, hur
anonymiteten fungerar, lagringstiden och rättigheterna (tillgång, rättelse,
**radering**). Radering stöds: du kan radera en studie, en panelist, en tes och en
kommentar, och en administratör kan radera ett användarkonto helt.

## Snabbkontroll före publicering

1. AI på eller av? Passar det materialets känslighet?
2. Känslig panel → facilitator-blind.
3. Panelisterna informerade? Inbjudan bär automatiskt AI-omnämnandet och /privacy-länken.
4. Teamets roller kontrollerade — är betraktare rätt roll för den som bara följer med?
5. AI-modellens version fastnaglad (reproducerbarhet, se AI-modelldokumentet)?
6. Exporter behandlas som konfidentiella; lagring och slutlig radering överenskomna.
7. Små celler i matrisen (n < 3) kontrollerade — inga siffror på cellnivå i rapporter
   utan samtycke.
8. När studien avslutas: 🔒 Anonymisera studien.
