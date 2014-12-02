#! /usr/bin/env python3

import random
import string

LIB_WORD = ('Jurai', 'Tomoyo', 'Hatoko', 'Sayumi', 'Chifuyu', 'Mirei')

class Hangman:
  
    STRING_HANGMAN = ("", " O ", " O \n | ", " O \n\\|", " O \n\\|/", " O \n\\|/\n | ", " O \n\\|/\n | \n/", " O \n\\|/\n | \n/ \\")

    def __init__(self):
        self.word = random.choice(LIB_WORD).upper()
        self.hit = []
        for c in self.word:
            self.hit += [False]
        self.incorrect_guess = 0
        self.guessed_letters = []

    def get_letter(self):
        while True:
            try:
                x = input('Pick a letter --> ').upper()
                if len(x) > 1:
                    raise ValueError("\'{0}\' has more than one letter.".format(x))
                elif x not in string.ascii_uppercase:
                    raise ValueError("\'{0}\' is not a valid letter.".format(x))
                elif x in self.guessed_letters:
                    raise ValueError("Sorry, you already guessed \'{0}\'".format(x))
                return x
            except ValueError as err:
                print(err)

    def print_word(self):
        word = ""
        for i in range(len(self.word)):
            if self.hit[i]:
                word += self.word[i]
            else:
                word += '_'
        print(word)

    def print_guessed(self):
        print("Guessed letters: " + " ".join(self.guessed_letters))

    def print_hangman(self):
        print(self.STRING_HANGMAN[self.incorrect_guess])

    def run(self):
        print("Welcome to hangman. You get seven chances to guess the mystery word.")
        while self.incorrect_guess < 7 and not all(self.hit):
            self.print_word()
            letter = self.get_letter()
            self.guessed_letters += [letter]
            if letter in self.word:
                for (i, x) in enumerate(self.word):
                    if x == letter:
                        self.hit[i] = True
            else:
                self.incorrect_guess += 1

            self.print_guessed()
            print("")
            self.print_hangman()

        if self.incorrect_guess == 7:
            self.print_word()
            print("\nSo sorry. You struck out.\nThe mystery word was \'{0}\'".format(self.word))
        else:
            self.print_word()
            print("Congratulations!")

if __name__ == "__main__":
    Hangman().run()
