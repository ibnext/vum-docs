# Workflow

## Branches
De repository kent meerdere branches. Dit zijn dev, staging, testing en master.<br>
Elke branch naam is gekozen voor elke omgeving dat op het moment bestaat en gebruikt wordt. Dus elke omgeving heeft een andere versie van de koppelvlak specificatie.

In de dev branch worden er nieuwe commits gemaakt en vervolgens, als het kan of nodig is, kan de staging branch de nieuwe wijzigingen overnemen. Hetzelfde geld voor testing en master op chronologische volgorde.

In dit geval is het master branch voor developers die gebruik maken van het product het belangrijkste. Want dit koppelvlak is hetgene wat uiteindelijk gebruikt wordt op productie.<br>
Hierdoor is er ook rekening gehouden met bezoekers van dit repository, dat zij het master branch het eerste zien, zodat er geen verwarringen ontstaan voor non-developers.

## Tags
Er is ook gekozen voor om tags te gebruiken. De tag is een referentie naar een commit op de branch.<br>
Het doel van de tag is om het makkelijker te maken om een oudere versie te vinden van de koppelvlak specificaties. <br>
Anders zou het een developer of zelfs een non-developer moeite hebben om een oudere versie te vinden tussen al de commits dat plaats heeft gevonden tijdens de development van de specificaties. 