import json

username = input("Qual o seu nome? ")
filename = 'arquivos/username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"Vamos lembrar de você quando voltar, {username}")
