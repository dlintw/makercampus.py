#!/usr/bin/python3
# generate by walle2, can not run
import random
number_to_guess = random.randint(1, 100)
print("Welcome to the guess the number game!")
while True:
 guess = int(input("Please enter your guess (between 1 and 100): "))
 if guess < number_to_guess:
 print("Too low! Try again.")
 elif guess > number_to_guess:
 print("Too high! Try again.")
 else:
 print("Congratulations! You guessed the number correctly!")
 break
