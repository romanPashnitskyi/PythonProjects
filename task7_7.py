#!/usr/bin/env python3

import sys
import string
import re

def snake2camel(name):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), name)

def camel2snake(name):
    first_cap_re = re.compile('(.)([A-Z][a-z]+)')
    all_cap_re = re.compile('([a-z0-9])([A-Z])')
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()

choice = int(input("1 = конвертувати на snakeCase : \n2 = конвертувати на camel_case: \nВаш вибір: "))

if choice == 1:
    line1 = input("Введіть рядок: ")
    print("Результат: ", snake2camel(line1))
elif choice == 2:
    line2 = input("Введіть рядок: ")
    print("Результат: ", camel2snake(line2))
