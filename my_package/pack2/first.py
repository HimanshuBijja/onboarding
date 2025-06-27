import tkinter as tk
from tkinter import ttk, messagebox

    
def submit_data():
    name = name_entry.get()
    gender = gender_var.get()
    subscribed = "Yes" if subscribe_var.get() else "No"
    selected_fruit_indices = fruits_listbox.curselection()
    selected_fruits = [fruits_listbox.get(i) for i in selected_fruit_indices]
    country = country_combobox.get()
    
    message = (
        f"Name: {name}\n"
        f"Gender: {gender}\n"
        f"Subscribed: {subscribed}\n"
        f"Fruits Selected: {', '.join(selected_fruits)}\n"
        f"Country: {country}"
    )
    messagebox.showinfo("Submitted Data", message)

# Create main window
root = tk.Tk()
root.title("GUI with 8 Widgets")
root.geometry("400x500")

# 1. Label
tk.Label(root, text="Enter your Name:").pack(pady=5)

# 2. Entry
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# 3. RadioButton
tk.Label(root, text="Select Gender:").pack(pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

# 4. CheckButton
subscribe_var = tk.BooleanVar()
tk.Checkbutton(root, text="Subscribe to Newsletter", variable=subscribe_var).pack(pady=5)

# 5. Listbox with Scrollbar
tk.Label(root, text="Select your favorite fruits:").pack(pady=5)

listbox_frame = tk.Frame(root)
listbox_frame.pack()

fruits_listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, height=5)
scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=fruits_listbox.yview)
fruits_listbox.config(yscrollcommand=scrollbar.set)

# 6. Listbox
for fruit in ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Watermelon"]:
    fruits_listbox.insert(tk.END, fruit)

fruits_listbox.pack(side=tk.LEFT)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 7. Combobox
tk.Label(root, text="Select your Country:").pack(pady=5)
country_combobox = ttk.Combobox(root, values=["India", "USA", "UK", "Germany", "Australia"])
country_combobox.pack(pady=5)
country_combobox.current(0)

# 8. Button
tk.Button(root, text="Submit", command=submit_data).pack(pady=20)

# Start the application
root.mainloop()