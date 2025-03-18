#ejemplo que sean aplicable a un contexto como 
#Estudiante de VIII semestre de Sistemas Computacionales.
def convertir_bases(numero):
    """
    Convierte un número decimal a binario, octal y hexadecimal.
    """
    return {
        "binario": bin(numero),        # Convierte a binario
        "octal": oct(numero),          # Convierte a octal
        "hexadecimal": hex(numero)     # Convierte a hexadecimal
    }

numero = 25
conversiones = convertir_bases(numero)
print(conversiones)  # Muestra los valores en diferentes bases
