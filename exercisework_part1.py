# File name: exercisework_part2.py
# Author: Tiia Iire
# Description: classes for vets appointment informations


# First make a class for owners information
class Owner():
    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname

    def set_fname(self):
        self.fname = str(input("What is your first name?"))

    def set_lname(self):
        self.lname = str(input("What is your last name?"))

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

    def set_username(self):
        self.name = str(input("What is your username?"))

    def get_username(self):
        return self.name

    def set_password(self):
        self.password = input("Insert here what password you want to use: ")

    def get_password(self):
        return self.password

    def __str__(self):
        return "Hello " + format(Owner.__str__(self))

# Next the Pet class to ask for the pets information
# Also inheriting User class and as User class inherits Owner class, we get that also
class Pet(User):
    def __init__(self, specie, race, age, name):
        User.__init__(self, "tiiaiire", "kau") # inheriting the init function from User class
        self.specie = specie
        self.race = race
        self.age = age
        self.name = name
        
    def set_specie(self):
        self.specie = str(input("What is your pets specie?"))

    def set_race(self):
        self.race = str(input("What is your pets race?"))

    def set_name(self):
        self.name = str(input("What is your pets name?"))

    def set_age(self):
        self.age = int(input("What is your pets age?"))

    def get_specie(self):
        return self.specie

    def get_race(self):
        return self.race

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return format(User.__str__(self)) + " Your pet's specie is: " + format(self.specie) + " and it is: " + format(self.race) +
    " Your " + format(self.specie) + " is " + format(self.age) + " years old and is called " + format(self.name)
    
