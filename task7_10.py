#!/usr/bin/env python3

import sys

def func(string):
    minlen = 100
    for x in string.split(' '):
        if minlen > len(x):
            minlen = len(x)
            word = x
    print(string + '\nНайкоротше слово - ', word, ',', minlen, ' символів')


func(input('Введіть рядок: '))