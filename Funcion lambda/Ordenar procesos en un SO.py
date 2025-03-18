#ejemplo que sean aplicable a un contexto como 
#Estudiante de VIII semestre de Sistemas Computacionales.
procesos = [
    {"nombre": "Proceso A", "prioridad": 3},
    {"nombre": "Proceso B", "prioridad": 1},
    {"nombre": "Proceso C", "prioridad": 2}
]

# Se ordena la lista de procesos según la prioridad usando una función lambda
procesos_ordenados = sorted(procesos, key=lambda p: p["prioridad"])

# Se imprimen los procesos ordenados
for p in procesos_ordenados:
    print(f"{p['nombre']} - Prioridad {p['prioridad']}")
