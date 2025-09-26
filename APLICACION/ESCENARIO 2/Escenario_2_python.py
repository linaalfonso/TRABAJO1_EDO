# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 19:05:45 2025

@author: gijug
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def h_exponential(t):
    """
    Solución exponencial de la ecuación diferencial:
    h(t) = 14*e^(-0.00125*t)
    """
    return 14 * np.exp(-0.00125 * t)

# Leer el archivo CSV variables_2.csv
csv_filename = 'variables_2.csv'

try:
    # Leer el archivo CSV
    data = pd.read_csv(csv_filename)
    
    # Mostrar las primeras filas y columnas disponibles para verificar
    print("Columnas disponibles en variables_2.csv:")
    print(data.columns.tolist())
    print("\nPrimeras 5 filas:")
    print(data.head())
    
    # Asume que la primera columna es tiempo y la segunda es h(t)
    # Ajusta estos índices o nombres según tu archivo
    if 'time' in data.columns:
        t_csv = data['time'].values
    else:
        t_csv = data.iloc[:, 0].values  # Primera columna
    
    # Para h(t), busca una columna que contenga 'h' en el nombre
    h_column = None
    for col in data.columns:
        if 'h' in col.lower() or 'height' in col.lower():
            h_column = col
            break
    
    if h_column:
        h_csv = data[h_column].values
    else:
        h_csv = data.iloc[:, 1].values  # Segunda columna por defecto
    
    print(f"\nUsando columnas: tiempo='{data.columns[0]}', h(t)='{h_column or data.columns[1]}'")
    
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{csv_filename}'")
    print("Por favor, asegúrate de que el archivo esté en el directorio correcto.")
    print("Creando datos de ejemplo para demostración...")
    
    # Crear datos de ejemplo si no se encuentra el archivo
    t_csv = np.linspace(0, 2000, 500)
    # Añadir un pequeño ruido para simular datos numéricos
    h_csv = h_exponential(t_csv) + np.random.normal(0, 0.05, len(t_csv))

except Exception as e:
    print(f"Error leyendo el archivo: {e}")
    print("Creando datos de ejemplo...")
    t_csv = np.linspace(0, 2000, 500)
    h_csv = h_exponential(t_csv) + np.random.normal(0, 0.05, len(t_csv))

# Crear un rango de tiempo para la solución exponencial que cubra el rango del CSV
t_min = 0
t_max = max(t_csv) if len(t_csv) > 0 else 2000
t_exponential = np.linspace(t_min, t_max, 2000)
h_values_exponential = h_exponential(t_exponential)

# Crear la gráfica de la solución exponencial
plt.figure(figsize=(12, 8))

plt.plot(t_exponential, h_values_exponential, 'b-', linewidth=4, 
         label='h(t) = 14e^(-0.00125t)', alpha=0.9)

plt.grid(True, alpha=0.3)
plt.xlabel('Tiempo (t)', fontsize=12)
plt.ylabel('h(t)', fontsize=12)
plt.title('Solución Exponencial de la Ecuación Diferencial\nh(t) = 14e^(-0.00125t)', 
          fontsize=14, pad=20)

plt.legend(fontsize=12)
plt.tight_layout()

# Mostrar información sobre la función exponencial
print(f"\n=== INFORMACIÓN DE LA FUNCIÓN EXPONENCIAL ===")
print(f"Valor inicial h(0): {h_exponential(0):.4f}")
print(f"Valor en t=500: {h_exponential(500):.4f}")
print(f"Valor en t=1000: {h_exponential(1000):.4f}")
print(f"Valor en t=2000: {h_exponential(2000):.4f}")

plt.show()