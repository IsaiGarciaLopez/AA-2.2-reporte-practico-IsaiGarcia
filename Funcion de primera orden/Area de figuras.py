def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    import math
    return math.pi * radio ** 2

# Cálculo de áreas
print("Área del cuadrado:", area_cuadrado(5))
print("Área del rectángulo:", area_rectangulo(4, 6))
print("Área del círculo:", area_circulo(3))