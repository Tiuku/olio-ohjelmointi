#File name: exercise5_task5_PlayerClass.py
#Author: Tiia Iire
# Description: Class for getting players first and last name, players id and roll the dice for the player

import random

class Player():
    def __init__(self):
        self.__firstname = "firstname"
        self.__lastname = "lastname"
        self.__id = 0
        self.__dice = 0

    def set_firstname(self):
        self.__firstname = str(input("What is players firstname? "))

    def set_lastname(self):
        self.__lastname = str(input("What is players lastname? "))

    def set_id(self):
        self.__id = int(input("What is players id? "))

    def set_dice(self):
        self.__dice = random.randint(1, 6)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_id(self):
        return self.__id

    def get_dice(self):
        return self.__dice

    def __str__(self):
        return "ID: " + format(self.__id) + " Last name: " + format(self.__lastname)
        + " First name: " + format(self.__firstname) + " Dice side: " + format(self.__dice)
