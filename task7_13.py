#!/usr/bin/env python3

import sys

line1 = input("Введіть перший рядок: ")
line2 = input("Введіть другий рядок: ")

index = ''

for i in line1:
    if line2.count(i) == True:
        index += i

print(index)


if index != '':
    print("Другий рядок можна утворити з таких символів : ", index)
else:
    print("Неможна утворити другий рядок із символів першого рядка!")


