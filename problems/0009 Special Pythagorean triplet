'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math

a = 1
b = 1
for a in range(100000):
    for b in range(100000):
        c = math.sqrt(a**2 + b**2)
        if c % 1 == 0 and (a + b + c) == 1000:
            r = a * b * c
            if r > 0:
                print(int(r))
                exit()

#answer: 31875000
