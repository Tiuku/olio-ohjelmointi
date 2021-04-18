# File name: exercisework_finalpart_main.py
# Author: Tiia Iire
# Description: veterinary booking

#First we need to import classes 
import exercisework_finalpart_class as user

def login():
    # make the object
    my_user = user.User("tiiaiire", "kapu")
    users = {}
    x = input("Do you have an account?")
    if x == "yes":
        username = input("Username: ")
        passwrd = input("Password: ")
        f = open("data.txt", "r")
        for line in f.readlines():
            us, pw = line.strip().split()
            if (username in us) and (passwrd in pw):
                return "Welcome back!"
                
        print("incorrect username or password")
        return login()
            
    else:
        my_user.set_fname()
        my_user.set_lname()
        my_user.set_username()
        usern = my_user.get_username()
        f = open("data.txt", "r")
        for line in f.readlines():
            us, pw = line.strip().split()
            while (usern in us):
                print("username already taken!")
                my_user.set_username()
                usern = my_user.get_username()
        my_user.set_password()
        user_file = open("data.txt", "a")
        acc = "\n" + my_user.get_username() + " " + my_user.get_password()
        user_file.write(acc)
        user_file.close()
        print("Welcome! Registration completed")
        return login()

# function for booking
def booking():
    #Ask fo the pets information
    # make the object
    my_pet = user.Pet("dog", "sheltie", 11, "kapu")
    my_pet.set_specie()
    my_pet.set_race()
    my_pet.set_age()
    my_pet.set_name()
    #First make the list of the vets
    vets = ["Kumpulainen Jouni", "Oja Jaana", "Pikkarainen Pirkko"]
    y = input("What is the reason for the appointment?")
    print("Our vets: ", vets)
    z = input("Which vet you want?")
    print("Reason: ", y, " Vet you chose: ", z)

    #Make lists for every vet where is the times that are left for next week
    if z == "Kumpulainen Jouni":
        times = ["ma 12.4. klo 10:00", "ma 12.4. klo 10:20", "ma 12.4. klo 10:40"]
    elif z == "Oja Jaana":
        times = ["ti 13.4. klo 10:00", "ti 13.4. klo 13:00", "ke 14.4. klo 12:30"]
    else:
        times = ["ke 14.4. klo 14:00", "pe 16.4. klo 10:20", "pe 16.4. klo 11:00"]

    print(z, " has these times left: ", times)
    time = input("Which time is fine for you?")
    print("You have booked: ", time, " for ", z, " for ", y, my_pet)

def main():
    print(login())
    booking()

main()
