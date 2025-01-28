# // Author: Daniel Flesch//
# // Date: 01/27/2025//
# // Blackjack Terminal Game//

import numpy as np
import pandas as pd


class Dealer:
    def __init__(self):
        self.hand = []

    def deal(self):
        rng = np.random.default_rng()  # Create a random number generator
        self.hand = [rng.integers(1, 11)]  # Generate a random integer between 1 and 10 for the first card
        self.hand.append(rng.integers(1, 11))  # Generate a random integer between 1 and 10 for the second card
        print("Dealer's hand: ", self.hand[0], "and an unknown card") #Display the dealers first card

        return self.hand

    def reveal_hand(self): # Reveal the dealer's hand
        if len(self.hand) >= 1:
            print("Dealer's hand: %d and %d" % (self.hand[0], self.hand[1]))
            print("Dealer's total: ", sum(self.hand),)
            print("--------------------------------------")

        else:
            print("Dealer's hand isn't fully dealt yet") 
        return self.hand

    def hit(self):
        if sum(self.hand) < 17:
            rng = np.random.default_rng()
            new_card = rng.integers(1, 11)
            self.hand.append(new_card)
            print("Dealer hits and draws a", new_card)
    
            if sum(self.hand) > 21:
                print("Dealer busts!")
            elif sum(self.hand) > 17 and sum(self.hand) < 21:
                print("Dealer stands with a total of", sum(self.hand), "\n")
                print("--------------------------------------")

            else: 
                print("Dealer's total: ", sum(self.hand), "\n")
                print("--------------------------------------")


class Player:
    def __init__(self):
        self.player_hand = []

    def deal_player(self):
        rng = np.random.default_rng()  # Create a random number generator
        self.player_hand = [rng.integers(1, 11)]  # Generate a random integer between 1 and 10 for the first card
        self.player_hand.append(rng.integers(1, 11))  # Generate a random integer between 1 and 10 for the second card
        print("Player's hand: ", self.player_hand[0], " and ", self.player_hand[1]) #Display the dealers first card
        print("Players's total: ", sum(self.player_hand), "\n")
        return self.player_hand

    def hit_player(self):
        dealer = Dealer()
        if sum(self.player_hand) <= 21:
            rng = np.random.default_rng()
            new_card = rng.integers(1, 11)
            self.player_hand.append(new_card)
            print("Player hits and draws a", new_card)
        if sum(self.player_hand) > 21:
            print("Player busts!")
            print("Game Over!")
            return
        else: 
            print("Player's total: ", sum(self.player_hand), "\n")
            dealer.reveal_hand()
        
        choice = input("Hit again or stand? ").lower()
        if choice == "h":
            print("--------------------------------------")
            return self.hit_player()

        elif choice == "s": 
                print("Player stands with a total of", sum(self.player_hand))
                print("--------------------------------------")
                return

    def win_or_lose(self):
        dealer = Dealer()
        player_total = sum(self.player_hand)
        dealer_total = sum(dealer.hand)
        if player_total > 21:
            print("Player busts! Dealer wins!")
        elif dealer_total > 21:
            print("Dealer busts! Player wins!\n")
            print_trophy()
        elif player_total > dealer_total:
            print("Player wins!\n")
            print_trophy()

        elif player_total < dealer_total:
            print("Dealer wins!")
        elif player_total == dealer_total:
            print("It's a tie!")

def game():
    dealer = Dealer()
    player = Player()

    start = input("Press Enter to deal the cards \n")
    if start == "":
        print("--------------------------------------")
        dealer.deal()
        print("--------------------------------------")
        player.deal_player()
        choice = input("Press h to hit or s to stand: ").lower()
        if choice == "h":
            print("--------------------------------------")
            player.hit_player()
            dealer.deal()
            dealer.reveal_hand()
            while sum(dealer.hand) < 17:
                dealer.hit()
                if sum(dealer.hand) >= 17:
                    player.win_or_lose()

        elif choice == "s":
            print("--------------------------------------")
            print("Player stands with a total of", sum(player.player_hand), "\n")
            print("--------------------------------------")
            dealer.reveal_hand()
            while sum(dealer.hand) < 17:
                dealer.hit()
                if sum(dealer.hand) >= 17:
                    player.win_or_lose()
            player.win_or_lose()

        else:
            print("Please enter a valid option. Bye!")
            return game()
        
    else:
        print("\n","Invalid option. Press Enter to deal the cards","\n")
        return game()

def print_trophy():
    trophy = """
       ___________
      '._==_==_=_.'
      .-\\:      /-.
     | (|:.     |) |
      '-|:.     |-'
        \\::.    /
         '::. .'
           ) (
         _.' '._
        `"""""""`
    Congratulations, you win!
    """
    print(trophy)
    print("--------------------------------------")



def main_menu() -> str:
    print("\n","Welcome to Blackjack!", "\n")
    print("a. Play Game")
    print("b. View Rules")
    print("c. View Leaderboard")    
    print("d. Exit")
    choice = input("\nPlease select an option: ").lower()

    if choice == int:
        print("\nPlease enter a valid option\n")
        return main_menu()
    return choice


def main():
    choice = main_menu()
    if choice == "a":
        print("Play Game\n")
        game()
    elif choice == "b":
        print("View Rules")
    elif choice == "c":
        print("View Leaderboard")
    elif choice == "d":
        print("Exit")
    else:
        print("\nPlease enter a valid option\n")
        return main_menu()
    

if __name__ == "__main__":
    main()
    