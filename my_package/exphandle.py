try:
    n = int(input('Enter the numerator: '))
    d = int(input('Enter the denominator: '))
    print(f'Result: {n / d}')
except ZeroDivisionError as e:
    print('Error:', e)
except ValueError as e:
    print('Error:', e)
finally:
    print('Execution complete')
