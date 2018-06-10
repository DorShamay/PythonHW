#!/bin/usr/env python36



class NotPositiveError(UserWarning):
	pass
while True:
	n = input("Please enter a positive number: ")
	try:
		number = int(n)
		if number <= 0:
			raise NotPositiveError
		break
	except ValueError:
		print("This was not a number, please try again.")
	except NotPositiveError:
		print("The number was not positive, please try again.")
print("The divisors of the number are:")
for i in range(1,number):
    if(number%i==0):
        print(i)