# <a name=Accreditatieomgeving>Accreditatieomgeving</a>

De accreditatieomgeving is een omgeving die is gemaakt om de aansluiting met VUM te testen. In deze omgeving kan de werking van VUM worden uitgeprobeerd, ofwel via het bevragen van een bron van BIDN of een eigen aangesloten bron.

Deze omgeving is afgeschermd, om gebruik te maken van deze omgeving dient u eerst als organisatie geregistreerd en gewhitelist te zijn.

# <a name=Testsets>Testsets</a>

Een aantal Postman collecties worden beschikbaar gesteld om de connectie met de API te verifiëren. Deze collecties bevatten een aantal requests die de verschillende endpoints van de API aanspreken.
De collecties zijn ontworpen zodat deze eenvoudig geïmporteerd kunnen worden in Postman en met minimale aanpassingen kunnen worden gebruikt.
De requests zijn zo opgezet dat deze gebruik maken van de de bijbehorende data bestanden.
In de upload bestanden zijn de profielen terug te vinden die beschikbaar worden gesteld in de BIDN bron.

Om deze Postman collecties te gebruiken, volg deze stappen:

- Importeer de Postman collectie ([...]\_coll.json) en de Postman environment (Accreditatie_environment.json) in Postman.
- Selecteer de geïmporteerde environment in Postman.
- Pas de volgende environment variabelen aan:
  - x-vum-fromparty: het OIN nummer van het BIDN, deze staat al ingevuld in de Accreditatie_environment.json
  - x-vum-viaparty: het OIN nummer van uw organisatie
- Registreer het PKI overheid certificaat in Postman via de instellingen. Hierbij is de HOST gelijk aan "https://ib-api.acc.diginetwerk.inlichtingenbureau.nl"
- Voer de collectie uit via de Collection Runner in Postman.

# <a name=VUM_testen_als_bemiddelaar>VUM testen als bemiddelaar</a>

Om VUM puur als bemiddelaar te testen, zonder een eigen bron aan te sluiten, kan VUM worden aangesproken door de headers in te vullen met de volgende informatie:

| **VUM Header**      | **Waarde**                                             |
| ------------------- | ------------------------------------------------------ |
| X-VUM-fromparty     | Het OIN nummer van het BIDN                            |
| X-VUM-toparty       | Het OIN nummer van het BIDN                            |
| X-VUM-viaparty      | Het OIN nummer van uw organisatie                      |
| API-Version         | Het versienummer zoals aangegeven in de OAS contracten |
| X-VUM-berichtVersie | Het versienummer zoals aangegeven in de OAS contracten |
| X-VUM-suwiparty     | True                                                   |

Door requests te versturen met deze headers, wordt de door BIDN beschikbaar gestelde testdata bevraagd. Het kan zijn dat er geen resultaten worden teruggegeven indien de zoekvraag te specifiek is. In de JSON bestanden aangemerkt met "\_upload" staan de profielen die beschikbaar zijn in de BIDN bron.

Bij ieder request wordt verwacht dat een PKI overheid certificaat wordt meegegeven.

# <a name=eigen_bron>Eigen bron testen</a>

In het geval dat een eigen bron is aangesloten op de accreditatieomgeving, kan deze worden aangesproken via VUM door de headers in te vullen met de volgende informatie:

| **VUM Header**      | **Waarde**                                             |
| ------------------- | ------------------------------------------------------ |
| X-VUM-fromparty     | Het OIN nummer van uw bron                             |
| X-VUM-toparty       | Het OIN nummer van het BIDN                            |
| X-VUM-viaparty      | Het OIN nummer van uw organisatie                      |
| API-Version         | Het versienummer zoals aangegeven in de OAS contracten |
| X-VUM-berichtVersie | Het versienummer zoals aangegeven in de OAS contracten |
| X-VUM-suwiparty     | True of False                                          |

Bij ieder request wordt verwacht dat een PKI overheid certificaat wordt meegegeven.
