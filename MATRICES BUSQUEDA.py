matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):          # Recorre las filas
        for j in range(len(matriz[i])):   # Recorre las columnas
            if matriz[i][j] == valor:     # Si encuentra el valor
                return (i, j)             # Retorna la posición (fila, columna)
    return None

# Valor a buscar
valor_buscado = 50

# Búsqueda
posicion = buscar_valor(matriz, valor_buscado)

# Resultados
print("Matriz:")
for fila in matriz:
    print(fila)

if posicion:
    print(f"\nEl valor {valor_buscado} fue encontrado en la posición {posicion} (fila, columna).")
else:
    print(f"\nEl valor {valor_buscado} no se encuentra en la matriz.")