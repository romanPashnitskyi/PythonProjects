#! /usr/bin/env python3
import sys

weight = input("Введіть Вашу вагу в кг: ")
height = input("Введіть Ваш зріст в метрах : ")

weight = float(weight)
height = float(height)

print('Індекс Маси Тіла - ', + weight / height** 2)
