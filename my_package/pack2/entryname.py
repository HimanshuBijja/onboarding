from tkinter import *

w = Tk()

def dis():
    str1 = e1.get() + e2.get()
    Label(text=str1).grid(row=3)

L1 = Label(w, text='First Name')
L1.grid(row=0, column=0)

L2 = Label(w, text='Last Name')
L2.grid(row=1, column=0)

e1 = Entry(w)
e1.grid(row=0, column=1)

e2 = Entry(w)
e2.grid(row=1, column=1)

b = Button(w, text='Submit', command=dis)
b.grid(row=2, column=1)

w.mainloop()
