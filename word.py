#I added for creativity a max limit of guess attempts for the user!
import turtle

print("Welcome to the word guessing game!\n")

def choose_word():
    secret = 'turtle'
    return secret

def generate_initial_hint(secret):
    return ''.join(['_' for _ in secret])

def display_hint(hint):
    print(f"Hint: {hint}")

def guess_word(secret):
    guess_count = 0
    max_attempts = 3

    initial_hint = "This animal lives on the land or sea."
    display_hint(initial_hint)

    hint = generate_initial_hint(secret)
    display_hint(hint)

    while guess_count < max_attempts:
        user_guess = input("What is your guess?").lower()

        if len(user_guess) != len(secret):
            print("Invalid guess length. Try again.")
            continue

        guess_count += 1

        new_hint = ""
        for i in range(len(secret)):
            secret_char = secret[i]
            guess_char = user_guess[i]

            if guess_char == secret_char:
                new_hint += guess_char.upper()
            elif guess_char in secret:
                if guess_char != secret[i]:
                    new_hint += guess_char.lower()
                else:
                    new_hint += guess_char.upper()
            else:
                new_hint += hint[i]

        hint = new_hint
        display_hint(hint)

        if user_guess == secret:
            print(f"Your guess was correct! You guessed in {guess_count} guesses!")
            return

    print(f"Sorry, you've reached the maximum number of attempts. The correct word was not revealed.")

secret_word = choose_word()
guess_word(secret_word)
