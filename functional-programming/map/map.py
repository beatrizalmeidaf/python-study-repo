counters = [1, 2, 3, 4]

def inc(x): return x + 10

print(list(map(inc, counters))) # mapeia cada elemento para a funcao inc e salva em uma lista os resultados

# usando lambda
print(list(map((lambda x: x + 3), counters)))


S1 = 'abc'
S2 = 'xyz123'
print(list(zip(S1, S2))) # cria pares de elementos