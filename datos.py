#Yeferson Monroy Molina 
#213022_1031
#Ingenieria en Sistemas
#Fase 5
#Nivel de compromiso del cliente 

# Matriz de datos [ID, Duracion, Clics]

sesiones = [
    [101, 200, 10],  # Fila 0
    [102, 45, 2],    # Fila 1
    [103, 120, 5],   # Fila 2
    [104, 300, 15],  # Fila 3
    [105, 50, 10]    # Fila 4
]
print("--- Sistema de Evaluacion de Compromiso ---")

def clasificar_compromiso(cliente):
    # Se extraen los datos de la lista 'cliente'
    # cliente[0] es el ID, cliente[1] es tiempo, cliente[2] es clics
    tiempo = cliente[1]
    clics = cliente[2]
    
    # Se aplica la  lógica de condicionales
    if tiempo > 180 and clics > 8:
        return "Alto"
    elif tiempo < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"
    
# 3. PROCESAMIENTO Y SALIDA
print(f"{'ID CLIENTE':<12} | {'CLASIFICACION'}")
print("-" * 30)

# Recorre la matriz 'sesiones'
for fila in sesiones:
    # Llama a la funcion y guardamos el resultado
    resultado = clasificar_compromiso(fila)
    
    # Se muestra el ID (que esta en fila[0]) y el resultado
    print(f"{fila[0]:<12} | {resultado}")
