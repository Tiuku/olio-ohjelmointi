# File name: exercise3_task6.py
# Author: Tiia Iire
# Description: Rolls two dices, tells them color and numbers color and also sums up their numbers.

import random

class Dice:
    def __init__(self):
        self.roll = "1"
        self.color = "Black"
        self.numcolor = "White"

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

def main():
    my_dice = Dice()
    second_dice = Dice()

    print("Rolling the first Dice...")
    my_dice.diceroll()
    my_dice.dicecolor()
    my_dice.dicenumcolor()

    print("Number or the first Dice is: ", my_dice.get_num())
    print("Color of the first Dice is: ", my_dice.get_dicecolor())
    print("Color of the numbers in the first Dice is: ", my_dice.get_numcolor())

    second_dice.diceroll()
    second_dice.dicecolor()
    second_dice.dicenumcolor()

    print("Rolling the second Dice...")
    print("Number or the second Dice is: ", second_dice.get_num())
    print("Color of the second Dice is: ", second_dice.get_dicecolor())
    print("Color of the numbers in the second Dice is: ", second_dice.get_numcolor())

    print("Sum of the two dices is: ", second_dice.get_num() + my_dice.get_num())

main()
