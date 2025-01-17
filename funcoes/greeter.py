def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("Informe seu nome:")
    f_name = input("Primeiro nome: ")
    l_name = input("Último nome: ")
    formatted_name = get_formatted_name(f_name, l_name)

    resposta = input("Gostaria de sair? (S/N): ").strip().lower()
    if resposta == 's':
        print(f"Até logo {formatted_name}!")
        break
    else:
        print(f"Olá, {formatted_name}!")
