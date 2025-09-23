informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}
informacion_personal["ciudad"] = "Guayaquil"
informacion_personal["profesion"] = "Diseñador Gráfico"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"
    del informacion_personal["edad"]
    print(informacion_personal)