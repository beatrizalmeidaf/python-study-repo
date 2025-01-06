""" 2.3 Mensagem pessoal: Armazene o nome de uma pessoa em uma variável e
apresente uma mensagem a essa pessoa. Sua mensagem deve ser simples,
como “Alô Eric, você gostaria de aprender um pouco de Python hoje?”. """

name = input("Qual o seu nome?\n")
print(f"Alô {name.title()}, você gostaria de aprender um pouco de Python hoje?\n")

""" 2.4 – Letras maiúsculas e minúsculas em nomes: Armazene o nome de uma
pessoa em uma variável e então apresente o nome dessa pessoa em letras
minúsculas, em letras maiúsculas e somente com a primeira letra maiúscula. """

print(f'{name.upper()}\n{name.lower()}\n{name.title()}\n')

""" 2.5/2.6 Citação famosa: Encontre uma citação de uma pessoa famosa que você
admire. Exiba a citação e o nome do autor. Sua saída deverá ter a aparência
a seguir, incluindo as aspas: Albert Einstein certa vez disse: “Uma pessoa que
nunca cometeu um erro jamais tentou nada novo.” """

citador = "Albert Einstein"
citacao = "O espírito humano precisa prevalecer sobre a tecnologia."

print(f'{citador} certa vez disse: "{citacao}"\n')


"""Removendo caracteres em branco de nomes: Armazene o nome de alguma
coisa e inclua alguns caracteres em branco no início e no final do nome."""
movie_name = " Panico "
print(movie_name.rstrip().lstrip())