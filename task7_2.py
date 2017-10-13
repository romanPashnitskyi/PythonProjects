#! /usr/bin/env python3

import sys

def func(line):
	newLine = line.lower()
	b = newLine.replace('%','').replace('$','').replace('@','').replace('*','').replace('.','').replace('!','').replace('&','').replace(',','').replace('?','').replace(' ','').replace('#','').replace('_','').replace('-','').replace('{','').replace('}','').replace('>','').replace('<','').replace('/','').replace('+','').replace('[','').replace(']','').replace('(','').replace(')','').replace('=','').replace(';','').replace(':','').replace("'",'')
	a = b[::-1]
	if b == a:
  		print(True)	
	else:
  		print(False)

line = input("Введіть слово або фразу : ")
func(line)
