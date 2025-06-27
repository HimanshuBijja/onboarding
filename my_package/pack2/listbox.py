from tkinter import *

w = Tk()
w.geometry('200x200')
w.title("Listbox Example")

Lb = Listbox(w, selectmode="multiple")
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Perl')
Lb.insert(5, 'Any other')  # fixed index from 4 to 5

Lb.pack()

w.mainloop()
