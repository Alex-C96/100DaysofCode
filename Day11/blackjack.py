# Calculator Program
# Alexander Clarke
# 12/26/2021

import random
from art import logo
from time import time
# import only system from os
from os import system, name
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
seed = lambda: int(time() * 1000)

random.seed(seed())

def display_final_results(player_hand, computer_hand):

    print(f'\tYour final hand: {player_hand}, final score: {sum(player_hand)}')
    print(f'\tComputer\'s final hand: {computer_hand}, final score: {sum(computer_hand)}')

def display_results(player_hand, computer_hand):

    print(f'\tYour cards: {player_hand}, current score: {sum(player_hand)}')
    print(f'\tComputer\'s first card: {computer_hand[0]}')


def check_for_winner(player_hand, computer_hand):

    player_score = sum(player_hand)
    computer_score = sum(computer_hand)
    if computer_score == 21:
        display_final_results(player_hand, computer_hand)
        print('Lose, opponent has Blackjack 😱')
        return True
    elif player_score == 21:
        display_final_results(player_hand, computer_hand)
        print('You win with Blackjack 😁')
        return True
    elif computer_score > 21:
        display_final_results(player_hand, computer_hand)
        print('Opponent went over. You win 😁')
        return True
    elif player_score > 21:
        display_final_results(player_hand, computer_hand)
        print('You went over. You lose 😤')
        return True
    else:
        return False

def check_for_ace_loss(player_hand, computer_hand):
    if sum(player_hand) > 21 and 11 in player_hand:
        pos = player_hand.index(11)
        player_hand.insert(pos, 1)
        player_hand.remove(11)
        print('Ace is now 1')
    if sum(computer_hand) > 21 and 11 in computer_hand:
        computer_hand.remove(11)
        computer_hand.append(1)
    
def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # clear screen and start game
    clear()
    print(logo)
    player_hand = []
    computer_hand = []
    game_over = False
    # Deal cards
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    # Check for winner off the draw
    display_results(player_hand, computer_hand)
    game_over = check_for_winner(player_hand, computer_hand)
    if game_over:
        return # start over

    # Player plays their hand
    hit_me = True
    while hit_me:
        deal_me_another = input("Type 'y' to get another card, type 'n' to pass: ")
        if deal_me_another == 'y':
            player_hand.append(random.choice(cards))
            check_for_ace_loss(player_hand, computer_hand)
            game_over = check_for_winner(player_hand, computer_hand) 
            if game_over:
                return
            display_results(player_hand, computer_hand)
        else:
            hit_me = False
    
    # Computer plays their hand
    while sum(computer_hand) < 17:
        computer_hand.append(random.choice(cards))
        check_for_ace_loss(player_hand, computer_hand)
        game_over = check_for_winner(player_hand, computer_hand)
        if game_over:
            return # start over
    
    display_final_results(player_hand, computer_hand)
    if sum(player_hand) > sum(computer_hand):
        print('You win 😁')
    elif sum(player_hand) == sum(computer_hand):
        print('It\'s a draw')
    else:
        print('You lose 😤')
        

keep_playing = True
while keep_playing:
    user_input = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if user_input == 'n':
        print('Game Over')
        keep_playing = False
    else:
        blackjack()