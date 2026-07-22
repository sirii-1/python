text = "  Hello, Python World!  "
print(text.strip())

lower_text = text.lower()
upper_text = text.upper()
replaced = text.replace("World", "Developer")

name = "Alice"
age = 30
formatted = f"Name: {name}, Age: {age}"

csv_data = "apple,banana,cherry"
fruits_list = csv_data.split(",")
joined_text = " - ".join(fruits_list)

print(text.startswith("  Hello"))
print("Python" in text)