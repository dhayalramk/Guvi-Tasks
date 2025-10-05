secret_number = 7

while True:
    guess = input("Enter your guess: ")
    guess = int(guess)

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You got it! Congratulations!")
        break