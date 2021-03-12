# File name: exercise8_task1_main.py
# Author: Tiia Iire
# Description: cleaning the flat

import exercise8_task1_Flat as flat

def main():
    my_apartment = flat.Flat("dirty", "dirty", "unmade", "dusty", "empty", "not enough")

    print(my_apartment)

    print("Let's start with cleaning the windows and made the bed")

    my_apartment.set_windows()
    my_apartment.set_bed()

    print("Now windows are ", my_apartment.get_windows(), " and bed is ", my_apartment.get_bed())
    print("Let's vacuum floors next and dust the surfaces")

    my_apartment.set_floors()
    my_apartment.set_surfaces()

    print("Now that floors are ", my_apartment.get_floors(), " and the surfaces are ", my_apartment.get_surfaces())
    print("Now we can go to grocerie shop and buy groceries and toilet paper")

    my_apartment.set_fridge()
    my_apartment.set_paper()

    print("Now there is ", my_apartment.get_paper(), " and fridge is ", my_apartment.get_fridge())
    print("We can now add more paper so there is more than enough paper in toilet")

    my_apartment.set_paper()

    print("Now everything is perfect! ", my_apartment)

main()
