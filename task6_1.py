#! /usr/bin/env python3

import sys
import math
a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))

pivPer = (a + b + c) / 2
S = float(math.sqrt(pivPer * (pivPer - a) * (pivPer - b) * (pivPer - c)))
print("Площа трикутника = ", round(S,3))
