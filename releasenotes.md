# Releasenotes VUM Koppelvlak specificaties v3.0.0

Deze versie van de VUM Koppelvlak specificaties is gebaseerd op versie 1.5 van de VUM Gegevensstandaard.

Versie 3.0.0 van de VUM Koppelvlak specificaties introduceert een aantal vereenvoudigingen en verbeteringen ten opzichte van de voorgaande 2.0.0 release.  
Er is sprake van zogenaamde breaking changes. Daarom is het major versienummer verhoogd van 2 naar 3.  

De belangrijkste wijzigingen zijn:

### Algemeen
- Binnen de entiteit **Webadres** is attribuut **URL** verlengd van een maximum van 512 naar 1000 posities
  - URL's kunnen en mogen tegenwoordig langer zijn dan 512 posities. Deze verlenging zorgt ervoor dat ook langere URL's correct kunnen worden verwerkt.
- Binnen de entiteit **Mobiliteit** is attribuut **Bemiddelingspostcode** verplicht gesteld in het resultaat van een zoekvraag naar werkzoekenden
- Binnen de entiteit **Adres** is attribuut **Postcode** verplicht gesteld in het resultaat van een zoekvraag naar vacatures

Een aantal velden zijn nu toegevoegd aan het resultaat van een eerste zoekvraag.  

**Voor vacatures:**
- Werkgever
  - handelsnaamOrganisatie
  - webadres
- ArbeidsVoorwaarden
  - omschrijvingArbeidsvoorwaarden
- Opleiding
  - toelichtingOpleiding
- Sollicitatiewijze
  - webadres
- Vervoermiddel
  - codeVervoermiddel

**Voor werkzoekenden:**
- Arbeidsmarktkwalificatie
    - Interesse
      - naamInteresse
    - Opleiding
        - toelichtingOpleiding
        - codeStatusOpleiding
        - datumAanvangVolgenOpleiding
        - datumEindeVolgenOpleiding
        - naamOpleidingsinstituut
- Vervoermiddel
  - codeVervoermiddel
- Opleiding:
  - toelichtingOpleiding
  - codeStatusOpleiding
  - datumAanvangVolgenOpleiding
  - datumEindeVolgenOpleiding
  - naamOpleidingsinstituut
- Werkervaring:
  - toelichtingWerkervaring

## Nieuwe, gewijzigde en verwijderde entiteiten en attributen

### Verwijderd uit Flexibiliteit
Binnen de entiteit **Flexibiliteit** (alleen binnen het koppelvlak Vacatures) is attribuut **datumAanvangBeschikbaarVoorWerk** verwijderd.  
Dit veld is in het verleden foutief overgenomen uit het koppelvlak voor werkzoekenden. Verder heeft dit gegeven dezelfde dekking als datumaanvangWerkzaamheden.

### Competentiestructuur volledig vernieuwd
In v2 werd gewerkt met **Gedragscompetentie** met de volgende structuur:
- gedragscompetentie
- codeGedragscompetentie
- omschrijvingGedragscompetentie

In v3 is dit vervangen door **Competentiebeheersing** bestaande uit enkel het attribuut:
- codeCompetentie (URI)

We gaan gebruik maken van de competenties van CompetentNL (skills).    
De entiteit **Gedragscompetentie** is daarmee niet meer opgenomen in de gegevensstandaard, maar kan worden opgehaald via een referentie bij CompetentNL.

### Beroepsnaam → Beroep
In v2 bestond het type **Beroepsnaam** (gecodeerd/ongecodeerd).  
In v3 is dit vervangen door **Beroep** met een eenvoudiger structuur:
- codeBeroepsnaam (URI)

Er wordt dus geen onderscheid meer gemaakt tussen gecodeerd en ongecodeerd.  
Verwijzingen die voorheen werden gedaan naar Beroepsnaam (zoals in Werkervaring) verwijzen nu naar Beroep.

### Opleiding is gewijzigd    
In v2 bestond het type **Opleidingsnaam** (gecodeerd/ongecodeerd).    
In v3 is dit vervangen door **codeOpleidingsnaam** en verwijst naar een id van het type URI zoals gebruikt in de CompetentNL API.    
CompetentNL zal hier dus leidend zijn t.a.v. gedefinieerde beroepen.

In v3 is **toelichtingOpleiding** toegevoegd om meer context te kunnen geven bij een opleiding.  
De volgende objecten zijn dus verwijderd t.b.v. verduidelijking en consistentie:
- Opleidingsnaam
- OpleidingsnaamGecodeerd
- OpleidingsnaamOngecodeerd

Verder zijn bestaande attributen inhoudelijk hetzelfde gebleven.

### Cursus uitgebreid
In v3 zijn de volgende attributen aan het type Cursus toegevoegd:
- indicatieCertificaat
- toelichtingCursus

Dit is gedaan om meer detail te kunnen geven over een cursus en een mogelijkheid tot toelichting.

### Mobiliteit aangescherpt
In v3 is het veld **bemiddelingspostcode** als antwoord op een eerste zoekvraag voor werkzoekenden verplicht gemaakt.

### AdresHouding sterk vereenvoudigd
In V2 was **AdresHouding** een uitgebreid en complex gegevenstype met meerdere subtypes.  
In V3 is dit vereenvoudigd tot een enkel gegevenstype **Adres** met de volgende structuur:  
- postcode
- straatnaam
- huisnummer
- huisnummertoevoeging

Dit **Adres** type is ons inziens voldoende om aan te geven wat het adres van een vacature of werkgever is.    
VUM beperkt zich tot de Nederlandse arbeidsmarkt. Matching o.b.v. buitenlandse adressen wordt niet ondersteund binnen de historische werking van VUM.  
Om die reden is ook **Voorkeursland** verwijderd.

### Indicatie LDR registratie alleen nog beschikbaar in detail resultaten werkzoeken  
**indicatieLdrRegistratie** is overal verwijderd, behalve uit de detail resultaten van werkzoekenden. 
Dit veld is privacygevoelig en daarom alleen nog maar te zien in de details.

### Uitbreiding zoekselecties
- Bij het zoeken naar werkzoekende profielen is het nu mogelijk om te zoeken op **datumAanvangBeschikbaarVoorWerk**.

### Uitbreiding eerste zoekresultaat
- Binnen de entiteit **Vacature** zijn de attributen **omschrijvingVacature**, **naamVacature** en **Webadres** nu ook beschikbaar in het antwoord op een eerste zoekvraag voor vacatures
- Binnen de entiteit **Werkgever** is het attribuut **HandelsnaamOrganisatie** nu ook beschikbaar in het antwoord op een eerste zoekvraag voor vacatures
- Binnen de entiteit **Arbeidsvoorwaarden** is het attribuut **omschrijvingArbeidsvoorwaarden** nu ook beschikbaar in het antwoord op een eerste zoekvraag voor vacatures
- Alle gegevens uit de entiteit **Opleiding** zijn nu beschikbaar binnen het antwoord van een eerste zoekvraag.
- Alle gegevens uit de entiteit **Cursus** zijn nu beschikbaar binnen het antwoord van een eerste zoekvraag.

### Voorbereidingen Introductie CompetentNL
We spraken al eerder over de rol van CompetentNL t.a.v. beroepen en competenties.  
Hieronder nog een keer een samenvatting van de voorbereidingen daarvoor:
- Binnen de entiteit **Beroep** is attribuut **codeBeroepsnaam** gewijzigd van een variable alfanumerieke waarde van maximaal 10 posities naar een URI die verwijst naar een Beroep gedefinieerd bij ComponentNL.   
- Ook binnen de toegevoegde entiteit **Competentiebeheersing** wordt attribuut **codeCompetentie** getypeerd als een URI, zijnde een referentie naar een **Competentie/Skill** bij CompetentNL.  

## Ondersteuning van oudere API‑versies
Onze specificatie voor de selectievraag is zo ontworpen dat nieuwe uitbreidingen in toekomstige minor versies geen breuk veroorzaken met bestaande implementaties. Dit betekent dat een bron of vraagsteller tijdelijk met verschillende versies van de selectievraag kan werken zonder dat het koppelvlak direct moet worden aangepast.

### Hoe dit technisch mogelijk is
De JSON‑schemas van het koppelvlak staan toe dat onbekende of niet‑gedefinieerde attributen en operatoren in de selectievraag voorkomen. Deze worden:
- geaccepteerd door systemen die een oudere versie ondersteunen, en
- genegeerd bij de verwerking als ze niet binnen de ondersteunde versie vallen.

Hierdoor ontstaat een soepele overgang tussen versies:
- Nieuwe attributen/operatoren kunnen al worden meegestuurd, ook als een bron nog een oudere versie ondersteunt.
- Verwijderde attributen/operatoren veroorzaken geen foutmeldingen bij systemen die al op de nieuwe versie zitten.

### Wat dit betekent voor bronnen
Een bron verwerkt alleen de selectiecriteria die binnen de door die bron ondersteunde versie vallen.  
Criteria die horen bij een nieuwere versie worden genegeerd. De bron levert dus resultaten op basis van de subset van criteria die hij begrijpt.

### Wat dit betekent voor vraagstellers
Tijdens een overgangsperiode kan het voorkomen dat:
- niet alle bronnen alle selectiecriteria toepassen, en
- de uiteindelijke resultaten daardoor records bevatten die door nieuwere selectiecriteria eigenlijk uitgesloten zouden worden.

Als een vraagsteller wil voorkomen dat deze “te brede” resultaten worden teruggegeven, kan hij tijdens de overgangsperiode de ontbrekende selectiecriteria lokaal toepassen op de ontvangen resultaten.

### Praktische gevolgen tijdens een versieovergang
- Gedurende de overgangsperiode kunnen verschillende bronnen verschillende versies ondersteunen.
- De selectievraag blijft geldig voor alle bronnen, maar niet alle criteria worden overal toegepast.
- Vraagstellers die volledige consistentie nodig hebben, moeten zelf aanvullende filtering uitvoeren.