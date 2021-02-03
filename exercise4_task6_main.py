# File name: exercise4_task6_main.py
# Author: Tiia Iire
# Description: Main file for getting phone model, manufacturer, retailprice and ID
# Program will also roll the dice and see which phone equals the dice number
# it will print the details from the phone that equals dice

import exercise4_task4_Class as phone
import exercise4_task6_Dice as dice

def main():
    my_phone1 = phone.CellPhone()
    my_phone2 = phone.CellPhone()
    my_phone3 = phone.CellPhone()
    my_phone4 = phone.CellPhone()
    my_phone5 = phone.CellPhone()
    my_phone6 = phone.CellPhone()
    my_dice = dice.Dice()

    my_dice.diceroll()

    print("Dice number: ", my_dice.get_num())

    my_phone1.set_Manufact()
    my_phone1.set_Model()
    my_phone1.set_RetailPrice()
    my_phone1.set_ID()
    my_phone1.correct_id()
    my_phone1.get_ID()


    my_phone2.set_Manufact()
    my_phone2.set_Model()
    my_phone2.set_RetailPrice()
    my_phone2.set_ID()
    my_phone2.correct_id()
    my_phone2.get_ID()

   
    my_phone3.set_Manufact()
    my_phone3.set_Model()
    my_phone3.set_RetailPrice()
    my_phone3.set_ID()
    my_phone3.correct_id()
    my_phone3.get_ID()


    my_phone4.set_Manufact()
    my_phone4.set_Model()
    my_phone4.set_RetailPrice()
    my_phone4.set_ID()
    my_phone4.correct_id()
    my_phone4.get_ID()


    my_phone5.set_Manufact()
    my_phone5.set_Model()
    my_phone5.set_RetailPrice()
    my_phone5.set_ID()
    my_phone5.correct_id()
    my_phone5.get_ID()


    my_phone6.set_Manufact()
    my_phone6.set_Model()
    my_phone6.set_RetailPrice()
    my_phone6.set_ID()
    my_phone6.correct_id()
    my_phone6.get_ID()


    if my_phone1.get_ID() == my_dice.get_num():
        print(my_phone1)
    elif my_phone2.get_ID() == my_dice.get_num():
        print(my_phone2)
    elif my_phone3.get_ID() == my_dice.get_num():
        print(my_phone3)
    elif my_phone4.get_ID() == my_dice.get_num():
        print(my_phone4)
    elif my_phone5.get_ID() == my_dice.get_num():
        print(my_phone5)
    else:
        print(my_phone6)
    
main()
