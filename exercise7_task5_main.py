# File name: exercise7_task5_main.py
# Author: Tiia Iire
# Description: main to get pet and student

import exercise7_task5_Petandstudent as student

def main():
    my_student = student.Student("Tiia", "Iire", 1903416)
    print("Please identidy yourself first: ")
    my_student.set_first_name()
    my_student.set_last_name()
    my_student.set_student_ID()

    print("Good, now we can add your pets information: ")

    my_student.add_pets()

    
    x = input("Do you want to add more pets?")
    while x == "yes":
        my_student.add_pets()
        x = input("Do you want to add more pets?")

    
    y = input("Did you made some mistake and want to remove some pet?")
    while y == "yes":
        my_student.remove_pets()
        y = input("Did you made some mistake and want to remove some pet?")

    print("Let's see what kind of pets you have.. ")
    print(my_student.print_pets())

main()
    
