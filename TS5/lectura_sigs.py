#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:55:30 2023

@author: mariano
"""

import numpy as np
from scipy import signal as sig

import matplotlib.pyplot as plt
   
import scipy.io as sio
from scipy.io.wavfile import write


#%%

##################
# Lectura de ECG #
##################

fs_ecg = 1000 # Hz


##################
## ECG con ruido
##################

# para listar las variables que hay en el archivo
#io.whosmat('ECG_TP4.mat')
# mat_struct = sio.loadmat('./ECG_TP4.mat')

# ecg_one_lead = mat_struct['ecg_lead']
# N = len(ecg_one_lead)

# hb_1 = mat_struct['heartbeat_pattern1']
# hb_2 = mat_struct['heartbeat_pattern2']

# plt.figure()
# plt.plot(ecg_one_lead[5000:12000])

# plt.figure()
# plt.plot(hb_1)

# plt.figure()
# plt.plot(hb_2)

##################
## ECG sin ruido
##################
eps = 1e-12
ecg_one_lead = np.load('ecg_sin_ruido.npy')


# %% copilot

# Señal a analizar: podés cambiar ecg_one_lead, ppg o wav_data
signal_to_analyze = ecg_one_lead
fs = fs_ecg   # cambiar según la señal: fs_ppg o fs_audio

# --- 1) Periodograma ventaneado ---
f_per, Pxx_per = sig.periodogram(signal_to_analyze, fs, window='hamming', scaling='density')

plt.figure()
#plt.semilogy(f_per, Pxx_per)
plt.plot(f_per, Pxx_per)
plt.title("PSD - Periodograma ventaneado (Hamming)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Densidad espectral [V^2/Hz]")
plt.grid(True)

print(np.var(Pxx_per))

# --- 2) Método de Welch ---
f_welch, Pxx_welch = sig.welch(signal_to_analyze, fs, window='hamming', nperseg=1024, scaling='density')
#f_black, Pxx_ecg_ham1 = sig.welch(ecg_one_lead, fs_ecg, 'hamming', axis=-1, nperseg=len(ecg_one_lead), noverlap=None)
#f_black, Pxx_ecg_bla1 = sig.welch(ecg_one_lead, fs_ecg, 'blackmanharris', axis=-1, nperseg=len(ecg_one_lead), noverlap=None)
# f_3k, Pxx_den_ecg_3 = sig.welch(ecg_one_lead, fs_ecg, 'blackmanharris', axis=-1, nperseg=2000, noverlap=1000, nfft=2*len(ecg_one_lead))


plt.figure()
plt.semilogy(f_welch, Pxx_welch, label='con semilogy')
plt.plot(f_welch, 10*np.log10(Pxx_welch + eps), label='con log')
plt.title("PSD - Método de Welch")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Densidad espectral [V^2/Hz]")
plt.legend()
plt.grid(True)

print(np.var(Pxx_welch))

# --- 3) Método Blackman-Tukey ---
# Se calcula la autocorrelación y luego su FFT
Rxx = sig.correlate(signal_to_analyze, signal_to_analyze, mode='full')
Rxx = Rxx[len(Rxx)//2:]  # parte causal
window = np.blackman(len(Rxx))
Rxx_win = Rxx * window
Pxx_bt = np.abs(np.fft.fft(Rxx_win))
f_bt = np.fft.fftfreq(len(Rxx_win), d=1/fs)

#print(np.var(Pxx_bt))
plt.figure()
#plt.semilogy(f_bt[:len(f_bt)//2], Pxx_bt[:len(f_bt)//2])
plt.plot(f_bt[:len(f_bt)//2], Pxx_bt[:len(f_bt)//2])
plt.title("PSD - Método Blackman-Tukey")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Densidad espectral [V^2/Hz]")
plt.grid(True)

plt.show()


# %% mio

#plt.figure()
#plt.plot(ecg_one_lead)

#welch(x, fs=1.0, window='hann_periodic', nperseg=None, noverlap=None, nfft=None, detrend='constant', return_onesided=True, scaling='density', axis=-1, average='mean')

# f_1k, Pxx_den_ecg_1 = sig.welch(ecg_one_lead, fs_ecg, 'blackmanharris', axis=-1, nperseg=len(ecg_one_lead), noverlap=None)
# f_2k, Pxx_den_ecg_2 = sig.welch(ecg_one_lead, fs_ecg, 'blackmanharris', axis=-1, nperseg=6000, noverlap=5000)
# f_3k, Pxx_den_ecg_3 = sig.welch(ecg_one_lead, fs_ecg, 'blackmanharris', axis=-1, nperseg=2000, noverlap=1000, nfft=2*len(ecg_one_lead))


# plt.figure(2)
# plt.clf()
# Pxx_den_ecg_db_1000=10*np.log10(Pxx_den_ecg_1000**2 + eps)
# Pxx_den_ecg_db_3000=10*np.log10(Pxx_den_ecg_3000**2 + eps)

# plt.plot(f_1k,Pxx_den_ecg_1, label='metodo 1')
# plt.plot(f_2k,Pxx_den_ecg_2, label='metodo 2') 
# plt.plot(f_3k,Pxx_den_ecg_3, label='metodo 3') 
# plt.legend()

# print(np.var(Pxx_den_ecg_1))
# print(np.var(Pxx_den_ecg_2))
# print(np.var(Pxx_den_ecg_3))


# plt.figure(3)
# plt.hist(Pxx_den_ecg, bins=20)


##poca varianza segmento chicos




#%%

####################################
# Lectura de pletismografía (PPG)  #
####################################

fs_ppg = 400 # Hz

##################
## PPG con ruido
##################

# # Cargar el archivo CSV como un array de NumPy
# ppg = np.genfromtxt('PPG.csv', delimiter=',', skip_header=1)  # Omitir la cabecera si existe


##################
## PPG sin ruido
##################

# ppg = np.load('ppg_sin_ruido.npy')

# plt.figure()
# plt.plot(ppg)


#%%

####################
# Lectura de audio #
####################

# Cargar el archivo CSV como un array de NumPy
##fs_audio, wav_data = sio.wavfile.read('la cucaracha.wav')
# fs_audio, wav_data = sio.wavfile.read('prueba psd.wav')
# fs_audio, wav_data = sio.wavfile.read('silbido.wav')

# plt.figure()
# plt.plot(wav_data)

# si quieren oirlo, tienen que tener el siguiente módulo instalado
# pip install sounddevice
# import sounddevice as sd
# sd.play(wav_data, fs_audio)

