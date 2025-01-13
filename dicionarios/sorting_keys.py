D = {'a': 1, 'b': 2, 'c': 3}

Ks = list(D.keys()) # transforma em uma lista
print(Ks)

for key in Ks:
    print(key, '->', D[key])