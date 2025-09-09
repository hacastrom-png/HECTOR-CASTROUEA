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

def promedio_por_ciudad(ciudades, temperaturas, dias_semana, semanas):

    resultados = {}
    for i, ciudad in enumerate(ciudades):
        suma_total = 0
        cantidad = 0
        for dia in range(len(dias_semana)):
            for semana in range(semanas):
                suma_total += temperaturas[i][dia][semana]
                cantidad += 1
        promedio = suma_total / cantidad
        resultados[ciudad] = promedio
    return resultados

promedios = promedio_por_ciudad(ciudades, temperaturas, dias_semana, semanas)

print(" temperatura promedio por ciudad durante todo el período:\n")
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f} °C")