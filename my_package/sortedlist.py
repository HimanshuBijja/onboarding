def chksrt(l):
    x = list(l)
    x.sort()
    print(x == l)

a = input('list of elements (separated by spaces): ')
l = a.split()
chksrt(l)
