motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducatti'
print(motorcycles)

motorcycles.append('honda') # acrescentar no final da lista
print(motorcycles)

motorcycles.insert(0, 'yamaha') # acrescentar elemento em qualquer posição
print(motorcycles)

del motorcycles[0] # deletar elemento em uma posição conhecida 
print(motorcycles)

popped_motorcycle = motorcycles.pop() #  remove o último item de uma lista, mas permite trabalar com esse item depois da remoção
print(motorcycles)
print(f'A motocicleta removida foi {popped_motorcycle}') # mostra o elemento que foi tirado

# é possivel escolher a posição do elemento removido com pop

first_motorcycle = motorcycles.pop(1)
print(f'A primeira bicicleta era a {first_motorcycle}')

motorcycles.remove('ducatti')
print(motorcycles)