# File name: exercise4_task6_Dice.py
# Author: Tiia Iire
# Description: Class where we roll the Dice

import random

class Dice:
    def __init__(self):
        self.roll = 1

    def diceroll(self):
        if random.randint(0, 5) == 0:
            self.roll = 1
        elif random.randint(0, 5) == 1:
            self.roll = 2
        elif random.randint(0, 5) == 2:
            self.roll = 3
        elif random.randint(0, 5) == 3:
            self.roll = 4
        elif random.randint(0, 5) == 4:
            self.roll = 5
        else:
            self.roll = 6

    
    def get_num(self):
        return self.roll

