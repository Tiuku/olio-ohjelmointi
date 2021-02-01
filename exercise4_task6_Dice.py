# File name: exercise4_task6_Dice.py
# Author: Tiia Iire
# Description: Class where we roll the Dice, tell its color and numbers color

import random

class Dice:
    def __init__(self):
        self.roll = "1"
        self.color = "Black"
        self.numcolor = "White"

    def diceroll(self):
        if random.randint(0, 5) == 0:
            self.roll = "1"
        elif random.randint(0, 5) == 1:
            self.roll = "2"
        elif random.randint(0, 5) == 2:
            self.roll = "3"
        elif random.randint(0, 5) == 3:
            self.roll = "4"
        elif random.randint(0, 5) == 4:
            self.roll = "5"
        else:
            self.roll = "6"

    def dicecolor(self):
        if random.randint(0, 3) == 0:
            self.color = "Black"
        elif random.randint(0, 3) == 1:
            self.color = "Pink"
        elif random.randint(0, 3) == 2:
            self.color = "Purple"
        else:
            self.color = "Blue"

    def dicenumcolor(self):
        if random.randint(0, 3) == 0:
            self.numcolor = "White"
        elif random.randint(0, 3) == 1:
            self.numcolor = "Red"
        elif random.randint(0, 3) == 2:
            self.numcolor = "Green"
        else:
            self.numcolor = "Yellow"

    def get_num(self):
        return self.roll

    def get_dicecolor(self):
        return self.color

    def get_numcolor(self):
        return self.numcolor
