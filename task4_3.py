#! /usr/bin/env python3
import sys
import decimal

number = input("Введіть місячний дохід працівника : ")
dohFiz = decimal.Decimal(number) * decimal.Decimal(18) / decimal.Decimal(100)
warZbir = decimal.Decimal(number) * decimal.Decimal(1.5) / decimal.Decimal(100)
print("Сума податків : ", float(dohFiz) + float(warZbir))

