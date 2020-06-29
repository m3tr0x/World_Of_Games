# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty.

# Methods
# 1. generate_number(difficulty) –
# A. Will get a number variable named difficulty
# B. Will return a random number between 1 to difficulty.

# 2. get_guess_from_user(difficulty) –
# A. Will get a number variable named difficulty
# B. Will ask the user to guess a number between 1 to difficulty and return the number the
# user guessed.

# 3. compare_results(difficulty, secret_number) –
# A. Will get 2 variables: number variable named difficulty number variable named
# secret_number
# B. Will compare the secret generated number to the one prompted by the
# get_guess_from_user.

# 4. play(difficulty) –
# A. Will get a number variable named difficulty
# B. Will call the functions above and play the game.
# C. Will return True / False if the user lost or won.

from random import seed
from random import randint
import time
from Utils import screen_cleaner


def generate_number(difficulty):
    seed_val = randint(1, 5)
    seed(seed_val)
    num = randint(1, difficulty)
    return num


def get_guess_from_user(difficulty):
    guess = input(f"Please guess a number from 1 to {difficulty}: ")
    return guess


def compare_results(difficulty, secret_number):
    if int(secret_number) == int(difficulty):
        print("You won")
        return 1
    else:
        print("You Lost")
        return 0


def play(difficulty):
    num = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    result = compare_results(guess, num)
    # Will return 1 to let the Live script knows user won, else will return 0
    if result == 1:
        return 1
    else:
        print("The number was", num, "\n")
        time.sleep(3)
        screen_cleaner()
        return 0





