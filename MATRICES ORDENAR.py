matriz = [
    [34, 12, 25],
    [45, 5, 18],
    [90, 72, 10]
]


# Función Bubble Sort para ordenar una listass
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiamos los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    if fila < 0 or fila >= len(matriz):
        print("Fila inválida.")
        return matriz

    # Copiamos la matriz original
    nueva_matriz = [fila.copy() for fila in matriz]
    nueva_matriz[fila] = bubble_sort(nueva_matriz[fila])
    return nueva_matriz


# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la fila 1 (segunda fila, índice 1)
fila_a_ordenar = 1
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)