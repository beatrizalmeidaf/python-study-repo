S = 'Spam'
print(len(S)) # len() retorna o número de caracteres em uma string
print(f'Primeira letra: {S[0]}')
print(f'Última letra: {S[-1]}')

print(f'Três primeiras letras: {S[0:3]}')

print(S[1:]) # imprime todos os caracteres da string, exceto o primeiro
print(S[:-1]) # imprime todos os caracteres da string, exceto o último

new_string = S + " " + 'from Google '
print(new_string)

print(new_string*3)

# S[0] = 'x' strings são imutáveis, não é possível alterar um caractere específico em uma string