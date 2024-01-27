
<!-- čo je Klíčový prostor DONE

Jak souvisi pravidla klice vuci transpozicim

vazby delky klicu pomocou eliptickych krivek 
- je to asymetricka kryptografie

nebude tam elipsy


Vernamova šifra a 3 pravidla šifrování 
-->


# <center>Poznámky z kryptologie</center>

## 1. Úvod

### Kryptografická pravidla
1. Stejným klíčem by něměly být nikdy zašifrovány dva různé texty.
2.  Dbát na dostatečnou délku klíče.
3.  Klíč by měl být co nejméně “uhodnutelný”.
4.  Pokud používáme více klíčů, ze znalosti jednoho by nemělo být možno 
odvodit další klíče (jména rodinných příslušníků, dětí, měsíce v roce atd..).

### Klíčový prostor
- Substituční - permutace ​k! 

- Klasický systém​ - n $^k$ (n - abeceda, k - délka klíče) ​třeba abeceda 26 znaků a délka klíče 8 >​ 26^8 

Nejstarší a nejjednodušší (Monoalfabetické substituční) šifry v podstatě nepoužívají klíč - klíčem je substituční abeceda. Pro počet možných substitucí tedy platí **Permutace n prvků substituční abecedy** - tedy počet možných seřazení množiny o n prvcích bez opakování.

𝑷(𝒏)=𝒏!

Pro většinu ostatních šifer a počet všech možností klíče platí Variace s opakováním - tedy výběr podmnožiny o k prvcích z konečné množiny o n prvcích a záleží tady na pořadí!!! 

𝑽"<sub>𝒌</sub>𝒏=𝒏<sup>𝒌</sup>

Počty možných klíčů pro moderní symetrické šifry (DES, 3DES, AES...) - binární reprezentace klíče - tedy abecedu 2 počet bitů:
- 56 bitů (DES): 2 $^{56}$=  7.21*10 $^{16}$
- 128 bitů (AES): 2 $^{128}$ =  3.4*10 $^{38}$
- 168 bitů (3DES): 2 $^{168}$ =  3.74*10 $^{50}$
- 192 bitů (AES): 2 $^{192}$ =  6.28*10 $^{57}$
- 256 bitů (AES): 2 $^{256}$ =  1.16*10 $^{77}$
- 512 bitů (AES): 2 $^{512}$ =  1.34*10 $^{154}$

## 2. Systemy a rozdeleni sifer
### Symetrická kryptografie
Výhody:
- Jednoduchost šifrovacího a dešifrovacího algoritmu.
- Rychlé algebraické/binární operace často opakované v iteracích.
- Rychlost (stovky i více Mbit/s).

Nevýhody:
- Nutnost sdílení/přenosu klíče předem nebo při inicializaci komunikace jiným zabezpečeným 
- análem (sms, osobní domluva, jiné algoritmy a workflow).
- Při komunikaci s více účastníky, nutnost velkého množství klíčů - dáno krypto pravidly.

### Asymetrická kryptografie
Výhody
- Odpadá nutnost přenosu/sdílení klíče před inicializací komunikace.
- Pro více uživatelů není potřeba tolik klíčů – v tomto případě stačí jeden klíčový pár.

Nevýhody
- Velmi vysoké výpočetní nároky (komplikovaný matematický vztah mezi klíči a zejména pak šifrovací a dešifrovací funkce pracující s umocněním a mod funkcí pro velmi velké čísla).
-  Nízká rychlost a nepraktičnost pro datové přenosy (cca 100x pomalejší než symetrická).
-  Nutnost dobře zabezpečit a kontrolovat veřejný klíč - od toho máme certifikáty a digitální 
podpisy (jednoduchý útok - výměna veřejného klíče).
