from tkinter import *

w = Tk()
w.geometry('200x150')  # increased size a bit for better spacing

def dis():
    print(x.get())
    print(y.get())

x = IntVar()
y = StringVar()

s1 = Spinbox(w, from_=0, to=10, textvariable=x, command=dis)
s2 = Spinbox(w, values=('man', 'rat', 'cat', 'bat', 'mat', 'tin'), textvariable=y, command=dis)

s1.pack(pady=5)
s2.pack(pady=5)

w.mainloop()
