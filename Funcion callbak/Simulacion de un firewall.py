#ejemplo que sean aplicable a un contexto como 
#Estudiante de VIII semestre de Sistemas Computacionales.
def analizar_trafico(paquete, callback):
    """
    Analiza el tráfico de red y ejecuta un callback si se detecta actividad sospechosa.
    """
    if "malicioso" in paquete:
        callback("⚠️ Tráfico bloqueado")
    else:
        callback("✅ Tráfico permitido")

def log_red(mensaje):
    """Registra un mensaje en el log de red."""
    print(mensaje)

# Análisis de tráfico con un callback de log
analizar_trafico("GET /index.html HTTP/1.1", log_red)  # ✅ Tráfico permitido
analizar_trafico("malicioso: ataque DDoS", log_red)  # ⚠️ Tráfico bloqueado
