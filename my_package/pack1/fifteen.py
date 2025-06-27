import geometry

print('Select a shape:')
print('1. Circle')
print('2. Rectangle')
print('3. Triangle')

c = int(input('Enter your choice (1/2/3): '))

match c:
    case 1:
        r = int(input('Enter the radius of the circle: '))
        print(f'Circle Area: {geometry.areac(r):.2f}, Perimeter: {geometry.peric(r):.2f}')
    
    case 2:
        l = int(input('Enter the length of the rectangle: '))
        b = int(input('Enter the width of the rectangle: '))
        print(f'Rectangle Area: {geometry.arear(l, b)}, Perimeter: {geometry.perir(l, b)}')
    
    case 3:
        b = int(input('Enter the base of the triangle: '))
        h = int(input('Enter the height of the triangle: '))
        print(f'Triangle Area: {geometry.areat(b, h)}')
        print('Note: Triangle perimeter calculation requires side lengths.')
        a = int(input('Enter the length of side 1: '))
        b = int(input('Enter the length of side 2: '))
        c = int(input('Enter the length of side 3: '))
        print(f'Triangle Perimeter: {geometry.perit(a, b, c)}')


import math

def areac(rad):
    return math.pi * rad ** 2

def peric(rad):
    return 2 * math.pi * rad

def arear(l, b):
    return float(l * b)

def perir(l, b):
    return float(2 * (l + b))

def areat(b, h):
    return float(0.5 * b * h)

def perit(a, b, c):
    return float(a + b + c)


