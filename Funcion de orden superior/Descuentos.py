def aplicar_descuento(productos, funcion_descuento):
    return {producto: funcion_descuento(precio) for producto, precio in productos.items()}

def descuento_10(p):
    return p * 0.9

def descuento_20(p):
    return p * 0.8

productos = {"Laptop": 1000, "Celular": 500, "Tablet": 300}

# Aplicando descuentos usando función de orden superior
print("Precios con 10% de descuento:", aplicar_descuento(productos, descuento_10))
print("Precios con 20% de descuento:", aplicar_descuento(productos, descuento_20))
