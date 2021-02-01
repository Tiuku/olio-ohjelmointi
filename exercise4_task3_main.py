# File name: exercise4_task3_main.py
# Author: Tiia Iire
# Description: Main file for getting phone model, manufacturer and retailprice

import exercise4_task3_Class

def main():
    my_phone = exercise4_task3_Class.CellPhone()

    my_phone.Manufact()
    my_phone.Model()
    my_phone.RetailPrice()

    print("Manufacturer: ", my_phone.get_manufact())
    print("Model Number: ", my_phone.get_model())
    print("Retail price: ", my_phone.get_retailPrice())

main()
