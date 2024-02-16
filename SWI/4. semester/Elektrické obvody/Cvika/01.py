import matplotlib.pyplot as plt

# Rx Merany odpor = (Rxx*Rv)/(Rv-Rxx)
# Rxx Vypocet odporu vypočítaný z údajov meriacich prístrojov = (Uv/Ia)
# Ra Odpor amérmetra 
# perc Chyba merania v percentách
# P = U*I

# Prve merania
meranie1 = {
    "Uv": 20,
    "Ia": 0.091,
    "Ra": 6,
}

meranie2 = {
    "Uv": 16,
    "Ia": 0.073,
    "Ra": 6,

}

meranie3 = {
    "Uv": 12,
    "Ia": 0.055,
    "Ra": 6,

}

meranie4 = {
    "Uv": 8,
    "Ia": 0.036,
    "Ra": 6,

}

meranie5 = {
    "Uv": 4,
    "Ia": 0.017,
    "Ra": 8.5,
}


# Druhé merania

meranie6 = {
    "Uv": 20,
    "Ia": 0.000042,
    "Ra": 226,
}

meranie7 = {
    "Uv": 16,
    "Ia": 0.000034,
    "Ra": 226,
}

meranie8 = {
    "Uv": 12,
    "Ia": 0.000025,
    "Ra": 658,
}

meranie9 = {
    "Uv": 8,
    "Ia": 0.0000165,
    "Ra": 658,
}

meranie10 = {
    "Uv": 4,
    "Ia": 0.0000083,
    "Ra": 3130,
}


# Tretie merania

meranie11 = {
    "Uv": 20,
    "Ia": 0.091,
    "Rv": 1580000,
}

meranie12 = {
    "Uv": 16,
    "Ia": 0.073,
    "Rv": 1580000,
}

meranie13 = {
    "Uv": 12,
    "Ia": 0.055,
    "Rv": 1580000,
}

meranie14 = {
    "Uv": 8,
    "Ia": 0.036,
    "Rv": 500000,
}

meranie15 = {
    "Uv": 4,
    "Ia": 0.017,
    "Rv": 500000,
}

# Štvrté merania

meranie16 = {
    "Uv": 20,
    "Ia": 0.000042,
    "Rv": 1580000,
}

meranie17 = {
    "Uv": 16,
    "Ia": 0.000034,
    "Rv": 1580000,
}

meranie18 = {
    "Uv": 12,
    "Ia": 0.000025,
    "Rv": 1580000,
}

meranie19 = {
    "Uv": 8,
    "Ia": 0.0000165,
    "Rv": 500000,
}

meranie20 = {
    "Uv": 4,
    "Ia": 0.0000083,
    "Rv": 500000,
}


merania1 = [meranie1, meranie2, meranie3, meranie4, meranie5]
merania2 = [meranie6, meranie7, meranie8, meranie9, meranie10]
merania3 = [meranie11, meranie12, meranie13, meranie14, meranie15]
merania4 = [meranie16, meranie17, meranie18, meranie19, meranie20]

vsetky_merania = [merania1, merania2, merania3, merania4]

def vypocet_odporu(meranie):
    if "Rv" in meranie:
        Rxx = round((meranie["Uv"]/meranie["Ia"]),2)
        Rx = round((Rxx*meranie["Rv"])/(meranie["Rv"]-Rxx),2)
        print((Rxx*meranie["Rv"]), (meranie["Rv"]-Rxx))
        P = round((meranie["Uv"]*meranie["Ia"]),5)
        chyba = round(100-((Rxx/Rx)*100),5)
        return Rxx, Rx, P, chyba
    
    if "Rv" not in meranie:
        Ra = meranie["Ra"]
        Rxx = round((meranie["Uv"]/meranie["Ia"]),2)
        Raa = round((Rxx-Ra),2)
        P = round((meranie["Uv"]*meranie["Ia"]),5)
        chyba = round(100-((Raa/Rxx)*100),3)
        return Rxx, Raa, P, chyba

def vypis_merania(merania):
    for meranie in vsetky_merania:
        print(f"Meranie: {merania.index(meranie)+1}")
        for i in meranie:
            Rxx, Rx, P, chyba = vypocet_odporu(i)
            print(f"R'x: {Rxx} Ohm", f"     Rx: {Rx} Ohm", f"       P: {P} W", f"       Chyba: {chyba}%")
        print("\n\n")


vypis_merania(vsetky_merania)

# generovanie grafu

maraniaPreGraf = [[20,0.091],[18,0.082],[16,0.073],[14,0.064],[12,0.055],[10,0.046],[8,0.036],[6,0.026],[4,0.017],[2,0.0075]]

def generuj_graf(meranie):
    x = [i[0] for i in meranie]
    y = [i[1] for i in meranie]
    plt.xlabel('Uv')
    plt.ylabel('Ia')
    plt.title('Graf závislosti prúdu Ia na napätí Uv')
    plt.plot(x, y, marker = 'o')
    plt.show()
    
generuj_graf(maraniaPreGraf)