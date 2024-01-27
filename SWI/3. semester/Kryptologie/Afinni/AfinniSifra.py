import tkinter as tk
from tkinter import Entry, END, Button, Label, W, messagebox, NSEW
from unidecode import unidecode


"""Okno"""
window = tk.Tk()
window.title('Afinní Šifra')
window.geometry('475x240')
window.minsize(475, 240)
window.configure(bg='#2b303a')
window.eval('tk::PlaceWindow . center')


"""Definovanie abecedy a modulo"""
abeceda=["A","B","C","D","E","F","G","H","I","J","K","L","M",
         "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
modulo=len(abeceda)


"""Entry pre parameter a"""
labelPreZadanieParametruA = Label(window, text="Parameter A:", anchor=W)
labelPreZadanieParametruA.grid(column=0, row=0, sticky=W)
entryPreZadanieParametruA = Entry(window, width=6)
entryPreZadanieParametruA.place(in_=labelPreZadanieParametruA,relx=1.0, x=2, rely=0)
entryPreZadanieParametruA.insert(0,"5")


"""Entry pre parameter b"""
labelPreZadanieParametruB = Label(window, text="Parameter B:", anchor=W)
labelPreZadanieParametruB.grid(column=1, row=0, columnspan = 26, sticky= W)
entryPreZadanieParametruB = Entry(window, width=6)
entryPreZadanieParametruB.place(in_=labelPreZadanieParametruB,relx=1.0, x=2, rely=0)
entryPreZadanieParametruB.insert(0,"9")


"""Entry pre vloženie textu a jeho label"""
labelPreZadanieTextu = Label(window, text="Vložte text:", width=15, bg="#92dce5")
labelPreZadanieTextu.grid(column=0, row=1)
entryPreZadanieTextu = Entry(window, width= 60)
entryPreZadanieTextu.grid(column=1, row=1, columnspan = 26, sticky= W)
entryPreZadanieTextu.insert(0,"Ahoj Pepo, sejdeme se v 5 u mostu.")


"""Tlačítko pre filtrvanie"""
buttonPreFiltrovanie = Button(window,text="Filtrovať",  bg="#7c7c7c",
                            command=lambda:(VlozenieTextuDoEntry(entryPreFiltrovanieTextu, filtrovanie(Vybranie_textu_z_entry(entryPreZadanieTextu))),
                                            prepis_zasifrovanej_abecedy()))
buttonPreFiltrovanie.grid(column=1, row=2, columnspan = 26, sticky= W)


"""Entry pre vloženie filtrovaného textu"""
labelPreFiltrovanyText =Label(window, text="Filtrovaný text:", width=15, bg="#92dce5")
labelPreFiltrovanyText.grid(column=0, row=3)
entryPreFiltrovanieTextu = Entry(window, width= 60)
entryPreFiltrovanieTextu.grid(column=1, row=3, columnspan = 26, sticky= W)


"""Tlačítko pre Zašifrovanie"""
buttonPreZasifrovanie = Button(window, text="Zašifrovať", bg="#7c7c7c", 
                            command= lambda:(VlozenieTextuDoEntry(entryPreZasifrovanyText,Zasifrovanie(Vybranie_textu_z_entry(entryPreFiltrovanieTextu))),
                                                prepis_zasifrovanej_abecedy()))
buttonPreZasifrovanie.grid(column=1, row=4, columnspan = 26, sticky= W)


"""Entry pre vloženie zašifrovaného textu"""
labelPreZasifrovanyText = Label(window, text="Zašifrovaný text:", width=15, bg="#92dce5")
labelPreZasifrovanyText.grid(column=0, row=5)
entryPreZasifrovanyText = Entry(window, width= 60)
entryPreZasifrovanyText.grid(column=1, row=5, columnspan = 26, sticky= W)


"""Tlačítko pre dešifrovanie"""
buttonPreDesifrovanie = Button(window, text="Dešifrovať", bg="#7c7c7c", 
                            command=lambda:(VlozenieTextuDoEntry(entryPreDesifrovanyText,Desifrovanie(Vybranie_textu_z_entry(entryPreZasifrovanyText))),
                                            prepis_zasifrovanej_abecedy()))
buttonPreDesifrovanie.grid(column=1, row=6, columnspan = 26, sticky= W)


"""Entry pre vloženie dešifrovanie textu"""
labelPreDesifrovanyText = Label(window, text="Dešifrovaný text:", width=15, bg="#92dce5")
labelPreDesifrovanyText.grid(column=0, row=7)
entryPreDesifrovanyText = Entry(window, width= 60)
entryPreDesifrovanyText.grid(column=1, row=7, columnspan = 26, sticky= W)


"""Vypisanie abecedy"""
labelPreAbecedu = Label(window, text="Abeceda", bg="#92dce5")
labelPreAbecedu.grid(column=0, row=8, sticky=NSEW)


a = 0
for (character) in abeceda:
    Label(window, text= character, width=1).grid( column= a+1, row= 8, sticky= W)
    a+=1
    
AL = []
ALCisla =[]
for i in range(0,26):
    ALCisla.append(str(i))


"""Vypisanie zašifrovanej abecedy"""
labelPreAbecedu = Label(window, text="Zašifrovaná", bg="#92dce5")
labelPreAbecedu.grid(column=0, row=9, sticky=NSEW)


def zasifrovana_abeceda():
    if str(Vybranie_textu_z_entry(entryPreZadanieParametruA))=="" or str(Vybranie_textu_z_entry(entryPreZadanieParametruB))=="":
        return
    if mod_inverse(int(Vybranie_textu_z_entry(entryPreZadanieParametruA)),modulo) == -1:
        return    
    a=0
    for character in ALCisla:
        temp = abeceda[int(character)]
        label = Label(window, text= str(abeceda[(int(Vybranie_textu_z_entry(entryPreZadanieParametruA))*ziskaj_index(temp)
                                     + int(Vybranie_textu_z_entry(entryPreZadanieParametruB)))%modulo]), width=1)
        label.grid( column= a+1, row= 9, sticky= W)
        AL.append(label)
        a+=1


def prepis_zasifrovanej_abecedy():
    if str(Vybranie_textu_z_entry(entryPreZadanieParametruA))=="" or str(Vybranie_textu_z_entry(entryPreZadanieParametruB))=="":
        return
    if mod_inverse(int(Vybranie_textu_z_entry(entryPreZadanieParametruA)),modulo) == -1 :
        return 
    for x, l in zip(ALCisla,AL):
        temp = str(abeceda[(int(Vybranie_textu_z_entry(entryPreZadanieParametruA))*ziskaj_index(abeceda[int(x)])
                                     + int(Vybranie_textu_z_entry(entryPreZadanieParametruB)))%modulo])
        l.config(text=temp)
    
    
"""Filtrovanie"""
def filtrovanie(txt):
    kontrola = vypisanie_error_message(entryPreZadanieParametruA,entryPreZadanieParametruB, modulo)
    if kontrola == False:
        return
    fitxt = ""
    exclude ="Łł][Đđ}{@&#>'€|"
    for character in txt:
        if(character == " "):
            fitxt += "XMEZERAX"
        if(character.isalnum()==True) and (character in exclude) == False:
            fitxt = fitxt + str((unidecode(character)).upper())
        else:
            fitxt += ""
    return fitxt


"""Zašifrovanie"""
def Zasifrovanie(txt):
    kontrola = vypisanie_error_message(entryPreZadanieParametruA,entryPreZadanieParametruB, modulo)
    if kontrola == False:
        return
    entxt =""
    for character in txt:
        if(character.isalpha()==True):
            entxt += str(abeceda[(int(Vybranie_textu_z_entry(entryPreZadanieParametruA))*ziskaj_index(character)
                                     + int(Vybranie_textu_z_entry(entryPreZadanieParametruB)))%modulo]) 
        if(character.isnumeric()==True):
            entxt += character 
    entxtsm = Pridanie_medzier(entxt, 5)     
    return entxtsm


"""Dešifrovanie"""
def Desifrovanie(txt):
    kontrola = vypisanie_error_message(entryPreZadanieParametruA,entryPreZadanieParametruB, modulo)
    if kontrola == False:
        return
    txt = Odstranenie_medzier(txt)
    detxt = ""   
    for character in txt:
        if(character.isalpha()==True):
            detxt += str(abeceda[(((ziskaj_index(character)-int(Vybranie_textu_z_entry(entryPreZadanieParametruB)))
                                          *mod_inverse(int(Vybranie_textu_z_entry(entryPreZadanieParametruA)),modulo))%modulo)])
        else:
            detxt+=character
    detxt = detxt.replace("XMEZERAX", " ")
    return detxt


"""Získannie indexu"""
def ziskaj_index(txt):
    return abeceda.index(txt)


"""Pridanie medzier"""
def Pridanie_medzier(txt, cislo):
    res= ""
    for i in range(0, len(txt),cislo):
        res += txt[i:i+cislo] + " "
    return res


"""Odstranenie medzier"""
def Odstranenie_medzier(txt):
    res = ""
    for character in txt:
        if (character== " "):
            res += ""
        else:
            res += character
    return res
    

"""Inverzia modula"""
def mod_inverse(parA , modulo):
    for x in range(1,modulo):
        if (((parA%modulo) * (x%modulo))%modulo == 1):
            return x
    return -1


"""Vkladanie vyber z entry"""
def Vybranie_textu_z_entry(entry):
    a = entry.get()
    return a


def VlozenieTextuDoEntry(entry, text):
    text = str(text)
    entry.delete(0,END)
    entry.insert(0,text)
    
    
"""Error message"""
def error_message_zle_cislo():
    messagebox.showerror("python error","Error: Nezadali ste adekvátne číslo pre parameter A\n          skúste napríklad 5")


def error_message_zly_text():
    messagebox.showerror("python error","Error: Parametre obsahujú nesprávne znaky")


"""Vypísanie error message"""
def vypisanie_error_message(parA,parB, modulo):
    kontrola = kontrola_parametrov(Vybranie_textu_z_entry(parA),Vybranie_textu_z_entry(parB))
    if kontrola ==False or Vybranie_textu_z_entry(parA) == '' or Vybranie_textu_z_entry(parB) == '':
        error_message_zly_text()
        return False 
    if (mod_inverse(int(Vybranie_textu_z_entry(parA)),modulo)==-1) :
        error_message_zle_cislo()
        return False
    else: return True


def kontrola_parametrov(parameter_a,parameter_b):
    povolene = "0123456789"
    if all(ch in povolene for ch in parameter_a) and all(ch in povolene for ch in parameter_b):
        return True
    else:
        return False


zasifrovana_abeceda()
window.mainloop()