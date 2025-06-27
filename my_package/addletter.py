s = input('Enter the file name: ')
f = open(s, 'r')
st = f.read()
st = st.split('\n')
for i in st:
    if i != '':
        print(i)

print('I', 'a', '', sep='\n')
