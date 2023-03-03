'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

a = 0
b = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
c = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def d(n):
    if n < 20:
        return len(b[n-1])
    elif n < 100:
        if n%10 == 0:
            return len(c[n//10-2])
        else:
            return len(c[n//10-2] + b[n%10-1])
    elif n < 1000:
        if n%100 == 0:
            return len(b[n//100-1] + 'hundred')
        else:
            return len(b[n//100-1]+ 'hundred' + 'and') + d(n%100)
    elif n == 1000:
        return len('one' + 'thousand')
for i in range(1, 1001):
    a += d(i)
print(a)

#answer: 21124
