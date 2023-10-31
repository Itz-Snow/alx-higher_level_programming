#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number > 0):
    print(f"{number:d} is positvie")
elif (number == 0):
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")
