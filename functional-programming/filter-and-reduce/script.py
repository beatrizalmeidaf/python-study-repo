from functools import reduce

print(list(range(-5, 5)))

# filtra os itens da lista que atendem a uma condição
print(list(filter((lambda x: x > 0), range(-5, 5))))


# reduz a lista a um unico valor
numeros = [1, 2, 3, 4]

soma = reduce(lambda x, y: x + y, numeros)  
produto = reduce(lambda x, y: x * y, numeros)  

print(soma)
print(produto)