# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 13:34:35 2025

@author: nicko
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos desde CSV
datos = pd.read_csv('variables_1.csv')

# Definir el rango de tiempo para la solución analítica
t = np.linspace(0, 52, 200)  
h = 14 - 0.25 * t

# Graficar ambos en la misma figura
plt.figure(figsize=(8,5))

# Datos del CSV
plt.plot(datos['time'], datos['h'], label="Datos CSV", color='r')

# Solución analítica
plt.plot(t, h, label=r'$h(t) = 14 - 0.25t$', color='b')

# Personalización
plt.title("Comparación: Openmodelica vs Python")
plt.xlabel("t")
plt.ylabel("h(t)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

