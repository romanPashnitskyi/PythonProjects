#! /usr/bin/env python3

import sys
import math

a = int(input("Введіть a : "))
b = int(input("Введіть b : "))
c = int(input("Введіть c : "))

D = b * b - 4 * a * c;

x1 = (-b  + math.sqrt(D)) / (2 * a)
x2 = (-b  - math.sqrt(D)) / (2 * a)

print("Корені = ", int(x2), ", ", int(x1))
