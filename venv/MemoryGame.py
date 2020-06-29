# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember.
# If he was right with all the numbers the user will win otherwise he will lose.

# Methods
# 1. generate_sequence(difficulty) –
# A. Will get a number variable named difficulty
# B. Will generate a list of random numbers between 1 to 101. The list length will be
# difficulty.
# C. The list will be shown for 0.7 seconds (using Utils.py module).

# 2. get_list_from_user(difficulty) –
# A. Will get a number variable named difficulty
# B. Will prompt the user the following message:
# After seeing the numbers enter the numbers you saw, each one separated with
# Enter.
# C. Will return a list of numbers prompted from the user. The list length will be in the size
# of difficulty.

# 3. is_list_equal(list_a, list_b) –
# A. Will get 2 variables named list_a and list_b
# B. The function will compare the two lists (list_a & list_b).
# C. The function will return True / False if the lists equal or not.

# 4. play(difficulty) -
# A. Will get a number variable named difficulty
# B. Will call the functions above and play the game.
# C. Will return True / False if the user lost or won (based on is_list_equal()).

from random import seed
from random import randint
import time
import array as arr
from Utils import screen_cleaner


def generate_sequence(difficulty):
    seed_val = randint(1, 10)
    seed(seed_val)
    gen_list = arr.array("i", [])
    for i in range(difficulty):
        rand_num = randint(1, 101)
        gen_list.append(rand_num)
    print(*gen_list, sep = ", ")
    time.sleep(0.7)
    screen_cleaner()
    return gen_list


def get_list_from_user(difficulty):
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter")
    user_list = arr.array("i", [])
    for i in range(difficulty):
        while True:
            num = input("")
            try:
                user_list.append(int(num))
            except ValueError:
                print("You've inserted a non integer value, please try again")
                continue
            else:
                break
    return user_list


def is_list_equal(list_a, list_b):
    if list_a == list_b:
        print("You won")
        return 1
    else:
        print("You Lost")
        print("\n")
        time.sleep(3)
        screen_cleaner()
        return 0


def play(difficulty):
    list_a = generate_sequence(difficulty)
    list_b = get_list_from_user(difficulty)
    result = is_list_equal(list_a, list_b)
    # Will return 1 to let the Live script knows user won, else will return 0
    if result == 1:
        return 1
    else:
        return 0
