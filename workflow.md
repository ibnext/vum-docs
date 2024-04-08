# Workflow

## Algemeen

Aanpassingen in de koppelvlakspecificaties worden op de gebruikelijke manier gerealiseerd: als branches in de git repository die na een pull request worden gemerged naar `develop` en `main`. Geaccepteerde revisies krijgen een tag die de versie aangeeft, waarbij semantic versioning wordt gevolgd.

## Endpoints en gegevensmodel

Er is een zeer grote overlap in het gegevensmodel voor de verschillende koppelvlakken. Het is daarom zinnig om een onderscheid te maken tussen de weergave van het gegevensmodel. welke gedeeld wordt tussen de verschillende koppelvlakken, en de specificatie van de endpoints, die voor elk koppelvlak anders is.

De `src` subdirectory bevat daarom het bestand `components.yaml` dat het gedeelde gegevensmodel bevat en een viertal `VUM-*.yaml` documenten die enkel de endpoints van de koppelvlakken beschrijven. Deze vier bestanden missen dan de `components` property van het OAS contract. 

Daarnaast bevat deze directory een `add_components.py` script dat de benodigde `components` property uit het bestand `components.yaml` toevoegt aan een `VUM-*.yaml` bestand en het resultaat als `json` en `yaml` wegschrijft in de opgegeven directory:

```
usage: add_components.py [-h] [-c COMPONENTS_FILE] -f OPENAPI_FILE -o OUTPUT_DIRECTORY

Add the components definition section to the yaml files for the interface.

options:
  -h, --help           show this help message and exit
  -c COMPONENTS_FILE
  -f OPENAPI_FILE
  -o OUTPUT_DIRECTORY
```

Als voorbeeld voor het gebruik:

```
$> ./add_components -c ./components.yaml -f VUM-Bemiddelaar-Vacatures.yaml -o ../OAS_Contracten
```

In sommige gevallen is nodig om in het generieke deel van `components.yaml` toch een onderscheid te kunnen maken tussen de invulling van een schema met dezelfde referentie voor werkzoekenden en vacatures, of tussen bron en bemiddelaar. Dit kan door in het `components.yaml` document het betreffende schema een toevoeging te geven die aangeeft waar deze moet worden toegepast:

* `_V` als toevoeging zorgt dat de definitie in components.yaml wordt gebruikt in het vacature domein.
* `_W` als toevoeging zorgt dat de definitie in components.yaml wordt gebruikt in het werkzoekende domein.
* `_VUM` als toevoeging zorgt dat de definitie in components.yaml wordt gebruikt op het bemiddelaar koppelvlak (VUM is de server).
* `_BRN` als toevoeging zorgt dat de definitie in components.yaml wordt gebruikt op het bron koppelvlak (de bron is server).

Bij het invoegen in het contract document worden de toevoegingen verwijderd door het invoegscript. Zie de huidige definities voor `emailadres`, `vumID`, `idVacature` en `idWerkzoekende` in het bestand `components.yaml` als voorbeeld.

## Aanpassingen

De verwachting is dat de VUM Gegegevensstandaard, en de weergave daarvan in JSON, stabiel zal zijn. Wijzigingen worden dan vooral verwacht met betrekking tot de selectievraag.

Specifiek is de verwachting dat er wijzigingen in de selectievraag zullen komen in de vorm van toegevoegde operatoren en toegevoegde gegevens die bevraagd kunnen worden. Bij zulke toevoegingen moet zorgvuldig worden gewerkt om te zorgen dat het JSON schema forwards compatible blijft: toekomstige toevoegingen moet toegestaan worden in het huidige schema. Allereerst betekent dit dat er voor de selectievraag altijd `additionalProperties = True` moet gelden (dit is de default als dit property afwezig is). Daarnaast moet opgelet worden dat er bij het gebruik van een `oneOf` er geen overlap kan bestaan tussen de verschillende keuzes. De `oneOf` zal anders toekomstige aanpassingen die in die overlap vallen gaan afwijzen omdat dan meerdere keuzes van toepassing zijn. Zie de definitie van `codeWerkEnDenkNiveauMinimaal_selectie` als voorbeeld. Daar wordt expliciet de aanwezigheid van `$lte` in één van de keuzes onmogelijk gemaakt met een `not` om te voorkomen dat er een overlap is tussen de twee keuzes.

Het verlies van de forward-compatibility kan zeer grote impact hebben op de mogelijkheden om aan de toekomstige wensen voor wijzigingen tegemoet te komen. Toets een wijziging zorgvuldig met een JSON schema expert, zeker als er gebruik wordt gemaakt van `oneOf` of `not`.

Tot slot, als de forward-compatibility gehandhaafd blijft, zijn toekomende wijzigingen altijd non-breaking, en er is dus hoogstens een ophoging van het minor deel van het versienummer.

