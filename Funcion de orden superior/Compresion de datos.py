#ejemplo que sean aplicable a un contexto como 
#Estudiante de VIII semestre de Sistemas Computacionales.
import zlib
import base64

def aplicar_compresion(datos, metodo):
    """
    Aplica un método de compresión a los datos proporcionados.
    """
    return metodo(datos.encode())  # Convierte a bytes y aplica la función de compresión

def compresion_zlib(datos):
    """Comprime datos usando zlib."""
    return zlib.compress(datos)

def compresion_base64(datos):
    """Comprime datos usando Base64."""
    return base64.b64encode(datos)

texto = "Este es un mensaje importante en redes."
print(aplicar_compresion(texto, compresion_zlib))  # Comprime con zlib
print(aplicar_compresion(texto, compresion_base64))  # Comprime con base64
