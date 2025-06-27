d = {}
while True:
    k = input("Enter a key (press Enter to stop): ")
    if k == "":
        break
    else:
        v = input(f"Enter a value for '{k}': ")
        d[k] = v

print("Original Dictionary:")
print(d)

l = list(d.items())
il = []
for i in range(len(l)):
    temp = l[i][::-1]
    il.append(temp)

il = dict(il)
print("Inverted Dictionary:")
print(il)
