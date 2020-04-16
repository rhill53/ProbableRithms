"""
CS4050 Algorithms
Spring 2020
Test for prime numbers
Robb Hill
"""

import math
import random

p = random.randint(3, 100)
print(f'P = {p}')
prime = []
not_prime = []
k = 0
while k < 1000:
    n = random.randint(2, p-1)
    if p % n != 0:
        not_prime.append(n)
    else:
        prime.append(n)
    k += 1

if not prime:
    print(f'P is prime!')
else:
    print(f'P is NOT prime :-(')
