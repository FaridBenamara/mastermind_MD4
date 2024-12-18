import random


possible_colors = ["black", "green", "orange", "blue", "yellow", "red"]
max_attemps = 10
combination_length = 4

def generate_secret_combination():
    secret_combination = [random.choice(possible_colors) for index in range(combination_length)]
    return secret_combination

# result = generate_secret_combination()
# print(f"generated combination is: {result}")


def guess_player():
    while True:
        guess_input = input("entrez vos 4 couleurs(en an glais) separer par des espaces: ")
        guess_list = guess_input.lower().split()
        if len(guess_list) != combination_length:
            print(f"la combinaison doit contenir exactement {combination_length} couleur")
            continue
        valid = True
        for color in guess_list:
            if color not in possible_colors:
                valid = False
                break
        if not valid:
            print(f"une ou plusieurs couleurs sont invalide. choisissez parmi : {', '.join(possible_colors)}.")
        else:
            return guess_list
        
result = guess_player()
print(f"generated player guess: {result}")

        
