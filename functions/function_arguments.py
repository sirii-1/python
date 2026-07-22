def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

def add_numbers(*args):
    total = sum(args)
    print("Sum of numbers:", total)

def print_user_profile(**kwargs):
    print("User profile data:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

describe_pet("Fabi")
describe_pet("Snow", "cat")
describe_pet(animal_type="hamster", pet_name="Hami")

add_numbers(10, 20)
add_numbers(1, 2, 3, 4, 5)

print_user_profile(username="bob01", email="my@test.com", status="active")