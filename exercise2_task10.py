# File name: exercise2_task10.py
# Author: Tiia Iire
# Description: This will first ask what time you want to wake up and
# Wakes you up at the right time or tells you that it is not time to wake up yet. 
import datetime


def set_alarm():
    alarm = str(input("Do you want to set alarm? "))
    if alarm == "yes":
        hour = int(input("Enter the hour: "))
        minute = int(input("Enter the minute: "))
        second = int(input("Enter the second: "))
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        day = int(input("Enter the day: "))

        setted_time = datetime.datetime(year, month, day, hour, minute, second)

        return setted_time
    else:
        return "No alarm setted"

def time_now():
    current_time = datetime.datetime.now()
    return current_time

def main():
    if set_alarm() == time_now():
        print("Time to wake up!")
    else:
        print(time_now(), "No alarm yet")

main()
    
    
                                
                                                        
