M = [[1, 2, 3],
 [4, 5, 6], 
 [7, 8, 9]]

print(M)

print(M[0])

print(M[0][2])

col2 = [row[1] for row in M]
print(col2)

diag = [M[i][i] for i in [0, 1, 2]] 
print(diag)

result = [row[1] + 1 for row in M if row[1] % 2 == 0]
print(result)

numeros = [1, 2, 3, 4, 5]
resultado = [numero * 2 for numero in numeros]
print(resultado)

palavra = "spam"
dobro = [letra * 2 for letra in palavra]
print(dobro)