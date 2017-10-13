#! /usr/bin/env python3

import sys
import math

def fun(sumNayavna, sumPotr, procStav):
	countDay = 0
	while sumNayavna < sumPotr:
		countDay = countDay + 1
		sumNayavna = sumNayavna + (sumNayavna * procStav / 100)
	return countDay

sumNayavna = int(input("Введіть наявну суму: "))
sumPotr = int(input("Введіть потрібну суму: "))
procStav = float(input("Річна процентна ставка: "))

print("Кількість років необхідних для зростання депозиту до потрібної суми = ", fun(sumNayavna, sumPotr, procStav))
