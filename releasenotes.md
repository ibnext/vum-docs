# Releasenotes Koppelvlak specificaties VUM v1.0.0

**Openstaande punten in deze release (v1.0.0)**

 - De koppelvlakspecificaties staan lege waardes toe voor attributen. Dit komt niet overeen met de VUM Gegevensstandaard. Dit betreft lege lijsten, lege objecten en lege tekst. 

 - De koppelvlakspecificaties staan attributen toe in de dataobjecten die niet in de specificatie zijn opgenomen. De VUM Gegevensstandaard sluit alle attributen uit die niet in de VUM Gegevensstandaard zijn opgenomen.

 - De wijze waarop “oneOf” constructies zijn geformuleerd heeft het onverwachte resultaat dat alle waardes voor de betreffende atttributen door de koppelvlakspecificaties afgewezen worden. Dit betreft de attributen 'beroep', 'opleidingsnaam', 'adres' en 'adresDetailsBuitenland'. De implemenatie van de VUM Uitwisselingsvoorziening wijkt hierin af van de koppelvlakspecificaties en accepteert de gewenste waardes voor deze attributen wel. De 'oneOf' constructies werken niet als verwacht omdat de definities van de keuzes elkaar niet volledig uitsluiten en elke waarde vervolgens aan alle keuzes voldoet. Als het gewenst is om de OpenAPI bestanden geautomatiseerd te verwerken, dan kan ‘"additionalProperties": false’ worden toegevoegd aan de schemadefinities van de keuzes voor de ‘oneOf’ constructies. 

 - Enumeraties uit de VUM Gegevensstandaard zijn niet in de koppelvlakspecificaties opgenomen. Dit staat waardes toe die wel aan het patroon voor het attribuut voldoen maar niet in de enumeratie van de VUM Gegevensstandaard voorkomen. 

 - De betekenis van de gebruikte formaat specificatie ‘URL’ voor het attribuut 'url' is niet nader gedefinieerd en heeft daarmee geen beperkende betekenis.

 - Een aantal attributen hebben in de koppelvlakspecificaties een ander type dan in de VUM Gegevenstandaard. De implementatie van de VUM Gegevensuitwisseling volgt de koppelvlakspecificaties voor deze attributen.
 
- De volgende attributen hebben een string als datatype in de koppelvlakspecificaties maar zijn een integer in de VUM Gegevensstandaard:    

```
    codeOpleidingsnaam
    codeGedragscompetentie
    codeTypeOvereenkomst
    codeWerkEnDenkniveauMinimaal
    indicatieBeschikbaarheidContactgegevens
    datumAanvangAdres
    datumAanvangBeschikbaarVoorWerk
    datumAanvangWerkzaamheden
    datumEindeAdres
    datumEindeBeschikbaarVoorWerk
    datumEindeWerkzaamheden
    sluitingsDatumVacature
    datumAanvangVolgenCursus
    datumCertificaat
    datumEindeVolgenCursus
    datumAanvangVolgenOpleiding
    datumDiploma
    datumEindeVolgenOpleiding
    idVacature
    nummerVacature
```

 - Het attribuut ‘indicatieLdrRegistratie’ is een integer in de koppelvlakspecificaties en een boolean in de VUM Gegevensstandaard. 
 - Het attribuut ‘postbusnummerBuitenland’ heeft de maximale lengte van 9 posities in de koppelvlakspecificaties en van maar 7 posities in de VUM Gegevensstandaard, . 
 - Het attribuut 'url' heeft een geen limiet op de lengte in de koppevlakspecificaties maar een maximum lengte van 512 in de VUM Gegevensstandaard. 
 - Het attribuut ‘vakvaardigheid’ is in de koppelvlakspecificaties weergegeven als een object met een ingebed attribuut 'omschrijving'. In de VUM Gegevensstandaard is ‘vakvaardigheid’ een enkel  - attribuut 'omschrijving vakvaardigheid' van type 'string'.
 


<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 40%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>versie</strong></th>
<th><strong>nr</strong></th>
<th><strong>aanpassing</strong></th>
<th><strong>motivatie</strong></th>
</tr>
<tr class="header">
<th>1.0.0</th>
<th>1</th>
<th>-</th>
<th>Publicatie 1.0.0 versie</th>
</tr>
<tr class="odd">
<th>0.99.7</th>
<th>1</th>
<th>Postcode en Straal velden verwijderd uit het zoekopdracht voor
Vacature en WerkzoekendeProfielen.</th>
<th>Deze velden werden alleen gebruikt door de broker voor geo matching,
er is voor nu gekozen om dit te laten vervallen voor het Vacature
endpoint. Voor het werkzoekende endpoint worden nu andere velden
gebruikt, zodat de bron hier ook op kan filteren.</th>
</tr>
<tr class="header">
<th>0.99.7</th>
<th>2</th>
<th>Mobiliteit object en velden bemiddelingspostcode &amp;
maximaleReisafstand binnen het mobiliteits object verplicht gemaakt
t.b.v. geomatching op bronnen en filteren van resultaten door
bronnen.</th>
<th>Velden moeten verplicht zijn zodat de geo matching kan plaatsvinden
en de bron zijn resultaten kan filteren.</th>
</tr>
<tr class="odd">
<th>0.99.6</th>
<th>1</th>
<th>Beroepsnaam en opleidingsnaam een extra object gegeven</th>
<th>Voor betere compatibiliteit bij implementaties en voor consistentie
met de andere plekken waar nu OneOf gebruikt wordt.</th>
</tr>
<tr class="header">
<th>0.99.6</th>
<th>2</th>
<th>Integer10 gewijzigd naar Integer10AsString met een Regex</th>
<th>Voor betere compatibiliteit bij implementaties voldoet dit veld nu
aan rfc8259. Dit betekend dat getallen boven 2^53 nu geformat worden als
string.</th>
</tr>
<tr class="odd">
<th>0.99.6</th>
<th>3</th>
<th>Straal heeft een hoger maximale waarde</th>
<th>De oude waarde was te laag.</th>
</tr>
<tr class="header">
<th>0.99.6</th>
<th>4</th>
<th>Yaml veld bemiddelingspostcode heeft een example</th>
<th>De json example binnen swagger plaatste een waarde als ‘string’ in
dit veld en dit wordt nu ‘1234AB’ anders wordt dit afgekeurd door de
regex</th>
</tr>
<tr class="odd">
<th>0.99.5</th>
<th>1</th>
<th>Integer waarden hadden een 'maxLength' qualifier, dat is aangepast
naar 'maximum'</th>
<th>Dit is de correcte wijze van inperken van het Integer datatype.</th>
</tr>
<tr class="header">
<th>0.99.5</th>
<th>2</th>
<th>Aanpassing de omvang van het werkzoekende profiel in contract
VUM-Bron-WerkzoekendeProfielen.</th>
<th>Contract VUM-Bron-WerkzoekendeProfielen specificeerde in de response
van de matches endpoint onterecht de structuur van een compleet
werkzoekende profiel in plaats van een beperkt matchingprofiel</th>
</tr>
<tr class="odd">
<th>0.99.5</th>
<th>3</th>
<th>positie antwoordnummer aangepast</th>
<th>Het antwoordnummer veld bij een antwoordnummeradres stond niet op
het juiste nivo opgenomen in de vacature contracten.</th>
</tr>
<tr class="header">
<th>0.99.4</th>
<th>1</th>
<th>X-VUM-* header parameters toegevoegd aan request specificatie van
detail-bevraging endpoints</th>
<th>Deze parameters ontbraken ten onrechte</th>
</tr>
<tr class="odd">
<th>0.99.4</th>
<th>2</th>
<th>verruimen van het datatype van een aantal id's: idWerkzoekende,
idVacature, bronID naar String200</th>
<th>Flexibiliteit voor implementators van de API</th>
</tr>
<tr class="header">
<th>0.99.4</th>
<th>3</th>
<th>Toevoegen van SGR entiteit Adres aan entiteit Werkgever in Vacature
contracten</th>
<th>Adres was per abuis weggelaten uit het VUM gegevensmodel 0.8.4, en
niet opgenomen in de koppelvlakspecificaties</th>
</tr>
<tr class="odd">
<th>0.99.4</th>
<th>4</th>
<th>Twee servers (test en acceptatie) toegevoegd aan de bemiddelaars
contracten</th>
<th>Ter referentie voor de pilots</th>
</tr>
<tr class="header">
<th>0.99.3</th>
<th>1</th>
<th>vumID vervangen door idVacature in contract VUM-Bron-Vacatures</th>
<th>In contract VUM-Bron-Vacatures werd ten onrechte vumID in plaats van
idVacature geretourneerd</th>
</tr>
<tr class="odd">
<th>0.99.2</th>
<th>1</th>
<th>Header X-VUM-SUWIparty verplicht gemaakt</th>
<th>n.a.v. review</th>
</tr>
<tr class="header">
<th>0.99.2</th>
<th>2</th>
<th>vumID van Integer14 naar String500 veranderd</th>
<th>In verband met de toe te passen techniek voor het werken met
vum-ID's binnen de uitwisselingsvoorziening.</th>
</tr>
<tr class="odd">
<th>0.99.2</th>
<th>3</th>
<th>idWerkzoekende naar Integer14 aangepast (was String200)</th>
<th>Om logisch gegevensmodel te volgen</th>
</tr>
<tr class="header">
<th>0.99.1</th>
<th>1</th>
<th><p>Toevoeging 2 OAS3 contracten tbv Vacatures, bestanden:<br />
VUM-Bron-Vacatures-0.99.1.yaml</p>
<p>VUM-Bemiddelaar-Vacatures-0.99.1.yaml</p></th>
<th>Qua opzet analoog aan de 2 contracten voor Werkzoekenden, maar dan
op basis van het gegevensmodel bij de uniforme Vacaturestandaard</th>
</tr>
<tr class="odd">
<th>0.99.1</th>
<th>2</th>
<th>codeTypeOvereenkomst was 1 karakter groot, aangepast naar 2 volgens
het model.</th>
<th>Correctie</th>
</tr>
<tr class="header">
<th>0.99.1</th>
<th>3</th>
<th>Op een aantal plaatsen in de documentatie en bestandsnamen werd nog
van werkzoekende<strong>n</strong>Profielen vermeld</th>
<th>vervangen door werkzoekendeProfielen</th>
</tr>
<tr class="odd">
<th>0.99.0</th>
<th>1</th>
<th>401 'not authorized' status code toegevoegd</th>
<th>Om autorisatie fouten op standaardwijze te kunnen terugkoppelen</th>
</tr>
<tr class="header">
<th>0.99.0</th>
<th>2</th>
<th>‘default’ sectie bij HTTP status codes in de contracten
verwijderd</th>
<th>Alleen de expliciet gedefinieerde response codes worden
ondersteund</th>
</tr>
<tr class="odd">
<th>0.99.0</th>
<th>3</th>
<th>Lijst met VUM error code en messages toegevoegd</th>
<th>Bij een aantal HTTP status codes kan in de response een VUM error
worden toegevoegd, bestaande uit een code, message en details. In het
document is hier een tabel voor opgenomen.</th>
</tr>
<tr class="header">
<th>0.99.0</th>
<th>4</th>
<th>maximumAantalResultatenBereikt attribuut toegevoegd</th>
<th>Om bij een set matchingprofielen aan te geven dat een bron meer
matches zou kunnen leveren dan de teruggeleverde set. Er is momenteel
vanuit VUM een maximum gesteld van 100 matches per bron</th>
</tr>
<tr class="odd">
<th>0.99.0</th>
<th>5</th>
<th>Document: op verzoek een aantal voorbeelden van restricties en
limieten toegevoegd</th>
<th>De restricties en limieten die door VUM zijn gespecificeerd worden
niet afgedwongen door de contracten omdat deze configureerbaar worden.
Op verzoek een aantal voorbeelden benoemd.</th>
</tr>
<tr class="header">
<th>0.99.0</th>
<th>6</th>
<th>Contracten: consequent gebruik werkzoekendeProfielen ipv
werkzoekende<strong>n</strong>Profielen</th>
<th>Uniformeren van deze aanduiding in beschrijving en contract
elementen</th>
</tr>
<tr class="odd">
<th>0.99.0</th>
<th>7</th>
<th>Een aantal relaties met Werkzoekende enkelvoudig gemaakt ipv
mogelijk meervoudig: Werktijden, Flexibiliteit, Mobiliteit, Eis aan
werk, Arbeidsmarktkwalificatie</th>
<th>In het contract was het mogelijk om genoemde elementen meerdere
keren op te nemen bij een werkzoekende. Dit was niet volgens de
specificatie van het model.</th>
</tr>
<tr class="header">
<th>0.99.0</th>
<th>8</th>
<th>Lijst met VUM Identifiers toegevoegd, aanduiding in contract
gelijkgetrokken</th>
<th>De door VUM opgestelde lijst met identifiers is overgenomen in de
specificaties, en aanduidingen in de contracten zijn zoveel mogelijk
hierop aangepast. RequestID is bijvoorbeeld aangepast naar VraagID.</th>
</tr>
<tr class="odd">
<th>0.99.0</th>
<th>9</th>
<th>bronID toegevoegd in response van endpoint
/werkzoekendeProfielen/{vumID}</th>
<th>bronID toegevoegd aan response van /werkzoekendeProfielen/{vumID},
zodat de bemiddelaar kan verwijzen naar de bron</th>
</tr>
<tr class="header">
<th>0.99.0</th>
<th>10</th>
<th>endpoint /werkzoekendeProfielen/zoekMatches hernoemd naar
/werkzoekendeProfielen/matches ivm API standaard</th>
<th>In verband met naamgevingconventies in de Logius REST API
standaarden is /zoekMatches vervangen door /matches</th>
</tr>
<tr class="odd">
<th>0.98.1</th>
<th>1</th>
<th>Duidelijker samenhang tussen matchingprofiel en detailprofiel</th>
<th>Herstel van een onvolkomenheid bij het onderscheid tussen
matchingprofielen en detailprofielen</th>
</tr>
<tr class="header">
<th>0.98.0</th>
<th>1</th>
<th>postcode/straal parameters verplaats van query naar request
body</th>
<th>Aansluiting bij de standaard voor POST requests</th>
</tr>
<tr class="odd">
<th>0.98.0</th>
<th>2</th>
<th>toevoegen diverse HTTP status codes</th>
<th>Om te voldoen aan de eisen van de door Logius nog op te leveren
Digikoppeling REST/JSON standaard: API-47 (API Design Rules): APIs
should at least support the following HTTP status codes: 200, 201, 204,
304, 400, 401, 403, 404, 405, 406, 409, 410, 415, 422, 429, 500, and
503. Relevante codes zijn toegevoegd, sommige codes hebben betrekking op
PATCH, PUT operaties die geen onderdeel van het contract uitmaken.</th>
</tr>
<tr class="header">
<th>0.98.0</th>
<th>4</th>
<th>Header velden toegevoerd voor o.a. routering</th>
<th>Routering header velden toevoegen ivm ondersteuning SAAS scenario.
Aangesloten partij acteert voor meedere bemiddelaars/bronnen.Verzoek van
VUM: ondersteuning van functionaliteit in geval berichtinhoud in de
toekomst encrypted zou worden.</th>
</tr>
<tr class="odd">
<th>0.98.0</th>
<th>6</th>
<th>Nieuw contract toegevoegd tussen Uitwisselingsvoorziening en
bronnen</th>
<th>De API tussen bron en uitwisselingsvoorziening hebben grotendeels
betrekking op dezelfde gegevens, maar met een aantal verschillen die een
eigen contract nodig maken. Zo is de communicatie synchroon, en zijn er
een aantal verschillen bij de meta-gegevens die worden
gecommuniceerd.</th>
</tr>
<tr class="header">
<th>0.97.0</th>
<th>1</th>
<th>Datatypes strakker gedefinieerd: beperking op lengte, datum velden
hebben een Date format gekregen, postcode format toegevoegd</th>
<th>N.a.v. feedback Herman Miedema</th>
</tr>
<tr class="odd">
<th>0.97.0</th>
<th>2</th>
<th>Een inconsistentie gelijkgetrokken: zowel matchID als vumID kwamen
voor</th>
<th>overal wordt nu vumID ipv matchID gebruikt, met datatype
integer14</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
