# File name: exercise6_task7_Classes.py
# Author: Tiia Iire
# Description: Inherits Student and teacher with course

import exercise6_task3_AnimalClass as animal

class Course(animal.Wildanimal):
    def __init__(self):
        animal.Wildanimal.__init__(self)
        self.__coursename = "python"
        self.__courseID = 0

    def set_ID(self):
        self.__courseID = int(input("What is the course ID? "))

    def set_name(self):
        self.__coursename = str(input("What is courses name? "))

    def get_ID(self):
        return self.__courseID

    def get_name(self):
        return self.__coursename

    def __str__(self):
        return "Course ID: " + format(self.__courseID) + "\n Courses name: " + format(self.__coursename)

class Teacher(Course):
    def __init__(self):
        Course.__init__(self)
        self.__tfname = "fname"
        self.__tlname = "lname"

    def set_tfname(self):
        self.__tfname = str(input("What is Teachers first name? "))

    def set_tlname(self):
        self.__tlname = str(input("What is Teachers last name? "))

    def get_tfname(self):
        return self.__fname

    def get_tlname(self):
        return self.__lname

    def __str__(self):
        return format(Course.__str__(self)) + "\n Teachers name: " + format(self.__tfname) + format(self.__tlname)

class Student(Teacher):
    def __init__(self):
        Teacher.__init__(self)
        self.__fname = "fname"
        self.__lname = "lname"
        self.__studentnumber = 0

    def set_fname(self):
        self.__fname = str(input("What is Students first name? "))

    def set_lname(self):
        self.__lname = str(input("What is Students last name? "))

    def set_studentnumber(self):
        self.__studentnumber = int(input("What is Students number? "))

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_studentnumber(self):
        return self.__studentnumber

    def __str__(self):
        return format(Teacher.__str__(self)) + "\n Students name: " + format(self.__fname) + format(self.__lname)
            + "\n Studentnumber: " + format(self.__studentnumber)

    
