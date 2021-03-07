# File:         main.py
# Author:       Tiia Iire
# Description:  Deck of cards and card games.

import exercise7_task4_Card as card
import exercise7_task4_Deck as deck
import exercise7_task4_Player as player

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
   # print("Let's play a game. Draw 3 cards and see which wins")
    
  #  card1 = my_deck.draw_card()
  #  card1.show_card()
   # card2 = my_deck.draw_card()
    #card2.show_card()
   # card3 = my_deck.draw_card()
    #card3.show_card()

    #while True:
     #   if card1.get_value() < card3.get_value() and card2.get_value() < card3.get_value():
      #      print("winner is: ")
       #     card3.show_card()
        #    return False
       # elif card2.get_value() < card1.get_value() and card3.get_value() < card1.get_value():
        #    print("winner is: ")
         #   card1.show_card()
          #  return False
       # elif card1.get_value() < card2.get_value() and card3.get_value() < card2.get_value():
        #    print("winner is: ")
         #   card2.show_card()
          #  return False
        #else:
         #   print("There is a tie, we have to draw again!")
          #  card1 = my_deck.draw_card()
           # card1.show_card()
           # card2 = my_deck.draw_card()
           # card2.show_card()
           # card3 = my_deck.draw_card()
           # card3.show_card() 
        
    # Exercise 7 task 4 b game here
    print("Let's play blackjack!")
    print("Who is playing?")
    player1 = player.Player("Tiia")
    player2 = player.Player("Oona")
    dealer = player.Player("Ritva")
    print("Hello and welcome to play blackjack. My name is: ", dealer.set_name(), "Player 1 is: ", player1.set_name(), " and Player 2 is: ", player2.set_name())

    my_deck.shuffle_deck()
    my_deck.show_deck()

    player1hand = []
    player2hand = []
    dealerhand = []
    
    print("Player 1 hand")
    for p in range(2):
        player1 = my_deck.draw_card()
        player1.show_card()
        player1hand.append(player1.get_value())
        
    print("Player 2 hand")
    for o in range(2):
        player2 = my_deck.draw_card()
        player2.show_card()
        player2hand.append(player2.get_value()) 

    print("Dealers hand")
    for d in range(2):
        dealer = my_deck.draw_card()
        dealer.show_card()
        dealerhand.append(dealer.get_value())

    print("Dealer has now: ", sum(dealerhand), "Player 1 has now: ", sum(player1hand), " Player 2 has now: ", sum(player2hand), " Do you want to get a new card?")
    x = input()
    while x == "yes":
        player1 = my_deck.draw_card()
        player1.show_card()
        player1hand.append(player1.get_value())
        player2 = my_deck.draw_card()
        player2.show_card()
        player2hand.append(player2.get_value())
        dealer = my_deck.draw_card()
        dealer.show_card()
        dealerhand.append(dealer.get_value())

        print("Dealer has now: ", sum(dealerhand), "Player has now: ", sum(player1hand), " Player 2 has now: ", sum(player2hand), " Do you want to get a new card")
        x = input()


    if sum(player1hand) <= 21 and sum(player1hand) > sum(dealerhand):
        print("Player 1 wins the Dealer!")
    elif sum(player1hand) >= 22:
        print("Dealer wins Player 1")
    elif sum(player1hand) <= 21 and sum(player1hand) >= 22:
        print("Player 1 wins the Dealer!")
    elif sum(dealerhand) >= 22 or sum(player1hand) >= 22:
        print("Player 1 wins the Dealer!")
    else:
        print("Dealer wins Player 1")


    if sum(player2hand) <= 21 and sum(player2hand) > sum(dealerhand):
        print("Player 2 wins the Dealer!")
    elif sum(player2hand) >= 22:
        print("Dealer wins Player 2")
    elif sum(player2hand) <= 21 and sum(player2hand) >= 22:
        print("Player 2 wins the Dealer!")
    elif sum(dealerhand) >= 22 or sum(player2hand) >= 22:
        print("Player 2 wins the Dealer!")
    else:
        print("Dealer wins Player 2")
    
    
        
            

# Calling the main function here, do not change...
main()
