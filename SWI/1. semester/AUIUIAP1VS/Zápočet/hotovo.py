import tkinter as tk
from tkinter import *
import math
from math import degrees,acos

root= tk.Tk()

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

def validate(u_input): 
    return u_input.isdigit()

a_x1 = tk.Entry(root.register(validate))


a_y = tk.Entry(root)

b_x = tk.Entry(root)
b_y = tk.Entry(root)

c_x = tk.Entry(root)
c_y = tk.Entry(root)    



def tabulka():
    canvas.delete("all")
    canvas.create_text(250, 80, fill="black", text=("Bod A"))
    canvas.create_text(150, 100, fill="black", text=("X: "))
    canvas.create_window(250, 100, window=a_x)
    canvas.create_text(150, 150, fill="black", text=("Y: "))
    canvas.create_window(250, 150, window=a_y)

    canvas.create_text(500, 80, fill="black", text=("Bod B"))
    canvas.create_window(500, 100, window=b_x)
    canvas.create_window(500, 150, window=b_y)

    canvas.create_text(750, 80, fill="black", text=("Bod C"))
    canvas.create_window(750, 100, window=c_x)  
    canvas.create_window(750, 150, window=c_y)

    button1 = tk.Button(text='Nakresli Trojuholnik', command=vypocty)
    canvas.create_window(500, 200, window=button1)

#toto bere udaje a ak zle udaje su zadane tak to informuje uzivatela
def vypocty():
    global a1
    
    if a_x.get().isdigit():
        canvas.delete("warningA1")
        a1 = int(a_x.get())
    else:
        canvas.delete("warningA1")
        canvas.create_text(250,110,fill="red",font="Times 20",text="Nesprávny údaj!",anchor="n", tag="warningA1")

    global a2
    if a_y.get().isdigit():
        canvas.delete("warningA2")
        a2 = int(a_y.get())
    else:
        canvas.delete("warningA2")
        canvas.create_text(250,160,fill="red",font="Times 20",text="Nesprávny údaj!",anchor="n", tag="warningA2")
        
    global b1
    if b_x.get().isdigit():
        canvas.delete("warningB1")
        b1 = int(b_x.get())
    else:
        canvas.delete("warningB1")
        canvas.create_text(500,110,fill="red",font="Times 20",text="Nesprávny údaj!",anchor="n", tag="warningB1")
        
    global b2
    if b_y.get().isdigit():
        canvas.delete("warningB2")
        b2 = int(b_y.get())
    else:
        canvas.delete("warningB2")
        canvas.create_text(500,160,fill="red",font="Times 20",text="Nesprávny údaj!",anchor="n", tag="warningB2")
    
    global c1
    if c_x.get().isdigit():
        canvas.delete("warningC1")
        c1 = int(c_x.get())
    else:
        canvas.delete("warningC1")
        canvas.create_text(750,110,fill="red",font="Times 20",text="Nesprávny údaj!",anchor="n", tag="warningC1")
        
       
    global c2
    if c_y.get().isdigit():
        canvas.delete("warningC2")
        c2 = int(c_y.get())
    else:
        canvas.delete("warningC2")
        canvas.create_text(750,160,fill="red",font="Times 20",text="Nesprávny údaj!",anchor="n", tag="warningC2")


    # Definice a následující výpočet strany A
    global strana_A
    strana_A = (((b1-c1)**2+(b2-c2)**2)**0.5)
    strana_A = round(strana_A,2)

    # Definice a následující výpočet strany B
    global strana_B
    strana_B= (((c1-a1)**2+(c2-a2)**2)**0.5)
    strana_B = round(strana_B,2)

    # Definice a následující výpočet strany C
    global strana_C
    strana_C = (((a1-b1)**2+(a2-b2)**2)**0.5)
    strana_C = round(strana_C,2)
    
    # Definice a následující výpočet obvodu
    global obvod
    obvod = strana_A+strana_B+strana_C
    obvod = round(obvod,2)

    # Mezivýpočet pro obsah
    s = (obvod)/2

    # Definice a následující výpočet obsahu
    global obsah
    obsah = ((s*(s-strana_A)*(s-strana_B)*(s-strana_C))**0.5)
    obsah = round(obsah,2)

    # Výpočet úhlů:

    # Alfa:
    global alfa
    alfa = round(degrees(math.acos(((strana_B**2)+(strana_C**2)-(strana_A**2))/(2*strana_B*strana_C))),2)
    # Beta:
    global beta
    beta = round(degrees(math.acos(((strana_C**2)+(strana_A**2)-(strana_B**2))/(2*strana_C*strana_A))),2)
    # Gama:
    global gama
    gama = round(degrees(math.acos(((strana_A**2)+(strana_B**2)-(strana_C**2))/(2*strana_A*strana_B))),2)

    # Funkce if, která rozhodne, jestli se vůbec vykreslí trojúhelník, nebo ne
    if strana_A+strana_B>strana_C and strana_B+strana_C>strana_A and strana_A+strana_C>strana_B:
        # Pokud lze narýsovat potom:
        print("Trojúhelník lze narýsovat")

        # Spustí kresbu na canvas a vypsání všech informací na canvas:
        kresba()

        # Vypíše souřadnice do konzole:
        print("  ","X","   ","Y")
        print("A:",a1,",",a2)
        print("B:",b1,",",b2)
        print("C:",c1,",",c2)

        # Vypíše délky stran do konzole:
        print("Délka strany A:",strana_A,"\nDélka strany B:",strana_B,"\nDélka strany C:",strana_C)

        # Vypíše obvod a obsah do konzole:
        print("Obvod:",obvod,"\nObsah:",obsah)

        # Vypíše úhly do konzole:
        print("Úhel alfa:",alfa,"\nÚhel beta:",beta,"\nÚhel gama:",gama)

        # Vypíše jestli trojúhelník je nebo není pravoúhlý:
        if alfa==90 or beta==90 or gama == 90:
            # Vypíše, že je pravoúhlý do konzole
            print("Trojúhelník je pravoúhlý")

            # Vypíše, že je pravoúhlý na canvas
            canvas.create_text(470,635,fill="black",font="Times 10",text="Trojúhelník je pravoúhlý",anchor="w")
        else:
            # Vypíše, že není pravoúhlý do konzole
            print("Trojuhelník není pravoúhlý") 

            # Vypíše, že není pravoúhlý na canvas
            canvas.create_text(470,635,fill="black",font="Times 10",text="Trojúhelník není pravoúhlý",anchor="w")

    else:
        # Pokud nelze narýsovat, potom:
        print("Trojúhelník nelze narýsovat")

        # Vypíše i na canvas, že nelze narýsovat trojúhelník:
        canvas.create_text(100,100,fill="red",font="Times 30",text="Trojúhelník nelze narýsovat",anchor="w")
        
def kresba():
    canvas.delete("all")
    # Narýsuje trojúhelník
    #canvas.create_line(a1,a2,b1,b2,c1,c2,a1,a2,fill="blue",width=5)
    canvas.create_line(a1,a2,b1,b2,fill="blue",width=5)
    canvas.create_line(b1,b2,c1,c2,fill="blue",width=5)
    canvas.create_line(c1,c2,a1,a2,fill="blue",width=5)

    # Vypíše informace o trojúhelníku na canvas, ať nejsou vypsané jenom v konzoli

    # Souřadnice bodů:
    canvas.create_text(135,635,fill="black",font="Times 10",text=("X     Y"),anchor="w")
    canvas.create_text(25,650,fill="black",font="Times 10",text="Souřadnice bodu A:" + str(a1) +"  "+ str(a2),anchor="w")
    canvas.create_text(25,665,fill="black",font="Times 10",text="Souřadnice bodu B:" + str(b1) + "  "+ str(b2),anchor="w")
    canvas.create_text(25,680,fill="black",font="Times 10",text="Souřadnice bodu C:" + str(c1) + "  "+ str(c2),anchor="w")

    # Nadepsání bodů
    canvas.create_text(a1-20,a2-20,fill="black",font="Times 20",text="A",anchor="w")
    canvas.create_text(b1+20,b2-20,fill="black",font="Times 20",text="B",anchor="w")
    canvas.create_text(c1-20,c2+20,fill="black",font="Times 20",text="C",anchor="w")

    # Nadepsání stran
    canvas.create_text((a1+b1)/2,(a2+b2)/2,fill="red",font="Times 20",text="c",anchor="w")
    canvas.create_text((b1+c1)/2,(b2+c2)/2,fill="red",font="Times 20",text="a",anchor="w")
    canvas.create_text((a1+c1)/2,(a2+c2)/2,fill="red",font="Times 20",text="b",anchor="w")

    # Délky stran:
    canvas.create_text(200,650,fill="black",font="Times 10",text=("Délka strany A:" + str(strana_A)),anchor="w")
    canvas.create_text(200,665,fill="black",font="Times 10",text=("Délka strany B:" + str(strana_B)),anchor="w")
    canvas.create_text(200,680,fill="black",font="Times 10",text=("Délka strany C:" + str(strana_C)),anchor="w")
    
    # Obvod a obsah:
    canvas.create_text(350,650,fill="black",font="Times 10",text=("Obvod:" + str(obvod) + "px"),anchor="w")
    canvas.create_text(350,665,fill="black",font="Times 10",text=("Obsah:" + str(obsah) + "px²"),anchor="w")

    # Úhly:
    canvas.create_text(470,650,fill="black",font="Times 10",text=("Úhel alfa:" + str(alfa) + "°"),anchor="w")
    canvas.create_text(470,665,fill="black",font="Times 10",text=("Úhel beta:" + str(beta) + "°"),anchor="w")
    canvas.create_text(470,680,fill="black",font="Times 10",text=("Úhel gama:" + str(gama) + "°"),anchor="w")

    # Tlačítko pre nový trojuholník:
    button2 = tk.Button(text="Nový Trojuholník", command=tabulka)
    canvas.create_window(100, 580, window=button2)

tabulka()
root.mainloop()
# Toto nevíme, co dělá, ale nepůjde to bez toho:
canvas.mainloop()