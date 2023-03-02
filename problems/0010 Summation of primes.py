'''
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

def is_prime(k):
    for i in range(2,int(math.sqrt(k))+1):
        if (k%i) == 0:
            return False
    return True

a = 2
b = 0
while a < 2000001:
    if is_prime(a):
        b += a
    a += 1
print(b)

#answer: 142913828922
