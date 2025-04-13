# Initialize num to 0
# Initialize guess to 0
# num = random number
# Loop endlessly
# Prompt the user to enter the guess number
# Check if num = guess
# If yes: display "Congratulations. You've got it right" Break loop
# If no: display "That was close. Try again" Next iteration

import random

num = 0
guess = 0

num = random.randint(0, 15)

loop = True
while loop:
    try:
        guess = int(input("Guess the number: "))

    # Handle Casting error
    except ValueError:
        print("Integers only, pleease.")
        loop = True
    else:
        if guess == num:
            loop = False
            print(f"Congratulations. You've got it right! The number was {guess}")
        else:
            loop = True
            print("That was close. Try again")
