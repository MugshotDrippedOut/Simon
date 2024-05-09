# Dynamicke programovanie
# potrebujem zakladnu funkciu, omezenie a kroky
# import math
# import re
# 
# 
# funkcia = input("Zadajte funkciu:\n format: x^2 + 3y^2\n") # x y z 
# omezenie = input("Zadajte omezenie:\n format: x^2 + y^2 <= 1\n")
# kroky = input("Zadajte kroky:\n format: 0.1\n")
# 
# class DynamickeProgramovanie:
#     def __init__(self, funkcia, omezenie, kroky):
#         self.funkcia = funkcia
#         self.omezenie = omezenie
#         self.kroky = kroky
#     
#     def myRe(self, text):
#         return re.findall(r"[-+]?\d*\.\d+|\d+", text)

# f => 3x^2 + y^2 + 1.5z^2
# o => x + y + z <= 0.5
# h => 0.1

import numpy as np
o = 0.5
h = 0.1

def myf(multiplier, x, power):
    return multiplier * (x ** power)

def myLoops(o,h):
    _ = 0
    __ = [round(_ + h, 2) for _ in np.arange(0, o, h)]
    print(__)
    return __

def myF():
    return


myLoops(o,h)
