# Objectif
Tester si la valeur de l'entropie peut vraiment compter les lignes B ? 

Comment ? en ne gardant que le centre et la partie interesssante ?

# Travail à faire
- [x] Réoganiser le projet (avec des classes/modules)
- [ ] Graphe de l'entropie sur une image Dicom dont on connait le nombre de lignes B
- [ ] 

# Programmation
- Fonction ou méthode pour enlever les ombres des côtes
    - [x] Fonction contraste noir et blanc
    - [x] Recherche des 2 zones
    - Recherche du pixel le plus à gauche dans l'ombre de droite et inversement
    - Jusqu'où aller en haut et en bas ?
- Tests unitaires

# Génie log
- Cahier des charges
- Diagramme UML

# idée pour le smooth
réduire la taille de l'image et trouver le rectangle, puis convertir ses coordonnées dans l'image originale


# déroulement du projet
- calcul de l'entropie sur les images entière.
  - Génération d'un graph afin de mettre en évidence un lien entre entropie et nombre de lignes B.

- rognage de l'image pour ne garder que la partie significative pour les lignes B
  - traitement afin de décider automatiquement quelle partie de l'image on garde
  - optimisation du traitement "smooth" car trop lent. (opencv)
  - 

- récupération des vrai images (dicom)
  - 