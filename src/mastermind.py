import random


possible_colors = ["black", "green", "orange", "blue", "yellow", "red"]
max_count = 10
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
        
# result = guess_player()
# print(f"generated player guess: {result}")

def compare_guess_to_solution(guess, solution):
    correct_position = 0
    false_position = 0

    solution_copy = solution[:]
    guess_copy = guess[:]


    for index in range(len(guess)):
        if guess[index] == solution[index]:
            correct_position += 1
            solution_copy[index] = "x"
            guess_copy[index] ="x"
    

    for index in range(len(guess)):
        if guess_copy[index] != "x" and guess_copy[index] in solution_copy:
            false_position += 1
            solution_copy[solution_copy.index(guess_copy[index])] = "x"

    return correct_position, false_position

        
# secret_combination = generate_secret_combination()
# player_guess = guess_player()
# result = compare_guess_to_solution(player_guess, secret_combination)
# print(f"Combinaison secrète: {secret_combination}")
# print(f"Résultat: {result[0]} bien placée(s), {result[1]} mal placée(s)")


def main():
    gut_solution = generate_secret_combination()
    print('Bienvenue dans le jeu Mastermind')
    print(f"soluition secréte : {gut_solution}")

    count = 0
    winner = False

    while count < max_count and not winner:
        guess = guess_player()

        correct, no_correct = compare_guess_to_solution(guess, gut_solution)


        if correct == combination_length:
            print("Félicitations, vous avez trouvé la solution ! 🎉")
            winner = True
        else:
            print(f"Résultat: {correct} bien placée(s), {no_correct} mal placée(s).")
            count += 1
            print(f"Il vous reste {max_count - count} tentative(s).")


    if not winner:
        print(f"Désolé, vous avec épuisé vos tentative. La solution était : {gut_solution}" )
    else:
        print(f"Vous avez gagné en {count + 1} tantatives.")


if __name__ == "__main__":
    main()
