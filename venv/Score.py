# A file which will manage the scores file.
# The scores file at this point will consist of only a number.
# That number is the accumulation of the winnings of the user.
# Amount of points for winning a game is = 1 point per difficulty level (difficulty 3 = 3 points).
# Each time the user is winning a game, the points he won will be added to his current amount of
# point saved in a file.

# Methods
# add_score() –
# A. The function’s input is a variable called points.
# B. The function will try to read the current score in the scores file, if it fails it will create a
# new one and will use it to save the current score.
# C. The function will print the user current score.

from Utils import scores_file_name
from pathlib import Path

def add_score(points):
    try:
        my_file = open(scores_file_name, 'r')
        content = my_file.read()
        new_score = int(content) + points
        my_file = open(scores_file_name, 'r+')
        my_file.write(str(new_score))
        my_file.close()
        print("Your score is", new_score)
    except IOError:
        print("Can't read Scores file, create new file named 'Current_Score'")
        my_file_new = open("E:\\Studies\\DevOps\\World_Of_Games2\\Current_Score.txt", 'w+')
        my_file_new.write(str(points))
        my_file_new.close()
        print("Your current score is", points, "\n")
        print("Creating a new Scores file")
        my_file_new = open("E:\\Studies\\DevOps\\World_Of_Games2\\Scores.txt", 'w+')
        my_file_new.write(str(points))
        my_file_new.close()
