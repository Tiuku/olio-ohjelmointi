# File name: exercise5_task4_main.py
# Author: Tiia Iire
# Description:

import exercise5_task4_DiceClass as dice

def roll_dice(my_dice):
    my_dice.roll_dice()
    return my_dice

def make_list():
    dice_list = []

    for number in range(1, 4):
        print("Dice ", number)

        my_dice = dice.Dice(dice_id, number)

        dice_list.append(my_dice)

    return list

def display_list(dice_list):
    for item in dice_list:
        print()
        print("Id: ", item.get_id())
        print("Side: ", item.get_side())

def roll_dice(dice_list):
    for item in dice_list:
        item.roll_dice()

def get_list(dice_list):
    side_list = []

    for item in dice_list:
        side_list.append(item.get_side())
    return side_list

def not_append(continue_list, dice_object):
    for i in range(len(continue_list)):
        if dice_object == continue_list[i]:
            return False

    return True

def check_tie(dice_list):
    if (len(dice_list) < 2):
        return dice_list

    else:
        tied_list = []
        side_list = get_side_list(dice_list)

        for i in range(len(side_list)):
            if side_list[i] == side_list[j]:
                if not_appended(tied_list, dice_list[j]):
                    tied_list.append(dice_list[i])

                if not_appended(tied_list, dice_list[j]):
                    tied_list.append(dice_list[j])

    return tied_list

def drop_lowest(dice_list):
    side_list = get_side_list(dice_list)
    lowest = min(side_list)

    for i in range(len(side_list)):
        if lowest == side_list[i]:
            dice_list.pop(i)

    return dice_list

def play_game(dices):
    print("Lets play!")
    roll_dice(dices)

    print("Situation after first round: ")
    display_list(dices)
    tied_list = check_tie(dices)

    while (len(tied_list) > 1):
        print("There is a tie!, we have to roll again.. ", get_side_list(tied_list))
        roll_dice(tied_list)
        tied_list = check_tie(dices)

    print("Now we can drop the lowest side out of the game.")
    dices = drop_lowest(dices)

    print("These are still in game: ")
    display_list(dices)

    return dices

def main():
    my_dice = dice.Dice()
    my_rolled_dice = roll_dice(my_dice)

    dices = make_list()

    print("Here are the dices ")
    display_list(dices)

    print("First round..")
    dices = play_game(dices)

    print("Second round..")
    dices = play_game(dices)

    print("We have a winner!")
    dices = play_game(dices)

main()
