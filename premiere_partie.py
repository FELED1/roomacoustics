import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import pyroomacoustics as pra

# l'ordre de la simulation est définit ici

# Je commence par définir un fichier à lire (qui est dans le dossier du code) qui donne deux informations:
# le signal et la fréquence d'echantillonage
fs, signal = wavfile.read("arctic_a0010.wav")

# Définir la pièce avec ses materiaux
corners = np.array([[0, 0], [0, 3], [5, 3], [5, 1], [3, 1], [3, 0]]).T  # [x,y]
wall_absorption = 0.2
wall_scattering = 0.1
m = pra.Material(wall_absorption, wall_scattering)

simulation_order = 2
room = pra.Room.from_corners(corners, fs=fs, max_order=simulation_order, materials=m, ray_tracing=True, air_absorption=True)

# Ajouter une source et un microphone
X_source = [1, 1]
room.add_source(X_source, signal=signal)
X_micro = np.array([[4], [2]])  # [[x], [y], [z]]
room.add_microphone(X_micro)

# Ajuster les paramètres du tracer de rayon
room.set_ray_tracing(receiver_radius=2, n_rays=100000, energy_thres=1e-5)

# calcule les sources images
room.image_source_model();

# trace un schema de la situation
fig, ax = room.plot(img_order=simulation_order)
plt.title('Schema de la pièce avec les sources images')

# Signaux d'entree et de sortie
room.simulate()

dt = 1/fs
fig, ax = plt.subplots(2, 1, sharex=True)
timeIn = np.linspace(0, dt*(len(signal)), len(signal))
ax[0].plot(timeIn, signal)
ax[0].set_ylabel('Pression [Pa]')
ax[0].set_title('Signal d entrée')

signal_out = room.mic_array.signals[0, :]
timeOut = np.linspace(0, dt*(len(signal_out)), len(signal_out))
ax[1].plot(timeOut, signal_out)
ax[1].set_ylabel('Pression [Pa]')
ax[1].set_title('Signal de sortie')
ax[1].set_xlabel('Temps [s]')

# faire un graphique de la RIR
plt.figure()
sig = room.rir[0][0]
time = np.linspace(0, dt*(len(sig)), len(sig))
plt.ylabel('RIR dans la grande pièce')
plt.plot(time, sig)
plt.xlabel('Time [s]');
plt.title('Réponse impulsionelle de la pièce')

# Le RT60 est une mesure du temps de réverberation de la pièce. Il équivault au temps lorsque le son est 60dB
# de moins que l'intensité sonore maximale.
plt.figure()
rt60 = room.measure_rt60(plot=True)
print("The measured RT60 is {}".format(rt60[0][0]))
