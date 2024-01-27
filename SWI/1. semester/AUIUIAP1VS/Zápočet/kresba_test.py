import tkinter as tk
from tkinter import Canvas


app = tk.Tk()
app.title("Canvas")

canvas = Canvas(app)
canvas.pack()

a_x=200
a_y=400
b_x=-300
b_y=-500
c_x=100
c_y=-200
"""
print(20*a_x**2)
print(20*a_y**2)
print(20*b_x**2)
print(20*b_y**2)
print(20*c_x**2)
print(20*c_y**2)
print(20*a_x**2,20*a_y**2,20*b_x**2,20*b_y**2)
print(abs(a_x)*50,abs(a_y)*50,abs(c_x)*50,abs(c_y)*50)
ax=abs(b_x)*20
print((abs(a_x)*50)-10,abs(abs(a_y)*50-abs(c_y)*50))
print(abs(b_x)*50,abs(b_y)*50,abs(c_x)*50,abs(c_y)*50)
print(abs(abs(b_x)*50-abs(c_x)*50)/2+abs(b_x))
print(abs(abs(b_x)*50-abs(c_x)*50)/2)
"""



def kresba():
    stranaA=[
        a_x,a_y,
        b_x,b_y,
    ]
    canvas.create_line(stranaA)
    
    stranaB=[
        b_x,b_y,
        c_x,c_y,
    ]
    canvas.create_line(stranaB)

    stranaC=[
        c_x,c_y,
        a_x,a_y,
    ]
    canvas.create_line(stranaC)
kresba()


#canvas.create_line(a_x,a_y,b_x,b_y)
app.mainloop()