#! /usr/bin/env python3

import sys

print("Введіть число: ")
string = input()
n = int(string)

def IsPrime(n):
	if n == 1:
		return False
	elif n != 1: 		
   		d = 2
   		while n % d != 0:
       			d += 1
   		return d == n
if IsPrime(n) == False:
	print("Число не є простим")
else:
	print("Число є простим")
