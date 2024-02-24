motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.insert(0, 'ducati')
del motorcycles[0]
popped_motorcycle = motorcycles.pop()

print(motorcycles) 
print(popped_motorcycle)
# = ['honda', 'yamaha', 'suzuki']
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles) 

motorcycles.append('ducati')
print(motorcycles) 
