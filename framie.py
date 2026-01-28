from tkinter import *
window=Tk()
frame1=Frame(master=window, width=300, height=300, bg="red")
frame1.pack(side=TOP)
frame2=Frame(master=window, width=200, height=200, bg="yellow")
frame2.pack(side=LEFT)
frame3=Frame(master=window, width=50, height=30, bg="yellow")
frame3.pack(side=RIGHT)
window.mainloop()
         