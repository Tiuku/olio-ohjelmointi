# File name: exercise8_task2_main.py
# Author: Tiia Iire
# Description: Washing car inside and outside, changing tires and fuel up the tank

import exercise8_task2_Car as car

def main():
    my_car = car.Car("dirty", "dirty", "wintertires", "near empty")

    print(my_car)
    print("We need to fix things up! Let's start by changing the tires")
    print("Changing tires..")

    my_car.set_tires()

    print(my_car, "Now we need to wash it outside, let's go get water and soap and sponge!")
    print("showering the car.. putting soap.. scrubbing with sponge.. washing soap off")

    my_car.set_outside()
    

    print(my_car, "Now we can move on to the inside.. let's vacuum it!")
    print("vacuuming...")

    my_car.set_inside()

    print(my_car, "Great! Now we can go to fuel up! Let's drive to the nearest gas station")
    print("fueling up..")
    
    my_car.set_tank()

    print(my_car, "And we are done YAY!")

main()

    
