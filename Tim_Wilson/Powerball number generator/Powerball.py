#! /usr/bin/env python3

import random

class Powerball:
    def __init__(self, n_set):
        self.drum_1 = Drum(53, 5)
        self.drum_2 = Drum(42, 1)
        self.n_set = n_set

    def run(self):
        for i_set in range(self.n_set):
            numbers_drawn = self.drum_1.draw() + self.drum_2.draw()
            numbers = [n + 1 for n in numbers_drawn]
            print("Your numbers: {0:>2} {1:>2} {2:>2} {3:>2} {4:>2}     Powerball: {5:>2}".format(*numbers))


class Drum:
    def __init__(self, n_balls, n_draw):
        self.n_balls = n_balls
        self.n_draw = n_draw

    def draw(self):
        numbers_drawn = []
        numbers_left = list(range(self.n_balls))
        for i_draw in range(self.n_draw):
            numbers_drawn.append(numbers_left.pop(random.choice(list(range(self.n_balls - i_draw)))))
        return numbers_drawn

def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            if x < 0:
                raise ValueError("Must be positive!")
            return x
        except ValueError as err:
            print(err)

def main():
    print("Official (but fruitless) Powerball number generator\n")
    powerball = Powerball(get_int("How many sets of numbers? "))
    print("")
    powerball.run()
        
if __name__ == "__main__":
    main()
