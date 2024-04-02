import random

secretNumber = random.randint(0, 30)

guess = int(input("I'm thinking of a number between 0 and 30. What's the number: "))

while (guess != secretNumber):
    if (guess > secretNumber):
        print("You're guess is too large")
    elif (guess < secretNumber):
        guess = print("Guess is smaller than my number")
    guess = int(input("Guess again: "))
    

print(f"You're right! {guess} is my secret number")