# File name: exercise2_task3.py
# Author: Tiia Iire
# Description: gives grade based on how many exercises user has done

exe = int(input("How many accepted exercises did you do?: "))

if exe == 9:
    print("Your grade is: 1")
elif exe == 10:
    print("your grade is: 2")
elif exe == 11:
    print("Your grade is: 3")
elif exe == 12:
    print("Your grade is: 4")
elif exe == 13:
    print("Your grade is: 5")
else:
    print("Your grade is: 0")
