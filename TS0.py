# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Mariano Gonzalez

import numpy as np

#%%Generador de senoidal
def mi_funcion_sen( vmax, dc, f0, ph, N, fs):
    tt=np.arange(0,N,1)*(1/fs)
    xx=dc + vmax*np.sin(2*np.pi*f0*tt + ph)
    return tt,xx 
import matplotlib.pyplot as plt

#%%Senoidal 
tt, xx = mi_funcion_sen( vmax = 1, dc = 0, f0 = 1, ph=0,N=100, fs = 100)
plt.figure()
plt.grid()
plt.plot(tt, xx)
plt.show()

#%%Generador de ruido
N=100
ruido=np.random.normal(0,0.1,N) # mu=0, sigma=0.1 de N muestra

#%%
ttr, xxr = mi_funcion_sen( vmax = 1, dc = 0, f0 = 1, ph=0,N=100, fs = 100)
yyr=xxr + ruido
plt.figure()
plt.grid()
plt.plot(ttr, yyr)
plt.show()

#%% cuantizando 
b=3 # b-bits
vfs=3 #volts
qq=vfs/2**b
xxq=np.round(xx/qq) 

plt.figure()
plt.grid()
plt.plot(tt, xxq)
plt.show()



"""  
snr=100
pr=1/(10**(snr/10)) #despeje 
varianza=np.var(xx)
print(pr)
print(varianza)
varianza2=np.var(y)
print(varianza2)
"""

     