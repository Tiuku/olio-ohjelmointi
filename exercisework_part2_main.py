# File name: exercisework_part2_main.py
# Author: Tiia Iire
# Description: veterinary booking

#First we need to import classes and also pickle for the dictionary
import exercisework_part2 as user
import pickle

def main():
    # make the object
    my_user = user.Pet("Dog", "sheltie", 11, "kapu")
    # make the dictionary
    users = {}
    # ask for the owners information and user information
    my_user.set_fname()
    my_user.set_lname()
    my_user.set_username()
    my_user.set_password()

    # get the user information in to dictionary
    users[my_user.get_username()] = my_user.get_password()
    user_file = open("data.txt", "wb")
    pickle.dump(users, user_file)
    user_file.close()
    # test if it has worked
    print(users)

    #Ask for the pets information
    my_user.set_specie()
    my_user.set_race()
    my_user.set_age()
    my_user.set_name()
    print(my_user)

main()
