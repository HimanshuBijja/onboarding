def do_twice(f, str):
    f(str)
    f(str)

def print_twice(a):
    print(a)
    print(a)

s = input()
do_twice(print_twice, s)
do_twice(print_twice, s)
do_twice(print_twice, s)
