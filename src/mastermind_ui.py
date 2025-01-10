import random
import pygame
import sys

pygame.init()
width, height = 750, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mastermind - FOAD HETIC MD4")

possible_colors = ["black", "green", "orange", "blue", "yellow", "red"]
combination_length = 4
max_count = 10

def generate_secret_combination():
    return [random.choice(possible_colors) for _ in range(combination_length)]

def compare_guess_to_solution(guess, solution):
    correct_position = 0
    fausse_position = 0
    solution_copy = solution[:]
    guess_copy = guess[:]

    for index in range(len(guess)):
        if guess[index] == solution[index]:
            correct_position += 1
            solution_copy[index] = "x"
            guess_copy[index] = "x"

    for index in range(len(guess)):
        if guess_copy[index] != "x" and guess_copy[index] in solution_copy:
            fausse_position += 1
            solution_copy[solution_copy.index(guess_copy[index])] = "x"

    return correct_position, fausse_position

def draw_buttons(colors, selected_color_index):
    x, y = 50, 150
    button_width = 100
    button_height = 50

    for index, color in enumerate(colors):
        button_rect = pygame.Rect(x + index * (button_width + 20), y, button_width, button_height)
        pygame.draw.rect(screen, pygame.Color(color), button_rect)
        if index == selected_color_index:
            pygame.draw.rect(screen, (100, 100, 100), button_rect, 3)

        font = pygame.font.SysFont("Arial", 24)
        text_surface = font.render(color, True, (255, 255, 255))
        screen.blit(text_surface, (button_rect.centerx - 40, button_rect.centery - 10))


def get_player_guess():
    selected_color_index = 0
    guess = []
    while len(guess) < combination_length:
        screen.fill((30, 30, 30))
        draw_buttons(possible_colors, selected_color_index)
        draw_text(f"Choisis la couleur pour la position {len(guess) + 1}", 200, 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_color_index = (selected_color_index + 1) % len(possible_colors)
                elif event.key == pygame.K_LEFT:
                    selected_color_index = (selected_color_index - 1) % len(possible_colors)
                elif event.key == pygame.K_RETURN:
                    guess.append(possible_colors[selected_color_index])

    return guess


def draw_text(text, x, y):
    font = pygame.font.SysFont("Arial", 24)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))
# Afficher les résultats
def display_game_results(correct, incorrect, remaining_attempts):
    draw_text(f"{correct} bien(s) placée(s), {incorrect} mal(s) placée(s)", 200, 100)
    draw_text(f"Il vous reste {remaining_attempts} tentative(s)", 200, 150)
def play_game():
    secret_comb = generate_secret_combination()
    attempts_left = max_count
    winner = False

    while attempts_left > 0 and not winner:
        guess = get_player_guess()
        correct, incorrect = compare_guess_to_solution(guess, secret_comb)

        screen.fill((30, 30, 30))
        display_game_results(correct, incorrect, attempts_left)

        if correct == combination_length:
            winner = True
            draw_text("Félicitations, vous avez gagné !", 200, 200)
        elif attempts_left == 1:
            draw_text(f"La solution était : {', '.join(secret_comb)}", 200, 200)

        pygame.display.update()
        pygame.time.wait(1000)

        attempts_left -= 1

    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    play_game()