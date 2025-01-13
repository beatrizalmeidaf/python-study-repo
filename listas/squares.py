squares = [] # inicializar a lista

for value in range(1,11):
    square = value**2 # quadrado perfeito 
    squares.append(square) # adiciona o quadrado perfeito a lista

print(squares)


# uso de list comprehension

squares = [value**2 for value in range(1,11)]
print(squares)