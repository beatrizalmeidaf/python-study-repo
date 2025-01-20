with open('arquivos/digitos.txt') as file_object:
    lines = file_object.readlines() # armazenar informações em uma lista para poder usar depois
    for line in lines:
        print(line.rstrip())

    #contents = file_object.read()
    #print(contents.rstrip())