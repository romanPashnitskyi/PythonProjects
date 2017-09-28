#! /usr/bin/env python3
import sys
import random


hodkompa = random.randint(1,3);
temp = input("Натисніть для вибору :\n1 - камінь\n2 - папір\n3 - ножиці\n")
hodusera = int(temp)
if hodusera < 0 and hodusera > 3:
	print("Значення введено не вірно")

if hodkompa == hodusera:
	print("Нічия!")
elif hodkompa == 3 and hodusera == 1:
	print("Ви перемогли")
elif hodkompa == 1 and hodusera == 2:
	print("Ви перемогли")
elif hodkompa == 2 and hodusera == 3:
	print("Ви перемогли")
elif hodkompa == 2 and hodusera == 1:
	print("Комп переміг")
elif hodkompa == 3 and hodusera == 2:
	print("Комп переміг")
elif hodkompa == 1 and hodusera == 3:
	print("Комп переміг")



