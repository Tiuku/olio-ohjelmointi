# File name: exercise3_task5.py
# Author: Tiia Iire
# Description: Rolls the dice, tells its color and its numbers color

# Pseudocode:
# Class Dice
# function __init__:
#   self.roll = "1"
#   self.color = "Black"
#   self.numberscolor = "White"
#
# function roll:
#   if random int from 0 to 5 equals 0:
#       self.roll equals 1
#   else if random int from 0 to 5 equals 1:
#       self.roll equals 2
#   else if random int from 0 to 5 equals 2:
#       self.roll equals 3
#   else if random int from 0 to 5 equals 3:
#       self.roll equals 4
#   else if random int from 0 to 5 equals 4:
#       self.roll equals 5
#   else:
#       self.roll equals 6
#
# function color:
#   if random int from 0 to 3 equals 0:
#       self.color equals "Black"
#   else if random int from 0 to 3 equals 1:
#       self.color equals "Pink"
#   else if random int from 0 to 3 equals 2:
#       self.color equals "Purple"
#   else:
#       self.color equals "Blue"
#
# function numberscolor:
#   else if random int from 0 to 3 equals 0:
#       self.numberscolor equals "White"
#   else if random int from 0 to 3 equals 1:
#       self.numberscolor equals "Red"
#   else if random int from 0 to 3 equals 2:
#       self.numberscolor equals "Green"
#   else:
#       self.numberscolor equals "Yellow"
#
# function get_number:
#   return value of function roll
#
# function get_color:
#   return value of function color
#
# function get_numberscolor:
#   return value of funtion numberscolor
#
# function main:
#   set my_dice as class Dice
#   print text "Rolling the dice.."
#
#   call function roll from the Dice class
#   call function color from the Dice class
#   call function numberscolor from the Dice class 
#   print text "Dices number is: " and value of function roll from the Dice class
#   print text "Dices color is: " and value of function color from the Dice class
#   print text "Dices numbers color is: " and value of function numberscolor from the Dice class
#
# call main function

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

def main():
    my_dice = Dice()

    print("Rolling the Dice...")
    my_dice.diceroll()
    my_dice.dicecolor()
    my_dice.dicenumcolor()

    print("Number or the Dice is: ", my_dice.get_num())
    print("Color of this Dice is: ", my_dice.get_dicecolor())
    print("Color of the numbers in this Dice is: ", my_dice.get_numcolor())

main()
