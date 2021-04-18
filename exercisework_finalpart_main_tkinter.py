# File name: exercisework_finalpart_main_tkinter.py
# Author: Tiia Iire
# Description: veterinary booking

#First we need to import classes and tkinter and tkcalendar
import exercisework_finalpart_class_tkinter as user
from tkinter import *
from functools import partial
from tkcalendar import *

#Function for login
def login():
    usern = username.get()
    passwrd = password.get()
    f = open("data.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split()
        if (usern in us) and (passwrd in pw):
            logcompLabel.grid(row=5, column=1)
            tkWindow.after(3000, booking_window)
            return
                
    wrongLabel.grid(row=6, column=1)
    return False

# Make window for login
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Veterinary appointment Login')

# Make username label and text entry box
usernameLabel = Label(tkWindow, text = "Username").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable = username).grid(row=0, column=1)


# Make same for password
passwordLabel = Label(tkWindow, text = "Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable = password, show='*').grid(row=1, column=1)

            

#Window for registration
def regist_window():
    rgWindow = Tk()
    rgWindow.geometry('400x150')
    rgWindow.title('Veterinary appointment registration')

    #Function for making new account
    def new_user():
        fname = firstname.get()
        lname = lastname.get()
        newuser = new_username()
        f = open("data.txt", "r")
        for line in f.readlines():
            us, pw = line.strip().split()
            if newuser in us:
                takenLabel.grid(row=6, column=1)
                return
        newpassw = new_password()
        user_file = open("data.txt", "a")
        acc = "\n" + newuser + " " + newpassw
        user_file.write(acc)
        user_file.close()
        regcomplLabel.grid(row=5, column=1)
        rgWindow.after(3000, rgWindow.destroy)

    def new_username():
        newname = str('%s' % (newnameEntry.get()))
        return newname

    def new_password():
        newpassword = str('%s' % (newpasswordEntry.get()))
        return newpassword
        

    # Make labels for users informations
    firstnameLabel = Label(rgWindow, text = "First name")
    firstnameLabel.grid(row=0, column=0)
    firstname = StringVar()
    firstnameEntry = Entry(rgWindow, textvariable = firstname)
    firstnameEntry.grid(row=0, column=1)

    lastnameLabel = Label(rgWindow, text = "Last name")
    lastnameLabel.grid(row=1, column=0)
    lastname = StringVar()
    lastnameEntry = Entry(rgWindow, textvariable = lastname)
    lastnameEntry.grid(row=1, column=1)

    newnameLabel = Label(rgWindow, text = "New username")
    newnameLabel.grid(row=2, column=0)
    newnameEntry = Entry(rgWindow)
    newnameEntry.grid(row=2, column=1)

    newpasswordLabel = Label(rgWindow, text = "New password")
    newpasswordLabel.grid(row=3, column=0)
    newpasswordEntry = Entry(rgWindow)
    newpasswordEntry.grid(row=3, column=1)

    regcomplLabel = Label(rgWindow, text = "Registration completed", foreground = "red")
    takenLabel = Label(rgWindow, text = "username already taken!", foreground = "red")
    # Button to confirm the registration
    confButton = Button(rgWindow, text = "Confirm", command = new_user).grid(row=4, column=0)    

# function for booking
def booking_window():
    # New window
    bkWindow = Tk()
    bkWindow.title("Appointment calendar")
    bkWindow.geometry("500x1200")

    #Pet's informatio Labels
    specieLabel = Label(bkWindow, text = "Pet's specie")
    specieLabel.grid(row=0, column=0)
    specie = StringVar()
    specieEntry = Entry(bkWindow, textvariable = specie)
    specieEntry.grid(row=0, column=1)

    raceLabel = Label(bkWindow, text = "Pet's race")
    raceLabel.grid(row=1, column=0)
    race = StringVar()
    raceEntry = Entry(bkWindow, textvariable = race)
    raceEntry.grid(row=1, column=1)

    ageLabel = Label(bkWindow, text = "Pet's age")
    ageLabel.grid(row=2, column=0)
    age = StringVar()
    ageEntry = Entry(bkWindow, textvariable = age)
    ageEntry.grid(row=2, column=1)

    petnameLabel = Label(bkWindow, text = "Pet's name")
    petnameLabel.grid(row=3, column=0)
    petname = StringVar()
    petnameEntry = Entry(bkWindow, textvariable = petname)
    petnameEntry.grid(row=3, column=1)

    #Then we do the Calendar
    hour_string=StringVar()
    min_string=StringVar()
    last_value_sec = ""
    last_value = ""        
    f = ('Times', 20)

    def display_msg():
        date = cal.get_date()
        m = min_sb.get()
        h = sec_hour.get()
        s = sec.get()
        t = f"Your appointment is booked for {date} at {m}:{h}:{s}. \n You can cancel your appointment by calling us, \n cancelling must be done at least 24 hours before appointment!"
        msg_display.config(text=t)
       

    #if functions to tell if minutes or seconds go over 59, it goes to zero
    if last_value == "59" and min_string.get() == "0":
        hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)   
        last_value = min_string.get()

    if last_value_sec == "59" and sec_hour.get() == "0":
        min_string.set(int(min_string.get())+1 if min_string.get() !="59" else 0)
    if last_value == "59":
        hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)            
        last_value_sec = sec_hour.get()

    fone = Frame(bkWindow)
    ftwo = Frame(bkWindow)

    fone.grid(column=1)
    ftwo.grid(column=1)

    cal = Calendar(fone, selectmode="day", year=2021, month=2, day=3)
    cal.pack()

    #Spinboxes for choosing the time
    min_sb = Spinbox(ftwo, from_=0, to=23, wrap=True, textvariable=hour_string, width=2, state="readonly", font=f, justify=CENTER)
    sec_hour = Spinbox(ftwo, from_=0, to=59, wrap=True, textvariable=min_string, font=f, width=2, justify=CENTER)
    sec = Spinbox(ftwo, from_=0, to=59, wrap=True, textvariable=sec_hour, width=2, font=f, justify=CENTER)

    min_sb.grid(row=10, column=1)
    sec_hour.grid(row=10, column=2)
    sec.grid(row=10, column=3)

    #Text after the spinboxes to tell user which box is which
    msg = Label(bkWindow, text="Hour  Minute  Seconds", font=("Times", 12))
    msg.grid(row=11, column=1)

    #Button to finish the booking
    actionBtn =Button(bkWindow, text="Book Appointment", padx=10, pady=10, command=display_msg)
    actionBtn.grid(column=1)

    msg_display = Label(bkWindow, text="")
    msg_display.grid(column=1)    
    

# Make login ang regitsration button and login succesfully
loginButton = Button(tkWindow, text = "Login", command = login).grid(row=4, column=0)
regButton = Button(tkWindow, text = "Create account", command = regist_window).grid(row=4, column=1)
logcompLabel = Label(tkWindow, text = "Logged in succesfully", foreground = "red")
wrongLabel = Label(tkWindow, text = "incorrect username or password", foreground = "red")

tkWindow.mainloop()
