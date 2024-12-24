import random

number = random.randint(1, 99)
name = input("Enter your name: ")
max_attempts = int(input("Enter attempt that you want: "))
attempts = 0

while attempts < max_attempts:
    guess = int(input("Enter a number from 1 to 99: "))

    if guess < number:
        print("Guess is low")
    elif guess > number:
        print("Guess is high")
    else:
        print(f"Congratulations {name}! You guessed it!")
        break

    attempts += 1
    print(f"Attempts remaining: {max_attempts - attempts}\n")
else:
    print(f"Out of attempts, You Lost. The number was {number}")


# The simple one
"""
import random

number = random.randint(1, 99)
guess = int(input("Enter a number from 1 to 99: "))

while True:
    if guess < number:
        print("Guess is low")
        guess = int(input("Enter a number from 1 to 99: "))
    elif guess > number:
        print("Guess is high")
        guess = int(input("Enter a number from 1 to 99: "))
    else:
        print("Congrats, you guessed it!")
        break
        
"""
