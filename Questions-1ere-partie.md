## Questions premiere partie:

Dans cette partie, utilisez la partie de code ci-dessous inspirée de la documentation _/notebooks/pyroomacoustics_demo.ipynb_ pour répondre aux questions ci-dessous. Remettez vos réponses à ces questions sous forme de cahier de laboratoire et déposez-les sur le site du cours.
1. Calculez le niveau sonore:
   1. Quel est le niveau sonore moyen (en dB) le long de la trace d'entrée et de sortie?
   2. Quelle fraction de l'énergie sonore est transmise entre la source et la réception?
   3. Faites un graphique du niveau sonore (en dB) en fonction du temps de la trace de l'entrée et celle de sortie pour un temps d'intégration de 0.1 secondes.
   4. Si l'incertitude sur une valeur de pression moyenne de 0.3 Pa est de 5% et que le taux d'échantillonage du micro est de 62.5 us (microsecondes). Quelle est l'incertitude sur le niveau sonore (en dB) si le temps d'intégration est de 0.1s? Qu'en est-il de si le temps d'intégration est de 1s? 

2. Décrivez par quelles opérations matématiques il est possible de calculer le RT60. Le RT60 est un standard pour décrire les échoes dans une pièce. Cette valeur décrit le temps où niveau acoustique est de 60dB sous la valeur maximale. 

3. Faites une transformée de fourier de votre signal de sortie. Dans quelle intervalle de fréquence est-ce que la majorité de votre signal se trouve? Est-ce typique d'une voix humaine? Comment faire pour obtenir la fréquence du signal en fonction du temps? (indice: cette fonction s'appelle la "short time fourier transform" ou le spectrogram.

4. Qu'est-ce l'ordre de l'image (img_order) et quelle est son influence sur vos résultats.
