"""3.1 – Nomes: Armazene os nomes de alguns de seus amigos em uma lista
chamada names. Exiba o nome de cada pessoa acessando cada elemento da
lista, um de cada vez."""

names = ['Andre', 'Roberta', 'william', 'fernanda', 'Alice']

for name in range(len(names)):
    print(names[name].title())

"""3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas.
O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve
estar personalizada com o nome da pessoa.
"""

for name in range(len(names)):
    print(f'Olá {names[name].title()}, tudo bem com você?')
