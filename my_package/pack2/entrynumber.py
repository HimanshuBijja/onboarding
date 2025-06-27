import tkinter as t

w = t.Tk()

def even():
    n = int(e1.get())
    if n % 2:
        res = "Odd"
    else:
        res = "Even"
    t.Label(w, text=res).grid(row=3, column=1)

L1 = t.Label(w, text="Number")
L1.grid(row=0, column=0)

e1 = t.Entry(w)
e1.grid(row=0, column=1)

rb = t.Button(w, text='Check', command=even)
rb.grid(row=1, column=1)

w.mainloop()
