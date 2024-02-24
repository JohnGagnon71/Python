players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:\n")
print('1\n')

for player in players[:3]:
    print(player.title())

print('2\n')
for player in players[1:4]:
    print(player.title())

print('3\n')
for player in players[-3:]:
    print(player.title())        