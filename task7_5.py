#!/usr/bin/env python3

import sys

line = input("Введіть рядок: ")
vowels = 0

for i in line:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        vowels += 1

print("У рядку ", vowels, " голосних літер")
