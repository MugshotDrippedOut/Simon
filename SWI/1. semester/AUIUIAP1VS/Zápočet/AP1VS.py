import tkinter
import math
from math import degrees,acos
kanvas = tkinter.Canvas(height=700, width=700)
kanvas.pack()

def trojuhelnik():
    # Program vypíše informace pro uživatele
    print("Canvas má rozmezí 700x600 px\nPro vykreslení je potřeba zadat kladné hodnoty\n1 cm = 37.7952755906 pixelů")
    # Nadefinování souřadnic bodu A, následně program čeká na zadání souřadnic uživatelem
    print("Zadej hodnotu pro bod A:")

    global a_x
    global a_y
    
    a_x=input("Hodnota bodu A pozice X")
    a_y=input("Hodnota bodu A pozice Y")

    
    # Nadefinování souřadnic bodu B, následně program čeká na zadání souřadnic uživatelem
    print("Zadaj hodnotu pro bod B:")

    global b_x
    global b_y
    
    b_x=int(input("Hodnota bodu B pozice X"))
    b_y=int(input("Hodnota bodu B pozice Y"))

    # Nadefinování souřadnic bodu C, následně program čeká na zadání souřadnic uživatelem
    print("Zadaj hodnotu pro bod C:")

    global c_x
    global c_y
    
    c_x=int(input("Hodnota bodu C pozice X"))
    c_y=int(input("Hodnota bodu C pozice Y"))
       
def vypocty():
    
    # Definice a následující výpočet strany A
    global strana_A
    strana_A = (((b_x-c_x)**2+(b_y-c_y)**2)**0.5)
    strana_A = round(strana_A,2)

    # Definice a následující výpočet strany B
    global strana_B
    strana_B= (((c_x-a_x)**2+(c_y-a_y)**2)**0.5)
    strana_B = round(strana_B,2)

    # Definice a následující výpočet strany C
    global strana_C
    strana_C = (((a_x-b_x)**2+(a_y-b_y)**2)**0.5)
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

    # Zaokrouhlení úhlů:
    alfa = round(alfa)
    beta = round(beta)
    gama = round(gama)

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
            kanvas.create_text(470,635,fill="black",font="Times 10",text="Trojúhelník je pravoúhlý",anchor="w")
        else:
            # Vypíše, že není pravoúhlý do konzole
            print("Trojuhelník není pravoúhlý") 

            # Vypíše, že není pravoúhlý na canvas
            kanvas.create_text(470,635,fill="black",font="Times 10",text="Trojúhelník není pravoúhlý",anchor="w")

    else:
        # Pokud nelze narýsovat, potom:
        print("Trojúhelník nelze narýsovat")

        # Vypíše i na canvas, že nelze narýsovat trojúhelník:
        kanvas.create_text(100,100,fill="red",font="Times 30",text="Trojúhelník nelze narýsovat",anchor="w")
        
def kresba():
    # Narýsuje trojúhelník
    kanvas.create_line(a_x,a_y,b_x,b_y,c_x,c_y,a_x,a_y,fill="blue",width=5)

    # Vypíše informace o trojúhelníku na canvas, ať nejsou vypsané jenom v konzoli

    # Souřadnice bodů:
    kanvas.create_text(155,635,fill="black",font="Times 10",text=("X   Y"),anchor="w")
    kanvas.create_text(25,650,fill="black",font="Times 10",text=("Souřadnice bodu A:",a_x,a_y),anchor="w")
    kanvas.create_text(25,665,fill="black",font="Times 10",text=("Souřadnice bodu B:",b_x,b_y),anchor="w")
    kanvas.create_text(25,680,fill="black",font="Times 10",text=("Souřadnice bodu C:",c_x,c_y),anchor="w")

    # Nadepsání bodů
    kanvas.create_text(a_x-20,a_y-20,fill="black",font="Times 20",text="A",anchor="w")
    kanvas.create_text(b_x+20,b_y-20,fill="black",font="Times 20",text="B",anchor="w")
    kanvas.create_text(c_x-20,c_y+20,fill="black",font="Times 20",text="C",anchor="w")

    # Délky stran:
    kanvas.create_text(200,650,fill="black",font="Times 10",text=("Délka strany A:",strana_A),anchor="w")
    kanvas.create_text(200,665,fill="black",font="Times 10",text=("Délka strany B:",strana_B),anchor="w")
    kanvas.create_text(200,680,fill="black",font="Times 10",text=("Délka strany C:",strana_C),anchor="w")
    
    # Obvod a obsah:
    kanvas.create_text(350,650,fill="black",font="Times 10",text=("Obvod:",obvod,"px"),anchor="w")
    kanvas.create_text(350,665,fill="black",font="Times 10",text=("Obsah:",obsah,"px²"),anchor="w")

    # Úhly:
    kanvas.create_text(470,650,fill="black",font="Times 10",text=("Úhel alfa:",alfa,"°"),anchor="w")
    kanvas.create_text(470,665,fill="black",font="Times 10",text=("Úhel beta:",beta,"°"),anchor="w")
    kanvas.create_text(470,680,fill="black",font="Times 10",text=("Úhel gama:",gama,"°"),anchor="w")


# Program spustí metodu definice souřadnic:
trojuhelnik()

# Následně program spustí výpočet, ve kterém je už kresba nadefinovaná a proběhne pouze pokud se dá trojúhelník narýsovat:
vypocty()

# Toto nevíme, co dělá, ale nepůjde to bez toho:
kanvas.mainloop()