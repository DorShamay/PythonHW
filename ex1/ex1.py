#!/bin/usr/env python
#Creator : DorShamay
#Version : 0.0.1

def vars():
    x = int(input("Enter an integer: "))
    return x

def SUM(x,y):
    sum = x+y
    print('The sum of ', x, ' and ', y, ' is ', sum, '')

def Multyiply(x,y):
    multiply = x * y
    print('The mutliplication of ', x, ' and ', y, ' is ', multiply, '')

def Module(x,y):
    module = x / y
    print('The module of ', x, ' and ', y, ' is ', module, '')

def vars1():
    y = int(input("Enter another integer: "))
    return y
x=vars()
y=vars1()
SUM(x,y)
Multyiply(x,y)
Module(x,y)