from tkinter import *

class Myradio:
    def __init__(self, w):
        self.var = IntVar()

        self.r1 = Radiobutton(w, text="Male", variable=self.var, value=1, command=self.display)
        self.r2 = Radiobutton(w, text="Female", variable=self.var, value=2, command=self.display)

        self.r1.place(x=50, y=100)
        self.r2.place(x=200, y=100)

        self.w = w  # store reference to parent window if needed

    def display(self):
        x = self.var.get()
        msg = ""

        if x == 1:
            msg += "You selected: Male"
        if x == 2:
            msg += "You selected: Female"

        Label(text=msg, fg="blue").place(x=50, y=150, width=200, height=20)

w = Tk()
w.title("Gender Selection")
w.geometry("400x250")
mb = Myradio(w)
w.mainloop()
