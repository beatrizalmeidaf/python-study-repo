import os 

# Obtendo o valor da variável de ambiente PATH
path = os.environ.get('PATH')
print(f'Variável PATH: {path}')

# Definindo uma nova variável de ambiente
os.environ['NOVA_VARIAVEL'] = 'VALOR'
print(f'Variável NOVA_VARIAVEL: {os.environ["NOVA_VARIAVEL"]}')
