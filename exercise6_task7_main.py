# File name: exercise6_task7_main.py
# Author: Tiia Iire
# Description: Main class for getting course,
# teachers name and students name and studentnumber

import exercise6_task7_Classes as classes

def main():
    x = classes.Student()

    x.set_ID()
    x.set_name()
    x.set_tfname()
    x.set_tlname()
    x.set_fname()
    x.set_lname()
    x.set_studentnumber()

    print(x)

main()

    
