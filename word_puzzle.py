def choose_word():
    word = "turtle"
    return word

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def word_guessing_game():
    guessed_letters = []
    secret_word = choose_word()

print("Welcome to the word guessing game!\n")

guess = input(f"\n")
