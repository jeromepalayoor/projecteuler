'''
10001st prime
Problem 7
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
