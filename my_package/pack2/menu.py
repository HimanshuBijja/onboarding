from tkinter import *

w = Tk()
w.title("Menu Example")

menubar = Menu(w)  # fixed: W → w
w.config(menu=menubar)

# File menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=w.quit)
menubar.add_cascade(label="File", menu=filemenu)  # fixed: add cascade → add_cascade

# Edit menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")  # fixed: add command → add_command
editmenu.add_command(label="Copy")
menubar.add_cascade(label="Edit", menu=editmenu)

# Help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)  # fixed: missing menu argument

w.mainloop()
