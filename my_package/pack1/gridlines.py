r = int(input('Enter the number of rows: '))
c = int(input('Enter the number of columns: '))

def line(c):
    for i in range(0, c):
        print('+' + '-' * 4, end=" ")
    print('+')

def line2(c):
    for j in range(0, 4):
        for i in range(0, c):
            print('|' + ' ' * 9, end="")
        print('|')

for i in range(0, r):
    line(c)
    line2(c)
line(c)
