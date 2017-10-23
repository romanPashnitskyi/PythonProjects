#!/usr/bin/env python3

import sys

def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0


def averageValue(lst):
    lenList = len(lst)
    c = sum(lst) / lenList
    return c

lst=[]
n = int(input('Кількість елементів: '))
for i in range(n):
     a = int(input('Введіть число: '))
     lst.append(a)

print('Середнє значення масиву : ', averageValue(lst))
print('Медіана масиву: ', median(lst))