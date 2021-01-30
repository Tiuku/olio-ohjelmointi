# File name: exercise3_task7.py
# Author: Tiia Iire
# Description: Three players rolls dices and this program shows who loses first and then the
# other two dices will be rolled again to see who wins the game.

import random

class Dice:
    def __init__(self):
        self.roll1 = "1"
        self.roll2 = "1"
        self.roll3 = "1"

    def diceroll1(self):
        if random.randint(0, 5) == 0:
            self.roll1 = 1
        elif random.randint(0, 5) == 1:
            self.roll1 = 2
        elif random.randint(0, 5) == 2:
            self.roll1 = 3
        elif random.randint(0, 5) == 3:
            self.roll1 = 4
        elif random.randint(0, 5) == 4:
            self.roll1 = 5
        else:
            self.roll1 = 6

    def diceroll2(self):
        if random.randint(0, 5) == 0:
            self.roll2 = 1
        elif random.randint(0, 5) == 1:
            self.roll2 = 2
        elif random.randint(0, 5) == 2:
            self.roll2 = 3
        elif random.randint(0, 5) == 3:
            self.roll2 = 4
        elif random.randint(0, 5) == 4:
            self.roll2 = 5
        else:
            self.roll2 = 6

    def diceroll3(self):
        if random.randint(0, 5) == 0:
            self.roll3 = 1
        elif random.randint(0, 5) == 1:
            self.roll3 = 2
        elif random.randint(0, 5) == 2:
            self.roll3 = 3
        elif random.randint(0, 5) == 3:
            self.roll3 = 4
        elif random.randint(0, 5) == 4:
            self.roll3 = 5
        else:
            self.roll3 = 6
            
    def firstround(self):
        while self.roll1 = self.roll2 or self.roll2 = self.roll3 or self.roll1 = self.roll3:
            
            if self.roll1 < self.roll2 && self.roll1 < self.roll3:
                print("Player 1 loses, player 2 and player 3 will roll again...")
                return self.roll1
            elif self.roll2 <self.roll1 && self.roll2 < self.roll3:
                print("Player 2 loses, player 1 and player 3 will roll again...")
                return self.roll2
            elif self.roll3 < self.roll1 && self.roll3 < self.roll2:
                print("Player 3 loses, player 1 and player 2 will roll again...")
                return self.roll3
            elif self.roll1 = self.roll2:
                print("Players 1 and 2 have the same number, you have to roll again")
                diceroll1()
                diceroll2()
            elif self.roll2 = self.roll3:
                print("Players 2 and 3 have the same number, you have to roll again")
                diceroll2()
                diceroll3()
            elif self.roll3 = self.roll1:
                print("Players 1 and 3 have the same number, you have to roll again")
                diceroll1()
                diceroll3()
            else:
                print("All players has the same number, you have to roll again")
                diceroll1()
                diceroll2()
                diceroll3()
            

    def get_num1(self):
        return self.roll1
    
    def get_num2(self):
        return self.roll2
    
    def get_num3(self):
        return self.roll3

    def get_loser1(self):
        return firstround()

    def get_second_round_players(self):
        return 


def main():
    my_dice = Dice()
    second_dice = Dice()
    third_dice = Dice()

    print("Roll the dices..")
    my_dice.diceroll1()
    my_dice.diceroll2()
    my_dice.diceroll3()

    print("Loser of the first round is: ", my_di
    

main()
