import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("400x100")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
def validate(u_input): # callback function
    return u_input.isdigit()
my_valid = my_w.register(validate) # register 
l1=tk.Label(my_w,text='Enter Number only')
l1.grid(row=1,column=1,padx=20,pady=20)
e1 = Entry(my_w,validate='key',validatecommand=(my_valid,'%S'))
e1.grid(row=1,column=2,padx=20)

my_w.mainloop()  # Keep the window open