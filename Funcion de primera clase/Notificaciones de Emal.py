def notificacion_email():
    return "📩 Enviando correo electrónico..."

def notificacion_sms():
    return "📱 Enviando mensaje de texto..."

def notificacion_push():
    return "🔔 Enviando notificación push..."

# Asignar funciones a variables
notificar = notificacion_email
print(notificar())

notificar = notificacion_sms
print(notificar())

notificar = notificacion_push
print(notificar())
