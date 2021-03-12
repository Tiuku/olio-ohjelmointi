# File name: exercise8_task3_main.py
# Author: Tiia Iire
# Description: baking cookies

import exercise8_task3_Cookie as cook

def main():
    my_cookie = Cook.Cookie("bake", "frost", "flavor")
    cookies = []

    my_cookie.set_bake()
    my_cookie.set_flavor()
    favorite = str(input("What is your favorite flavor?"))
    while favorite != my_cookie.get_flavor():
        my_cookie.set_flavor()

    cookies.append(my_cookie)
    

    while my_cookie.get_bake() == "yes":
        my_cookie.set_bake()
        my_cookie.set_flavor()
        while favorite != my_cookie.get_flavor():
            my_cookie.set_flavor()
            
        cookies.append(my_cookie)

    for cookie in range(len(cookies)):
        my_cookie.set_frost()
        if my_cookie.get_frost() != "yes":
            print("We have to frost every cookie")
            my_cookie.set_frost()
    
    for i in cookies:
        print(i.get_flavor())


main()
