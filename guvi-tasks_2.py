import random

guess_from = 1
guess_to = 100

secret_number = random.randint(guess_from, guess_to)


while True:
    guess = int(input(f"Guess a number between {guess_from} and {guess_to}: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You got it! Congratulations!")
        break