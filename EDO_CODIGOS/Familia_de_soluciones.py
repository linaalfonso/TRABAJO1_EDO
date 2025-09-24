# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 16:46:30 2025

@author: nicko
"""

import numpy as np
import matplotlib.pyplot as plt

# Solución general 
def y_sol(x, C):
    return 50 / (20*x + 4 + C*np.exp(5*x))

# Para la solución particular con y(0)=2, el valor de C es 21
C_part = 21

# Rango de x
x_vals = np.linspace(0, 2, 200)

#Gráfica 1: solución particular 
y_part = y_sol(x_vals, C_part)

plt.figure(figsize=(8,5))
plt.plot(x_vals, y_part, 'r', label="Solución particular, y(0)=2")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Solución particular de la EDO")
plt.grid(True)
plt.legend()
plt.show()

#Gráfica 2: campo de pendientes + familia de soluciones 
# Definimos el campo de pendientes (dy/dx = 2xy^2 - 5y)
X, Y = np.meshgrid(np.linspace(0, 2, 20), np.linspace(0, 5, 20))
dY = 2*X*Y**2 - 5*Y
dX = np.ones_like(dY)

# Normalizamos flechas
M = np.hypot(dX, dY)
dX, dY = dX/M, dY/M

plt.figure(figsize=(8,5))
plt.quiver(X, Y, dX, dY, angles="xy")

# Dibujamos 4 miembros de la familia de soluciones
C_values = [5, 10, 50, 100]
for C in C_values:
    plt.plot(x_vals, y_sol(x_vals, C), label=f"C={C}")

# Dibujamos también la particular
plt.plot(x_vals, y_sol(x_vals, C_part), 'r', linewidth=2, label="Particular y(0)=2")

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Familia de soluciones y campo de pendientes")
plt.grid(True)
plt.legend()
plt.show()
