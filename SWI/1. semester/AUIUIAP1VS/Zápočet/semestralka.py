import tkinter
canvas=tkinter.Canvas()
canvas.pack()


def trojuholnik():
    print("Zadaj hodnotu pre bod A:")
    global a_x
    a_x=int(input("Hodnota bodu A pozicia X"))
    global a_y
    a_y=int(input("Hodnota bodu A pozicia Y"))
    print("Zadaj hodnotu pre bod B:")
    global b_x
    b_x=int(input("Hodnota bodu B pozicia X"))
    global b_y
    b_y=int(input("Hodnota bodu B pozicia Y"))
    print("Zadaj hodnotu pre bod C:")
    global c_x
    c_x=int(input("Hodnota bodu C pozicia X"))
    global c_y
    c_y=int(input("Hodnota bodu C pozicia Y"))
    print("  ","X","","Y")
    print("A",a_x,",",a_y)
    print("B",b_x,",",b_y)
    print("C",c_x,",",c_y)
    strana_A=((a_x - b_x)**2+(a_y - b_y)**2)**(1/2)
    strana_A =round(strana_A, 2)
    print("strana A:",strana_A)
    strana_B=((b_x - c_x)**2+(b_y - c_y)**2)**(1/2)
    strana_B =round(strana_B, 2)
    print("strana B:",strana_B)
    strana_C=((a_x - c_x)**2+(a_y - c_y)**2)**(1/2)
    strana_C =round(strana_C, 2)
    print("strana C:",strana_C)
    print("Obvod:",strana_A+strana_B+strana_C)
    s=(strana_A+strana_B+strana_C)/2
    obsah=(s*(s-strana_A)*(s-strana_B)*(s-strana_C))**(1/2)
    obsah=round(obsah, 2)
    print("obsah:",obsah)
    
    if strana_A+strana_B>strana_C and strana_B+strana_C>strana_A and strana_A+strana_C>strana_B:
        print("Trojúhelník lze narýsovat")
    else:
        print("Trojúhelník nelze narýsovat")
    if strana_A**2+strana_B**2==strana_C**2 or strana_B**2+strana_C**2==strana_A**2 or strana_A**2+strana_C**2==strana_B**2:
        print("je pravouhly")
    else:
        print("nie je pravouhly")
        
def kresba():
    canvas.create_line(20*a_x**2,20*a_y**2,20*b_x**2,20*b_y**2)
    canvas.create_oval((20*a_x**2)/2,(20*a_y**2),(20*b_x**2)/2,(20*b_y**2))
    canvas.create_line(20*b_x**2,20*b_y**2,20*c_x**2,20*c_y**2)    
    canvas.create_line(20*a_x**2,20*a_y**2,20*c_x**2,20*c_y**2)
    
trojuholnik()
kresba()
canvas.create_line(a_x,a_y,b_x,b_y)
