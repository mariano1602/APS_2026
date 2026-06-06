# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:41:27 2026

@author: Mariano
"""

from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt

b = [1,1,1,1]   #a)
#b = [1,1,1,1,1]  #b)
#b = [1, -1]     #c)
#b = [1,0,-1]    #d)

a = [1]       # denominador

w, H = freqz(b, a, worN=1024)
plt.clf()
plt.figure(1)
plt.plot(w, np.abs(H),  label = 'Amplitud')
plt.plot(w, np.angle(H), label = 'Fase')
plt.xlabel('Frecuencia [rad/muestra]')
plt.ylabel('∠H(w) y |H(w)|  [rad]')
plt.grid(True)
plt.legend()
plt.show()

