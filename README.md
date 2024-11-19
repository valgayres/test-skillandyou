# Test technique Skill&You Data

## Contexte

On possède aujourd'hui sur bigquery, alimenté via DBT (en mode full refresh tous les jours), une table avec les réponses des élèves à différents questionnaires

Pour l'un de ces questionnaires, on a une réponse qualitative.
On souhaiterait extraire de cette réponse des informations quantitatives.

Pour cela, on va labelliser à l'aide d'une IA les réponses.

## Objectifs

- Proposer un système permettant d'avoir par jour / semaine, pour chaque formation, le nombre d'avis pour chaque label (system design).

- Proposer des débuts d'implémentation pour quelques briques de ce système.


## Détails

La question qui nous intéresse est la question 3 du questionnaire 1.
