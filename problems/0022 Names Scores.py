with open('0022_names.txt', 'r') as f:
    names = f.readlines()[0].strip().replace('"', '').split(',')

names = sorted(names)
total = 0

for i, name in enumerate(names):
    value = 0
    for c in name:
        value += ord(c) - ord('A') + 1
    total += value * (i+1)

print(total)

# answer: 871198282