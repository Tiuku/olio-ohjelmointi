# File name: list.py
# Author: Tiia Iire
# Description: Asks user for 10 items and makes them list.
# Sorts the list alphabetically

list = []

for i in range(10):
    item = str(input("Write your items name: "))
    list.append(item)

list.sort()
print(list)
