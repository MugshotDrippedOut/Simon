import math
import matplotlib.pyplot as plt

Rv = 11_040_000
Ra = 5.6
Rwi =5.2
Rwu =2006

L_bezJadra = 0.31
L_sJadrom = 0.752
C_kapacita = 0.000_025

Ug = [30, 35, 40, 45, 50]

U_bezJadra = [29.95,35.45,39.6,44.9,50]
U_sJadrom = [30, 35.3,40.1,45.5,49.8]
U_pkk = [30.2, 34.6, 39.9 ,44.7,50]

# I je v mA
I_bezJadra = [63.4, 75, 82, 94.6,107]
I_sJadrom = [50,59,66.6,75.4,82.6]
I_Pkk = [236.6, 271.4, 314, 374.6, 389.2]

P_bezJadra = [2,2.75,3.25,4.25,5.25]
P_sJadrom = [1.5,1.75,2.25,2.75,3.5]
P_pkk = [1,1.25,1.5,1.75,2] # Paralelni kombinace kondenzatoru

def Pwu(U, Rwu):
    return (U**2)/(Rwu)

def Pwi(I,Rwi):
    I = I/1_000 # mA -> A
    return (I**2) * Rwi


def Pu(U, Rv):
    return (U**2)/(Rv)

def Pi(I, Ra):
    I = I/1_000 # mA -> A
    return (I**2) * Ra

def Pzu(P, Pwu, Pu):
    return P - Pwu - Pu

def Pzi(P, Pwi, Pi):
    return P - Pwi - Pi

def absChyba(teoreticky, mereny):
    return abs(teoreticky - mereny)

def relChyba(teoreticky, mereny):
    return abs((teoreticky - mereny)/mereny) * 100

Pwu_res = [Pwu(i, Rwu) for i in Ug]
Pwi_res = [Pwi(i, Rwi) for i in I_bezJadra]
Pu_res = [Pu(i, Rv) for i in Ug]

Pwu_bezJadra_res = [Pwu(i, Rwu) for i in U_bezJadra]
Pwu_sJadrom_res = [Pwu(i, Rwu) for i in U_sJadrom]
Pwu_pkk_res = [Pwu(i, Rwu) for i in U_pkk]

Pwi_bezJadra_res = [Pwi(i, Rwi) for i in I_bezJadra]
Pwi_sJadrom_res = [Pwi(i, Rwi) for i in I_sJadrom]
Pwi_pkk_res = [Pwi(i, Rwi) for i in I_Pkk]

Pu_bezJadra_res = [Pu(i, Rv) for i in U_bezJadra]
Pu_sJadrom_res = [Pu(i, Rv) for i in U_sJadrom]
Pu_pkk_res = [Pu(i, Rv) for i in U_pkk]

Pi_bezJadra_res = [Pi(i, Ra) for i in I_bezJadra]
Pi_sJadrom_res = [Pi(i, Ra) for i in I_sJadrom]
Pi_pkk_res = [Pi(i, Ra) for i in I_Pkk]

Pzu_bezJadra_res = [Pzu(P_bezJadra[i], Pwu_bezJadra_res[i], Pu_bezJadra_res[i]) for i in range(len(Ug))]
Pzu_sJadrom_res = [Pzu(P_sJadrom[i], Pwu_sJadrom_res[i], Pu_sJadrom_res[i]) for i in range(len(Ug))]
Pzu_pkk_res = [Pzu(P_pkk[i], Pwu_pkk_res[i], Pu_pkk_res[i]) for i in range(len(Ug))]

Pzi_bezJadra_res = [Pzi(P_bezJadra[i], Pwi_bezJadra_res[i], Pi_bezJadra_res[i]) for i in range(len(Ug))]
Pzi_sJadrom_res = [Pzi(P_sJadrom[i], Pwi_sJadrom_res[i], Pi_sJadrom_res[i]) for i in range(len(Ug))]
Pzi_pkk_res = [Pzi(P_pkk[i], Pwi_pkk_res[i], Pi_pkk_res[i]) for i in range(len(Ug))]


Rel_beJadra = [relChyba(P_bezJadra[i], Pzi_bezJadra_res[i]) for i in range(len(Ug))]
Rel_sJadrom = [relChyba(P_sJadrom[i], Pzi_sJadrom_res[i]) for i in range(len(Ug))]
Rel_pkk = [relChyba( Pzi_pkk_res[i],P_pkk[i]) for i in range(len(Ug))]

# Výpočet výkonů spotřebovaných wattmetrem, voltmetrem, ampérmetrem a zátěží
print("Prve zapojeni")
print("Bez jadra")
print("|  Ug[V]  |  Pwi[W]  |  Pi[W]  |  P1z[W]  | Rel. chyba[%]  |")
for i in range(len(Ug)):
    print(f"|  {Ug[i]:<6} | {Pwi_bezJadra_res[i]:<8.2f} | {Pi_bezJadra_res[i]:<8.2f} | {Pzi_bezJadra_res[i]:<9.2f} | {Rel_beJadra[i]:<5.2f}% |")

print("\nS Jadrem")
print("|  Ug[V]  |  Pwi[W]  |  Pi[W]  |  P1z[W]  | Rel. chyba[%]  |")
for i in range(len(Ug)):
    print(f"|  {Ug[i]:<6} | {Pwi_sJadrom_res[i]:<8.2f} | {Pi_sJadrom_res[i]:<8.2f} | {Pzi_sJadrom_res[i]:<9.2f} | {Rel_sJadrom[i]:<5.2f}% |")
    
print("\nParalelni kombinace kondenzatoru")
print("|  Ug[V]  |  Pwi[W]  |  Pi[W]  |  P1z[W]  | Rel. chyba[%]  |")
for i in range(len(Ug)):
    print(f"|  {Ug[i]:<6} | {Pwi_pkk_res[i]:<8.2f} | {Pi_pkk_res[i]:<8.2f} | {Pzi_pkk_res[i]:<9.2f} | {Rel_pkk[i]:<5.2f}% |")
# Teoretický výpočet činného, zdánlivého a jalového výkonu 
# symbolicko-komplexní metodou pro jednotlivé zátěží
def Z(U,I):
    return U/(I/1_000)

def S(U,I):
    return U*(I/1_000)

def Q(S, P):
    # využití Pythagorovy věty
    try:
        return math.sqrt(S**2 - P**2)
    except:
        return -1

Z_bezJadra = [Z(Ug[i], I_bezJadra[i]) for i in range(len(Ug))]
Z_sJadrom = [Z(Ug[i], I_sJadrom[i]) for i in range(len(Ug))]
Z_pkk = [Z(Ug[i], I_Pkk[i]) for i in range(len(Ug))]

S_bezJadra = [S(Ug[i], I_bezJadra[i]) for i in range(len(Ug))]
S_sJadrom = [S(Ug[i], I_sJadrom[i]) for i in range(len(Ug))]
S_pkk = [S(Ug[i], I_Pkk[i]) for i in range(len(Ug))]

print("\Vypocet cinneho, zdanliveho a jaloveho vykonu")
print("\nBez jadra")
print("|  Ug[V]  |  Z[Ohm]  |  I[mA]  |  P[W]  |  Q[VAr]  |  S[VA]  |")
for i in range(len(Ug)):
    print(f"|  {Ug[i]:<6} | {Z_bezJadra[i]:<8.3f} | {I_bezJadra[i]:<7.1f} | {Pzi_bezJadra_res[i]:<5.2f} | {Q(S_bezJadra[i], Pzi_bezJadra_res[i]):<8.3f} | {S_bezJadra[i]:<6.2f} |")
    
print("\nS Jadrem")
print("|  Ug[V]  |  Z[Ohm]  |  I[mA]  |  P[W]  |  Q[VAr]  |  S[VA]  |")
for i in range(len(Ug)):
    print(f"|  {Ug[i]:<6} | {Z_sJadrom[i]:<8.3f} | {I_sJadrom[i]:<7.1f} | {Pzi_sJadrom_res[i]:<5.2f} | {Q(S_sJadrom[i], Pzi_sJadrom_res[i]):<8.3f} | {S_sJadrom[i]:<6.2f} |")

print("\nParalelni kombinace kondenzatoru")
print("|  Ug[V]  |  Z[Ohm]  |  I[mA]  |  P[W]  |  Q[VAr]  |  S[VA]  |")
for i in range(len(Ug)):
    print(f"|  {Ug[i]:<6} | {Z_pkk[i]:<8.3f} | {I_Pkk[i]:<7.1f} | {Pzi_pkk_res[i]:<5.2f} | {Q(S_pkk[i], Pzi_pkk_res[i]):<9.3f}| {S_pkk[i]:<6.2f} |")   
