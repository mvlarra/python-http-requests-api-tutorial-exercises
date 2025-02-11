import requests

url = "https://assets.breatheco.de/apis/fake/sample/time.php"
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()  # Convertir la respuesta a JSON (diccionario)
    
    # Obtener los valores de horas, minutos y segundos
    hours = data["hours"]
    minutes = data["minutes"]
    seconds = data["seconds"]
    
    # Formatear la salida
    formatted_time = f"Current time: {hours} hrs {minutes} min and {seconds} sec"
    
    # Imprimir el resultado
    print(formatted_time)
else:
    print("Error fetching the time:", response.status_code)
