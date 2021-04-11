# File name: exercisework_part3_main.py
# Author: Tiia Iire
# Description: veterinary booking

#First we need to import classes and also pickle for the dictionary
import exercisework_part2 as user
import pickle

#def login():
#    users = {}
#    x = input("Do you have an account?")
#    if x == "yes":
#        username = input("Username: ")
#        passwrd = input("Password: ")
#        with open("data.txt") as f:
#            for line in f:
#                (key, val) = line.split()
#                users[(key)] = val
                
#        if username in users and users[username] == passwrd:
#            print("Welcome back!")
#        else:
#            print("incorrect username or password")
            
#    else:
#        my_user.set_fname()
#        my_user.set_lname()
#        my_user.set_username()
#        my_user.set_password()
#        users[my_user.get_username()] = my_user.get_password()
#        user_file = open("data.txt", "ab")
#        pickle.dump(users, user_file)
#        user_file.close()

# function for booking
def booking():
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
    print("You have booked: ", time, " for ", z, " for ", y)

def main():
    # make the object
    my_user = user.User("tiiaiire", "kapu")
    #login()
        
    

    #Ask for the pets information
    my_pet = user.Pet("dog", "sheltie", 11, "kapu")
    my_pet.set_specie()
    my_pet.set_race()
    my_pet.set_age()
    my_pet.set_name()
    print(my_user, my_pet)
    booking()

main()
