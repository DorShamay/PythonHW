#!/usr/bin/env python

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(type(a))
val = int(input("Please insert a number"))

newlist = set(a)

def remove_values_from_list(newlist, val):
    while val in newlist:
        newlist.remove(val)

remove_values_from_list(a,val)
print(a)