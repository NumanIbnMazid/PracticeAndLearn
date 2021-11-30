import math
import os
import random
import re
import sys

# Task
    # Given an integer, x, perform the following conditional actions:

        # If x is odd, print Weird
        # If x is even and in the inclusive range of 2 to 5, print Not Weird
        # If x is even and in the inclusive range of 6 to 20, print Weird
        # If x is even and greater than 20, print Not Weird

# number = 10

def check_condition(number):
    if not number % 2 == 0:
        print("Weird")
    if number % 2 == 0 and number in range(2, 5):
        print("Not Weird")
    if number % 2 == 0 and number in range(6, 20):
        print("Weird")
    if number % 2 == 0 and number > 20:
        print("Not Weird")

# check_condition(24)

# numbers = [3, 24]

# for number in numbers:
#     check_condition(number)


# Solution:
if __name__ == '__main__':
    n = int(input().strip())

    if not n % 2 == 0:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 5):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 20):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    else:
        print("Weird")
