import numpy as np
import matplotlib.pyplot as plt

def h(t):
    """
    Solución de la ecuación diferencial:
    h(t) = 200 + 0.25606*sin((2π/180)t) - 7.15344*cos((2π/180)t) - 178.84656*e^(-1.25×10^(-3)*t)
    """
    term1 = 200
    term2 = 0.25606 * np.sin((2 * np.pi / 180) * t)
    term3 = -7.15344 * np.cos((2 * np.pi / 180) * t)
    term4 = -178.84656 * np.exp(-1.25e-3 * t)
    
    return term1 + term2 + term3 + term4

# Crear el rango de tiempo
t = np.linspace(0, 5000, 2000)  # De 0 a 5000 unidades de tiempo con 2000 puntos

# Calcular los valores de h(t)
h_values = h(t)


# Crear una segunda gráfica enfocada en el comportamiento inicial
plt.figure(figsize=(12, 6))
t_short = np.linspace(0, 365, 1000)
h_short = h(t_short)

plt.plot(t_short, h_short, 'g-', linewidth=2, label='h(t)')
plt.grid(True, alpha=0.3)
plt.xlabel('Tiempo (t)', fontsize=12)
plt.ylabel('h(t)', fontsize=12)
plt.title('Comportamiento Inicial de h(t) (primer año)', fontsize=14)
plt.axhline(y=200, color='r', linestyle='--', alpha=0.7, label='y = 200')
plt.legend()
plt.tight_layout()
plt.show()