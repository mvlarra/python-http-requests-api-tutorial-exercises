import requests

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url)

body = response.json()

""" Get the author name of the first post. """

out = body["posts"][0]["author"]["name"]

# print (type(out))
# Esto lo uso para irme dando cuenta si el nivel al que necesito acceder 
# es una lista (accedo con el indice entre []) o 
# es un diccionario (accedo con el nombre de la clave entre [""])

print (out)
