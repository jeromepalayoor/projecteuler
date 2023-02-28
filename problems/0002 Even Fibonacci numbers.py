'''
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''

fib = 1
fibprev = 0
a = 0

while fib < 4000000:
    new = fib + fibprev
    if new % 2 == 0:
        a += new
    fibprev = fib
    fib = new
print(a)


#answer : 4613732
