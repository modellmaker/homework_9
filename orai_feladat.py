import random
secret = 0
lives = 0
interval = 0

name = input("Please add your name: ")
print("Welcome, " + name.title() + "!")
level = input("Choose level (Easy, Medium, Hard): ")
level = level.lower()

if level == "easy":
    lives = 20
    interval = 5
elif level == "medium":
    lives = 10
    interval = 15
elif level == "hard":
    lives = 5
    interval = 30
else:
    print("You didn't provide a suitable level.")

secret = random.randint(1, interval)

for i in reversed(range(lives)):
    guess = int(input("You have " + str(i+1) + " guesses. Guess The number: "))
    if guess != secret:
        print("Sorry, try again!")
    else:
        print("You've guessed it! The secret number was " + str(secret) + "!")
        break
