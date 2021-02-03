# File name: exercise4_task8_mammal.py
# Author: Tiia Iire
# Description: Class where we define mammals ID, species, name, size,
# weight and height

class Mammal:
    def __init__(self):
        self.ID = 0
        self.specie = "dog"
        self.name = "chiara"
        self.size = 0
        self.weight = 0
        self.height = 0

    def set_ID(self):
        self.ID = int(input("Pick an ID for your mammal (1-6): "))

    def set_specie(self):
        self.specie = str(input("What is your mammals specie? "))

    def set_name(self):
        self.name = str(input("What is your mammals name? "))

    def set_size(self):
        self.size = int(input("What is the size of your mammal? "))

    def set_weight(self):
        self.weight = int(input("How much does your mammal weighs? "))

    def set_height(self):
        self.height = int(input("How tall is your mammal? "))

    def get_ID(self):
        while not(Mammal.correct_id(self.ID)):
            self.ID = int(input("ID you chose is not available, choose again (1-6): "))
        else:
            return self.ID

    def get_specie(self):
        return self.specie

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def correct_id(input):
        if input == 1 or input == 2 or input == 3 or input == 4 or input == 5 or input == 6:
            return True
        else:
            return False

    def __str__(self):
        return f""" your mammals ID: {self.ID} your mammals specie: {self.specie} your {self.specie}s name: {self.name}
        your {self.specie}s size: {self.size} Your {self.specie}s weight: {self.weight} your {self.specie}s height: {self.height} """
        
