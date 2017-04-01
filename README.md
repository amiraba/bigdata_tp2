# TP2 - Patterns Big Data

## Activité 1
### Patron de filtrage

Etant validé en classe, le principe est de définir des mappers qui se chargent du filtrage des commentaires dont la longeur ne dépasse pasune seule et un reducer qui va permettre de calculer leur nombre.

## Activité 2
### Patron récapitulatif: Index
Ici, les mappers effectuent la tâche de filtrage de chaque ligne en une sortie dont la clé est le mot en question, suivie par l'id du commentaire. Par la suite, les reducers vont calculer le nombre d'occurences de chaque mot une fois qu'ils les reçoient de façon ordonnée.
![act2_lancer](https://cloud.githubusercontent.com/assets/23452983/24572608/e5b9f34c-1671-11e7-83c9-bd3ac3510bfd.png)

![act2_difficult_cmd](https://cloud.githubusercontent.com/assets/23452983/24572611/e8fd8820-1671-11e7-8005-3454318803b5.png)

![act2_difficult](https://cloud.githubusercontent.com/assets/23452983/24572614/f1663aac-1671-11e7-845c-8b7e69692d5c.png)

![act_2_difficulty](https://cloud.githubusercontent.com/assets/23452983/24572576/aa2d05b2-1671-11e7-8244-e48f0d7674ff.png)

## Activité 3 
### Patron récapitulatif: Résumé sous forme de moyenne
Les mappers filtrent les lignes en un couple (jour de la semaine, coût). Après le Sort et le Shuffle, les reducers vont permettre de calculer le coût total de chaque jour de la semaine ainsi que le nombre afin d'en générer la moyenne.

![act3_lancer](https://cloud.githubusercontent.com/assets/23452983/24572625/25a16242-1672-11e7-9adc-6670ec094fa3.png)

![act3_mapredceprogress](https://cloud.githubusercontent.com/assets/23452983/24572627/2917a210-1672-11e7-887c-7e9f48f1a064.png)

![act3_mapreducesuccessfully](https://cloud.githubusercontent.com/assets/23452983/24572629/2bbb8f4a-1672-11e7-814a-fc035326cd20.png)

![act3_sunday](https://cloud.githubusercontent.com/assets/23452983/24572630/2ed8efa6-1672-11e7-8350-42bcf2ea4918.png)

## Activité 4
### Introduction du "Combiner" dans le patron récapitulatif
On constate bien que lors de l'utilisation classique de notre méthode, une grande partie du calcul est à la charge du reducer tandis que les mappers sont en disposition d'alléger cette charge en effectuant des calculs intémédiaires de la moyenne du jour de la semaine. Dans ce cas, un coefficient bien défini doit être envoyé au reducer pour chaque jour afin de garantir la cohérence des résultats. On remarque déjà la rapidité avec laquelle le job reducer se rélalise relativement à l'approche normale comme le montre la figure ci dessous 

![act4_s7i7_rq_rapiditedureduce](https://cloud.githubusercontent.com/assets/23452983/24572643/6519abbe-1672-11e7-9769-2456ab30adbc.png)

Ce qui est bien confirmé par la réduction significative du nombre des input reduce records de l'approche classique à l'approche utilisant le Combiner:

![reduce input records](https://cloud.githubusercontent.com/assets/23452983/24572640/5b2c43be-1672-11e7-9e91-643eca969bdb.jpg)

![act4_reduce input records 2](https://cloud.githubusercontent.com/assets/23452983/24572641/5b2f57de-1672-11e7-8731-5f6c719f9bcb.png)

## Homework
### Patron de conception structurel
Les mappers se chargent du filtrage des champs demandés de chaque fichier tout en gardant comme première colonne de l'output l'id de l'auteur (le champs en commun). Une fois trié et mếlés aux reducers, chacun va stocker pour toute série de lignes ayant le même identifiant de l'auteur, les données à récupérer sur cet auteur ainsi qu'une liste de celles des commentaires de cet auteur. A la fin, on procède par l'affichage du contenu de cette liste sous la structure d'output souhaité par l'énoncé. 
![homework - test](https://cloud.githubusercontent.com/assets/23452983/24572659/9b3bc984-1672-11e7-8d06-08525e331a06.png)

La reputation de l'auteur ayant l'id 100002517 est 6149



# Conclusion
Grâce à ce TP, nous avons pu mettre en oeuvre les patrons de conception de filtrage, récapitulatifs et structurels pour répondre au besoin d'informations demandées. On a pu ainsi implémenter des solutions standars aux problèmes de conception récurrents dans le monde des Big Data. De cette manière, on a pu constater les avantages de l'utilisation de chacun, tel que le Combiner qui a contribué à une amélioration considérable des performances du job MapReduce en question.
