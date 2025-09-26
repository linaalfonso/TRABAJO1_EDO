# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 13:04:47 2025

@author: nicko
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de tiempo t
t = np.linspace(0, 52, 200)  

# Definir la solución de la EDO
h = 14 - 0.25 * t

# Graficar
plt.figure(figsize=(8,5))
plt.plot(t, h, label=r'$h(t) = 14 - 0.25t$', color='b')

plt.title("Escenario 1: h(t) = 14 - 0.25t")
plt.xlabel("t")
plt.ylabel("h(t)")

plt.grid (True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
