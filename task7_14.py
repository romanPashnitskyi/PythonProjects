#!/usr/bin/env python3

import sys

import re

import re
def validate(email):
    match=re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$",email)
    if match:
        return 'Valid email.'
    else:
        return 'Invalid email.'

line = input("Enter the mail address: ")
print(validate(line))