#!/usr/bin/env python3

import sys
import collections

def f(seq, n):
    assert n > 0

    dq = collections.deque(seq)
    r = n - 1

    while len(dq) > 1:
        dq.rotate(-r)
        dq.popleft()

    return list(dq)

myPeople = int(input("Введіть кількість людей: "))
step = int(input("Введіть крок: "))
print("Самогубець під номером : ", f(range(1, myPeople + 1), step))
