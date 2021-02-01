# File name: exercise4_task4_Class.py
# Author: Tiia Iire
# Description: Class where we get phones manufacturer, model, price and ID (between 1-6)

import random

class CellPhone:
    def __init__(self):
        self.manufacturer = "manufact"
        self.model = "model"
        self.price = "price"
        self.ID = "ID"

    def set_Manufact(self):
        self.manufacturer = str(input("What is your phones manufacturer? "))

    def set_Model(self):
        self.model = str(input("What is your phones model? "))

    def set_RetailPrice(self):
        self.price = float(input("What is your phones retail price? "))

    def set_ID(self):
        self.ID = int(input("What is your phones ID? (1-6) "))

    def get_manufact(self):
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_retailPrice(self):
        return self.price

    def get_ID(self):
        while not(CellPhone.correct_id(self.ID)):
            self.ID = int(input("ID you chose is not available, choose again (1-6): "))
        else:
            return self.ID
        
        
    def correct_id(input):
        if input == 1 or input == 2 or input == 3 or input == 4 or input == 5 or input == 6:
            return True
        else:
            return False
            
    def __str__(self):
        return f"""Manufacturer: {self.manufacturer} Model: {self.model} Retail price: {self.price} Phone ID: {self.ID}"""
