#!/usr/bin/env python36

###################################
#
#
###################################


num = int(input("Please enter an integer "))
num1 = int(input("Please enter another integer"))
# =
if num % 2 == 0:
    print("You picked an even number.")
else:
    print("You picked an odd number.")

if num % 4 == 0:
    print ("You picked an multiplication of 4 ")
else:
    print ("Your number isnt multiplication of 4 ")

if num % num1 == 0:
    print ("Your number", num ,"can be divide with" ,num1)
else:
    print ("Your number isn't dividing by " )