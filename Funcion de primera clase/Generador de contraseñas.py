#ejemplo que sean aplicable a un contexto como 
#Estudiante de VIII semestre de Sistemas Computacionales.
import random
import string

def generar_password():
    """
    Genera una contraseña aleatoria de 12 caracteres combinando letras, números y símbolos.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(12))

# Se asigna la función a una variable y se ejecuta
password_generator = generar_password
print("Nueva contraseña:", password_generator())
