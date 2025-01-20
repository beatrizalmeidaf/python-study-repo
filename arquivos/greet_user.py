import json

filename = 'arquivos/username.json'

with open(filename) as f:
    user = json.load(f)

print(f"Seja bem vindo {user}")