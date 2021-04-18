# File name: exercisework_finalpart_class_tkinter.py
# Author: Tiia Iire
# Description: classes for vets appointment informations


# First make a class for owners information
class Owner():
    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname

    def set_fname(self, name):
        self.fname = name

    def set_lname(self, lastname):
        self.lname = lastname

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def __str__(self):
        return format(self.fname) + " " + format(self.lname)

# Next we need to have the user information to log in to schedule appointment
# Inheriting Owner class to here
class User(Owner):
    def __init__(self, username, passw):
        Owner.__init__(self, "Tiia", "Iire") # inheriting the init function from Owner class
        self.username = username
        self.password = passw        

    def set_username(self, uname):
        self.name = uname

    def get_username(self):
        return self.name

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def __str__(self):
        return "Hello " + format(Owner.__str__(self))

# Next the Pet class to ask for the pets information
class Pet():
    def __init__(self, specie, race, age, name):
        self.specie = specie
        self.race = race
        self.age = age
        self.name = name
        
    def set_specie(self, spec):
        self.specie = spec

    def set_race(self, rac):
        self.race = rac

    def set_name(self, petname):
        self.name = petname

    def set_age(self, petage):
        self.age = petage

    def get_specie(self):
        return self.specie

    def get_race(self):
        return self.race

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return "Your pet's specie is: " + format(self.specie) + " and it is: " + format(self.race) + " Your " + format(self.specie) + " is " + format(self.age) + " years old and is called " + format(self.name)
    
