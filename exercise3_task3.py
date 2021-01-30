# File name: exercise3_task3.py
# Author: Tiia Iire
# Description: tosses coin and lets the user choose which currency the coin is

import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"
        self.currency = "Euro"

    def toss(self):
        if random.randint(0, 3) == 0:
            self.__sideup = "Heads"
        elif random.randint(0, 3) == 1:
            self.__sideup = "Tails"
        elif random.randint(0, 3) == 2:
            self.__sideup = "Coin landed upright"
        else:
            self.__sideup = "Coin dropped on the ground"

    def coincurrency(self):
        curr = input("Choose what currency you want to use: ")
        self.currency = curr

    def get_sideup(self):
        return self.__sideup

    def get_currency(self):
        return self.currency

def main():
    my_coin = Coin()

    print("This side is up: ", my_coin.get_sideup())
    print("I am tossing the coin ...")
    my_coin.toss()
    my_coin.coincurrency()

    print("This side is up: ", my_coin.get_sideup())
    print("Currency of this coin is: ", my_coin.get_currency())

main()
