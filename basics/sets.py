raw_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(raw_numbers)
print("unique_numbers:", unique_numbers)

unique_numbers.add(6)
unique_numbers.discard(3)
print("updated set:", unique_numbers)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("union (|):", set_a | set_b)
print("intersection (&):", set_a & set_b)
print("difference (-):", set_a - set_b)