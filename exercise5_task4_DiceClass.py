# File name: exercise5_task4_DiceClass.py
# Author: Tiia Iire
# Description: Class for rolling dice

import random

class Dice:
    def __init__(self):
        self.__id = 0
        self.__side = random.randint(1, 6)
        self.__sum = 0
        self.__playernum = 0

    def roll_dice(self):
        self.__side = random.randint(1, 6)

    def set_id(self):
        self.__id = random.randint(1, 100)

    def set_sum(self):
        self.__sum += self.__side

    def set_players(self):
        self.__playernum = int(input("How many players? "))

    def get_side(self):
        return self.__side

    def get_id(self):
        return self.__id

    def get_sum(self):
        return self.__sum

    def get_players(self):
        return self.__playernum
    
    def __str__(self):
        return "Dice " + format(self.__id) + " side is: " + format(self.__side)
