import json

filename = 'arquivos/number.json'

with open(filename) as f: 
    numbers = json.load(f) # modo leitura

print(numbers)
