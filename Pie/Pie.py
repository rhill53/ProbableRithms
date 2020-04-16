"""
CS4050 Algorithms
Spring 2020
Probability of dart in a circle inside a square
Robb Hill
"""

import math
import random
import os

darts = 1000000
points_in_circle = 0
points_out_circle = 0

i = 0
while i < darts:
    x = random.randint(0, 200)
    y = random.randint(0, 200)

    if ((x-100) ** 2 + (y-100) ** 2) < 10000:
        points_in_circle += 1
    else:
        points_out_circle += 1

    i += 1

print(f'Points inside the circle: {points_in_circle}')
print(f'Points outside the circle: {points_out_circle}')

print('Approximation of Pi = ' + str(4 * (points_in_circle/darts)))

os.system("PAUSE")
