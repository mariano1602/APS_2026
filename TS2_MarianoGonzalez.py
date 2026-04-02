# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:12:23 2026

@author: Mariano Gonzalez
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import scipy.signal as sig 

#%%Generador de senoidal
def mi_funcion_sen( vmax, dc, f0, ph, N, fs):
    tt=np.arange(0,N,1)*(1/fs)
    xx=dc + vmax*np.sin(2*np.pi*f0*tt + ph)
    return tt,xx 

# %% variables globales

#fase= np.pi/2  #fase
fs= 1000 #frecuencia de muestreo
nn=fs #muestra
f0=int(fs/nn) #f0
df=f0 #resolucion espectral
ts=1/fs

#%% cuantizador 
b=8 # b-bits
vfs=2 #volts "full scale"
qq=(vfs)/(2**b) # paso de cuantizacion
pq= (qq**2)/12 # potencia señal
kn=16 #secuencia
pn=kn*pq

#%%Generador de ruido
ruido=np.random.normal(0,np.sqrt(pn),nn) # mu=0, sigma=varianza del ruido de nn muestra
#SNR=10
#pr=10**(-SNR/10)

# %%
tt, xx = mi_funcion_sen( vmax = 1, dc = 0, f0 = f0, ph=0,N=nn, fs =fs)

sr = xx + ruido

xxq=np.round(sr/qq) *qq

un_ciclo=int((fs/f0)/8) #para ver de un cliclo completo

plt.figure(1)
plt.clf()
plt.grid()
plt.plot(tt[:un_ciclo],xx[:un_ciclo],'--', label='Senoidal')
plt.plot(tt[:un_ciclo],sr[:un_ciclo], label='senoidal + ruido')
plt.plot(tt[:un_ciclo],xxq[:un_ciclo], label='Senoidal muestreada')
plt.ylabel('Amplitud [V]')
plt.xlabel('Tiempo [s]')
plt.title(f"Señal muestreada por un ADC de {b} bits y kn= {kn}")
plt.legend()
plt.show()

# %% FFTs

# FFT de senoidal limpia
XX=fft(xx)
XXabs=np.abs(XX) 
XXang=np.angle(XX)
XXabs_2=XXabs**2# densidad espectral 

#FFT de senoidal + ruido
SR=fft(sr)
SRabs=np.abs(SR) 
SRang=np.angle(SR)
SRabs_2=SRabs**2 # densidad espectral

#FTT de senoidal + ruido cuantizada
XXQ=fft(xxq)
XXQabs=np.abs(XXQ) 
XXQang=np.angle(XXQ)
XXQabs_2=XXQabs**2  # densidad espectral

FX= np.arange(nn)*df #defino el eje X en Hertz

plt.figure(3)
plt.clf()
plt.plot(FX,np.log10(XXabs_2)*10, label="FFT senoidal")
plt.plot(FX,np.log10(SRabs_2)*10, label="FFT ruido")
plt.plot(FX,np.log10(XXQabs_2)*10, label="FFT ruido cuantizado")
plt.plot()
plt.grid()
plt.title("Densidad espectral de potencia")
plt.ylabel('Densidad de potencia [dB]')
plt.xlabel('Frecuencia [Hz]')
plt.legend()
plt.show()

# %% DSP

# Autocorrelación (biased)
R = sig.correlate(xx, xx)/nn ## autocorrelacion de xx con si misma
lags = np.arange(-nn+1, nn)

S_psd = np.fft.fftshift(fft(R))
freqs = np.fft.fftshift(np.fft.fftfreq(len(R), 1/fs))

# Magnitud en dB
S_psd_db = 10*np.log10(np.abs(S_psd))

plt.figure(figsize=(10,5))
plt.plot(R)
# plt.plot(freqs, S_psd_db)
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("PSD [dB]")
# plt.title("PSD como FFT de la autocorrelación")
plt.grid(True)
plt.show()



# %% ruido cuantizado

#secuencia de error
xxq=np.round(xx/qq) *qq #quedan en la misma magnitud que la senoidal
ee=xxq-xx #secueencia de error

plt.figure(4)
plt.clf()
plt.grid()
plt.hist(ee)
#plt.plot(ee, label='xxq' )
plt.legend()
plt.title(f"Ruido de cuantizacion para {b} bits Vfs= {vfs} - q={qq}" )