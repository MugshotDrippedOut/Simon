import math
import matplotlib.pyplot as plt

Rv = 11_040_000
Ra = 5.6
Rwi =5.2
Rwu =2006

LbezJadra = 0.31
LsJadrom = 0.752
Ckapacita = 0.000_025


Ug = [30, 35, 40, 45, 50]

def Pwx(Ug, Rwu):
    return (Ug**2)/(Rwu)

Pwx1 = [Pwx(i, Rwu) for i in Ug]
print("Pwx")
for i in Pwx1:
    print(round(i,3))


def Px(Ug, Rv):
    return (Ug**2)/(Rv)

print("\nPx")
Px1 = [Px(i, Rv) for i in Ug]

for i in Px1:
    print(round(i*1_000_000,2))


PbezJadra = [2,2.75,3.25,4.25,5.25]
PsJadrom = [1.5,1.75,2.25,2.75,3.5]
def Pz(P, Pwx, Px):
    return round(P - Pwx - Px, 2)
print("\nPz")
for p in PbezJadra:
    print(f"{Ug[PbezJadra.index(p)]} => {Pz(p, Pwx1[0], Px1[0])}")
""" 
print("\nPz")
for p in PsJadrom:
    print(f"{Ug[PsJadrom.index(p)]} => {Pz(p, Pwx1[0], Px1[0])}") """