import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import pyroomacoustics as pra



# Je commence par définir un fichier à lire (qui est dans le dossier du code) qui donne deux informations:
# le signal et la fréquence d'echantillonage
fs, signal_in = wavfile.read("arctic_a0010.wav")

# Définir la pièce avec ses materiaux
corners = np.array([[0, 0], [0, 3], [5, 3], [5, 1], [3, 1], [3, 0]]).T  # [x,y]
wall_absorption = 0.2
wall_scattering = 0.1
m = pra.Material(wall_absorption, wall_scattering)

# l'ordre de la simulation est définit ici
simulation_order = 2

#création de la pièce
room = pra.Room.from_corners(corners, fs=fs, max_order=simulation_order, materials=m, ray_tracing=True, air_absorption=True)

# Ajouter une source et un microphone
X_source = [1, 1]
room.add_source(X_source, signal=signal_in)
X_micro = np.array([[4], [2]])  # [[x], [y], [z]]
room.add_microphone(X_micro)

# Ajuster les paramètres du tracer de rayon
room.set_ray_tracing(receiver_radius=2, n_rays=10000, energy_thres=1e-5)

# calcule les sources images
room.image_source_model();

# trace un schema de la situation
fig, ax = room.plot(img_order=simulation_order)
plt.title('Schema de la pièce avec les sources images')

# Signaux d'entree et de sortie
room.simulate()

# Cette partie sert à convertir les signaux en pression réaliste. Sinon, ces vecteurs sont uniquement des fichiers .wav.
signal_in = np.array(signal_in)/1e4
signal_out = np.array(room.mic_array.signals[0, :])/2e4

# On met en graphique les signaux d'entree et de sortie
dt = 1/fs
fig, ax = plt.subplots(2, 1, sharex=True)
timeIn = np.linspace(0, dt*(len(signal_in)), len(signal_in))
ax[0].plot(timeIn, signal_in)
ax[0].set_ylabel('Pression [Pa]')
ax[0].set_title('Signal d entrée')

timeOut = np.linspace(0, dt*(len(signal_out)), len(signal_out))
ax[1].plot(timeOut, signal_out)
ax[1].set_ylabel('Pression [Pa]')
ax[1].set_title('Signal de sortie')
ax[1].set_xlabel('Temps [s]')

# faire un graphique de la RIR
plt.figure()
signal_rir = room.rir[0][0]
time = np.linspace(0, dt*(len(signal_rir)), len(signal_rir))
plt.ylabel('RIR dans la grande pièce')
plt.plot(time, signal_rir)
plt.xlabel('Time [s]');
plt.title('Réponse impulsionelle de la pièce')

# Le RT60 est une mesure du temps de réverberation de la pièce. Il équivault au temps lorsque le son est 60dB
# de moins que l'intensité sonore maximale.
plt.figure()
rt60 = room.measure_rt60(plot=True)
print("The measured RT60 is {}".format(rt60[0][0]))

