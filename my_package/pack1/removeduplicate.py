lst = input('list of elements (separated by spaces): ')
lst = list(set(lst.split()))
lst.sort()
print(lst)
