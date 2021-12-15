#Step 2

import random

import hangman_art as art
import hangman_words as words

chosen_word = random.choice(words.word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

lives = len(art.stages) - 1
end_of_game = False

print(art.logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"{guess} has already been guessed.")

    # adds correct letters to display list
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # checks if user guessed wrong
    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        lives -= 1
        if lives == 0:
            print("Game over, You lose.")
            end_of_game = True
        

    print(' '.join(display))
 
    # checks if player wins
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(art.stages[lives])