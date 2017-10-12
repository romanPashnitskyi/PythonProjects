#! /usr/bin/env python3

import sys
import math

def fun(sumUAH, procStav, timeDep):
	summa = sumUAH * math.pow((1 + (procStav / 100)), timeDep)
	return summa

sumUAH = int(input("Введіть наявну суму: "))
procStav = float(input("Річна процентна ставка: "))
timeDep = int(input("Тривалість депозиту в роках: "))
print("Сума на момент завершення депозитної ставки: ", round(fun(sumUAH, procStav, timeDep), 2))

