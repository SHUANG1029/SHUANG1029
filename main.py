import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
NUMBER = random.randint(1, 100)
# This line is for testing
# print(f"The guessing number in mind is {NUMBER}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempt = 10
else:
    attempt = 5


def compare(guess_number):
    if guess_number > NUMBER:
        print("Too high.")
        return attempt - 1
    elif guess_number < NUMBER:
        print("Too low.")
        return attempt - 1


should_continue = True

while should_continue:
    print(f"You have {attempt} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    attempt = compare(user_guess)
    if user_guess != NUMBER:
        if attempt != 0:
            print("Guess again.")
    else:
        should_continue = False
        print(f"You got it! The answer was {NUMBER}.")
    if attempt == 0:
        print(f"You've run out of guesses. You lose")
        should_continue = False
