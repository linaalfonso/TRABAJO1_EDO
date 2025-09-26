# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 19:07:43 2025

@author: gijug
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --- Escenario 1: solución lineal ---
def h_lineal(t):
    return 14 - 0.25 * t

# --- Escenario 2: solución exponencial ---
def h_exponential(t):
    return 14 * np.exp(-0.00125 * t)

# Rango de tiempo compartido (que cubra ambos escenarios)
t = np.linspace(0, 2000, 500)

# Escenario 1 (se define hasta t=52, luego es 0)
h1 = np.where(t <= 52, h_lineal(t), 0)

# Escenario 2
h2 = h_exponential(t)

# Gráfica comparativa
plt.figure(figsize=(10,6))
plt.plot(t, h1, label="Escenario 1: $h(t)=14-0.25t$", color="blue", linewidth=2)
plt.plot(t, h2, label="Escenario 2: $h(t)=14e^{-0.00125t}$", color="red", linewidth=2)

plt.title("Comparación Escenario 1 vs Escenario 2", fontsize=14)
plt.xlabel("Tiempo (t)")
plt.ylabel("h(t)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
