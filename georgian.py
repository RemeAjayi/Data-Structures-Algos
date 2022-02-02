#!/bin/python3

import math
import os
import random
import re
import sys



import math
# Complete the 'lightBulbs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY states
#  2. INTEGER_ARRAY numbers
#

def lightBulbs(states, numbers):
    # Write your code here
    #edge cases
    #find prime factors
    for i in numbers:
        factors = set(primeFactors(i))
    #find multiple of prime factors
        for j in factors:
            for k in range(len(states)):
    #flip numbers whose indices correspond to multiples of prime factors
                if k % j == 0:
                    states[k] = 1 - states[k]
    return states
                
                
                
    #optimize

def primeFactors(n):
    factors = []
   
    for x in range(2, n + 1):
        while n % x == 0:
            factors.append(x)
            n = n // x
            
        if n == 1:
            return factors
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    states_count = int(input().strip())

    states = []

    for _ in range(states_count):
        states_item = int(input().strip())
        states.append(states_item)

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = lightBulbs(states, numbers)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
