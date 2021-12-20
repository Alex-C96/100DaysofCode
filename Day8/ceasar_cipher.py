from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    shift_amount %= 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position < 0:
                new_position += len(alphabet)
            elif new_position >= len(alphabet):
                new_position -=  len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {direction}d result: {end_text}")
        


print(logo)
continue_game = True
while(continue_game):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    play_again = input("please input 'yes' if you would like to go again. Otherwise type 'no'.\n")
    if play_again != 'yes':
        continue_game = False
print("Goodbye")
    