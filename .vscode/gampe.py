import random
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
guess = int(input())
while guess != number:
    if guess < number:
        print("Sorry, your guess is too low. Try again.")
    else:
        print("Sorry, your guess is too high. Try again.")
    guess = int(input())
print("Congratulations! You guessed the number!")