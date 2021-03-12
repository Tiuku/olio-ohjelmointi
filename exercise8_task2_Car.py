# File name: exercise8_task2_Car.py
# Author: Tiia Iire
# Description: class for cleaning car and changing tires

class Car():
    def __init__(self, inside, outside, tires, tank):
        self.__inside = inside
        self.__outside = outside
        self.__tires = tires
        self.__tank = tank

    def set_inside(self):
        self.__inside = str(input("Is the car dirty or clean on the inside?"))

    def set_outside(self):
        self.__outside = str(input("Is the car dirty or clean on the outside?"))

    def set_tires(self):
        self.__tires = str(input("Is there summertires or wintertires?"))

    def set_tank(self):
        self.__tank = str(input("Is the tank empty, full or half full?"))

    def get_inside(self):
        return self.__inside

    def get_outside(self):
        return self.__outside

    def get_tires(self):
        return self.__tires

    def get_tank(self):
        return self.__tank

    def __str__(self):
        return f"""The car is {self.__inside} inside and {self.__outside} outside,
        There is {self.__tires} and the tank is {self.__tank}"""
