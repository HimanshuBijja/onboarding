from tkinter import *

w = Tk()
w.title("Text and Message Widgets")

# Text Widget
t = Text(w, width=40, height=10, font=("Verdana", 14, "bold"),
         fg="blue", bg="yellow", wrap=WORD)
t.insert(END, "Text widget\nThis text is inserted into the text widget.\nThis is second line\nand this is third line\n")
t.pack(side=TOP)

# Message Widget
m = Message(w, text="This is a message that has more than one line of text",
            width=300, font=("Arial", 12), fg="green")
m.pack()

w.mainloop()
