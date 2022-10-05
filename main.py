from random import randint

# Todo check against all the users guesses and only allow uniq inputs


def get_user_input():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: (1 - 100) "))
            if 1 > guess or guess > 99:
                print("Sorry, your number is out of bounds")
            else:
                return guess
        except():
            print("Illegal input! You are lucky I'm looking out for you.")


def continue_playing():
    user_choice = input("Would you like to play? (y/n) ")
    return user_choice.lower() == "y"


print("""
Welcome to the guessing game!
I am your host: a smart computer that is totally not cheating :D
You have ten tries to guess my super secret number.
You can only guess whole numbers without "."'s or I will burn your computer lol

Good luck~!
""")

while continue_playing():
    target_number = randint(1, 99)
    tried_guesses = []
    remaining_guesses = 10
    while remaining_guesses > 0:
        print("\n")
        print(f"You have tried these numbers! Hope it helps because I'm going to win ;]\n{tried_guesses}")
        print(f"Btw! You have {remaining_guesses} remaining attempts :P")
        user_guess = get_user_input()
        tried_guesses.append(user_guess)
        if user_guess == target_number:
            print(f"Wow! you guessed right!\nMy secret number was: {target_number}.\nYou win!")
            break
        elif user_guess > target_number:
            print(f"{user_guess} is much higher than my secret number!")
        else:
            print(f"{user_guess} is much lower than my secret number!")
        remaining_guesses -= 1
    last_guess = tried_guesses.pop()
    print(f"Your last guess was {last_guess}\n")
    if last_guess == target_number:
        print("Wow, that is my secret number! You win!")
    else:
        print(f"Nope! My secret number was {target_number}! I win!")

print("Thanks for hanging out with me!")
