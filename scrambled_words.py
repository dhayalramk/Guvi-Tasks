import random


words = ['python', 'java', 'javascript', 'guvi', 'automation', 'selinium', 'pytest']

word = random.choice(words)

scrambled_words = ' '.join(random.sample(words, len(words)))

print("Scrambled words:", scrambled_words)

attempt = 0
while True:
    attempt += 1
    guess = input(f"Attempt number: {attempt}, Guess a word: ").lower()
    if guess == word:
        print("You got it! Congratulations!")
        break
    print("Sorry, that's wrong. Try again.\n")
