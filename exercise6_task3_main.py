# File name: exercise6_task3_main.py
# Author: Tiia Iire
# Description: Gets information from mammal and animal classes
# and asks user for specie, noise and diet and prints the information

import exercise4_task8_mammal as mammal
import exercise6_task3_AnimalClass as animal

def main():

    print("Let's first get one domestic animal")
    x = animal.Animal()
    x.set_specie()
    x.set_noise()
    x.set_diet()
    print(x)

    print("Now let's get one wild animal")
    y = animal.Wildanimal()
    y.set_specie()
    y.set_noise()
    y.set_diet()
    y.set_territory()
    print(y)
    
main()
