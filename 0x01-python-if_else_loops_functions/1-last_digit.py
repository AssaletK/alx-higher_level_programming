#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
r = number % 10
if r > 5:
    print(f"Last digit of {number} is {r} and is greater than 5")
if r == 0:
    print(f"Last digit of {number} is {r} and is 0")
if r < 5:
    print(f"Last digit of {number} is {r} and is lower than 5")
