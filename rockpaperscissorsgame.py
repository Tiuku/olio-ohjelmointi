# File name: rockpaperscissorsgame.py
# Author: Tiia Iire
# Description: player plays against computer (computer takes the random item)
# Also the code tells the score after every game

import random
def rps():
    playerwins = 0
    computerwins = 0

    computer = random.randint(1, 3)
    player = False

    while player == False:
        players = int(input("Choose your item 1 (rock), 2 (paper), 3 (scissors)?: "))

        if player == computer:
            print("Tie")
        elif players == 1:
            if computer == 2:
                computerwins += 1
                print("You lose :( ", computerwins, "-", playerwins)
            else:
                playerwins +=1
                print("You win! YAY!", computerwins, "-", playerwins)
        elif players == 2:
            if computer == 3:
                computerwins += 1
                print("You lose :( ", computerwins, "-", playerwins)
            else:
                playerwins +=1
                print("You win! YAY!", computerwins, "-", playerwins)
        elif players == 3:
            if computer == 1:
                computerwins += 1
                print("You lose :( ", computerwins, "-", playerwins)
            else:
                playerwins +=1
                print("You win! YAY!", computerwins, "-", playerwins)

rps()
    

        




    



