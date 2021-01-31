# File name: exercise3_task7.py
# Author: Tiia Iire
# Description: Three players rolls dices and this program shows who loses first and then the
# other two dices will be rolled again to see who wins the game.

import random

class Dice:
    def __init__(self):
        self.roll1 = 1
        self.roll2 = 1
        self.roll3 = 1

    def diceroll(self):
        self.roll1 = random.randint(1, 6)
        self.roll2 = random.randint(1, 6)
        self.roll3 = random.randint(1, 6)

    def get_roll1(self):
        return self.roll1

    def get_roll2(self):
        return self.roll2

    def get_roll3(self):
        return self.roll3
            
    def round(self):
        while True:
            if self.roll1 == self.roll2 == self.roll3:
                print("Tie, you have to roll the dices again!")
                Dice.diceroll()
                print("Player 1: ", self.get_roll1(), "Player 2: ",
                      self.get_roll2(), "Player 3: ", self.get_roll3())
            elif self.roll1 == self.roll2:
                print("Player 1 and player 2 got same number, you have to roll again!")
                self.roll1 = random.randint(1, 6)
                self.roll2 = random.randint(1, 6)
                print("Player 1: ", self.get_roll1(), "Player 2: ", self.get_roll2())
            elif self.roll2 == self.roll3:
                print("Player 2 and player 3 got same number, you have to roll again!")
                self.roll2 = random.randint(1, 6)
                self.roll3 = random.randint(1, 6)
                print("Player 2: ", self.get_roll2(), "Player 3: ", self.get_roll3())
            elif self.roll1 == self.roll3:
                print("Player 1 and player 3 got same number, you have to roll again!")
                self.roll1 = random.randint(1, 6)
                self.roll3 = random.randint(1, 6)
                print("Player 1: ", self.get_roll1(), "Player 3: ", self.get_roll3())
            else:
                return

def main():
    my_dice = Dice()

    my_dice.diceroll()

    print("Player 1: ", my_dice.get_roll1(), "Player 2: ", my_dice.get_roll2(),
          "Player 3: ", my_dice.get_roll3())

    my_dice.round()

    if (my_dice.get_roll1() > my_dice.get_roll2() > my_dice.get_roll3()
    or my_dice.get_roll2() > my_dice.get_roll1() > my_dice.get_roll3()):
        print("Player 3 loses.. Player 1 and player 2 will roll again!")

        my_dice.diceroll()
        print("Player 1: ", my_dice.get_roll1(), "Player 2: ", my_dice.get_roll2())

        my_dice.round()
        if my_dice.get_roll1() > my_dice.get_roll2():
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

    elif (my_dice.get_roll2() > my_dice.get_roll3() > my_dice.get_roll1()
    or my_dice.get_roll3() > my_dice.get_roll2() > my_dice.get_roll1()):
        print("Player 1 loses.. Player 2 and player 3 will roll again!")

        my_dice.diceroll()
        print("Player 2: ", my_dice.get_roll2(), "Player 3: ", my_dice.get_roll3())
        my_dice.round()
        
        if my_dice.get_roll2() > my_dice.get_roll3():
            print("Player 2 wins!")
        else:
            print("Player 3 wins!")

    elif (my_dice.get_roll3() > my_dice.get_roll1() > my_dice.get_roll2()
    or my_dice.get_roll1() > my_dice.get_roll3() > my_dice.get_roll2()):
        print("Player 2 loses.. Player 1 and player 3 will roll again!")

        my_dice.diceroll()
        print("Player 1: ", my_dice.get_roll1(), "Player 3: ", my_dice.get_roll3())
        my_dice.round()
        
        if my_dice.get_roll3() > my_dice.get_roll1():
            print("Player 3 wins!")
        else:
            print("Player 1 wins!")
    

main()
