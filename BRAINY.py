import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:

        num1 = float(entry1.get())
        
        product =2025-num1
        
        messagebox.showinfo("Result", f"The product is: {product}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x200")

label1 = tk.Label(root, text="Enter DOB:")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)


button = tk.Button(root, text="Calculate Product", command=calculate_product)
button.pack(pady=20)

root.mainloop()


