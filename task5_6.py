#! /usr/bin/env python3

import sys

a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))

if a + b > c and a + c > b and b + c > a:
	print("Трикутник існує")
else: 
	print("Трикутник неіснує")
