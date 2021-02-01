# File name: exercise4_task6_main.py
# Author: Tiia Iire
# Description: Main file for getting phone model, manufacturer, retailprice and ID

import exercise4_task4_Class as phone
import exercise4_task6_Dice as dice

def main():
    my_phone = phone.CellPhone()
    my_dice = dice.Dice()

    my_dice.diceroll()

    print("Dice number: ", my_dice.get_num())

    my_phone.set_Manufact()
    my_phone.set_Model()
    my_phone.set_RetailPrice()
    my_phone.set_ID()
    my_phone.correct_id()
    my_phone.get_ID()

    if my_phone.get_ID() == my_dice.get_num():
        print(my_phone)
    else:
        print("None")

    my_phone.set_Manufact()
    my_phone.set_Model()
    my_phone.set_RetailPrice()
    my_phone.set_ID()
    my_phone.correct_id()
    my_phone.get_ID()
    
    if my_phone.get_ID() == my_dice.get_num():
        print(my_phone)
    else:
        print("None")
   
    my_phone.set_Manufact()
    my_phone.set_Model()
    my_phone.set_RetailPrice()
    my_phone.set_ID()
    my_phone.correct_id()
    my_phone.get_ID()

    if my_phone.get_ID() == my_dice.get_num():
        print(my_phone)
    else:
        print("None")
    
main()
