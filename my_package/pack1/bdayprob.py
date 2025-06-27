import random

def genBdays(n):
    return [random.randint(1, 365) for _ in range(n)]

def sameBdays(bdays):
    return len(bdays) != len(set(bdays))

num = 23
samebdays = sum(sameBdays(genBdays(num)) for _ in range(100))
p = samebdays / 100
print(p)
