#ejemplo que sean aplicable a un contexto como 
#Estudiante de VIII semestre de Sistemas Computacionales.
def autenticar(usuario, contraseña, callback):
    """
    Valida credenciales y ejecuta un callback para mostrar el resultado.
    """
    if usuario == "admin" and contraseña == "1234":
        callback("Acceso concedido")
    else:
        callback("Acceso denegado")

def mostrar_mensaje(mensaje):
    """Imprime un mensaje en la consola."""
    print(mensaje)

# Se pasan credenciales válidas e inválidas con su respectivo callback
autenticar("admin", "1234", mostrar_mensaje)  # Acceso concedido
autenticar("user", "wrongpass", mostrar_mensaje)  # Acceso denegado
