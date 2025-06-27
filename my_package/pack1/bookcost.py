n = int(input('n: '))
p = 24.95 - (40 / 100) * 24.95
s = (n * p) + 3 + (0.75 * (n - 1))
print(f"The total cost is: $ {s:.2f}")
