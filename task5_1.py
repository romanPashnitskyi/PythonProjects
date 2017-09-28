#! /usr/bin/env python3
import sys

number = input("Введіть додатнє ціле число : ")
conversetoInt = int(number)
temp = (conversetoInt & (conversetoInt - 1)) == 0
if temp == True :
	print("Число є степенем двійки")
elif temp == False :
	print("Число не є степенем двійки")
