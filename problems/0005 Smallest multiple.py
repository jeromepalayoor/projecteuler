'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

n = 1
while True:
    if (n%4==0 and n%6==0 and n%8==0 and n%9==0 and n%10==0 and n%11==0 and n%12==0 and n%13==0 and n % 14 == 0 and n%15==0 and n%16==0 and n%17==0 and n%18==0 and n%19==0 and n%20==0):
        print(n)
        break
    else:
        n+=1

    

#answer : 232792560 (takes a couple a seconds to run)
