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
#from scipy.io.wavfile import write

from scipy.io import wavfile



# %%



#%%

import os
print(os.path.exists('la cucaracha.wav'))  # Debe imprimir True
print(os.getcwd())  # Muestra el directorio actual de Python
# %%


##################
# Lectura de ECG #
##################

fs_ecg = 1000 # Hz

####################################
# Lectura de pletismografía (PPG)  #
####################################

# fs_ppg = 400 # Hz
# signal_ppg = np.load('ppg_sin_ruido.npy')
eps = 1e-12
#ecg_one_lead = np.load('ecg_sin_ruido.npy')

####################
# Lectura de audio #
####################

# Cargar el archivo CSV como un array de NumPy
fs_cuca, wav_cuca = sio.wavfile.read(r'C:/Users/Mariano/Desktop/APS/TS0/TS5/la_cucaracha.wav')
fs_, wav_data = sio.wavfile.read(r'C:/Users/Mariano/Desktop/APS/TS0/TS5/prueba psd.wav')
fs_audio, wav_data = sio.wavfile.read(r'C:/Users/Mariano/Desktop/APS/TS0/TS5/silbido.wav')

plt.figure()
plt.plot(wav_cuca)

# si quieren oirlo, tienen que tener el siguiente módulo instalado
# pip install sounddevice
# import sounddevice as sd
# sd.play(wav_data, fs_audio)



# Periodograma ventaneado audio
fcuca_per_ham, cuca_per_ham = sig.periodogram(wav_cuca,fs_cuca, window='hamming')
fcuca_per_hamz, cuca_per_hamz = sig.periodogram(wav_cuca, fs_cuca, window='hamming', nfft=10*fs_ecg )
fcuca_per_blk, cuca_per_blk = sig.periodogram(wav_cuca, fs_cuca, window='blackmanharris', scaling='density')
fcuca_per_blkz, cuca_per_blkz = sig.periodogram(wav_cuca, fs_cuca, window='blackmanharris',nfft=10*fs_ecg )
                                         
plt.figure()
plt.plot(fcuca_per_ham, 10*np.log10(cuca_per_ham+eps), label='Hamming')
plt.plot(fcuca_per_hamz, 10*np.log10(cuca_per_hamz+eps), label='Hamming + ZPad')
plt.plot(fcuca_per_blk, 10*np.log10(cuca_per_blk+eps), label='BlackmanHarris')
plt.plot(fcuca_per_blkz, 10*np.log10(cuca_per_blkz+eps), label='BlackmanHarris + ZPad')
plt.title("PSD - Periodograma ventaneado - Audio Cuca")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Densidad espectral dB")
plt.legend()
plt.grid(True)

print('varianza Hamming:   ',np.var(cuca_per_ham))
print('varianza Hamming Zero Padding:   ',np.var(cuca_per_hamz))
print('varianza BlackHarrys:   ',np.var(cuca_per_blk))
print('varianza BlackHarrys Zero Padding:   ',np.var(cuca_per_blkz))

# %% copilot

# Señal a analizar: podés cambiar ecg_one_lead, ppg o wav_data
signal_ecg= np.load('ecg_sin_ruido.npy')
fs = fs_ecg   # cambiar según la señal: fs_ppg o fs_audio

# --- 1) Periodograma ventaneado ---
f_per_ham, Pxx_per_ham = sig.periodogram(signal_ecg, fs_ecg, window='hamming')
f_per_hamz, Pxx_per_hamz = sig.periodogram(signal_ecg, fs_ecg, window='hamming', nfft=10*fs_ecg )
f_per_blk, Pxx_per_blk = sig.periodogram(signal_ecg, fs_ecg, window='blackmanharris', scaling='density')
f_per_blkz, Pxx_per_blkz = sig.periodogram(signal_ecg, fs_ecg, window='blackmanharris',nfft=10*fs_ecg )
                                         
plt.figure()
plt.plot(f_per_ham, 10*np.log10(Pxx_per_ham+eps), label='Hamming')
plt.plot(f_per_hamz, 10*np.log10(Pxx_per_hamz+eps), label='Hamming + Zero Padding')
plt.plot(f_per_blk, 10*np.log10(Pxx_per_blk+eps), label='BlackmanHarrys')
plt.plot(f_per_blkz, 10*np.log10(Pxx_per_blkz+eps), label='BlackmanHarrys + Zero Padding')
plt.title("PSD - Periodograma ventaneado")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Densidad espectral [V^2/Hz]")
plt.legend()
plt.grid(True)

print('varianza Hamming:   ',np.var(Pxx_per_ham))
print('varianza Hamming Zero Padding:   ',np.var(Pxx_per_hamz))
print('varianza BlackHarrys:   ',np.var(Pxx_per_blk))
print('varianza BlackHarrys Zero Padding:   ',np.var(Pxx_per_blkz))




# %%

# Periodograma ventaneado audio
fcuca_per_ham, cuca_per_ham = sig.periodogram(fs_audio_cuca,fs_cuca, window='hamming')
fcuca_per_hamz, cuca_per_hamz = sig.periodogram(fs_audio_cuca, fs_cuca, window='hamming', nfft=10*fs_ecg )
fcuca_per_blk, cuca_per_blk = sig.periodogram(fs_audio_cuca, fs_cuca, window='blackmanharris', scaling='density')
fcuca_per_blkz, cuca_per_blkz = sig.periodogram(fs_audio_cuca, fs_cuca, window='blackmanharris',nfft=10*fs_ecg )
                                         
plt.figure()
plt.plot(f_per_ham, 10*np.log10(fcuca_per_ham+eps), label='Hamming')
plt.plot(f_per_hamz, 10*np.log10(fcuca_per_hamz+eps), label='Hamming + Zero Padding')
plt.plot(f_per_blk, 10*np.log10(Pxx_per_blk+eps), label='BlackmanHarrys')
plt.plot(f_per_blkz, 10*np.log10(fcuca_per_blkz+eps), label='BlackmanHarrys + Zero Padding')
plt.title("PSD - Periodograma ventaneado - Audio Cuca")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Densidad espectral dB")
plt.legend()
plt.grid(True)

print('varianza Hamming:   ',np.var(cuca_per_ham))
print('varianza Hamming Zero Padding:   ',np.var(cuca_per_hamz))
print('varianza BlackHarrys:   ',np.var(cuca_per_blk))
print('varianza BlackHarrys Zero Padding:   ',np.var(cuca_per_blkz))



# print(np.var(Pxx_per))
# # %% Método de Welch
# f_welch, ECG_welch_ham1 = sig.welch(signal_ecg, fs_ecg, 'hamming', axis=-1, nperseg=1000, noverlap=400 )
# f_welch2, ECG_welch_ham2 = sig.welch(signal_ecg, fs_ecg, 'hamming', axis=-1, nperseg=2000, noverlap=400 )
# f_black2, ECG_welch_blk2 = sig.welch(signal_ecg, fs_ecg, 'blackharr', axis=-1, nperseg=1000, noverlap=400)
# f_black3, ECG_welch_blk3 = sig.welch(signal_ecg, fs_ecg, 'blackharr', axis=-1, nperseg=2000, noverlap=1000)
# #f_black, Pxx_ecg_bla1 = sig.welch(ecg_one_lead, fs_ecg, 'blackmanharris', axis=-1, nperseg=len(ecg_one_lead), noverlap=None)
# # f_3k, Pxx_den_ecg_3 = sig.welch(ecg_one_lead, fs_ecg, 'blackmanharris', axis=-1, nperseg=2000, noverlap=1000, nfft=2*len(ecg_one_lead))


# plt.figure()
# plt.clf()
# #plt.semilogy(f_welch, Pxx_welch, label='con semilogy')
# plt.plot(f_welch, 10*np.log10(ECG_welch_ham1+eps), label='Hamming nperseg 1000')
# plt.plot(f_welch2, 10*np.log10(ECG_welch_ham2+eps), label='Hamming nperseg 2000')
# plt.plot(f_black2, 10*np.log10(ECG_welch_blk2+eps), label='BlkHarr nperseg 1000')
# plt.plot(f_black3, 10*np.log10(ECG_welch_blk3+eps), label='BlkHarr nperseg 2000')
# #plt.plot(f_black, 10*np.log10(ECG_welch_blk1+eps), label='BlackHarr nperseg 100 overlap 70')
# #plt.semilogy(f_welch, ECG_welch_ham1, label='semi nperseg 100')
# plt.title("PSD - Método de Welch")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("Densidad espectral dB")
# plt.legend()
# plt.grid(True)

# print('varianza Hamming nperseg 1000:   ',np.var(ECG_welch_ham1))
# print('varianza Hamming nperseg 2000:   ',np.var(ECG_welch_ham2))
# print('varianza BlackHarrys nperseg 1000:   ',np.var(ECG_welch_blk2))
# print('varianza BlackHarrys nperseg 2000:   ',np.var(ECG_welch_blk3))





# %% 2) estimador de BW

def estimar_ancho_banda(f, psd, umbral=0.99):
    """
    Retorna la frecuencia donde se acumula el `umbral` de la energía total.
    """
    energia_acumulada = np.cumsum(psd)
    energia_total = energia_acumulada[-1]
    idx = np.searchsorted(energia_acumulada, umbral * energia_total)
    return f[idx]



# bw95_ham1 = estimar_ancho_banda(f_welch, ECG_welch_ham1, 0.95)
# bw95_ham2 = estimar_ancho_banda(f_welch2, ECG_welch_ham2, 0.95)

# bw95_black2 = estimar_ancho_banda(f_black2, ECG_welch_blk2, 0.95)
# bw95_black3 = estimar_ancho_banda(f_black3, ECG_welch_blk3, 0.95)

bw95_per_ham = estimar_ancho_banda(f_per_ham, Pxx_per_ham, 0.95)
bw95_per_hamz = estimar_ancho_banda(f_per_hamz, Pxx_per_hamz, 0.95)

bw95_per_black = estimar_ancho_banda(f_per_blk, Pxx_per_blk, 0.95)
bw95_per_blackz = estimar_ancho_banda(f_per_blkz, Pxx_per_blkz, 0.95)



# print(f"Señal Haming 1000 - BW 95%: {bw95_ham1:.1f} Hz")
# print(f"Señal Haming 2000 - BW 95%: {bw95_ham2:.1f} Hz")


print(f"Señal Per Haming - BW 95%: {bw95_per_ham:.1f} Hz")
print(f"Señal Per Haming + ZP - BW 95%: {bw95_per_hamz:.1f} Hz")
print(f"Señal Per Blakmanharris - BW 95%: {bw95_per_black:.1f} Hz")
print(f"Señal Per Blakmanharris + ZP - BW 95%: {bw95_per_blackz:.1f} Hz")






# # --- 3) Método Blackman-Tukey ---
# # Se calcula la autocorrelación y luego su FFT
# Rxx = sig.correlate(signal_to_analyze, signal_to_analyze, mode='full')
# Rxx = Rxx[len(Rxx)//2:]  # parte causal
# window = np.blackman(len(Rxx))
# Rxx_win = Rxx * window
# Pxx_bt = np.abs(np.fft.fft(Rxx_win))
# f_bt = np.fft.fftfreq(len(Rxx_win), d=1/fs)

# #print(np.var(Pxx_bt))
# plt.figure()
# #plt.semilogy(f_bt[:len(f_bt)//2], Pxx_bt[:len(f_bt)//2])
# plt.plot(f_bt[:len(f_bt)//2], Pxx_bt[:len(f_bt)//2])
# plt.title("PSD - Método Blackman-Tukey")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("Densidad espectral [V^2/Hz]")
# plt.grid(True)

# plt.show()


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

# fs_ppg = 400 # Hz

##################
## PPG con ruido
##################

# # Cargar el archivo CSV como un array de NumPy
# ppg = np.genfromtxt('PPG.csv', delimiter=',', skip_header=1)  # Omitir la cabecera si existe


##################
## PPG sin ruido
##################

# fs_ppg = 400 # Hz
# ppg = np.load('ppg_sin_ruido.npy')

# plt.figure()
# plt.plot(ppg)


#%%


