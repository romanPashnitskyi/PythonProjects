#! /usr/bin/env python3
import sys
import math 

print("Введіть два невід'ємних дійсних числа: ")
num1 = float(input())
num2 = float(input())
suma = ((math.sqrt(float(num1 * num2))) / (math.exp(num1) * num2)) + (num1 * math.exp((2 * num1) / num2))
print("Результат: ", suma)


