#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    mod = number % 10
else:
    mod = number % -10
print(f"last digit of {number} is {mod}",end=' ')
if mod > 5:
    print(f"and is greater than 5")
elif mod == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
