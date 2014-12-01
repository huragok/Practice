#! /usr/bin/env python3

import random

def get_RPS(msg):
    while True:
        try:
            x = input(msg)
            if x.lower() not in ('r', 'p', 's'):
                raise ValueError("Input must be R(r), P(p), S(s)")
            return x.lower()
        except ValueError as err:
            print(err)

def get_points(msg):
    while True:
        try:
            x = int(input(msg))
            if x < 0:
                raise ValueError("Points to win must be positive")
            return x
        except ValueError as err:
            print(err)

class RPS:
    
    INDEX = {'r': 0, 'p': 1, 's': 2}
    FULL_NAME = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    MSG_RESULT = ['Computer wins!', 'Human wins!', 'A draw']

    def __init__(self, points_win):
        self.points_win = points_win
        self.points_human = 0
        self.points_computer = 0
 
    def run(self):
        while self.points_human < self.points_win and self.points_computer < self.points_win:
            if self.points_human + self.points_computer > 0:
                print("\nScore: Human {0}    Computer {1}".format(self.points_human, self.points_computer))
            choice_human = get_RPS("Choose (R)ock (P)aper, or (S)cissors? ")
            choice_computer = random.choice(('r', 'p', 's'))
            
            if (self.INDEX[choice_human] - self.INDEX[choice_computer]) % 3 == 1: # Human wins
                i_MSG = 1
                self.points_human += 1
            elif (self.INDEX[choice_human] - self.INDEX[choice_computer]) % 3 == 2: # Computer wins
                i_MSG = 0
                self.points_computer += 1
            else: # A draw
                i_MSG = 2
            
            print("\nHuman: {0}    Computer: {1}     {2}".format(self.FULL_NAME[choice_human], self.FULL_NAME[choice_computer], self.MSG_RESULT[i_MSG]))

        print("\nFinal Score: Human {0}    Computer {1}".format(self.points_human, self.points_computer))

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!\n")
    rps = RPS(get_points("How many points are required for a win? "))
    rps.run()
