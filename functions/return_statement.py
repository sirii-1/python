def multiply(a, b):
    return a * b

def get_min_max(numbers):
    return min(numbers), max(numbers)

def check_even(num):
    if num % 2 == 0:
        return True
    return False

result = multiply(4, 7)
print("Product:", result)

minimum, maximum = get_min_max([12, 45, 2, 89, 34])
print("Minimum:", minimum)
print("Maximum:", maximum)

print("Is 8 even?:", check_even(8))
print("Is 11 even?:", check_even(11))