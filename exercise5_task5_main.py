# File name: exercise5_task5_main.py
# Author: Tiia Iire
# Description: doing dictionary for players first and last name, players id and diceside.
# functions for looking up for player, adding player, displaying dictionary and quitting

import exercise5_task5_PlayerClass as player
import random
import pickle

LOOK_UP = 1
ADD = 2
DISPLAY = 3
QUIT = 4

FILENAME = "players.dat"

def make_dict():
    player_dct = {}

    return player_dct

def get_menu_choice():
    print("Menu")
    print("1 Look up players")
    print("2 Add new player")
    print("3 Display all players")
    print("4 Quit")

    choice = int(input("Enter what you want to do?"))

    if choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid number: "))

    return choice

def look_up(players):
    playerid = int(input("Enter players id: "))
    print(players.get(playerid, "That id is not found."))

def add(players):
    my_player.set_id()
    my_player.set_lastname()
    my_player.set_firstname()
    my_player.set_dice()
    entry = player.Player(get_id(), get_lastname(), get_firstname(), get_dice())

    if playerid not in players:
        players[playerid, lastname, firstname, diceside] = entry
        print("Player has been added")

def display(players):
    for playerid in players:
        print(players)

def main():
    my_player = player.Player()
    players = make_dict()
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(players)
        elif choice == ADD:
            add(players)
        elif choice == DISPLAY:
            display(players)

    
main()




    

    
