import requests

url = "https://assets.breatheco.de/apis/fake/sample/random-status.php"

response = requests.get(url)
# Just testing:
# print(response.status_code)
# print(response.content)
# print(response.text)

# Diccionario que mapea códigos de estado a mensajes
status_messages = {
    404: "The URL you asked for is not found",
    503: "Unavailable right now",
    200: "Everything went perfect",
    400: "Something is wrong with the request params"
}

if response.status_code == 200:
    print(response.text)
else:
    print("Something went wrong")

