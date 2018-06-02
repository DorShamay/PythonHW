#!/bin/usr/env python

#Creator : DorShamay
#Version : 0.0.1

def vars():
    x = int(input("Enter an integer: "))
    return x

def vars1():
    y = str(input("Enter a String"))
    return y

def vars2():
    z = str(input("Enter a second String"))
    return z

def CompareStr(y,z):
    if len(z) > len(y):
        print(len(z))
        print(z)
    else:
        print(len(y))
        print(y)



x=vars()
y=vars1()
z=vars2()
CompareStr(y,z)