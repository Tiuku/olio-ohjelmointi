# File name: exercise8_task5_main.py
# Author: Tiia Iire
# Description: quiz where user need to answer the right country to capital she/he gets

quiz = {}

with open("/Users/Iire/Desktop/olio-ohjelmointi-main/olio-ohjelmointi-main/olio-ohjelmointi/countries.txt") as c:
    for line in c:
        (key, val) = line.split()
        quiz[(key)] = val

def question(dictionary):
    right_questions = 0
    wrong_questions = 0
    for i in range(10):
        key, value = dictionary.popitem()
        print("Capital: ", value)
        country = input("Country: ")
        if country == key:
            print("That's right, good job!")
            right_questions += 1
        else:
            print("Wrong..")
            wrong_questions +=1

    print("Number of correct answers: ", right_questions)
    print("Number of incorrect answers: ", wrong_questions)

def main():
    dictionary = quiz
    question(dictionary)

main()
