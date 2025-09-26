# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 18:57:06 2025

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

# Crear la gráfica de comparación
plt.figure(figsize=(14, 10))

# Graficar ambas soluciones con líneas gruesas
plt.plot(t_exponential, h_values_exponential, 'b-', linewidth=4, 
         label='Solución Exponencial: 14e^(-0.00125t)', alpha=0.8)
plt.plot(t_csv, h_csv, 'r--', linewidth=3, 
         label='variables_2.csv', alpha=0.7)

plt.grid(True, alpha=0.3)
plt.xlabel('Tiempo (t)', fontsize=12)
plt.ylabel('h(t)', fontsize=12)
plt.title('Comparación: Solución Exponencial vs variables_2.csv\nh(t) = 14e^(-0.00125t)', 
          fontsize=14, pad=20)

plt.legend(fontsize=12)
plt.tight_layout()

# Calcular y mostrar estadísticas de comparación
if len(t_csv) > 0:
    # Interpolar la solución exponencial en los puntos de tiempo del CSV
    h_exponential_interp = np.interp(t_csv, t_exponential, h_values_exponential)
    
    # Calcular diferencias
    differences = h_csv - h_exponential_interp
    mse = np.mean(differences**2)
    rmse = np.sqrt(mse)
    max_abs_error = np.max(np.abs(differences))
    
    print(f"\n=== ESTADÍSTICAS DE COMPARACIÓN ===")
    print(f"Número de puntos en CSV: {len(t_csv)}")
    print(f"Rango de tiempo: [{t_min:.2f}, {t_max:.2f}]")
    print(f"Error cuadrático medio (MSE): {mse:.6f}")
    print(f"Raíz del error cuadrático medio (RMSE): {rmse:.6f}")
    print(f"Error absoluto máximo: {max_abs_error:.6f}")
    
    # Evitar división por cero
    non_zero_mask = h_exponential_interp != 0
    if np.any(non_zero_mask):
        relative_errors = np.abs(differences[non_zero_mask]/h_exponential_interp[non_zero_mask]) * 100
        print(f"Error relativo promedio: {np.mean(relative_errors):.4f}%")
    
    # Información adicional sobre la función exponencial
    print(f"\n=== INFORMACIÓN DE LA FUNCIÓN EXPONENCIAL ===")
    print(f"Valor inicial h(0): {h_exponential(0):.4f}")
    print(f"Valor en t=500: {h_exponential(500):.4f}")
    print(f"Valor en t=1000: {h_exponential(1000):.4f}")
    print(f"Valor en t=2000: {h_exponential(2000):.4f}")

plt.show()

print("\nNota: Si el archivo CSV no se encontró, se usaron datos de ejemplo.")
print("Para usar tus datos reales, asegúrate de:")
print("1. Colocar el archivo 'variables_2.csv' en el mismo directorio que este script")
print("2. Verificar que las columnas tengan los nombres esperados")