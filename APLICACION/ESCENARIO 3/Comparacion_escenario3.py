import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def h_analytical(t):
    """
    Solución analítica de la ecuación diferencial:
    h(t) = 200 + 0.25606*sin((2π/180)t) - 7.15344*cos((2π/180)t) - 178.84656*e^(-1.25×10^(-3)*t)
    """
    term1 = 200
    term2 = 0.25606 * np.sin((2 * np.pi / 180) * t)
    term3 = -7.15344 * np.cos((2 * np.pi / 180) * t)
    term4 = -178.84656 * np.exp(-1.25e-3 * t)
    
    return term1 + term2 + term3 + term4

# Leer el archivo CSV de OpenModelica
csv_filename = 'openmodelica_data.csv'  # Cambia este nombre por el de tu archivo

try:
    data = pd.read_csv(csv_filename)
    
    # Mostrar las primeras filas y columnas disponibles para verificar
    print("Columnas disponibles en el archivo CSV:")
    print(data.columns.tolist())
    print("\nPrimeras 5 filas:")
    print(data.head())
    
    # Asumimos que la primera columna es tiempo y la segunda es h(t)
    if 'time' in data.columns:
        t_openmodelica = data['time'].values
    else:
        t_openmodelica = data.iloc[:, 0].values  # Primera columna
    
    # Para h(t), busca una columna que contenga 'h' en el nombre
    h_column = None
    for col in data.columns:
        if 'h' in col.lower() or 'height' in col.lower():
            h_column = col
            break
    
    if h_column:
        h_openmodelica = data[h_column].values
    else:
        h_openmodelica = data.iloc[:, 1].values  # Segunda columna por defecto
    
    print(f"\nUsando columnas: tiempo='{data.columns[0]}', h(t)='{h_column or data.columns[1]}'")
    
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{csv_filename}'")
    print("Por favor, asegúrate de que el archivo esté en el directorio correcto.")
    print("Creando datos de ejemplo para demostración...")
    
    # Crear datos de ejemplo si no se encuentra el archivo
    t_openmodelica = np.linspace(0, 5000, 1000)
    # Añadir un pequeño ruido para simular datos numéricos
    h_openmodelica = h_analytical(t_openmodelica) + np.random.normal(0, 0.1, len(t_openmodelica))

except Exception as e:
    print(f"Error leyendo el archivo: {e}")
    print("Creando datos de ejemplo...")
    t_openmodelica = np.linspace(0, 5000, 1000)
    h_openmodelica = h_analytical(t_openmodelica) + np.random.normal(0, 0.1, len(t_openmodelica))

# Limitar el rango de tiempo hasta 365
t_limit = 365

# Filtrar datos de OpenModelica hasta t=365
mask_om = t_openmodelica <= t_limit
t_openmodelica_filtered = t_openmodelica[mask_om]
h_openmodelica_filtered = h_openmodelica[mask_om]

# Crear un rango de tiempo para la solución analítica hasta 365
t_analytical = np.linspace(0, t_limit, 2000)
h_values_analytical = h_analytical(t_analytical)

# Crear la gráfica de comparación
plt.figure(figsize=(14, 10))

# Graficar ambas soluciones
plt.plot(t_analytical, h_values_analytical, 'b-', linewidth=4, 
         label='Solución Analítica', alpha=0.8)
plt.plot(t_openmodelica_filtered, h_openmodelica_filtered, 'r--', linewidth=3, 
         label='OpenModelica', alpha=0.7)

plt.grid(True, alpha=0.3)
plt.xlabel('Tiempo (t)', fontsize=12)
plt.ylabel('h(t)', fontsize=12)
plt.title('Comparación: Solución Analítica vs OpenModelica (0-365 unidades de tiempo)\nh(t) = 200 + 0.25606sin((2π/180)t) - 7.15344cos((2π/180)t) - 178.84656e^(-1.25×10^(-3)t)', 
          fontsize=14, pad=20)

# Limitar el eje Y hasta 100
plt.ylim(0, 100)

plt.legend(fontsize=12)
plt.tight_layout()

# Calcular y mostrar estadísticas de comparación
if len(t_openmodelica_filtered) > 0:
    # Interpolar la solución analítica en los puntos de tiempo de OpenModelica
    h_analytical_interp = np.interp(t_openmodelica_filtered, t_analytical, h_values_analytical)
    
    # Calcular diferencias
    differences = h_openmodelica_filtered - h_analytical_interp
    mse = np.mean(differences**2)
    rmse = np.sqrt(mse)
    max_abs_error = np.max(np.abs(differences))
    
    print(f"\n=== ESTADÍSTICAS DE COMPARACIÓN (0-365) ===")
    print(f"Número de puntos en OpenModelica: {len(t_openmodelica_filtered)}")
    print(f"Rango de tiempo: [0, 365]")
    print(f"Error cuadrático medio (MSE): {mse:.6f}")
    print(f"Raíz del error cuadrático medio (RMSE): {rmse:.6f}")
    print(f"Error absoluto máximo: {max_abs_error:.6f}")
    print(f"Error relativo promedio: {np.mean(np.abs(differences/h_analytical_interp)*100):.4f}%")

plt.show()

print("\nNota: Si el archivo CSV no se encontró, se usaron datos de ejemplo.")
print("Para usar tus datos reales, asegúrate de:")
print("1. Colocar el archivo CSV en el mismo directorio que este script")
print("2. Cambiar 'csv_filename' al nombre correcto de tu archivo")
print("3. Verificar que las columnas tengan los nombres esperados")