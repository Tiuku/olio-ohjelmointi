# File name: exercise7_task4_Player.py
# Author: Tiia Iire
# Description: Class for creating a player
import exercise7_task4_Deck as deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def set_name(self):
        return self.name

    def set_hand(self):
        self.hand.append(deck.Deck.draw_card(self))
        return self.hand

    def show_hand(self):
        for card in self.hand:
            card.show()
            
