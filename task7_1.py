#! /usr/bin/env python3

import sys
import math

def func(length, number):
	if number > partLength or -number > partLength:
		print("Число перевищує половину довжини рядка")
	else:
		if number > 0:
			positive = line[number:len(line)] + line[0:number]
			print("Результат обертання додатнього числа : ", positive)
		elif number < 0:
			negative = line[number:] + line[0:number]
			print("Результат обертання від'ємного число : ", negative)


line = input("Введіть рядок : ")
number = int(input("Введіть число на яке здійснюється обертання : "))

length = len(line)
partLength = length / 2

func(length, number)



