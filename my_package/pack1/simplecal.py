a, b=float(input("number1: ")), float(input("number2: "))
print('Addition:', (a+b))
print('Subtraction:', (a-b))
print('Multiplication:', (a*b))
try:
    c=a/b
except ZeroDivisionError:
    c='Cannot divide by zero'
print('Division:',c)