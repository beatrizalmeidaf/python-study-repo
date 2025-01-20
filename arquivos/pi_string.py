with open('arquivos/digitos.txt') as file_object:
    lines = file_object.readlines()  # armazena informações em uma lista
    pi_string = ''  

    for line in lines:
        pi_string += line.rstrip()  # remove os espaços em branco à direita de cada linha

    aniversario = input("Entre com sua data de aniversário no formato ddmmyy: ")
    
    if aniversario in pi_string:
        print("O seu aniversário está em pi!")
    else:
        print("O seu aniversário não está em pi.")
        

print(pi_string[:5])
print(len(pi_string))
