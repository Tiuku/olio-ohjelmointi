def readnums():
    neg_count = 0
    
    while True:
        num = int(input("Write number: "))
        if num < 0:
            neg_count += 1
        elif num == 0:
            return neg_count
            

print("Number of negative integers: ", readnums())
