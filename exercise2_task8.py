# File name: exercise2_task8.py
# Author: Tiia Iire
# Description: tosses coin 

import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"

    def toss(self):
        if random.randint(0, 3) == 0:
            self.sideup = "Heads"
        elif random.randint(0, 3) == 1:
            self.sideup = "Tails"
        elif random.randint(0, 3) == 2:
            self.sideup = "Coin landed upright"
        else:
            self.sideup = "Coin dropped on the ground"

    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()

    print("This side is up: ", my_coin.get_sideup())
    print("I am tossing the coin ...")
    my_coin.toss()

    print("This side is up: ", my_coin.get_sideup())

main()
