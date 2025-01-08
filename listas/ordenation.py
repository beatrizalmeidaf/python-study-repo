cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars) # ordenação por ordem alfabética crescente

cars.sort(reverse=True)
print(cars) # ordenação por ordem alfabética decrescente

print('\n')

# Para preservar a ordem original de uma lista, mas apresentá-la de forma ordenada, podemos usar a função sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)

print('\n')

# ordenação em ordem reversa há outro método
cars.reverse()
print(cars)

# tamanho da lista
print(len(cars))