import random


possible_colors = ["black", "green", "orange", "blue", "yellow", "red"]
max_attemps = 10
combination_length = 4

def generate_secret_combination():
    secret_combination = [random.choice(possible_colors) for index in range(combination_length)]
    return secret_combination

result = generate_secret_combination()
print(f"generated combination is: {result}")
