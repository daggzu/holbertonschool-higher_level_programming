#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(str(number)[-1:])
if number < 0:
    lastdigit = -lastdigit
print("Last digit of ", end="")
if lastdigit > 5:
    print("{} is {} and is greater than 5".format(number, lastdigit))
elif lastdigit == 0:
    print("{} is {} and is 0".format(number, lastdigit))
else:
    print("{} is {} and is less than 6 and not 0".format(number, lastdigit))
