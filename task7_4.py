#!/usr/bin/env python3

import sys
import string

def myFunc(word):
    abc  = 'abcdefghijklmonpqrstuvwxyza'
    ab_st = list(abc)
    new_word = []
    for letter in list(word.lower().strip()):
        new_word.append(ab_st[abc.index(letter) + 1])
    new_word = "".join(new_word)
    return new_word

line = input("Введіть рядок: ")
print("Результат : ", myFunc(line))
