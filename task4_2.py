#! /usr/bin/env python3
import sys
import math 

print("Введіть три дійсних числа: ")
num1 = float(input())
num2 = float(input())
num3 = float(input())
suma = (1 / (num3 * math.sqrt(2 * math.pi))) * math.exp((-(num1 - num2)**2) / 2 * num3**3) 
print("Результат: ", suma)


