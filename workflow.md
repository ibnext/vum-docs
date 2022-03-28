# Workflow

## Branches 
Deze repository kent meerdere branches, dit zijn `dev`, `test`, `accept` en `main`.<br>
Elke branch naam heeft een corresponderende omgeving waarbinnen de applicatie draait met die versie van de koppelvlakspecificatie. Dus elke omgeving kan een andere versie van de koppelvlakspecificatie afdwingen aan de gebruikers.

Nieuwe wijzigingen in de koppelvlakspecificatie worden in eerste instantie in de `dev` branch gecommit. Nadat de wijzigingen uit de dev omgeving uitgerold worden in een opvolgende omgeving, kunnen de koppelvlakspecificatie in de corresponderende branch bijgewerkt worden vanuit de branch die voor de betreffende branch komt binnen de OTAP straat. <br>
dev (O) -> test (T) -> accept (A) -> main (P)

Voor ontwikkelaars die willen aansluiten op VUM is de `main` branch het belangrijkste. De productieomgeving van VUM gebruikt ten alle tijde de main branch van deze repository.

## Tags
Nieuwe (productie) releases van de koppelvlakspecificatie worden uitgebracht door middel van `tags`<br>
Elke release versie krijgt een corresponderende tag binnen de repository zodat oudere releases eenvoudig terug te vinden zijn. 

## JSON OAS Contracten
Voor elke [tag](https://gitlab.com/inlichtingenbureau/vum/koppelvlak/-/tags) binnen het project is er een json versie van de OAS contracten beschikbaar op de [registry](https://gitlab.com/inlichtingenbureau/vum/koppelvlak/-/packages) pagina.
##