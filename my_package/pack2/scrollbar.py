from tkinter import *

w = Tk()
w.title("Scrollbar Example")

# Create scrollbar
s = Scrollbar(w)
s.pack(side=RIGHT, fill=Y)

# Create listbox with scrollbar connection
mylist = Listbox(w, yscrollcommand=s.set)
for line in range(100):
    mylist.insert(END, 'This is line number ' + str(line))

mylist.pack(side=LEFT, fill=BOTH)

# Link scrollbar to listbox
s.config(command=mylist.yview)

w.mainloop()
