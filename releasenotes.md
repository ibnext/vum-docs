# Releasenotes VUM Koppelvlak specificaties v3.0.0

Deze versie van de VUM Koppelvlak specificaties is gebaseerd op versie 1.5 van de VUM Gegevensstandaard.

Versie 3.0.0 van de VUM Koppelvlak specificaties introduceert een aantal vereenvoudigingen en verbeteringen ten opzichte van de voorgaande 2.0.0 release.:
Er sprake van zogenaamde breaking changes. Daarom is het major versienummer verhoogd van 2 naar 3.  

De belangrijkste wijzigingen zijn:

## Nieuwe, gewijzigde en verwijderde velden

### Competentiestructuur volledig vernieuwd
In v2 werd gewerkt met **Gedragscompetentie** met de volgende structuur:
- gedragscompetentie
- codeGedragscompetentie
- omschrijvingGedragscompetentie

In v3 is dit vervangen door **Competentiebeheersing**:
- codeCompetentie (hex)
- codeCompetentieniveau (L1–L4)

We gaan gebruik maken van de competentie codes van CompetentNL.    
De omschrijving van de competentie en het competentieniveau is daarmee niet meer opgenomen in de gegevensstandaard, maar kan worden opgehaald via de code.    
Ook de codes voor competentieniveau zijn gewijzigd naar een meer generieke structuur, zodat deze ook voor andere typen competenties dan gedragscompetenties kunnen worden gebruikt.  
<TODO: Uitleg wat die L1 t/m L4 inhouden>  
Vakvaardigheid is komen te vervallen, omdat ........

### Beroepsnaam → Beroep
In v2 bestond het type **Beroepsnaam** (gecodeerd/ongecodeerd).  
In v3 is dit vervangen door **Beroep** met een eenvoudiger structuur:
- codeBeroepsnaam

Er wordt dus geen onderscheid meer gemaakt tussen gecodeerd en ongecodeerd.  
Verwijzingen die voorheen werden gedaan naar Beroepsnaam (zoals in Werkervaring) verwijzen nu naar Beroep.

### Opleiding is gewijzigd    
In v2 bestond het type **Opleidingsnaam** (gecodeerd/ongecodeerd).    
In v3 is dit vervangen door **codeOpleidingsnaam**. Het betreft dus alleen een code en het type is gewijzigd naar een hexadecimale waarde van precies 10 posities.    
Dit is gedaan om straks beter te kunnen aansluiten op de codes van CompetentNL.

In v3 is **toelichtingOpleiding** toegevoegd om meer context te kunnen geven bij een opleiding.  
De volgende objecten zijn dus verwijderd t.b.v. verduidelijking en consistentie:
- Opleidingsnaam
- OpleidingsnaamGecodeerd
- OpleidingsnaamOngecodeerd

Verder zijn bestaande velden inhoudelijk hetzelfde gebleven.

### Cursus uitgebreid
In v3 zijn de volgende velden aan het type Cursus toegevoegd:
- indicatieCertificaat
- toelichtingCursus

Dit is gedaan om meer detail te kunnen geven over een cursus en een mogelijkheid tot toelichting.

### Mobiliteit aangescherpt
In v2 was **bemiddelingspostcode** optioneel.  
In V3 is dit veld verplicht gemaakt.

### URL‑lengte vergroot
De maximale lengte van type **URL** is gewijzigd van 500 naar 1000.

### AdresHouding sterk vereenvoudigd
In V2 was **AdresHouding** een uitgebreid en complex gegevenstype met meerdere subtypes.  
In V3 is dit vereenvoudigd tot een enkel gegevenstype **Adres** met de volgende structuur:  
- postcode
- straatnaam
- huisnummer
- huisnummertoevoeging

Dit **Adres** type is ons inziens voldoende om aan te geven wat het adres van een vacature of werkgever is.    
VUM beperkt zich tot Nederlandse adressen, een goede reden om buitenlandse adressen niet meer te ondersteunen.

## Ondersteuning van oudere API versies
<TODO: Beter uitleggen wat dit inhoudt en waarom dit mogelijk is, en wat de gevolgen zijn voor vraagstellers en bronnen>

De specificatie van de selectievraag is zodanig opgesteld dat toekomstige toevoegingen niet worden uitgesloten.  
Dit is mogelijk omdat JSON schemas zodanig kunnen worden geformuleerd dat niet-benoemde gegevens en operatoren worden toegestaan op het koppelvlak. Bij de verwerking van de selectievraag zullen deze niet-benoemde gegevens en operatoren genegeerd worden. Hiermee wordt het mogelijk om gedurende een overgangsperiode twee verschillende versies van de selectievraag gelijktijdig in de VUM keten te ondersteunen: 

* De koppelvlak specificaties staan toe dat onbenoemde gegevens en operatoren voorkomen in de selectievraag: 
	* toegevoegde gegevens en operatoren worden dan geaccepteerd op een koppelvlak van de voorgaande versie
	* verwijderde gegevens en operatoren die toch aanwezig zijn, worden dan niet geweigerd op een koppelvlak van de nieuwe versie

* De ontvangende systemen verwerken de gegevens en operatoren van de ontvangen selectievraag die binnen de door hun ondersteunde versie van de selectievraag vallen. De selectiecriteria in de selectievraag die buiten de ondersteunde versie vallen worden genegeerd.

Gedurende de overgangsperiode tussen twee versies kan het voorkomen dat niet alle selectiecriteria in een specifieke selectievraag door alle bronnen worden gehonoreerd. Bronnen zullen de criteria die buiten de door hun ondersteunde versie van de selectievraag vallen, niet toepassen en dit kan resultaten opleveren die anders door die selectiecriteria uitgesloten zouden worden. Een vraagsteller ontvangt dan mogelijk resultaten die niet aan alle selectiecriteria in de gestelde selectievraag voldoen. Mocht dit ongewenst zijn, dan kan de vraagsteller gedurende de overgangsperiode de ongewenste resultaten uitfilteren door deze selectiecriteria lokaal toe te passen op de ontvangen resultaten.
