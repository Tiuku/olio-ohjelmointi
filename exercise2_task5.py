# File name: exercise2_task5.py
# Author: Tiia Iire
# Description: gives average of the course grades by asking all students grades

students = int(input("How many students were in this course?"))
list = []

for i in range(students):
    name = str(input("What is students name?"))
    grade = int(input("What was students grade?"))

    list.append(grade)

sumofgrades = sum(list)
average = sumofgrades / students

print("Average grade of this course was: ", average)
