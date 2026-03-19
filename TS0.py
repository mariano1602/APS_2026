# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Mariano Gonzalez

import numpy as np

def mi_funcion_sen( vmax, dc, f0, ph, N, fs):
    tt=np.arange(0,N,1)*(1/fs)
    xx=dc + vmax*np.sin(2*np.pi*f0*tt + ph)
    return tt,xx 
##N=4
##ruido=np.random.normal(0,0.1,N)
import matplotlib.pyplot as plt


tt, xx = mi_funcion_sen( vmax = 1, dc = 0, f0 = 500, ph=0,N=100, fs = 2000)
##y=xx + ruido
plt.figure()
plt.grid()
plt.plot(tt, xx)
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

     