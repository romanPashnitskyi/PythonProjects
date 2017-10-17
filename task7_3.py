#!/usr/bin/env python3

import sys


def func(line):
    myList = []

    for i in line:
        if i == "[" or i == "]" or i == "(" or i == ")" or i == "{" or i == "}" or i == "<" or i == ">":
            myList.append(i)


    if len(myList) == 0:
        return True

    elif myList.count("[") == myList.count("]") and myList.count("(") == myList.count(
            ")") and myList.count("{") == myList.count("}") and myList.count(
            "<") == myList.count(">"):

        j = 0
        try:
            while j != range(len(myList)):
                if myList[j] == "(" and myList[j + 1] == ")":
                    myList.pop(j)
                    myList.pop(j)
                    j = 0
                elif myList[j] == "{" and myList[j + 1] == "}":
                    myList.pop(j)
                    myList.pop(j)
                    j = 0
                elif myList[j] == "[" and myList[j + 1] == "]":
                    myList.pop(j)
                    myList.pop(j)
                    j = 0
                elif myList[j] == "<" and myList[j + 1] == ">":
                    myList.pop(j)
                    myList.pop(j)
                    j = 0
                else:
                    j += 1

        except:
            if (len(myList)) == 0:
                return True
            else:
                return False

    else:
        return False

line = input("Enter string : ")
print("Result : ", func(line))