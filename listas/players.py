# fatiando uma lista
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[1:4])
print(players[:4]) # começará no primeiro indice e vai até o 4
print(players[2:]) # começa a partir do segundo
print(players[-3:]) # exibe tres ultimos

print("\nOs primeiros três jogadores são:")
for player in players[:3]:
    print(player)