from tkinter import *

window=Tk("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nTHE BUTTON WAS CLICKED🚨")

button=Button(text="Click me!!!")    
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()