# Protocole Room acoustique

#### Contact:felix.levesque-desrosiers.1@ulaval.ca

Au cours de ce laboratoire, on utilise le package pyroomacoustics pour observer la propagation de l'acoustique dans différents espaces et différentes situations. Comme son nom l'indique, _Pyroomacoustics_ est un _package_ _python_ qui permet de simuler la propagation d'onde acoustiques dans une pièce en deux et en trois dimensions.

En plus d'offir l'opportunité de faire un laboratoire à distance pour remplacer le laboratoire d'acoustique qui avait besoin d'une mise-à-jour, ce laboratoire a pour objectif d'initier les étudiants aux simulations qui peuvent être une partie importante de la carrière de l'ingénieur en physique.

## Objectifs

Ce laboratoire sera en deux parties et nécessitera deux remises séparées. Dans un premier cas, vous pouvez remettre un court compte rendu sous forme de _Jupyter Notebook_ ou de document texte répondant à des questions posées dans ce présent document en faisant rouler le code donné dans le fichier _premiere_partie.py_ et en y apportant votre grain de sel. Ensuite, nous vous invitons à faire votre propre expérience.

Dans le but d'introduire ce laboratoire, une démonstration d'utilisation du logiciel sera faite dans le document _demonstration.ipynb_. Celle-ci a pour objectif de montrer, non-seulement comment faire fonctionner le code, mais aussi à introduire de la théorie sur la propagation de l'onde acoustique.

Ensuite, vous développerez une compréhension plus exhaustive de comment _Pyroomacoustics_ effectue ses calculs et ce qu'il prend en compte. Pour ce faire, utilisez _premiere_partie.py_ et modifiez le code pour répondre aux questions dans le fichier _questions-1ere-partie.md_.

En ce qui concerne la deuxième partie, nous vous invitons à faire une comparaison entre une expérience que vous ferez chez vous comparé à une simulation dans le logiciel. Pour ce faire, vous pouvez faire jouer un son et l'enregistrer sur un téléphone intelligent. Plus de détails vous sont donnés dans la partie _question-2e-partie.md_.

# Matériel

Pour effectuer ce laboratoire, vous aurez besoin

 - du logiciel _Python3_,
 - du package Pyroomacoustics (pip install pyroomacoustics)
 - Vous aurez aussi besoin de des librarairies données par Visual studio Tools disponible à l'adresse: https://visualstudio.microsoft.com/visual-cpp-build-tools/. Pyroomacoustics utilise des racourcis en C++ pour accélérer les calculs. Le téléchargement peut prendre 30 minutes.
 
## Documentation
Le GitHub monté par les fondateurs de _Pyroomacoustics_ est disponible à l'adresse:
https://github.com/LCAV/pyroomacoustics

Vous trouverez dans la documentation sur le package _Pyroomacoustics_ sous forme d'example ici: https://nbviewer.jupyter.org/github/LCAV/pyroomacoustics/blob/master/notebooks/pyroomacoustics_demo.ipynb

De plus, la commande ci-dessous offre de la documentation qui pourrait vous être utile:
 
'print(pra.room.\_\_doc\_\_)'.

Finalement, vous pouvez trouver des informations théori

La commade de documentation ci-dessus peut être utilisée pour presque toutes les fonctions dans _Pyroomacoustics_.

Finalement, vous trouverez de l'information théorique sur le calcul fait par le logiciel dans la publication:
R. Scheibler, I. Dokmanić and M. Vetterli. Raking Echoes in the Time Domain, ICASSP 2015, Brisbane, Australia, 2015.
