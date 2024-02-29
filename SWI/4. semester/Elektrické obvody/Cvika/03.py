import math
import matplotlib.pyplot as plt

prvaF =120 #hz f
druhaF = 520 #hz f
UlKonst = 7.14 #V Ul
tretiakonst = 33.5 #ohm R




# Prve merania
meranie1 = {
    "f" : prvaF,
    "Ug" : 10,
    "Ul": 7.14,
    "I" : 0.00936
}
meranie2 = {
    "f" : prvaF,
    "Ug" : 9,
    "Ul":  6.43,
    "I" : 0.00842
}

meranie3 = {
    "f" : prvaF,
    "Ug" : 8,
    "Ul": 5.72,
    "I" : 0.00748
}

meranie4 = {
    "f" : prvaF,
    "Ug" : 7,
    "Ul": 5.00,
    "I" : 0.00656
}

meranie5 = {
    "f" : prvaF,
    "Ug" : 6,
    "Ul": 4.30,
    "I" : 0.00562
}

meranie6 = {
    "f" : prvaF,
    "Ug" : 5,
    "Ul": 3.54,
    "I" : 0.00468
}


meranie7 = {
    "f" : prvaF,
    "Ug" : 4,
    "Ul": 2.84,
    "I" : 0.00374
}


meranie8 = {
    "f" : prvaF,
    "Ug" : 3,
    "Ul": 2.13,
    "I" : 0.00280
}


meranie9 = {
    "f" : prvaF,
    "Ug" : 2,
    "Ul": 1.43,
    "I" : 0.00186
}


meranie10 = {
    "f" : prvaF,
    "Ug" : 1,
    "Ul": 0.72,
    "I" : 0.00092
}

# Druhe merania

meranie11 = {
    "f" : druhaF,
    "Ug" : 10,
    "Ul": 7.14,
    "I" : 0.0021
}


meranie12 = {
    "f" : druhaF,
    "Ug" : 9,
    "Ul": 6.43,
    "I" : 0.00186
}


meranie13 = {
    "f" : druhaF,
    "Ug" : 8,
    "Ul": 5.72,
    "I" : 0.00164
}


meranie14 = {
    "f" : druhaF,
    "Ug" : 7,
    "Ul": 5.00,
    "I" : 0.00142
}


meranie15 = {
    "f" : druhaF,
    "Ug" : 6,
    "Ul": 4.30,
    "I" : 0.00122
}


meranie16 = {
    "f" : druhaF,
    "Ug" : 5,
    "Ul": 3.54,
    "I" : 0.00100
}

meranie17 = {
    "f" : druhaF,
    "Ug" : 4,
    "Ul": 2.84,
    "I" : 0.00078
}

meranie18 = {
    "f" : druhaF,
    "Ug" : 3,
    "Ul": 2.13,
    "I" : 0.00056
}

meranie19 = {
    "f" : druhaF,
    "Ug" : 2,
    "Ul": 1.43,
    "I" : 0.00032
}


meranie20 = {
    "f" : druhaF,
    "Ug" : 1,
    "Ul": 0.72,
    "I" : 0.00014
}

# 3. meranie
UgKonst = 10 #V

meranie21 = {
    "f" : 120,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.00934
}

meranie22 = {
    "f" : 220,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.0051
}

meranie23 = {
    "f" : 320,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.00348
}


meranie24 = {
    "f" : 420,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.0026
}


meranie25 = {
    "f" : 520,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.0021
}


meranie26 = {
    "f" : 620,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.0017
}


meranie27 = {
    "f" : 720,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.00142
}


meranie28 = {
    "f" : 820,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.00122
}


meranie29 = {
    "f" : 920,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.00100
}

meranie30 = {
    "f" : 1020,
    "Ug" : UgKonst,
    "Ul" : UlKonst,
    "I" : 0.0009
}



prve = [meranie1, meranie2, meranie3, meranie4, meranie5, meranie6, meranie7, meranie8, meranie9, meranie10]
druhe = [meranie11, meranie12, meranie13, meranie14, meranie15, meranie16, meranie17, meranie18, meranie19, meranie20]
tretie = [meranie21, meranie22, meranie23, meranie24, meranie25, meranie26, meranie27, meranie28, meranie29, meranie30]


merania = [prve, druhe]
def vypocetLs(meranie, odpor, frekvence):
    Ul = meranie["Ul"]
    I = meranie["I"]
    omega = 2 * math.pi * frekvence
    Ls = (1/omega) * math.sqrt((Ul/I)**2 - odpor**2)
    Ls = round(Ls, 3)
    return Ls

def vypocetZls(Ls, odpor, frekvence):
    omega = 2 * math.pi * frekvence
    Zls = math.sqrt((Ls**2)*(omega**2) + odpor**2)
    Zls = round(Zls, 1)
    return Zls

def vypocetXls(Ls, frekvence):
    omega = 2 * math.pi * frekvence
    Xls = Ls * omega
    Xls = round(Xls, 1)
    return Xls

def vypocetQ(Xls, odpor):
    Q = Xls / odpor
    Q = round(Q, 1)
    return Q

for meranie in merania:
    for x in meranie:
        print(f"Meranie: {meranie.index(x)+1}"+f"    f: {x['f']} Hz" + f"      Ug: {x['Ug']} V" + f"     Ul: {x['Ul']} V" + f"     I: {x['I']} A" + f"      Ls: {vypocetLs(x, tretiakonst, prvaF)} H")
        
    print("\n")
        #print(f"Meranie: {prve.index(meranie)+1}"+f"    f: {meranie['f']} Hz" + f"      Ug: {meranie['Ug']} V" + f"     Ul: {meranie['Ul']} V" + f"     I: {meranie['I']} A" + f"      Ls: {vypocetLs(meranie, tretiakonst, prvaF)} H")
    
for meranie in tretie:
    Ls = vypocetLs(meranie, tretiakonst, prvaF)
    Zls = vypocetZls(Ls, tretiakonst, prvaF)
    Xls = vypocetXls(Ls, prvaF)
    Q = vypocetQ(Xls, tretiakonst)
    print(f"Meranie: {tretie.index(meranie)+1}"+f"    f: {meranie['f']} Hz" + f"      Ug: {meranie['Ug']} V" + f"     Ul: {meranie['Ul']} V" + f"     I: {meranie['I']} A" + f"      Ls: {Ls} H" + f"      Zls: {Zls} Ohm" + f"      Xls: {Xls} Ohm" + f"      Q: {Q}")


def grafFZlsXls(meranie):
    #two graphs next ot each other
    f = []
    Zls = []
    Xls = []
    for x in meranie:
        f.append(x['f'])
        Ls = vypocetLs(x, tretiakonst, prvaF)
        Zls.append(vypocetZls(Ls, tretiakonst, prvaF))
        Xls.append(vypocetXls(Ls, prvaF))
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(f, Zls, marker = 'o')
    plt.title('Zls')
    plt.xlabel('f [Hz]')
    plt.ylabel('Zls [Ohm]')
    plt.subplot(1,2,2)
    plt.plot(f, Xls, marker = 'o')
    plt.title('Xls')
    plt.xlabel('f [Hz]')
    plt.ylabel('Xls [Ohm]')
    plt.show()
    
def grafUgI(prve, druhe):
    Ug1 = []
    I1 = []
    Ug2 = []
    I2 = []
    for x in prve:
        Ug1.append(x['Ug'])
        I1.append(x['I'])
    for x in druhe:
        Ug2.append(x['Ug'])
        I2.append(x['I'])
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1) 
    plt.plot(Ug1, I1, marker = 'o')
    plt.title('Prve meranie')
    plt.xlabel('Ug [V]')
    plt.ylabel('I [A]')
    plt.subplot(1,2,2)
    plt.plot(Ug2, I2, marker = 'o')
    plt.title('Druhe meranie')
    plt.xlabel('Ug [V]')
    plt.ylabel('I [A]')
    plt.show()
    

def grafFQFLs(meranie):
    f = []
    Q = []
    Ls = []
    for x in meranie:
        f.append(x['f'])
        Ls.append(vypocetLs(x, tretiakonst, prvaF))
        Xls = vypocetXls(Ls[-1], prvaF)
        Q.append(vypocetQ(Xls, tretiakonst))
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(f, Ls, marker = 'o')
    plt.title('Ls')
    plt.xlabel('f [Hz]')
    plt.ylabel('Ls [H]')
    plt.subplot(1,2,2)
    plt.plot(f, Q, marker = 'o')
    plt.title('Q')
    plt.xlabel('f [Hz]')
    plt.ylabel('Q')
    plt.show()


def graphs(prve,druhe,tretie):
    fTretie= []
    ZlsTretie = []
    XlsTretie = []
    for x in tretie:
        fTretie.append(x['f'])
        Ls = vypocetLs(x, tretiakonst, prvaF)
        Zls = vypocetZls(Ls, tretiakonst, prvaF)
        ZlsTretie.append(Zls)
        Xls = vypocetXls(Ls, prvaF)
        XlsTretie.append(Xls)
    plt.figure(figsize=(10,5))
    plt.subplot(3,2,1)
    plt.plot(fTretie, ZlsTretie, marker = 'o')
    plt.title('Frekvenční závislost impedance')
    plt.xlabel('f [Hz]')
    plt.ylabel('Zls [Ohm]')
    plt.subplot(3,2,2)
    plt.plot(fTretie, XlsTretie, marker = 'o')
    plt.title('Frekvenční závislost reaktance')
    plt.xlabel('f [Hz]')
    plt.ylabel('Xls [Ohm]')
    Ug1 = []
    I1 = []
    Ug2 = []
    I2 = []
    for x in prve:
        Ug1.append(x['Ug'])
        I1.append(x['I'])
    for x in druhe:
        Ug2.append(x['Ug'])
        I2.append(x['I'])
    plt.subplot(3,2,3)
    plt.plot(Ug1, I1, marker = 'o')
    plt.title('Voltamperová charakteristika pro 120Hz')
    plt.xlabel('Ug [V]')
    plt.ylabel('I [A]')
    plt.subplot(3,2,4)
    plt.plot(Ug2, I2, marker = 'o')
    plt.title('Voltamperová charakteristika pro 520Hz')
    plt.xlabel('Ug [V]')
    plt.ylabel('I [A]')
    QTretie = []
    LsTretie = []
    for x in tretie:
        Ls = vypocetLs(x, tretiakonst, prvaF)
        LsTretie.append(Ls)
        Xls = vypocetXls(Ls, prvaF)
        Q = vypocetQ(Xls, tretiakonst)
        QTretie.append(Q)
    plt.subplot(3,2,5)
    plt.plot(fTretie, LsTretie, marker = 'o')
    plt.title('Frekvenční závislost indukčnosti')
    plt.xlabel('f [Hz]')
    plt.ylabel('Ls [H]')
    plt.subplot(3,2,6)
    plt.plot(fTretie, QTretie, marker = 'o')
    plt.title('Frekvenční závislost činitele')
    plt.xlabel('f [Hz]')
    plt.ylabel('Q')
    plt.subplots_adjust(hspace = 0.9, wspace = 0.5)

    plt.show()
    
    
# grafFZlsXls(tretie)
# grafUgI(prve,druhe)
# grafFQFLs(tretie)

graphs(prve,druhe,tretie)
    
    