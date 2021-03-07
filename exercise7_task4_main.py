# File:         main.py
# Author:       Tiia Iire
# Description:  Deck of cards and card games.

import exercise7_task4_Card as card
import exercise7_task4_Deck as deck

def main():
    
    print("Let's test that a single card works...")
    
    my_card = card.Card("Hearts", 12)
    my_card.show_card()
    print(my_card)

    print("Single card testing is over.\n")

    print("Let's test that a deck of card is created...")

    my_deck = deck.Deck()
    my_deck.show_deck()

    print("Card deck testing is over.\n")

    print("Let's shuffle the deck.")
    my_deck.shuffle_deck()

    print("Let's test that a deck of card is shuffled...")

    my_deck.show_deck()

    print("Cards should be suffled now.\n")

    print("Let's draw 2 cards and show them.")
    print("You draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    print("Your opponent draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    
    # Code your Exercise 7 taks 4 game here. 
    print("Let's play a game. Draw 3 cards and see which wins")
    
    card1 = my_deck.draw_card()
    card1.show_card()
    card2 = my_deck.draw_card()
    card2.show_card()
    card3 = my_deck.draw_card()
    card3.show_card()

    while True:
        if card1.get_value() < card3.get_value() and card2.get_value() < card3.get_value():
            print("winner is: ")
            card3.show_card()
            return False
        elif card2.get_value() < card1.get_value() and card3.get_value() < card1.get_value():
            print("winner is: ")
            card1.show_card()
            return False
        elif card1.get_value() < card2.get_value() and card3.get_value() < card2.get_value():
            print("winner is: ")
            card2.show_card()
            return False
        else:
            print("There is a tie, we have to draw again!")
            card1 = my_deck.draw_card()
            card1.show_card()
            card2 = my_deck.draw_card()
            card2.show_card()
            card3 = my_deck.draw_card()
            card3.show_card()
        
        
    

# Calling the main function here, do not change...
main()
