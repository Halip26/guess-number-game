import random

number = random.randint(1, 99)
name = input("\nEnter your name: ")
max_attempts = int(input("Enter attempt that you want: "))
attempts = 0

while attempts < max_attempts:
    guess = int(input("Enter a number from 1 to 99: "))

    if guess < number:
        print("Your guess is low")
    elif guess > number:
        print("Your guess is high")
    else:
        print(f"Congratulations {name}! You guessed it!")
        break

    attempts += 1
    print(f"Attempts remaining: {max_attempts - attempts}")
else:
    print(f"Out of attempts, You Lost. The number was {number}")


# The simple one
"""
import random

number = random.randint(1, 99)
guess = int(input("Enter a number from 1 to 99: "))

while True:
    if guess < number:
        print("Your guess is low")
        guess = int(input("Enter a number from 1 to 99: "))
    elif guess > number:
        print("Your guess is high")
        guess = int(input("Enter a number from 1 to 99: "))
    else:
        print("Congrats, you guessed it!")
        break
        
"""
