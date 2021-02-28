# File name: exercise6_task8_main.py
# Author: Tiia Iire
# Description: Main class for getting course,
# teachers name and students name and studentnumber
# It also gets one domestic animal and one wild animal for both

import exercise6_task7_Classes as classes
import exercise6_task3_AnimalClass as animal

def main():
    x = classes.Student()
    y = classes.Student()
    course = []
    teacher = []
    student = []

    print("Let's get course information first: ")
    x.set_ID()
    x.set_name()
    course.append(x.get_ID(), x.get_name())
    print("Who is this courses teacher?" )
    x.set_tfname()
    x.set_tlname()
    print("Let's set teachers pet..")
    x.set_specie()
    x.set_noise()
    x.set_diet()
    teacher.append(x.get_tfname(), x.get_tlname(),
                   x.get_specie(), x.get_noise(), x.get_diet())
    print("Let's set teachers favorite wild animal..")
    x.set_specie()
    x.set_noise()
    x.set_diet()
    x.set_territory()
    teacher.append(x.get_specie(), x.get_noise(), x.get_diet(),
                   x.get_territory())
    print("Let's set the students information next")
    y.set_fname()
    y.set_lname()
    y.set_studentnumber()
    print("Let's set students pet..")
    y.set_specie()
    y.set_noise()
    y.set_diet()
    teacher.append(y.get_tfname(), y.get_tlname(),
                   y.get_specie(), y.get_noise(), y.get_diet())
    print("Let's set students favorite wild animal..")
    y.set_specie()
    y.set_noise()
    y.set_diet()
    y.set_territory()
    student.append(y.get_specie(), y.get_noise(), y.get_diet(),
                   y.get_territory())
    print(course, teacher, student)

main()

    
