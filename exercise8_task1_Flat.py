# File name: exercise8_task1_Flat.py
# Author: Tiia Iire
# Description: Class for helping the human to clean one by one

class Flat():
    def __init__(self, floors, windows, bed, surfaces, fridge, paper):
        self.__floors = floors
        self.__windows = windows
        self.__bed = bed
        self.__surfaces = surfaces
        self.__fridge = fridge
        self.__paper = paper

    def set_floors(self):
        self.__floors = str(input("Are the floors clean or dirty?"))

    def set_windows(self):
        self.__windows = str(input("Are the windows clean or dirty?"))

    def set_bed(self):
        self.__bed = str(input("Is the bed made or unmade?"))

    def set_surfaces(self):
        self.__surfaces = str(input("Are the surfaces dusty or clean?"))

    def set_fridge(self):
        self.__fridge = str(input("Is the fridge full or empty?"))

    def set_paper(self):
        self.__paper = str(input("Is there not enough, enough or more than enough paper?"))

    def get_floors(self):
        return self.__floors

    def get_windows(self):
        return self.__windows

    def get_bed(self):
        return self.__bed

    def get_surfaces(self):
        return self.__surfaces

    def get_fridge(self):
        return self.__fridge

    def get_paper(self):
        return self.__paper

    def __str__(self):
        return f"""Windows are {self.__windows}, floors are  {self.__floors}, Bed is {self.__bed},
        Surfaces are {self.__surfaces}, fridge is {self.__fridge} and there is {self.__paper} paper"""
