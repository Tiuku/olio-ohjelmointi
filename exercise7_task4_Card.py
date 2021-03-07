# File name: Exercise7_task4_Card.py
# Author: Tiia Iire
# Description:

class Card:

    def __init__(self, suit, val):
        self.__suit = suit
        self.__value = val


    def show_card(self):
        print(format(self.__value) + " of " + format(self.__suit))
        
    def get_value(self):
        return self.__value

    def __str__(self):
        return "Card is " + format(self.__value) + " of " + format(self.__suit)
