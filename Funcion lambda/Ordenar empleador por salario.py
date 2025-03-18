empleados = [
    {"nombre": "Carlos", "salario": 2500},
    {"nombre": "Ana", "salario": 3200},
    {"nombre": "Luis", "salario": 2800}
]

# Ordenamos por salario usando una función lambda
empleados_ordenados = sorted(empleados, key=lambda e: e["salario"], reverse=True)

# Mostramos los empleados ordenados
for empleado in empleados_ordenados:
    print(f"👨‍💼 {empleado['nombre']} - 💰 Salario: {empleado['salario']}")