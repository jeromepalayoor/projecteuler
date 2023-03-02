'''
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is 385.

The square of the sum of the first ten natural numbers is 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

a = 0
for i in range(101):
    a += i
a = a*a
b = 0
for i in range(101):
    b += i*i
print(a-b)

#answer: 25164150
