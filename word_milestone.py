import turtle

print("Welcome to the word guessing game!\n")

def choose_word():
    secret = 'turtle'
    return secret

def generate_initial_hint(secret):
    return '_' * len(secret)

def display_hint(hint):
    print(f'Current Hint: {hint}')

def guess_word(secret):
    guess_count = 0

    while True:

        user_guess = input("What is your guess?").lower()
        guess_count += 1
        if user_guess == secret:
            print(f"Your guess was correct! You guessed in {guess_count} guesses!")
            return
        else:
            print('Your guess was incorrect. Try Again!')
        

secret_word = choose_word()
guess_word(secret_word)
        
