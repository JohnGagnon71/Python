music = 'Jim Morrison'
inventor = 'Elon Musk'
pc = 'Bill Gates'
invite_list = []
invite_list.append(music)
invite_list.append(inventor)
invite_list.append(pc)

message = f'{invite_list[0]}, please come to dinner.'
print (message)
message = f'{invite_list[1]}, please come to dinner.'
print (message)
message = f'{invite_list[2]}, please come to dinner.'
print (message)

message = f'{invite_list[1]}, cannot make it to dinner.'
print(message)

invite_list.remove(invite_list[1])
invite_list.append('Marisa Bellucci')

message = f'{invite_list[0]}, please come to dinner.'
print (message)
message = f'{invite_list[1]}, please come to dinner.'
print (message)
message = f'{invite_list[2]}, please come to dinner.'
print (message)

print('I found a bigger table')
invite_list.insert(0, 'Katy Perry')
invite_list.insert(2, 'Taylor Swift')
invite_list.append('Allen Hobbs')

message = f'{invite_list[0]}, please come to dinner.'
print (message)
message = f'{invite_list[1]}, please come to dinner.'
print (message)
message = f'{invite_list[2]}, please come to dinner.'
print (message)
message = f'{invite_list[3]}, please come to dinner.'
print (message)
message = f'{invite_list[4]}, please come to dinner.'
print (message)
message = f'{invite_list[5]}, please come to dinner.'
print (message)

message ='I can only invite 2 people'
print(message)
uninvited = invite_list.pop()
message=f'{uninvited}, sorry I cannot invite you to dinner.'
print(message)
uninvited = invite_list.pop()
message=f'{uninvited}, sorry I cannot invite you to dinner.'
print(message)
uninvited = invite_list.pop()
message=f'{uninvited}, sorry I cannot invite you to dinner.'
print(message)
uninvited = invite_list.pop()
message=f'{uninvited}, sorry I cannot invite you to dinner.'
print(message)

message = f'{invite_list[0]}, please come to dinner.'
print (message)
message = f'{invite_list[1]}, please come to dinner.'
print (message)

number_of_guests = len(invite_list)
print ("The number of guests = %d" % (number_of_guests))

del invite_list[0]
del invite_list[0]

print(invite_list)