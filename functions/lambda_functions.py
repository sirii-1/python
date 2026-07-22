square = lambda x: x ** 2
print("Square of 6:", square(6))

add = lambda x, y: x + y
print("Sum of 15 and 25:", add(15, 25))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared list:", squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)