# File name: exercise6_task3_AnimalClass.py
# Author: Tiia Iire
# Description: Inherits mammal class and sets animals noise and diet

import exercise4_task8_mammal as mammal

class Animal(mammal.Mammal):
    def __init__(self):
        mammal.Mammal.__init__(self)
        self.__noise = "woof"
        self.__diet = "meat"

    def set_noise(self):
        self.__noise = str(input("What sound does the animal do? "))

    def set_diet(self):
        self.__diet = str(input("What kind of diet your animal has? "))

    def get_noise(self):
        return self.__noise

    def get_diet(self):
        return self.__diet

    def __str__(self):
        return "Animal is: " + format(mammal.Mammal_self.__specie) + "The animal does this sound: " + format(self.__noise) + " and eats: " + format(self.__diet)

class Wildanimal(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__territory = "woods"

    def set_territory(self):
        self.__territory = str(input("Where does this wild animal lives?: "))

    def get_territory(self):
        return self.__territory

    def __str__(self):
        return "The animal is: " + format(Mammal.self.__specie) + ". It makes this sound: " + format(Animal.self.__noise) + " and eats: " + format(Animal.self.__diet)
        + " This animal lives in: " + format(self.__territory)
