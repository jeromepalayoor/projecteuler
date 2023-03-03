'''
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

a = 0
while 1:
    a += 1
    tri = int((a*(a+1))//2)
    b = 0
    for i in range(1, int(tri**0.5)+1):
        if tri%i == 0:
            b += 1
    b *= 2
    if int(tri**0.5)**2 == tri:
        b -= 1
    if b > 500:
        print(tri)
        exit()

#answer: 76576500
