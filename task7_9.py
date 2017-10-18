#!/usr/bin/env python3

import sys

a=list(map(int, input("Введіть номер квитка: ")))
if len(a) % 2 == 1:
    c = sum(a[:len(a)//2])==sum(a[(len(a)//2) + 1:])
    print("Результат: ", c)
elif sum(a[:len(a)//2])==sum(a[len(a)//2:]):
    print("Результат: ", True)
else:
    print("Результат: ", False)
