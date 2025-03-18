#ejemplo que sean aplicable a un contexto como 
#Estudiante de VIII semestre de Sistemas Computacionales.
def log_error():
    """Registra un error en el sistema."""
    return "🚨 Error en el sistema."

def log_warning():
    """Registra una advertencia en el sistema."""
    return "⚠️ Advertencia de seguridad."

def log_info():
    """Registra información general."""
    return "ℹ️ Información general."

# Se asignan las funciones a una variable y se ejecutan
logger = log_error
print(logger())  # Ejecuta log_error

logger = log_warning
print(logger())  # Ejecuta log_warning
