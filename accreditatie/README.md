# <a name=Testsets>Testsets</a>

Een aantal Postman collecties worden beschikbaar gesteld om de connectie met de API te testen. Deze collecties bevatten een aantal requests die de verschillende endpoints van de API aanspreken.
De collecties zijn ontworpen zodat deze eenvoudig geïmporteerd kunnen worden in Postman en met minimale aanpassingen kunnen worden gebruikt.
De requests zijn zo opgezet dat deze gebruik maken van de de bijbehorende data bestanden.
In de upload bestanden zijn de profielen terug te vinden die beschikbaar zijn op de accreditatieomgeving.

Om deze Postman collecties te gebruiken, volg de volgende stappen:

- Importeer de Postman collectie (\_coll) en de Postman environment (\_environment) in Postman.
- Selecteer de geïmporteerde environment in Postman.
- Pas de volgende environment variabelen aan:
  - x-vum-fromparty: het OIN nummer van de bemiddelaar
  - x-vum-viaparty: het OIN nummer van de organisatie/techpartner
- Registreer het PKI overheid certificaat in Postman via de instellingen. Hierbij is de HOST "https://ib-api.acc.diginetwerk.inlichtingenbureau.nl"
- Voer de collectie uit via de Runner in Postman.
