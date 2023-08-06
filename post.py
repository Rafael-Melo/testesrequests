import requests

#Metodo POST
informacoes = '{"nome": "Nicole", "sobrenome": "Melo", "idade": "1"}'
requisicao = requests.post("https://testesrequests-default-rtdb.firebaseio.com/.json", data=informacoes)
print(requisicao)
print(requisicao.json())