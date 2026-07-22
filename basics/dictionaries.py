user = {"name": "Zee", "age": 26, "role": "Model"}

age = user.get("age", 0)
location = user.get("location", "Unknown")
print("age:", age)
print("location:", location)

user["location"] = "New York"
user["age"] = 29
print("updated user:", user)

email = user.pop("email", None)
print("popped email:", email)

print("--- User Items ---")
for key, value in user.items():
    print(f"{key}: {value}")

scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
passed = {name: score for name, score in scores.items() if score >= 80}
print("passed dictionary:", passed)