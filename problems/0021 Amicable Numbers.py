amicable = []

def d(n):
    divisors = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

for a in range(1, 10000):
    if a in amicable:
        continue
    b = d(a)
    if d(b) == a and a != b:
        amicable.append(a)
        amicable.append(b)

print(sum(set(amicable)))

# answer: 31626