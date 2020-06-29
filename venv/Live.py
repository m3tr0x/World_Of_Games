# welcome(name) - This function gets a person name as an input and returns a welcome string.
# load_game() - This function:
# 1. Will print out the game selection text
# 2. Will get an input from the user about the game he chose – 1/2.
# 3. After receiving the game number from the user, the function will get the level of difficulty from 1 to 5
# 4. Will start a new function of the corresponding game with the given difficulty.
# The function will check the input of the chosen game (the input supposed to be a number
# between 1 to 2), also will check the input of level of difficulty (input should be a number between
# 1 to 5).
# In case of an invalid choice, return the ERROR_MESSAGE (Utils.py).
# In case the user won the game, the function will call the function called add_score() (in score.py
# module) to add the new score the user won to the score saved in the Scores.txt function.
# In case the user lost, call load_game() again.

from Utils import error, screen_cleaner
from Score import add_score


def welcome(name):
    print("Hello", name, "and welcome to the World of Games (WoG) \n")
    print("Here you can find many cool games to play")


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n")
    print("2. Guess Game - guess a number and see if you chose like the computer \n")
    while True:
        selection = input("Select which game you'd like to play: ")
        try: #Checking value is an integer
            if int(selection) == 1:
                from MemoryGame import play
                diff = input("Please choose game difficulty from 1 to 5: ")
                if int(diff) > 5 or int(diff) < 1: #Checking value not crossing 1-5
                    screen_cleaner()
                    print(error)
                    result = 0
                else:
                    result = play(int(diff))
            elif int(selection) == 2:
                from GuessGame import play
                diff = input("Please choose game difficulty from 1 to 5: ")
                if int(diff) > 5 or int(diff) < 1: #Checking value not crossing 1-5
                    screen_cleaner()
                    print(error)
                    result = 0
                else:
                    result = play(int(diff))
            else:
                screen_cleaner()
                print(error)
                result = 0
        except ValueError:
            print("You've inserted a non integer value, please try again \n")
            continue
        else:
            break
    # Selected game will return 1 in order to update score. else will return 0 to intiate the reload game.
    if result == 1:
        add_score(int(diff))
        return 1 # Will return 1 to finish the game w/o reload.
    else:
        return 0
