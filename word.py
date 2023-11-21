#I made the error message like a fun AI voice that tells you to do better!
import turtle

print('Welcome to the Word game!\n')

def choose_word():
    word = "turtle"
    no_letters = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 's', 'v', 'w', 'x', 'y', 'z']
    letters = ['t', 'u', 'r', 'l', 'e']
    return word, no_letters, letters

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def guess_word(word, no_letters, letters):
    guessed_letters = []
    guess_count = 0
    
    while True:
        guessed_letter = input("What is your next letter? ").lower()
        
        if guessed_letter in no_letters:
            print("You thought it was that easy?! Try again!")
            continue
        
        guessed_letters.append(guessed_letter)
        guess_count += 1

        current_display = display_word(word, guessed_letters)

        print(f"Current status: {current_display}")

        if set(letters).issubset(set(guessed_letters)):
            print(f"Congratulations! You guessed the word in {guess_count} guesses!")
            break

word, no_letters, letters = choose_word()
guess_word(word, no_letters, letters)
