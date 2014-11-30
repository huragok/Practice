#! /usr/bin/env python3

import random

def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            if x < 1 or x > 100:
                raise ValueError("You need to guess a number between 1 and 100!")
            return x
        except ValueError as err:
            print(err)

class Guessing_game:

    def __init__(self):
        self.right_number = random.randint(1, 100)
        self.last_guess = None
        self.count_guess = 0
        print("Time to play a guessing game.\n")
        
    def run(self):
        while self.last_guess != self.right_number:
            if self.count_guess == 0:
                self.last_guess = get_int("Enter a number between 1 and 100: ")
            elif self.last_guess > self.right_number:
                self.last_guess = get_int("Too high. Try again: ")
            else:
                self.last_guess = get_int("Too low. Try again: ") 
            self.count_guess += 1
       
        print("\nCongratulations! You got it in {0} guesses".format(self.count_guess))

if __name__ == "__main__":
    Guessing_game().run()
