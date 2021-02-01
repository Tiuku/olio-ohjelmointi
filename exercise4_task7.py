# File name: exercise4_task7.py
# Author: Tiia Iire
# Description: Asks user cars model, make, mileage, price, maximum load limit and trunk size

class Car:
    def __init__(self):
        self.__make = "make"
        self.__model = "model"
        self.__mileage = "mileage"
        self.__price = "price"
        self.__maxload = "maxload"
        self.__trunksize = "trunk"

    def set_make(self):
        self.__make = str(input("What is your cars make? "))

    def set_model(self):
        self.__model = input("What is your cars model? ")

    def set_mileage(self):
        self.__mileage = int(input("How much is the mileage? "))

    def set_price(self):
        self.__price = int(input("How much is the price? "))

    def set_maxload(self):
        self.__maxload = int(input("How much is maximum load limit? "))

    def set_trunk(self):
        self.__trunksize = int(input("How big is the truck? "))

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_maxload(self):
        return self.__maxload

    def get_trunksize(self):
        return self.__trunksize

    def __str__(self):
        return f""" Cars make: {self.__make}, Cars model: {self.__model}, Cars mileage: {self.__mileage} km,
        Cars price: {self.__price} €, Cars maxload: {self.__maxload} kg, Cars trunk size: {self.__trunksize} m2"""


def main():
    my_car = Car()

    my_car.set_make()
    my_car.set_model()
    my_car.set_mileage()
    my_car.set_price()
    my_car.set_maxload()
    my_car.set_trunk()
    
    print(my_car)
main()
