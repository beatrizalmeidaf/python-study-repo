f = lambda x, y, z: x + y + z
print(f(2, 3, 4))


L = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]

for f in L:
    print(f(2))

print(L[0](3)) # printar o primeiro lambda com a expressao 3

lower = (lambda x, y: x if x < y else y)
print(lower('bb', 'aa'))

# usando map
numeros = [1, 2, 3, 4, 5]

dobrar = list(map(lambda x: x**2, numeros))
print(dobrar)