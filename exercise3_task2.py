# File name: exercise3_task2.py
# Author: Tiia Iire
# Description: tosses coin and tells which currency it is

import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"
        self.currency = "Euro"

    def toss(self):
        if random.randint(0, 3) == 0:
            self.sideup = "Heads"
        elif random.randint(0, 3) == 1:
            self.sideup = "Tails"
        elif random.randint(0, 3) == 2:
            self.sideup = "Coin landed upright"
        else:
            self.sideup = "Coin dropped on the ground"

    def coincurrency(self):
        if random.randint(0, 4) == 0:
            self.currency = "Euro"
        elif random.randint(0, 4) == 1:
            self.currency = "Pound"
        elif random.randint(0, 4) == 2:
            self.currency = "Dollar"
        elif random.randint(0, 4) == 3:
            self.currency = "Ruble"
        else:
            self.currency = "Yen"

    def get_sideup(self):
        return self.sideup

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
