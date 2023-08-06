import requests

#Metodo DELETE
requisicao = requests.delete("https://testesrequests-default-rtdb.firebaseio.com/-NbBGSzYwxI9effZylyD.json")
print(requisicao)
print(requisicao.json())