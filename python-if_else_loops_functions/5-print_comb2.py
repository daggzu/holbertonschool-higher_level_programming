#!/usr/bin/python3
for numero in range(0, 100):
    if numero < 99:
        print("{:02}".format(numero), end=", ")
    else:
        print("{}".format(numero))
