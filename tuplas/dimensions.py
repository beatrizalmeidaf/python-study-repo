dimensions = (200,50)
print(dimensions[0])

# dimensions[0] = 250 -> isso mostra que é imutavel

# mas é possivel sobrescrever uma tupla

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:") 
for dimension in dimensions:
    print(dimension)
