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
