"""4.3 – Contando até vinte: Use um laço for para exibir os números de 1 a 20,
incluindo-os.
"""

for value in range(1,21):
    print(value)

"""4.6 – Números ímpares: Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos
os números.
"""

numeros_impares = [value for value in range(1,21,2)]
print(numeros_impares)


"""4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.
"""

mult_tres = [value*3 for value in range(3,11)]
print(mult_tres)

"""4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.
"""

cubos = [value**3 for value in range(1,11)]
print(cubos)