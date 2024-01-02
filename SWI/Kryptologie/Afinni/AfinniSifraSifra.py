abeceda=["A","B","C","D","E","F","G","H","I","J","K","L","M",
   "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
modulo=len(abeceda)

aParameter = 5
bParameter = 9 

txt="T"

def GetIndex(txt):
    return abeceda.index(txt)  


def Encription(txt):
    entxt =""
    for character in txt:
        entxt = entxt + str(abeceda[(aParameter*GetIndex(character) + bParameter)%modulo])
    return entxt

  
index=GetIndex(txt)

txt1="THEINITIAL"

entxt =Encription(txt1)
print(entxt)


def modInverse(a , m):
    for x in range(1,m):
        if (((a%m) * (x%m))%m == 1):
            return x
    return -1

print(modInverse(aParameter,modulo))

def Decription(txt):
    detxt = ""
    for character in txt:
        detxt = detxt + str(abeceda[(((GetIndex(character)-bParameter)*modInverse(aParameter,modulo))%26)])
    return detxt

detxt = Decription(entxt)
print(detxt)


