import requests

#Metodo GET
requisicao = requests.get("https://testesrequests-default-rtdb.firebaseio.com/.json")
print(requisicao)
print(requisicao.json())
