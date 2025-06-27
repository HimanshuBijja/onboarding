from tkinter import *

class MyButtons:
    def __init__(self, w):
        self.b1 = Button(w, text="ClickMe", width=15, height=2, command=self.buttonClick)
        self.b2 = Button(w, text="close", width=15, height=2, command=w.destroy)
        self.b1.grid(row=0, column=1)
        self.b2.grid(row=0, column=2)
        self.w = w  # Store reference for use in buttonClick

    def buttonClick(self):
        self.lbl = Label(self.w, text="Welcome to Python", width=20, height=2,
                         font=("Courier", -30, "bold underline"), fg="blue")
        self.lbl.grid(row=2, column=0)

w = Tk()
mb = MyButtons(w)
w.mainloop()
