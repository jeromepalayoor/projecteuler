'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
n = 0
for i in range(100,1000):
    for j in range(100,1000):
        k = str(i*j)
        if len(k)%2==0:
            if k[:len(k)//2] == k[len(k)//2:][::-1]:
                if int(k) > n:
                    n = int(k)
        else:
            if k[:(len(k)-1)//2] == k[(len(k)+1)//2:][::-1]:
                if int(k) > n:
                    n = int(k)

print(n)

#answer : 906609
