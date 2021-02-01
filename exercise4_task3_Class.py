# File name: exercise4_task3_Class.py
# Author: Tiia Iire
# Description: Class where we get phones manufacturer, model and price

import random

class CellPhone:
    def __init__(self):
        self.manufacturer = "manufact"
        self.model = "model"
        self.price = "price"

    def set_Manufact(self):
        self.manufacturer = str(input("What is your phones manufacturer? "))

    def set_Model(self):
        self.model = str(input("What is your phones model? "))

    def set_RetailPrice(self):
        self.price = float(input("What is your phones retail price? "))

    def get_manufact(self):
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_retailPrice(self):
        return self.price

    def __str__(self):
        return f"""Manufacturer: {self.manufacturer} Model: {self.model} Retail price: {self.price}"""
