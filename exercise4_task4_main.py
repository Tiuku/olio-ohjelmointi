# File name: exercise4_task3_main.py
# Author: Tiia Iire
# Description: Main file for getting phone model, manufacturer, retailprice and ID

import exercise4_task4_Class

def main():
    my_phone = exercise4_task4_Class.CellPhone()

    my_phone.set_Manufact()
    my_phone.set_Model()
    my_phone.set_RetailPrice()
    my_phone.set_ID()
    my_phone.correct_ID()
    my_phone.get_ID()

    print(my_phone)

main()
