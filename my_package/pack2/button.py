from tkinter import *

def Clickme():
    print("you have clicked me")

w = Tk()
f = Frame(w, height=200, width=300)
f.pack()

b = Button(f, text="My Button", width=15, height=2, bg="yellow", fg="blue",
           activebackground="green", activeforeground="red", command=Clickme)
b.pack()

w.mainloop()
