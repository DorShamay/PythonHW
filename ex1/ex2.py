#!/bin/usr/env python

#Creator : DorShamay
#Version : 0.0.1

def vars():
    x = int(input("Enter an integer: "))
    if 1 <= x <= 3:
        pass
        print('Thanks')
    else:
        print('Please enter a valid integer')
        vars()

def vars1():
    y = str(input("Enter a String"))
    return y

def vars2():
    z = str(input("Enter a second String"))
    return z

def CompareStr(y,z):
    if len(z) > len(y):
        print(z, 'Contains more letters than', y)
    elif len(y) > len(z):
        print(y, 'Contains more letters than', z)
    else:
        len(y) == len(z)
        print(y, 'Contains same amount of letters', z)

def CompareStr1(y,z):
    if y in z:
        print(y, 'is inside' ,z )
    elif z in y:
        print(z, 'is inside' ,y )
    else:
        print(z, 'not inside at all', y)


x=vars()
y=vars1()
z=vars2()
CompareStr(y,z)
CompareStr1(y,z)