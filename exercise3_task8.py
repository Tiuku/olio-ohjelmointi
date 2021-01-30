# File name: exercise3_task8.py
# Author: Tiia Iire
# Description: Class where we get phones manufacturer, model and price

# Pseudocode:
# make class CellPhone
#   function init which has three data-attributes:
#       self.manufacturer equals manuf
#       self.model equals model
#       self.price equals price
#
#   function Manufact
#       Ask user what is phones manufacturer
#
#   function Model
#       Ask the model from user
#
#   function RetailPrice
#       Ask the price from user
#
#   function get_manufact
#       return function Manufact
#
#   function get_model
#       return function Model
#
#   function get_retailPrice
#       return function RetailPrice
#
#   function __str__
#       return the print from all the data-attributes

import random

class CellPhone:
    def __init__(self):
        self.manufacturer = "manufact"
        self.model = "model"
        self.price = "price"

    def Manufact(self):
        self.manufacturer = str(input("What is your phones manufacturer? "))

    def Model(self):
        self.model = str(input("What is your phones model? "))

    def RetailPrice(self):
        self.price = float(input("What is your phones retail price? "))

    def get_manufact(self):
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_retailPrice(self):
        return self.price

    def __str__(self):
        return f"""Manufacturer: {self.manufacturer} Model: {self.model} Retail price: {self.price} """
