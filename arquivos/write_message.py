filename = 'arquivos/programming.txt'

with open(filename, 'w') as file_object: 
    file_object.write("I love programming.") 


# se quiser acrescentar conteúdos em um arquivo em vez de sobrescrever
# o conteúdo existente, pode abrir o arquivo em modo de concatenação 'a'