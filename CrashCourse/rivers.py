rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'rio grand': 'usa',
    }

print('Here are the rivers:')

for k, v in rivers.items():
    print(k)

print('Here are the countries:')

for v in set(rivers.values()):
    print(v)

list_of_rivers = ['nile', 'mississippi', 'rio grand', 'ohio']

for river in list_of_rivers:
    if river in rivers:
        print(f"{river}, thanks for participating")
    else:
        print(f"{river}, join our list please")






