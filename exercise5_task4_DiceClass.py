# File name: exercise5_task4_DiceClass.py
# Author: Tiia Iire
# Description:

import random

class Dice:
    def __init__(self, diceid, diceside):
        self.__id = diceid
        self.__side = diceside

    def roll_dice(self, diceside):
        self.__side = random.randint(1, 6)

    def set_id(self, diceid):
        self.__id = diceid

    def get_side(self):
        return self.__side

    def get_id(self):
        return self.__id
    
    def __str__(self):
        return "Dice " + format(self.__id) + " side is: " + format(self.__side)
