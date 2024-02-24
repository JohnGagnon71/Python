numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

print(max(digits))

print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print (squares)

num_list = []
for value in range(1,21):
    num_list.append(value)
    print(value)

mil_list = [value for value in range(1, 1000001)]

print(min(mil_list))
print(max(mil_list))
print(sum(mil_list))

# for number in mil_list:
#    print(number)

odd_numbers = [value for value in range(1, 20, 2)]
for number in odd_numbers:
    print(number)

third_numbers = [value for value in range(3, 31, 3)]
for number in third_numbers:
    print(number)    

cube_numbers = [value**3 for value in range(1, 11)]
for number in cube_numbers:
    print(number)        