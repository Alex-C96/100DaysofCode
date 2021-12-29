from art import logo
import random

random.seed()

the_number = random.randint(1, 100)

print(logo, '\n')

continue_playing = True

print('Welcome to the Number Guessing Game!')

while(continue_playing):
    print('I\'m thinking of a number between 1 and 100.')

    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if (game_mode == 'hard'):
        number_of_guesses = 5
    else:
        number_of_guesses = 10

    print(f"You have {number_of_guesses} attempts remaining to guess the number.")

    while(number_of_guesses > 0):
        guess = int(input('Make a guess: '))
        if guess > the_number:
            print('Too high.')
            print('Guess again')
            number_of_guesses -= 1
            print(f'You have {number_of_guesses} attempts remaining to guess the number.')
        elif guess < the_number:
            print('Too low.')
            print('Guess again.')
            number_of_guesses -= 1
            print(f'You have {number_of_guesses} attempts remaining to guess the number.')
        else:
            print(f'You got it! The answer was {the_number}')
            input = input("Would you like to play again? type 'y' or 'n'")
            if input != 'y':
                continue_playing = False
            break
        if number_of_guesses == 0:
            print('You\'ve run out of guesses, you lose.')
            input = input("Would you like to play again? type 'y' or 'n'")
            if input != 'y':
                continue_playing = False


