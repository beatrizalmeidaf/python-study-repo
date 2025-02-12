import os

diretorio_atual = os.getcwd()
print(f'\nO diretório atual é {diretorio_atual}\n')

arquivos = os.listdir(diretorio_atual)
print(f'Os arquivos no diretório atual são {arquivos}\n')

novo_diretorio = 'novo_diretorio'
if os.path.isdir(novo_diretorio):
    os.chdir(novo_diretorio)
    print(f'O novo diretório {novo_diretorio} existe e estamos nele')
else:
    print(f'O novo diretório {novo_diretorio} não existe e será criado')
    os.mkdir(novo_diretorio)
    os.chdir(novo_diretorio)

resposta = input('Deseja remover o diretório criado? (s/n) ')
if resposta == 's':
    os.chdir(diretorio_atual)
    os.rmdir(novo_diretorio)
    print(f'O diretório {novo_diretorio} foi removido')
else:
    print(f'O diretório {novo_diretorio} não foi removido')