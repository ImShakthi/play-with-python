#!/usr/bin/env python

import random


def printRandom():
    x = random.randrange(10, 99)
    print("rand x:", x)


def getRandNumbers(n):
    numbers = []
    for i in range(n):
        numbers.append(random.randrange(0, 100))
    return numbers

print(random.random())

randNum = random.randrange(0, 10)
print("random number %d" % randNum)


# 1. Make a program that creates a random number and stores it into x.
printRandom()

# 2. Make a program that prints 3 random numbers.
for i in range(3):
    printRandom()

# 3. Create a program that generates 100 random numbers and find the frequency of each number.
numbers = getRandNumbers(100)
print(numbers)
freqCounter = {1: 1}
for n in numbers:
    if n in freqCounter:
        freqCounter[n] = freqCounter[n] + 1
    else:
        freqCounter[n] = 1

values = list(freqCounter.values())

print("freqCounter=", max(values))
