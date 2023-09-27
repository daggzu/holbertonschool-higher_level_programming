#!/usr/bin/python3

def print_last_digit(number):
    if isinstance(number, int):
        number = str(number)
    number = int(str(number)[-1])
    print(number, end="")
    return number
