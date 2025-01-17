# *toppings agrupa tantos argumentos quantos forem fornecidos
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')