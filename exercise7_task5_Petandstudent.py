# File name: exercise7_task5_Petandstudent.py
# Author: Tiia Iire
# Description: class where we inherit a pet for student

class Pet():
    def __init__(self, specie, name):
        self.__specie = specie
        self.__name = name

    def set_specie(self):
        self.specie = input("What is the pets specie? ")

    def get_specie(self):
        return self.__specie

    def set_name(self):
        self.__name = input("What is the pets name? ")

    def get_name(self):
        return self.__name

    def __str__(self):
        return "The pet is: ", self.__specie, " And the pets name is: ", self.__name

class Student(Pet):
    def __init__(self, first_name, last_name, student_ID):
        Pet.__init__(self, "Cat", "Ilmari")
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_ID = student_ID
        self.__pets = []

    def set_first_name(self):
        self.__first_name = input("What is your first name? ")

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self):
        self.__last_name = input("What is your last name? ")

    def get_last_name(self):
        return self.__last_name

    def set_student_ID(self):
        self.__student_ID = int(input("What is your student ID? "))

    def get_student_ID(self):
        return self.__student_ID

    def add_pets(self):
        Pet.set_specie(self)
        Pet.set_name(self)
        self.__pets.append(Pet.__str__(self))

    def remove_pets(self):
        Pet.set_specie(self)
        Pet.set_name(self)
        self.__pets.remove(Pet.__str__(self))

    def print_pets(self):
        return self.__pets

    def __str__(self):
        return "Students name: ", get_first_name(), get_last_name(), "Students ID: ",
        get_student_ID(), "Students pets: ", print_pets()
    



    
