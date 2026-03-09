#Program Title : Interactive Guessing Game: Develop a number guessing game where the program generates a random number, and the user has to guess it. Implement loops and conditional statements for user interaction.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 26/02/2026       DOS : 05/03/2026

import random
number = random.randint(1, 100)
guess = 0
print("Guess the number between 1 and 100")

while guess != number:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")