#! /usr/bin/env python3

import string

VOWEL = ('a', 'e', 'i', 'o', 'u', 'y')
CONSONENT = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
def process_word(word):
    
    flag_init_capital = False
    if word != '':
        flag_init_capital = word[0].isupper()
    else:
        return ''

    idx = 0
    for c in word:
        if c.lower() in VOWEL:
            break
        else:
            idx += 1 
    if idx < len(word):
        word_tmp = word[idx:] + word[:idx] + 'ay'
    else:
        word_tmp = word + 'yay'

    if flag_init_capital:
        word_tmp = word_tmp.capitalize()

    return word_tmp

def process_line(line):
    line_processed = ''
    word = ''
    for c in line:
        if c in string.punctuation + ' ' + string.digits:
            line_processed += (process_word(word) + c)
            word = ''
        else:
            word += c
    line_processed += process_word(word)
    return line_processed

def main():
     while True:
         line = input("--> ")
         print(process_line(line))

if __name__ == '__main__':
    main()
