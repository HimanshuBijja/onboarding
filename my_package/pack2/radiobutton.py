from tkinter import *

w = Tk()
w.title("Radiobutton Example")
w.geometry("400x250")

def dis():
    print(x.get())

x = IntVar()
r1 = Radiobutton(w, text="Male", variable=x, value=1, command=dis)
r2 = Radiobutton(w, text="Female", variable=x, value=2, command=dis)

r1.place(x=50, y=100)
r2.place(x=200, y=100)

w.mainloop()
