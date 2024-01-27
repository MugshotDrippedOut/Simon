import tkinter as tk
import math
from math import degrees,acos, sqrt

root= tk.Tk()

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()


a_x = tk.Entry(root)

a_y = tk.Entry(root)

b_x = tk.Entry(root)
b_y = tk.Entry(root)

c_x = tk.Entry(root)
c_y = tk.Entry(root)

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

def vypocty():
    global a_x
    global a_y
    a_x = int(a_x.get())
    a_y = int(a_y.get())
    global b_x
    global b_y
    b_x = int(b_x.get())
    b_y = int(b_y.get())
    global c_x
    global c_y
    c_x = int(c_x.get())
    c_y = int(c_y.get())
    
    # Definice a následující výpočet strany A
    global strana_A
    strana_A = (((b_x-c_x)**2+(b_y-c_y)**2)**(1/2))
    strana_A = round(strana_A,2)

    # Definice a následující výpočet strany B
    global strana_B
    strana_B= (((c_x-a_x)**2+(c_y-a_y)**2)**(1/2))
    strana_B = round(strana_B,2)

    # Definice a následující výpočet strany C
    global strana_C
    strana_C = (((a_x-b_x)**2+(a_y-b_y)**2)**(1/2))
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
    alfa = degrees(math.acos(((strana_B**2)+(strana_C**2)-(strana_A**2))/(2*strana_B*strana_C)))
    # Beta:
    global beta
    beta = degrees(math.acos(((strana_C**2)+(strana_A**2)-(strana_B**2))/(2*strana_C*strana_A)))
    # Gama:
    global gama
    gama = degrees(math.acos(((strana_A**2)+(strana_B**2)-(strana_C**2))/(2*strana_A*strana_B)))

    global bod_ay
    global bod_ax
    bod_ax=(((b_x-c_x)**2+(b_y-c_y)**2)**(1/2))/2
    bod_ay=[b_x/2,b_y/2]

    #bod_b=[b_x,b_y,c_x/2,c_y/2]
    #bod_c=[c_x,c_y,a_x/2,a_y/2]
    
    
    # Funkce if, která rozhodne, jestli se vůbec vykreslí trojúhelník, nebo ne
    if strana_A+strana_B>strana_C and strana_B+strana_C>strana_A and strana_A+strana_C>strana_B:
        # Pokud lze narýsovat potom:
        print("Trojúhelník lze narýsovat")

        # Spustí kresbu na canvas a vypsání všech informací na canvas:
        kresba()

        # Vypíše souřadnice do konzole:
        print("  ","X","   ","Y")
        print("A",a_x,",",a_y)
        print("B",b_x,",",b_y)
        print("C",c_x,",",c_y)

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
    
    canvas.create_line(a_x,a_y,b_x,b_y,fill="blue",width=5,)
    canvas.create_line(b_x,b_y,c_x,c_y,fill="blue",width=5)
    canvas.create_line(c_x,c_y,a_x,a_y,fill="blue",width=5)
    canvas.create_text(bod_ax,bod_ay,fill="black",font="Times 10",text=("a"),anchor="w")
    
    canvas.create_text()
    # Vypíše informace o trojúhelníku na canvas, ať nejsou vypsané jenom v konzoli

    # Souřadnice bodů:
    canvas.create_text(155,635,fill="black",font="Times 10",text=("X   Y"),anchor="w")
    canvas.create_text(25,650,fill="black",font="Times 10",text=("Souřadnice bodu A:",a_x,a_y),anchor="w")
    canvas.create_text(25,665,fill="black",font="Times 10",text=("Souřadnice bodu B:",b_x,b_y),anchor="w")
    canvas.create_text(25,680,fill="black",font="Times 10",text=("Souřadnice bodu C:",c_x,c_y),anchor="w")

    # Nadepsání bodů
    canvas.create_text(a_x-20,a_y-20,fill="black",font="Times 20",text="A",anchor="w")
    canvas.create_text(b_x+20,b_y-20,fill="black",font="Times 20",text="B",anchor="w")
    canvas.create_text(c_x-20,c_y+20,fill="black",font="Times 20",text="C",anchor="w")

    # Délky stran:
    canvas.create_text(200,650,fill="black",font="Times 10",text=("Délka strany A:",strana_A),anchor="w")
    canvas.create_text(200,665,fill="black",font="Times 10",text=("Délka strany B:",strana_B),anchor="w")
    canvas.create_text(200,680,fill="black",font="Times 10",text=("Délka strany C:",strana_C),anchor="w")
    
    # Obvod a obsah:
    canvas.create_text(350,650,fill="black",font="Times 10",text=("Obvod:",obvod,"px"),anchor="w")
    canvas.create_text(350,665,fill="black",font="Times 10",text=("Obsah:",obsah,"px²"),anchor="w")

    # Úhly:
    canvas.create_text(470,650,fill="black",font="Times 10",text=("Úhel alfa:",alfa,"°"),anchor="w")
    canvas.create_text(470,665,fill="black",font="Times 10",text=("Úhel beta:",beta,"°"),anchor="w")
    canvas.create_text(470,680,fill="black",font="Times 10",text=("Úhel gama:",gama,"°"),anchor="w")



button1 = tk.Button(text='Nakresli Trojuholnik', command=vypocty)

canvas.create_window(500, 200, window=button1)

root.mainloop()

# Následně program spustí výpočet, ve kterém je už kresba nadefinovaná a proběhne pouze pokud se dá trojúhelník narýsovat:
vypocty()

# Toto nevíme, co dělá, ale nepůjde to bez toho:
canvas.mainloop()
    

