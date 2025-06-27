n1 = input('Enter the name of the first input file: ')
n2 = input('Enter the name of the second input file: ')
op = input('Enter the name of the output file: ')

try:
    i1 = open(n1, 'r')
    i2 = open(n2, 'r')
    o = open(op, 'w')
    s1 = i1.read()
    s2 = i2.read()
    o.write(s1 + s2)
    o.close()
    print('Merged content:')
    o = open(op, 'r')
    print(o.read())
except FileNotFoundError:
    print('One or more input files not found.')
