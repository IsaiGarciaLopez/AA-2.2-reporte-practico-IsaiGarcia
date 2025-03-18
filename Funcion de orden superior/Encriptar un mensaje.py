#ejemplo que sean aplicable a un contexto como 
#Estudiante de VIII semestre de Sistemas Computacionales.
def aplicar_cifrado(mensaje, funcion_cifrado):
    """
    Aplica una función de cifrado a un mensaje dado.
    """
    return funcion_cifrado(mensaje)

def cifrado_simple(texto):
    """
    Realiza un cifrado básico desplazando cada caracter en +1 ASCII.
    """
    return ''.join(chr(ord(c) + 1) for c in texto)

mensaje = "Hola Sistemas"
mensaje_cifrado = aplicar_cifrado(mensaje, cifrado_simple)
print(mensaje_cifrado)  # Mensaje cifrado
