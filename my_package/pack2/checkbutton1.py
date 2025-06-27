from tkinter import *

class Mycheck:
    def __init__(self, w):
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()

        self.c1 = Checkbutton(w, text="Java", variable=self.var1, command=self.display)
        self.c2 = Checkbutton(w, text=".NET", variable=self.var2, command=self.display)
        self.c3 = Checkbutton(w, text="Python", variable=self.var3, command=self.display)

        self.c1.place(x=50, y=100)
        self.c2.place(x=200, y=100)
        self.c3.place(x=350, y=100)

    def display(self):
        x = self.var1.get()
        y = self.var2.get()
        z = self.var3.get()

        result = ""
        if x == 1:
            result += "Java "
        if y == 1:
            result += ".NET "
        if z == 1:
            result += "Python"

        Label(text=result.strip(), fg="blue").place(x=50, y=150, width=300)

w = Tk()
w.geometry("500x300")
w.title("Language Selector")
mb = Mycheck(w)
w.mainloop()
