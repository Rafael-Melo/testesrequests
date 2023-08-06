import requests

#Metodo PATCH
informacoes ='{"nome": "Samara", "sobrenome": "Melo", "idade": "13"}'
requisicao = requests.patch("https://testesrequests-default-rtdb.firebaseio.com/-NbBFYoDBs9Pzqlk_lso.json", data=informacoes)
print(requisicao)
print(requisicao.json())