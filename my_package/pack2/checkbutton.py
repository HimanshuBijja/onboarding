from tkinter import *

w = Tk()
w.title("Checkbutton")
w.geometry("400x300")

# Variables to hold the checked state
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

# Checkbuttons with assigned variables
c1 = Checkbutton(w, text="C++", variable=var1)
c1.grid(row=0, column=0)

c2 = Checkbutton(w, text="Java", variable=var2)
c2.grid(row=1, column=0)

c3 = Checkbutton(w, text="Python", variable=var3)
c3.grid(row=2, column=0)

w.mainloop()
