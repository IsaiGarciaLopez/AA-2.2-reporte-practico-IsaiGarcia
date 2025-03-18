def procesar_pedido(producto, cantidad, callback):
    print(f"🛒 Procesando pedido: {cantidad} unidades de {producto}")
    callback(producto, cantidad)

def confirmar_pedido(producto, cantidad):
    print(f"✅ Pedido confirmado: {cantidad} unidades de {producto}")

def cancelar_pedido(producto, cantidad):
    print(f"❌ Pedido cancelado: {cantidad} unidades de {producto}")

# Uso de callbacks
procesar_pedido("Laptop", 2, confirmar_pedido)
procesar_pedido("Celular", 1, cancelar_pedido)
