# The purpose of this file is to call the functions from Live.py

from Live import welcome, load_game

#Calling starting functions welcome & load_game to start the game

name = input("What's your name? \n")
welcome(name)
result = 0
#Looping the load game in case of player's game over with loss.
while result == 0:
    result = load_game()



