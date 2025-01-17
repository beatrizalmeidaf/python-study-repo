class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def descricao(self):
        name = str(self.year) + ' ' + self.make + ' ' + self.model
        return name
    

# instância
car = Car('audi', 'a4', 2016)
print(car.descricao())