#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 100):
        if x % 3 == 0 and x % 5 == 0:
            print ("Fizz Buzz", end= " ")
        elif x % 3 == 0:
            print ("Fizz", end= " ")
        elif x % 5 == 0:
            print ("Buzz", end= " ")
        else:
            print (x, end= " ")
