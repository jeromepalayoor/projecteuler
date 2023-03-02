'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math

def is_prime(k):
    for i in range(2,int(math.sqrt(k))+1):
        if (k%i) == 0:
            return False
    return True

n = 0
a = 1
b = 0
while 1:
    if n == 10001:
        print(b)
        exit()
    a += 1
    if is_prime(a):
        n += 1
        b = a


#answer: 104743
