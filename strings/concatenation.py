primeiro_nome = input("Qual o seu primeiro nome?\n")
ultimo_nome = input("Qual o seu último nome?\n")

# Python usa o símbolo de adição para combinar strings
nome_completo = primeiro_nome + " " + ultimo_nome
print(f'Olá {nome_completo.title()}')