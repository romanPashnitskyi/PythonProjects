#!/usr/bin/env python3

import sys

for i in range(1,101):
	if i % 3 == 0 and not i % 5 == 0:
		print ("%d Fizz" % i)
	elif i % 5 == 0 and not i % 3 == 0:
		print ("%d Buzz" % i)
	elif i % 3 == 0 and i % 5 == 0:
		print ("%d FizzBuzz" % i)
	else:
		print (i)
