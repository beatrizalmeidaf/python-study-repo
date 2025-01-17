user_0 = {
'username': 'efermi', 
'first': 'enrico', 
'last': 'fermi' }

for key, value in user_0.items():
    print(f'Key: {key} -> Value: {value}\n')

favorite_languages = {
'jen': 'python', 
'sarah': 'c', 
'edward': 'ruby', 
'phil': 'python', }

# listar todas as chaves do dicionário e ordenar essa lista
for name in sorted(favorite_languages.keys()): 
    print(name.title())

# listar todos os valores do dicionário sem repetições de valores
for language in set(favorite_languages.values()): 
    print(language.title()) 