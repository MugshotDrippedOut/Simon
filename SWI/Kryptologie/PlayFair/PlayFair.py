import string
import unidecode


"""Funkcia pre vytvorenie abecedy bez vybraného písmena"""
def vytvorenie_abecedy(jazyk="CZ"):
    abeceda = list(string.ascii_uppercase)
    if jazyk == "CZ":
        abeceda.remove("W")
    if jazyk == "EN":
        abeceda.remove("Q")
    return abeceda


"""Funkcia pre zmenu abecedy na tabulku 5x5"""
def zmen_na_tabulku_5x5(abeceda):
    tabulka = []
    for i in range(5):
        tabulka.append(abeceda[i*5:i*5+5])
    return tabulka


"""Funkcia pre pridanie kľúča na začiatok abecedy"""
def abeceda_plus_klic(abeceda, klic):
    klic = list(klic)
    for i in klic:
        if i in abeceda:
            abeceda.remove(i)
    klic = klic[::-1]
    for i in klic:
        abeceda.insert(0, i)
    return abeceda


"""Funkcia pre odstránenie duplikátov v texte"""
def odstraneni_duplikatu_z_klice(text, abeceda= vytvorenie_abecedy()):
    text = text.upper()
    text = unidecode.unidecode(text)
    text_upraveny = ""
    for char in text:
        if char not in abeceda:
            text_upraveny += ""
        if char not in text_upraveny and char in abeceda:
            text_upraveny += char
    return text_upraveny


def nahrada_cisla_textrom(cislo,jazyk="CZ"):
    cisla = ["NULA", "JEDNA", "DVA", "TRI", "STYRI", "PAT", "SEST", "SEDM", "OSEM", "DEVAT"]
    numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGTH", "NINE"]
    if jazyk == "CZ":
        cisla = [i.replace(i, "CSL"+i+"CSL") for i in cisla]
        return cisla[int(cislo)]
    else:
        for i in numbers:
            numbers = [i.replace(i, "NUM"+i+"NUM") for i in numbers]
        return numbers[int(cislo)]


"""Funkcia pre filtrovanie textu"""
def filtrovani_textu(text,jazyk="CZ",abeceda=string.ascii_uppercase):
    text = text.upper()
    text = unidecode.unidecode(text)
    for i in range(10):
        text = text.replace(str(i), nahrada_cisla_textrom(str(i),jazyk))
    for i in text:
        if jazyk == "CZ":
            if i == " ":
                text = text.replace(i, "XYQZ")
            if i == "W":
                text = text.replace(i, "V")
            
        if jazyk == "EN":
            if i == " ":
                text = text.replace(i, "XYWZ")
            if i == "Q":
                text = text.replace(i, "O")    
        if i not in abeceda:
            text = text.replace(i, "")

        text = pridat_znaky_ak_je_text_neparny(text,jazyk)
        text = rozdelit_rovnake_znaky(text,jazyk)
    return text


"""Funkcia pre rozdelenie textu do dvojíc"""
def premenit_text_na_dvojice(text,jazyk="CZ"):
    text = pridat_znaky_ak_je_text_neparny(text,jazyk)
    dvojice = []
    i = 0
    while i < len(text):
            dvojice.append(text[i]+text[i+1])
            i+=2
    return dvojice


"""Funkcia pre rozdelenie rovnakých znakov v texte"""
def rozdelit_rovnake_znaky(text,jazyk="CZ"):
    text = text.upper()
    if jazyk == "CZ":
        for i in range(len(text)-1):
            if text[i] == text[i+1] and text[i] == "X":
                text = text[:i+1] + "QYNAHRAD" + text[i+1:]   
            if text[i] == text[i+1]:
                text = text[:i+1] + "XYNAHRAD" + text[i+1:]
                             
    if jazyk == "EN":
        for i in range(len(text)-1):
            if text[i] == text[i+1] and text[i] == "Z":
                text = text[:i+1] + "WYREPLAC" + text[i+1:]
            if text[i] == text[i+1]:
                text = text[:i+1] + "ZYREPLAC" + text[i+1:]
    return str(text)


"""Funkcia pre pridanie znakov ak je text nepárny"""
def pridat_znaky_ak_je_text_neparny(text, jazyk="CZ"):
    if jazyk == "CZ":
        if len(text)%2 != 0:
            if text[-1] == "X":
                text += "QXQNAHRAD"
            text += "XQXNAHRAD"
    if jazyk == "EN":
        if len(text)%2 != 0:
            if text[-1] == "Z":
                text += "WZWREPLAC"
            text += "ZWZREPLAC"
    return text


"""Funckia pre vylúčenie znakov z textu"""
def nahradit_dany_text(text, str_to_be_replaced, char_for_replacement=""):
    for item in str_to_be_replaced:
        text = text.replace(item, char_for_replacement)
    return text


"""Funkcia pre nahradenie čísel textom"""
def nahradit_text_cislami(text,jazyk="CZ"):
    cisla = []
    for i in range(10):
        cisla.append(nahrada_cisla_textrom(i,jazyk))
    for i in range(10):
        text = text.replace(cisla[i], str(i))
    return text


"""Funckia pre rozdelenie textu po piatich znakoch"""
def rozdelit_po_piatich_znakoch(text):
    text = [text[i:i+5] for i in range(0, len(text), 5)]
    text = " ".join(text)
    return text


"""Funckia pre zjednotenie textu"""
def zjednotit_text(text):
    text = text.replace(" ", "")
    return text


"""Funkcia pre premenenie dvojíc na text"""
def premenit_dvojice_na_text(dvojice,jazyk="CZ"):
    text = ""
    for i in dvojice:
        text += i
    if jazyk == "CZ":
        text = text.replace("XYQZ", " ")
        replace = [ "QYNAHRAD", "XYNAHRAD", "XQXNAHRAD","QXQNAHRAD"]
        text = nahradit_dany_text(text, replace)
        text = nahradit_text_cislami(text,jazyk)
    if jazyk == "EN":
        text = text.replace("XYWZ", " ")
        replace = [ "ZYREPLAC", "WYREPLAC", "ZWZREPLAC","WZWREPLAC"]
        text = nahradit_dany_text(text, replace)
        text = nahradit_text_cislami(text,jazyk)
    return text


"""Funkcia pre nájdenie pozície znaku v tabulke"""
def najdi_pozici(tabulka, pismeno):
    for i in range(5):
        for j in range(5):
            if tabulka[i][j] == pismeno:
                return i, j



"""Funkcia pre šifrovanie dvojíc"""
def sifrovani_dvojice(tabulka, dvojice):
    pozice1 = najdi_pozici(tabulka, dvojice[0])
    pozice2 = najdi_pozici(tabulka, dvojice[1])
    if pozice1 is None or pozice2 is None:
        return ""
    if pozice1[0] == pozice2[0]:# Oba znaky sú v jednom riadku, vráť znaky vedľa nich, pričom sa pri potrebe presunie na začiatok riadku
        return tabulka[pozice1[0]][(pozice1[1]+1)%5] + tabulka[pozice2[0]][(pozice2[1]+1)%5]
    elif pozice1[1] == pozice2[1]:# Oba znaky sú v jednom stĺpci, vráť znaky pod nimi, pričom sa pri potrebe presunie na začiatok stĺpca
        return tabulka[(pozice1[0]+1)%5][pozice1[1]] + tabulka[(pozice2[0]+1)%5][pozice2[1]]
    else:# ak nie sú ani v stĺpci ani v riadku, vytvor štvorec a vráť znaky v opačnom rohu štvorca
        return tabulka[pozice1[0]][pozice2[1]] + tabulka[pozice2[0]][pozice1[1]]


"""Funkcia pre dešifrovanie dvojíc"""
def desifrovani_dvojice(tabulka, dvojice):
    pozice1 = najdi_pozici(tabulka, dvojice[0])

    pozice2 = najdi_pozici(tabulka, dvojice[1])
    if pozice1 is None or pozice2 is None:
        return ""
    if pozice1[0] == pozice2[0]:# Oba znaky sú v jednom riadku, vráť znaky vedľa nich, pričom sa pri potrebe presunie na začiatok riadku
        return tabulka[pozice1[0]][(pozice1[1]-1)%5] + tabulka[pozice2[0]][(pozice2[1]-1)%5]
    elif pozice1[1] == pozice2[1]:# Oba znaky sú v jednom stĺpci, vráť znaky pod nimi, pričom sa pri potrebe presunie na začiatok stĺpca
        return tabulka[(pozice1[0]-1)%5][pozice1[1]] + tabulka[(pozice2[0]-1)%5][pozice2[1]]
    else:# ak nie sú ani v stĺpci ani v riadku, vytvor štvorec a vráť znaky v opačnom rohu štvorca
        return tabulka[pozice1[0]][pozice2[1]] + tabulka[pozice2[0]][pozice1[1]]


"""Funkcia pre šifrovanie a dešifrovanie textu"""
def playfair_sifra( klic, text, sifrovat=True,jazyk="CZ"):
    klic = odstraneni_duplikatu_z_klice(klic)
    abeceda = vytvorenie_abecedy(jazyk)
    tabulka = zmen_na_tabulku_5x5(abeceda_plus_klic(abeceda, klic))
    sifrovany_text = []
    if sifrovat == True:  
        for i in range(len(premenit_text_na_dvojice(filtrovani_textu(text,jazyk),jazyk))):
            sifrovany_text.append(sifrovani_dvojice(tabulka, premenit_text_na_dvojice(filtrovani_textu(text,jazyk),jazyk)[i]))
    if sifrovat == False:
        for i in range(len(text)):
            sifrovany_text.append(desifrovani_dvojice(tabulka, (text)[i]))
    return sifrovany_text 
    
def playfair_sifra_desifrovat( klic, text,jazyk="CZ"):
    klic = odstraneni_duplikatu_z_klice(klic)
    abeceda = vytvorenie_abecedy(jazyk)
    tabulka = zmen_na_tabulku_5x5(abeceda_plus_klic(abeceda, klic))
    sifrovany_text = []
    text = zjednotit_text(text)
    for i in range(len(premenit_text_na_dvojice(text,jazyk))):
        sifrovany_text.append(desifrovani_dvojice(tabulka, premenit_text_na_dvojice(text,jazyk)[i]))
    return sifrovany_text



if __name__ == '__main__':
    """ klic = "A"
    a = premenit_dvojice_na_text(playfair_sifra_desifrovat(klic, zjednotit_text("CFTOY ZTVFE MUVSY TCZVS XODPV RYMCF PCCYR VKDMX BEVRY MCFPC CYRVK DMXBE")))
    print(a) """
    klic= "robo"
    abeceda = vytvorenie_abecedy()
    #print(abeceda)
    text = "65123633001"
    filtrovany_klic = odstraneni_duplikatu_z_klice(klic)
    filtrovany_text = filtrovani_textu(text)
    print("Text: ", text)
    print("Filtrovany text: ", filtrovany_text)
    print(f"Tabulka: {zmen_na_tabulku_5x5(abeceda_plus_klic(abeceda, filtrovany_klic))}")
    print(f"Dvojice: {premenit_text_na_dvojice(filtrovany_text)}")
    print(f"Zasifrovane dvojice: {playfair_sifra(filtrovany_klic, text)}")
    print(f"Desifrovane dvojice: {playfair_sifra(filtrovany_klic, playfair_sifra(filtrovany_klic, text), False)}")
    print(f"Zasifrovany text: {premenit_dvojice_na_text(playfair_sifra(filtrovany_klic, text))}")
    print(f"Desifrovany text: {premenit_dvojice_na_text(playfair_sifra(filtrovany_klic, playfair_sifra(filtrovany_klic, text), False))}")
    

    """ klicEN = "Hello"
    abecedaEN = vytvorenie_abecedy("EN")
    textEN = "Hello, how are you"
    filtrovany_klicEN = odstraneni_duplikatu_z_klice(klicEN)
    filtrovany_textEN = filtrovani_textu(textEN,"EN",abecedaEN)
    print("Text: ", textEN)
    print("Filtrovany text: ", filtrovany_textEN)
    print("Tabulka: ", zmen_na_tabulku_5x5(abeceda_plus_klic(abecedaEN, filtrovany_klicEN)))
    print("Dvojice: ", premenit_text_na_dvojice(filtrovany_textEN,"EN"))
    print("Zasifrovane dvojice: ", playfair_sifra(filtrovany_klicEN, textEN,True,"EN"))
    print("Desifrovane dvojice: ", playfair_sifra(filtrovany_klicEN, playfair_sifra(filtrovany_klicEN, textEN,True,"EN"),False,"EN"))
    print("Zasifrovany text: ", premenit_dvojice_na_text(playfair_sifra(filtrovany_klicEN, textEN,True,"EN"),"EN"))
    print("Desifrovany text: ", premenit_dvojice_na_text(playfair_sifra(filtrovany_klicEN, playfair_sifra(filtrovany_klicEN, textEN,True,"EN"),False,"EN"),"EN")) """
    
    