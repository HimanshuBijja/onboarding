n = input('Enter the name of the file: ')
flag = True

try:
    s = input('Enter the words to find (comma-separated): ')
    sl = s.split(', ')
    f = open(n, 'r')
    il = f.read()
except FileNotFoundError:
    print(f'Error: File \'{n}\' not found.')
else:
    c = 0
    for i in sl:
        if i in il:
            flag = False
            if c == 0:
                print('The following words were found in the file:')
                c += 1
            print(i)
finally:
    if flag:
        print('None of the specified words were found in the file.')
