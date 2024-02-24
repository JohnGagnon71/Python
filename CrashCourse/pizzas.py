pizzas = []
pizzas.append('sausage')
pizzas.append('mushroom')
pizzas.append('margharita')

my_friends_pizzas = pizzas[:]

pizzas.append('cheese')
my_friends_pizzas.append('meatball')

print('mine')
for pizza in pizzas:
    print(f"{pizza}")

print('\nfriends')
for pizza in my_friends_pizzas:
    print(f"{pizza}")

message = 'I am a big fan of pizza.\n'

for pizza in pizzas:
    message += 'I love '+pizza+'.\n'

message += 'I really love pizza!'

print(message)

