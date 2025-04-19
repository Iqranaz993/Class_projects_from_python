import random

# Welcome messages
print("Welcome to the Number Guessing Game!")
print("Guess a number between 50 and 100.")
print("You have 5 attempts.")
print("Let's start!")

# Random number to guess
number_to_guess = random.randrange(50, 101)
max_attempts = 5
attempts_taken = 0

# Main game loop
while attempts_taken < max_attempts:
    attempts_taken += 1
    try:
        user_guess = int(input("Please enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        attempts_taken -= 1  # Don't count invalid inputs
        continue

    if user_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you found it right!! in the {attempts_taken} attempt(s).")
        break
    elif user_guess > number_to_guess:
        print("Your guess is too high, try again!")
    else:
        print("Your guess is too low, try again!")

# If loop ends without correct guess
if user_guess != number_to_guess:
    print(f"Oops, sorry! The number was {number_to_guess}. Better luck next time!")
