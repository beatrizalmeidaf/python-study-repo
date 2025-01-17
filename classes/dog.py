class Dog(): # o parâmetro self é obrigatório na definição do método e deve estar antes dos demais parâmetros
    def __init__(self, name, age): # inicializa os tributos name e age
        self.name = name 
        self.age = age

    def sit(self):
      """Simula um cachorro sentando em resposta a um comando"""
      print(self.name.title() + " is now sitting.")

    def rolar(self):
       """Simula um cachorro rolando em resposta a um comando"""
       print(self.name.title() + " rolled over!") 

    
# instanciando
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.rolar()
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
