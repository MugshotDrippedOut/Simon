from tkinter import *
import tkinter as tk
import math
from math import degrees,acos

root = tk.Tk()

frame = Frame(root)
frame.grid(row=0, column=0, sticky=N)
frame2 = Frame(root)
frame2.grid(row=0, column=0, sticky=E)

a_x = tk.Entry(frame,width=18)
a_y = tk.Entry(frame,width=18)

b_x = tk.Entry(frame,width=18)
b_y = tk.Entry(frame,width=18)

c_x = tk.Entry(frame,width=18)
c_y = tk.Entry(frame,width=18)    

def data():
    Label(frame, text="Číslo nesmie presiahnúť 500 \n a musí byť 3 ciferné!").grid(row=0, column=0, columnspan=10, sticky=N)
    Label(frame, text="X").grid(row=1, column=1, sticky=N)
    Label(frame, text="Y").grid(row=1, column=2, sticky=N)

    Label(frame, text="Bod A:").grid(row=2,column=0, sticky=NW)
    a_x.grid(row=2,column=1,sticky=W)
    a_y.grid(row=2,column=2,sticky=W)
    Label(frame, text="Bod B:").grid(row=4,column=0, sticky=NW)
    b_x.grid(row=4,column=1,sticky=W)
    b_y.grid(row=4,column=2,sticky=W)
    Label(frame, text="Bod C:").grid(row=6,column=0, sticky=NW)
    c_x.grid(row=6,column=1,sticky=W)
    c_y.grid(row=6,column=2,sticky=W)

    tk.Button(frame, text='Nakresli', command=checkWrongData, width=15).grid(row=8,column=1,columnspan=2, rowspan=2,sticky=N)


def checkWrongData():

    global labela
    labelA1=Label(frame, text="                                  ", fg="#FF0000", font="Helvetica 8 bold")
    labelA1.grid(row=3,column=1)

    labelA2=Label(frame, text="                                  ", fg="#FF0000", font="Helvetica 8 bold")
    labelA2.grid(row=3,column=2)

    labelB1=Label(frame, text="                                  ", fg="#FF0000", font="Helvetica 8 bold")
    labelB1.grid(row=5,column=1)

    labelB2=Label(frame, text="                                  ", fg="#FF0000", font="Helvetica 8 bold")
    labelB2.grid(row=5,column=2)

    labelC1=Label(frame, text="                                  ", fg="#FF0000", font="Helvetica 8 bold")
    labelC1.grid(row=7,column=1)

    labelC2=Label(frame, text="                                  ", fg="#FF0000", font="Helvetica 8 bold")
    labelC2.grid(row=7,column=2)
    

    
    aa = 0
    ab = 0
    ba = 0
    bb = 0
    ca = 0
    cb = 0
    
    global a1
    if len(a_x.get())<=3:
        if a_x.get().isdigit() and int(a_x.get()) <= 500:
            a1 = int(a_x.get())
            aa = 1
            labelA1
        else:
            labelA1.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelA1.config(text="↑ Priveľa znakov! ↑")

    global a2
    if len(a_y.get())<=3:
        if a_y.get().isdigit() and int(a_y.get()) <= 500:
            a2 = int(a_y.get())
            ab = 1
            labelA2
        else:
            labelA2.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelA2.config(text="↑ Priveľa znakov! ↑")

    global b1
    if len(b_x.get())<=3:
        if b_x.get().isdigit() and int(b_x.get()) <= 500:
            b1 = int(b_x.get())
            ba = 1
            labelB1
        else:
            labelB1.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelB1.config(text="↑ Priveľa znakov! ↑")

    global b2
    if len(b_y.get())<=3:
        if b_y.get().isdigit()and int(b_y.get()) <= 500:
            b2 = int(b_y.get())
            bb = 1
            labelB2
        else:
            labelB2.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelB2.config(text="↑ Priveľa znakov! ↑")

    global c1
    if len(c_x.get())<=3:
        if c_x.get().isdigit() and int(c_x.get()) <= 500:
            c1 = int(c_x.get())
            ca = 1
            labelC1
        else:
            labelC1.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelC1.config(text="↑ Priveľa znakov! ↑")

    global c2
    if len(c_y.get())<=3:
        if c_y.get().isdigit() and int(c_y.get()) <= 500:
            c2 = int(c_y.get())
            cb = 1
            labelC2
        else:
            labelC2.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelC2.config(text="↑ Priveľa znakov! ↑")

    if aa == 1 and ab == 1 and ba == 1 and bb == 1 and ca == 1 and cb == 1:
        vypis_vypocet()
    else:
        data()

def vypis_vypocet():

    # Výpočet strany A
    global strana_A
    strana_A = (((b1-c1)**2+(b2-c2)**2)**(1/2)) 
    strana_A = round(strana_A,2)

    # Výpočet strany B
    global strana_B
    strana_B= (((c1-a1)**2+(c2-a2)**2)**(1/2))
    strana_B = round(strana_B,2)

    # Výpočet strany C
    global strana_C
    strana_C = (((a1-b1)**2+(a2-b2)**2)**(1/2))
    strana_C = round(strana_C,2)
        
    if strana_A+strana_B>strana_C and strana_B+strana_C>strana_A and strana_A+strana_C>strana_B:
        Label(frame, text=("  Trojuholník sa dá narýsovať  "), font="Helvetica 15 bold", fg="white").grid(row=10,column=1, columnspan=2, sticky=N)

        # Výpis súradnic
        Label(frame2, text="Súradnice:", font="Helvetica 12 bold").grid(row=0,column=0, sticky=N)
        Label(frame2, text=("Bod A má súradnice X: "+str(a1)+" Y: "+str(a2)), font="Helvetica 10").grid(row=1,column=0, sticky=W)
        Label(frame2, text=("Bod B má súradnice X: "+str(b1)+" Y: "+str(b2)), font="Helvetica 10").grid(row=2,column=0, sticky=W)
        Label(frame2, text=("Bod C má súradnice X: "+str(c1)+" Y: "+str(c2)), font="Helvetica 10").grid(row=3,column=0, sticky=W)
        
        # Výpis strán
        Label(frame2, text="Strany:", font="Helvetica 12 bold").grid(row=0,column=1, sticky=N)
        Label(frame2, text=("Strana A je dlhá: "+str(strana_A)+" cm"), font="Helvetica 10").grid(row=1,column=1, sticky=W)
        Label(frame2, text=("Strana B je dlhá: "+str(strana_B)+" cm"), font="Helvetica 10").grid(row=2,column=1, sticky=W)
        Label(frame2, text=("Strana C je dlhá: "+str(strana_C)+" cm"), font="Helvetica 10").grid(row=3,column=1, sticky=W)

        # Výpočet obvodu
        global obvod
        obvod = strana_A+strana_B+strana_C
        obvod = round(obvod,2)

        # Mezivýpočet pro obsah
        s = (obvod)/2

        # Výpočet obsahu
        global obsah
        obsah = ((s*(s-strana_A)*(s-strana_B)*(s-strana_C))**(1/2))
        obsah = round(obsah,2)

        # Výpis obvodu a obsahu
        Label(frame2, text="Výpočty:", font="Helvetica 12 bold").grid(row=0,column=2, sticky=N)
        Label(frame2, text=("Obsah trojuholníka sa rovná: "+str(obsah)+" cm²"), font="Helvetica 10").grid(row=1,column=2, sticky=W)
        Label(frame2, text=("Obvod trojuholníka sa rovná: "+str(obvod)+" cm"), font="Helvetica 10").grid(row=2,column=2, sticky=W)
        kresba()
    else:
        Label(frame, text=("Trojuholník sa nedá narýsovať"), font="Helvetica 12 bold", fg="red").grid(row=10,column=0, columnspan=10, sticky=N)


def kresba():
    udaje = tk.Canvas(root, width=500, height=500, background='#c4c4c4')
    udaje.grid(row=0, column=1, columnspan=5)
    # Narýsuje trojúhelník
    udaje.create_line(a1,a2,b1,b2,fill="blue",width=5)
    udaje.create_line(b1,b2,c1,c2,fill="blue",width=5)
    udaje.create_line(c1,c2,a1,a2,fill="blue",width=5)

    # Nadepsání bodů
    udaje.create_text(a1-20,a2-20,fill="black",font="Times 20",text="A",anchor="w")
    udaje.create_text(b1+20,b2-20,fill="black",font="Times 20",text="B",anchor="w")
    udaje.create_text(c1-20,c2+20,fill="black",font="Times 20",text="C",anchor="w")

    # Nadepsání stran
    udaje.create_text((a1+b1)/2,(a2+b2)/2,fill="red",font="Times 20 bold",text="c",anchor="w")
    udaje.create_text((b1+c1)/2,(b2+c2)/2,fill="red",font="Times 20 bold",text="a",anchor="w")
    udaje.create_text((a1+c1)/2,(a2+c2)/2,fill="red",font="Times 20 bold",text="b",anchor="w")
    
data()

root.mainloop()