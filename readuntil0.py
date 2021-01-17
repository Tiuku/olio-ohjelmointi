def evennums(num):
    if num % 2 == 0:
        return "is even"
    else:
        return
def dividedbythree(num):
    if num > 0 and num % 3 == 0:
        return "is divided by three"
    else:
        return

def readnums():
    neg_count = 0
    even_count = 0
    divide = 0
    
    while True:
        num = int(input("Write number: "))
        if evennums(num) == "is even":
            even_count += 1
        elif dividedbythree(num) == "is divided by three":
            divide += 1
        if num < 0:
            neg_count += 1
        elif num == 0:
            print("Number of even integers: ", even_count)
            print("Number of negative integers: ", neg_count)
            print("Number of positive integers divided by three", divide)
            return

readnums()

        




    



