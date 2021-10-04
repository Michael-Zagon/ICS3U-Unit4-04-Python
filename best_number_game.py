#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Oct 2021
# This program is the best number guessing game

import random


def main():
    # This function is the best number guessing game

    random_number = random.randint(0, 10)

    # Input, Process and Output
    while True:
        guessed_number = input("Pick a number between 0-10: ")
        print("")

        try:
            integer_guess = int(guessed_number)
            if integer_guess == random_number:
                print("You guessed correctly!")
                break
            elif integer_guess > random_number:
                print("You guessed too high, try again.")
            else:
                print("You guessed too low, try again")

        except Exception:
            print("This is an invalid input")
            break

    print("\nDone.")


if __name__ == "__main__":
    main()
