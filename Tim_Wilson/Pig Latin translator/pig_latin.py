#! /usr/bin/env python3

VOWEL = ('a', 'e', 'i', 'o', 'u', 'y')
CONSONENT = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')

def find_upto_vowel(string):
    idx= 0
    for c in string:
        if c.lower() in VOWEL:
            break
        else:
            idx += 1 
    if idx > 0:
        return(string[:idx])
    else:
        return('')


