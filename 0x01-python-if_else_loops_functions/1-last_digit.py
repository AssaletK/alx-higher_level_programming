#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
     r = - number % 10
     print(f"Last digit of {number} is {-r} and is less than 6 and not 0")
else:
    r = number % 10
    if r > 5:
        print(f"Last digit of {number} is {r} and is greater than 5")
    else:
        if r == 0:
            print(f'Last digit of {number} is {r} and is 0')
        else:
    	    print(f"Last digit of {number} is {r} and is less than 6 and not 0")
