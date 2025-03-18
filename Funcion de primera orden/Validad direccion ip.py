#ejemplo que sean aplicable a un contexto como 
#Estudiante de VIII semestre de Sistemas Computacionales.
def validar_ip(ip):
    """
    Valida si una dirección IP está en el rango correcto (0-255 por octeto).
    """
    partes = ip.split(".")  # Separa la IP en 4 partes
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit() or not (0 <= int(parte) <= 255):
            return False
    return True

print(validar_ip("192.168.1.1"))  # True, IP válida
print(validar_ip("999.999.999.999"))  # False, IP inválida
