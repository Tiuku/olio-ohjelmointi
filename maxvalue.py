# File name: maxvalue.py
# Author: Tiia Iire
# Description: Asks for user to set max value, counts the number of terms and sum of terms

maxvalue = int(input("Set your maximum value: "))

x1 = 2
x2 = 4

def formula(x, y, max):
    numterms = 2
    sumterms = 0

    while True:
        z = x + y
        if z > max:
            print("Number: ", numterms)
            print("Sum: ", sumterms)
            return
        elif z == max:
            numterms +=1
            print("Number: ", numterms)
            print("Sum: ", z)
            return
        else:
            numterms += 1
            sumterms = x + y
            if x < y:
                x = z
            else:
                y = z

formula(x1, x2, maxvalue)

        




    



