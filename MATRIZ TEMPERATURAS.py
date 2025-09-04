import random

ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4


temperaturas = [
    [
        [random.uniform(10, 35) for _ in range(semanas)]
        for _ in range(len(dias_semana))
    ]
    for _ in range(len(ciudades))
]

# bucles anidados
print("📊 Promedios semanales de temperatura por ciudad:")
for i, ciudad in enumerate(ciudades):  # CIUDAD
    print(f"\nCiudad: {ciudad}")
    for semana in range(semanas):  # SEMAANAS
        suma = 0
        for dia in range(len(dias_semana)):  # DIAS
            suma += temperaturas[i][dia][semana]
        promedio = suma / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f} °C")
