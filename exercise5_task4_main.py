# File name: exercise5_task4_main.py
# Author: Tiia Iire
# Description: dice game, three rolls and best sum wins

import exercise5_task4_DiceClass as dice

def first_round(list):
    for i in list:
        print("Player ", i.get_id(), " got ", i.get_side())
    for step in range(1, len(list)):
        key = list[step]
        j = step - 1

        while j >= 0 and key.get_side() > list[j].get_side():
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = key

    n = 1
    biggest = [list[0]]

    for item in list:
        while n < len(list):
            if item.get_side() == list[n].get_side():
                biggest.append(list[n])
            n += 1


def winner(list):
    for i in list:
        print("Player ", i.get_id(), " got ", i.get_side())

    for step in range(1, len(list)):
        key = list[step]
        j = step - 1

        while j >= 0 and key.get_sum() > list[j].get_sum():
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = key

    n = 1
    biggest = [list[0]]
    for item in list:
        while n < len(list):
            if item.get_sum() == list[n].get_sum():
                biggest.append(list[n])
            n += 1

    if len(biggest) == 1:
        print("Player ", biggest[0].get_id() , " wins!")
        return
    else:
        print("There was a tie between ", len(biggest), " players, we have to roll again!")
        for i in biggest:
            i.roll_dice()
        return first_round(biggest)



def main():
    players = []
    my_dice = dice.Dice()
    my_dice.set_players()
    print("Let's play!")


    for r in range(my_dice.get_players()):
        my_dice = dice.Dice()
        my_dice.set_id()
        players.append(my_dice)
        for item in range(3):
            for item in players:
                item.roll_dice()
                item.get_sum()
                

    winner(players)

main()
