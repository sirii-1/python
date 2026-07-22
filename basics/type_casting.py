# type_casting.py

integer_number = 25
float_number = 7.8
string_number = "100"

print("Original Values")
print(integer_number, type(integer_number))
print(float_number, type(float_number))
print(string_number, type(string_number))

print()

print("After Type Casting")

a = float(integer_number)
b = int(float_number)
c = int(string_number)

print(a, type(a))
print(b, type(b))
print(c, type(c))