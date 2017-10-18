#!/usr/bin/env python3

import sys

line = input("Введіть кілька слів: ")
l = line.split()
ln = len(l)
for i in range(ln - 1):
    for j in range(ln - 1 - i):
        if len(l[j]) > len(l[j + 1]):
            l[j], l[j + 1] = l[j + 1], l[j]

line = ''
for i in range(ln):
    line += l[i] + ' '
print("Результат: ", line)

