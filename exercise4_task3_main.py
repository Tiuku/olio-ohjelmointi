# File name: exercise4_task3_main.py
# Author: Tiia Iire
# Description: Main file for getting phone model, manufacturer and retailprice

import exercise4_task3_Class

def main():
    my_phone = exercise4_task3_Class.CellPhone()

    my_phone.set_Manufact()
    my_phone.set_Model()
    my_phone.set_RetailPrice()

    print(my_phone)

main()
