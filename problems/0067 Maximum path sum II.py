'''
Maximum path sum II
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
https://projecteuler.net/project/resources/p067_triangle.txt
NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''

import random

a = []
with open('a.txt', 'r') as f:
    d = f.read().splitlines()
    for i in range(len(d)):
        a.append([])
        for x in d[i].split(' '):
            a[i].append(int(x))
b = 0
for i in range(len(a)-1):
    for j in range(len(a[len(a)-2-i])):
        c = max(a[len(a)-1-i][j], a[len(a)-1-i][j+1])
        a[len(a)-2-i][j] = a[len(a)-2-i][j] + c
b = a[0][0]
print(b)

#answer: 7273
