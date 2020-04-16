"""
CS4050 Algorithms
Spring 2020
Randomly look for number in an array
Robb Hill
"""

import math
import random

search = 0
searches = []
while search < 100:
    ary = []
    i = 0
    while i < 1000:
        ary.append(random.randint(0, 65535))
        i += 1

    value = ary[(random.randint(0, 999))]

    i = 0
    while i < 5000:
        search_index = random.randint(0, 999)
        if ary[search_index] == value:
            searches.append(i)
            print(f'Wow you found {value} on try {i}!')
            break
        if i == 4999:
            searches.append(5000)
            print(f'Sorry you could not find {value}.\nIt hid too well!')
        i += 1
    search += 1
print(f'Average number of searches was: {(sum(searches))/100}')
