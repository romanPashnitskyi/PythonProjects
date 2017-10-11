#! /usr/bin/env python3
import sys

width = input("Введіть ширину дверей : ")
height = input("Введіть висоту дверей: ")

widthBox = input("Введіть ширину коробки : ")
heightBox = input("Введіть висоту коробки : ")
lengthBox = input("Ведіть довжину коробки : ")

if heightBox <= height:
	if widthBox <= width:
		print("Коробка проходить")
	elif lengthBox <= width:
		print("Коробка проходить")
	else:
		print("Коробка не проходить")

elif widthBox <= height:
	if heightBox <= width:
		print("Коробка проходить")
	if lengthBox <= width:
		print("Коробка проходить")
	else: 
		print("Коробка не проходить")

elif lengthBox <= height:
	if heightBox  <= width:
		print("Коробка проходить")
	if widthBox <= width:
		print("Коробка проходить")
	else:
		print("Коробка не проходить")

else:
	print("Коробка не проходить")
	
