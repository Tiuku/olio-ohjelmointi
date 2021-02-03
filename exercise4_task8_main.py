# File name: exercise4_task8_main.py
# Author: Tiia Iire
# Description: Here we roll the dice, pick the right mammal
# looking for the same ID as the number of the dice.
# Then we check which car will have enough space and
# max load limit for that mammal

import exercise4_task8_mammal as mammal
import exercise4_task6_Dice as dice
import exercise4_task8_Car as car

def main():

    my_dice = dice.Dice()
    
    my_car1 = car.Car()
    my_car2 = car.Car()
    my_car3 = car.Car()
    my_car4 = car.Car()
    my_car5 = car.Car()
    my_car6 = car.Car()

    my_mammal1 = mammal.Mammal()
    my_mammal2 = mammal.Mammal()
    my_mammal3 = mammal.Mammal()
    my_mammal4 = mammal.Mammal()
    my_mammal5 = mammal.Mammal()
    my_mammal6 = mammal.Mammal()

    my_car1.set_make()
    my_car1.set_model()
    my_car1.set_maxload()
    my_car1.set_trunk()

    my_car2.set_make()
    my_car2.set_model()
    my_car2.set_maxload()
    my_car2.set_trunk()

    my_car3.set_make()
    my_car3.set_model()
    my_car3.set_maxload()
    my_car3.set_trunk()

    my_car4.set_make()
    my_car4.set_model()
    my_car4.set_maxload()
    my_car4.set_trunk()

    my_car5.set_make()
    my_car5.set_model()
    my_car5.set_maxload()
    my_car5.set_trunk()

    my_car6.set_make()
    my_car6.set_model()
    my_car6.set_maxload()
    my_car6.set_trunk()

    print("Dice number: ", my_dice.get_num())

    print("Let's see how is your mammal...")

    my_mammal1.set_ID()
    my_mammal1.set_specie()
    my_mammal1.set_name()
    my_mammal1.set_size()
    my_mammal1.set_weight()
    my_mammal1.set_height()

    my_mammal2.set_ID()
    my_mammal2.set_specie()
    my_mammal2.set_name()
    my_mammal2.set_size()
    my_mammal2.set_weight()
    my_mammal2.set_height()

    my_mammal3.set_ID()
    my_mammal3.set_specie()
    my_mammal3.set_name()
    my_mammal3.set_size()
    my_mammal3.set_weight()
    my_mammal3.set_height()

    my_mammal4.set_ID()
    my_mammal4.set_specie()
    my_mammal4.set_name()
    my_mammal4.set_size()
    my_mammal4.set_weight()
    my_mammal4.set_height()

    my_mammal5.set_ID()
    my_mammal5.set_specie()
    my_mammal5.set_name()
    my_mammal5.set_size()
    my_mammal5.set_weight()
    my_mammal5.set_height()

    my_mammal6.set_ID()
    my_mammal6.set_specie()
    my_mammal6.set_name()
    my_mammal6.set_size()
    my_mammal6.set_weight()
    my_mammal6.set_height()

    if my_mammal1.get_ID() == my_dice.get_num():
        print(my_mammal1)
        print("Let's see which cars trunk is big enough to take your mammal in..")
        if my_mammal1.get_size() <= my_car1.get_trunksize() and my_mammal1.get_weight() <= my_car1.get_maxload():
            print(my_car1)
        elif my_mammal1.get_size() <= my_car2.get_trunksize() and my_mammal1.get_weight() <= my_car2.get_maxload():
            print(my_car2)
        elif my_mammal1.get_size() <= my_car3.get_trunksize() and my_mammal1.get_weight() <= my_car3.get_maxload():
            print(my_car3)
        elif my_mammal1.get_size() <= my_car4.get_trunksize() and my_mammal1.get_weight() <= my_car4.get_maxload():
            print(my_car4)
        elif my_mammal1.get_size() <= my_car5.get_trunksize() and my_mammal1.get_weight() <= my_car5.get_maxload():
            print(my_car5)
        else:
            print(my_car6)
    elif my_mammal2.get_ID() == my_dice.get_num():
        print(my_mammal2)
        if my_mammal2.get_size() <= my_car1.get_trunksize() and my_mammal2.get_weight() <= my_car1.get_maxload():
            print(my_car1)
        elif my_mammal2.get_size() <= my_car2.get_trunksize() and my_mammal2.get_weight() <= my_car2.get_maxload():
            print(my_car2)
        elif my_mammal2.get_size() <= my_car3.get_trunksize() and my_mammal2.get_weight() <= my_car3.get_maxload():
            print(my_car3)
        elif my_mammal2.get_size() <= my_car4.get_trunksize() and my_mammal2.get_weight() <= my_car4.get_maxload():
            print(my_car4)
        elif my_mammal2.get_size() <= my_car5.get_trunksize() and my_mammal2.get_weight() <= my_car5.get_maxload():
            print(my_car5)
        else:
            print(my_car6)
    elif my_mammal3.get_ID() == my_dice.get_num():
        print(my_mammal3)
        if my_mammal3.get_size() <= my_car1.get_trunksize() and my_mammal3.get_weight() <= my_car1.get_maxload():
            print(my_car1)
        elif my_mammal3.get_size() <= my_car2.get_trunksize() and my_mammal3.get_weight() <= my_car2.get_maxload():
            print(my_car2)
        elif my_mammal3.get_size() <= my_car3.get_trunksize() and my_mammal3.get_weight() <= my_car3.get_maxload():
            print(my_car3)
        elif my_mammal3.get_size() <= my_car4.get_trunksize() and my_mammal3.get_weight() <= my_car4.get_maxload():
            print(my_car4)
        elif my_mammal3.get_size() <= my_car5.get_trunksize() and my_mammal3.get_weight() <= my_car5.get_maxload():
            print(my_car5)
        else:
            print(my_car6)
    elif my_mammal4.get_ID() == my_dice.get_num():
        print(my_mammal4)
        if my_mammal4.get_size() == my_car1.get_trunksize() and my_mammal4.get_weight() <= my_car1.get_maxload():
            print(my_car1)
        elif my_mammal4.get_size() == my_car2.get_trunksize() and my_mammal4.get_weight() <= my_car2.get_maxload():
            print(my_car2)
        elif my_mammal4.get_size() == my_car3.get_trunksize() and my_mammal4.get_weight() <= my_car3.get_maxload():
            print(my_car3)
        elif my_mammal4.get_size() == my_car4.get_trunksize() and my_mammal4.get_weight() <= my_car4.get_maxload():
            print(my_car4)
        elif my_mammal4.get_size() == my_car5.get_trunksize() and my_mammal4.get_weight() <= my_car5.get_maxload():
            print(my_car5)
        else:
            print(my_car6)
    elif my_mammal5.get_ID() == my_dice.get_num():
        print(my_mammal5)
        if my_mammal5.get_size() == my_car1.get_trunksize() and my_mammal5.get_weight() <= my_car1.get_maxload():
            print(my_car1)
        elif my_mammal5.get_size() == my_car2.get_trunksize() and my_mammal5.get_weight() <= my_car2.get_maxload():
            print(my_car2)
        elif my_mammal5.get_size() == my_car3.get_trunksize() and my_mammal5.get_weight() <= my_car3.get_maxload():
            print(my_car3)
        elif my_mammal5.get_size() == my_car4.get_trunksize() and my_mammal5.get_weight() <= my_car4.get_maxload():
            print(my_car4)
        elif my_mammal5.get_size() == my_car5.get_trunksize() and my_mammal5.get_weight() <= my_car5.get_maxload():
            print(my_car5)
        else:
            print(my_car6)
    else:
        print(my_mammal6)
        if my_mammal6.get_size() == my_car1.get_trunksize() and my_mammal6.get_weight() <= my_car1.get_maxload():
            print(my_car1)
        elif my_mammal6.get_size() == my_car2.get_trunksize() and my_mammal6.get_weight() <= my_car2.get_maxload():
            print(my_car2)
        elif my_mammal6.get_size() == my_car3.get_trunksize() and my_mammal6.get_weight() <= my_car3.get_maxload():
            print(my_car3)
        elif my_mammal6.get_size() == my_car4.get_trunksize() and my_mammal6.get_weight() <= my_car4.get_maxload():
            print(my_car4)
        elif my_mammal6.get_size() == my_car5.get_trunksize() and my_mammal6.get_weight() <= my_car5.get_maxload():
            print(my_car5)
        else:
            print(my_car6)

main()
