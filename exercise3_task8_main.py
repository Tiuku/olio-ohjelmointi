# File name: exercise3_task8_main.py
# Author: Tiia Iire
# Description: Main file for getting phone model, manufacturer and retailprice

import exercise3_task8

def main():
    my_phone = exercise3_task8.CellPhone()

    my_phone.Manufact()
    my_phone.Model()
    my_phone.RetailPrice()

    print("Manufacturer: ", my_phone.get_manufact())
    print("Model Number: ", my_phone.get_model())
    print("Retail price: ", my_phone.get_retailPrice())

main()
