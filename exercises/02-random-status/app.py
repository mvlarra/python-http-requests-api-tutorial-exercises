import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

# Diccionario que mapea códigos de estado a mensajes
status_messages = {
    404: "The URL you asked for is not found",
    503: "Unavailable right now",
    200: "Everything went perfect",
    400: "Something is wrong with the request params"
}

# Obtener el mensaje correspondiente al código de estado
print(status_messages.get(response.status_code, "Unknown status code"))

# 🔥1. status_messages
#     Es un diccionario que hemos definido anteriormente, donde las claves son los códigos de estado 
#     (como 200, 404, etc.) y los valores son los mensajes de texto asociados a esos códigos.

# 🔥2.response.status_code
#     Es un atributo del objeto response que contiene el código de estado HTTP devuelto por el servidor tras hacer una solicitud. 
#     Este código indica el resultado de la solicitud HTTP (404, 200, etc)

# 🔥3.status_messages.get(...)
#     El método .get() de los diccionarios en Python busca una clave específica (en este caso, 
#     el valor de response.status_code) y devuelve el valor asociado a esa clave. 
#     Si la clave no se encuentra, .get() puede devolver un valor por defecto.