# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 13:01:48 2025

@author: nicko
"""

import numpy as np
import matplotlib.pyplot as plt

def mapa_pendientes():
    x = np.linspace(-5, 5, 25)
    y = np.linspace(-5, 5, 25)
    X, Y = np.meshgrid(x, y)

    # Pendiente dy/dx
    derivada = 2*X*Y**2 - 5*Y

    deltax = 1
    deltay = derivada
    magnitud = np.sqrt(deltax**2 + deltay**2)
    deltax /= magnitud
    deltay /= magnitud

    plt.figure(figsize=(8, 6))
    plt.quiver(X, Y, deltax, deltay, color='blue')
    plt.title(r"Mapa de pendientes de $15y + 3\frac{dy}{dx} = 6xy^2$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

mapa_pendientes()


