from tkinter import *

# Create main window
w1 = Tk()

# Create canvas
c = Canvas(w1, bg="blue", height=700, width=1200, cursor="pencil")

# Draw shapes
id = c.create_line(50, 50, 200, 50, 200, 150, width=4, fill="white")
id = c.create_oval(100, 100, 400, 300, width=5, fill="yellow", outline="red")
id = c.create_polygon(10, 10, 200, 200, 300, 200, width=3, fill="green", smooth=1, activefill="lightblue")
id = c.create_rectangle(500, 200, 700, 600, width=2, fill="gray", outline="black", activefill="yellow")

# Add text
fnt = ("Times", 40, "bold italic underline")
id = c.create_text(500, 100, text="My canvas", font=fnt, fill="yellow", activefill="green")

# Pack and display canvas
c.pack()

# Start main loop
w1.mainloop()
