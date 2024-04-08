# Releasenotes VUM Koppelvlak specificaties v2.0.0

Versie 2.0.0 van de VUM Koppelvlak specificaties introduceert twee significante wijzigingen ten opzichte van de voorgaande 1.2.0 release:

* De zoekvraag van versie 1.2.0 is vervangen door de selectievraag in versie 2.0.0. De selectievraag neemt het JSON query formaat van MongoDB als kader en maakt gebruik van expliciete operatoren waarmee de gewenste selectie eenduidig uitgedrukt kan worden door de vraagstellende bemiddelaar. 
* De selectieresultaten worden vanaf versie 2.0.0 opgeleverd in het response bericht van de selectiedialoog. In versie 1.2.0 en daarvoor werden de zoekvraagresultaten asynchroon naar een callback server opgeleverd.

Daarnaast zijn in versie 2.0.0 de openstaande aandachtspunten opgelost met betrekking tot de weergave van de VUM Gegevensstandaard in JSON objecten.

De nieuwe selectievraag en de synchrone beantwoording van de selectievraag zijn "breaking changes" ten opzichte van de voorgaande versie en leiden tot een ophoging van het major versienummmer. De releasenotes van de voorgaande 1.x.x versies zijn met deze wijzigingen verminderd relevant en zijn daarom niet meer in dit document opgenomen.


## Toekomstige wijzigingen in de selectievraag

De specificatie van de selectievraag is zodanig opgesteld dat toekomstige toevoegingen niet worden uitgesloten. Dit is mogelijk omdat JSON schemas zodanig kunnen worden geformuleerd dat niet-benoemde gegevens en operatoren worden toegestaan op het koppelvlak. Bij de verwerking van de selectievraag zullen deze niet-benoemde gegevens en operatoren genegeerd worden. Hiermee wordt het mogelijk om gedurende een overgangsperiode twee verschillende versies van de selectievraag gelijktijdig in de VUM keten te ondersteunen: 

* De koppelvlak specificaties staan toe dat onbenoemde gegevens en operatoren voorkomen in de selectievraag: 
	* toegevoegde gegevens en operatoren worden dan geaccepteerd op een koppelvlak van de voorgaande versie
	* verwijderde gegevens en operatoren die toch aanwezig zijn, worden dan niet geweigerd op een koppelvlak van de nieuwe versie

* De ontvangende systemen verwerken de gegevens en operatoren van de ontvangen selectievraag die binnen de door hun ondersteunde versie van de selectievraag vallen. De selectiecriteria in de selectievraag die buiten de ondersteunde versie vallen worden genegeerd.

Gedurende de overgangsperiode tussen twee versies kan het voorkomen dat niet alle selectiecriteria in een specifieke selectievraag door alle bronnen worden gehonoreerd. Bronnen zullen de criteria die buiten de door hun ondersteunde versie van de selectievraag vallen, niet toepassen en dit kan resultaten opleveren die anders door die selectiecriteria uitgesloten zouden worden. Een vraagsteller ontvangt dan mogelijk resultaten die niet aan alle selectiecriteria in de gestelde selectievraag voldoen. Mocht dit ongewenst zijn, dan kan de vraagsteller gedurende de overgangsperiode de ongewenste resultaten uitfilteren door deze selectiecriteria lokaal toe te passen op de ontvangen resultaten.








