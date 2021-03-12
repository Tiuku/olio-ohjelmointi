# File name: exercise8_task3_Cookie.py
# Author: Tiia Iire
# Description: Class for baking cookies

import random

class Cookie():
    def __init__(self, bake, frost, flavor):
        self.__bake = bake
        self.__frost = frost
        self.__flavor = flavor

    def set_bake(self):
        self.__bake = str(input("Do you want to bake a cookie?"))

    def set_frost(self):
        self.__frost = str(input("Do you want to frost the cookie?"))

    def set_flavor(self):
        self.__flavor = random.randint(1,3)

    def get_bake(self):
        return self.__bake

    def get_frost(self):
        return self.__frost

    def get_flavor(self):
        if self.__flavor == 1:
            self.__flavor = "chocolate"
        elif self.__flavor == 2:
            self.__flavor = "cranberry"
        else:
            self.__flavor = "double chocolate"
        return self.__flavor

    def __str__(self):
        return f"""Cookies flavor: {get_flavor}"""
