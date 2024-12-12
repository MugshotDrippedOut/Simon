# OTÁZKY

1. **Energetická pásová struktura pevných látek; izolanty, polovodiče, kovy; typy vodivostí, drift a difúze.**
2. **Druhy polovodičů (vlastní a nevlastní polovodiče); generace a rekombinace páru elektron – díra.**
3. **P – N přechod, OPN, Schockleyho rovnice a voltampérová charakteristika P – N přechodu, měření charakteristiky, jevy na přechodu P – N.**
4. **Parametry polovodičových diod, technologie výroby polovodičů, druhy diod.**
5. **Diodové usměrňovače jednocestné, dvojcestné; porovnání vlastností jednotlivých typů usměrňovačů.**
6. **Stabilizátory napětí se Zenerovou diodou, integrované stabilizátory napětí.**
7. **Bipolární tranzistory, režimy tranzistorů, hybridní a admitanční charakteristiky, parametry bipolárních tranzistorů.**
8. **Základní zapojení bipolárních tranzistorů (SB, SC, SE), tranzistor ve funkci spínače.**
9. **JFET, odporový a saturační režim, mezní parametry, základní zapojení.**
10. **MESFET, ochuzovaní a obohacovací režim. IGBT a technologie CMOS.**
11. **MOSFET, zabudovaný a indukovaný kanál, mezní parametry, základní zapojení.**
12. **Tyristor, závěrný, blokovací a propustný režim. Tyristor jako spínač.**
13. **Diak a triak, voltampérové charakteristiky. Využití vícevrstvých součástek.**
14. **Fotoodpor, LED dioda, fototranzistor, fototyristor.**
15. **Fotodioda, odporový a hradlový režim. Optron, jeho využití.**
16. **Operační zesilovač, ideální a reálný OZ. Parametry OZ. Invertující a neinvertující zesilovač. Ochrana vstupů a výstupů OZ.**
17. **OZ jako napěťový sledovač; součtový, rozdílový OZ.**
18. **OZ ve funkci derivačního zesilovače a integračního zesilovače. OZ jako komparátor.**
19. **Číselné soustavy, převody mezi číselnými soustavami, aritmetické operace v číselných soustavách.**
20. **Kódy a kódování dat. Ochrana při přenosu kódů.**
21. **Logické funkce a základní logické členy, normy US, ČSN a IEC. Minimalizace logických funkcí.**
22. **Základní typy logik: logika DL, DTL, DCL, RTL a TTL.**
23. **Princip činnosti hradla NAND a NOR v TTL logice. Mezní parametry TTL logiky.**
24. **Statické (převodní, vstupní, výstupní, zatěžovací) a dynamické parametry TTL hradel. Měření parametrů hradel.**
25. **Logický zisk. Typy výstupů hradel TTL (s aktivním a pasivním výstupem, s otevřeným kolektorem, s třístavovým výstupem). Modifikace obvodů TTL.**
26. **Obvody CMOS. Princip činnosti investoru CMOS, princip činnosti hradla NAND v technologii CMOS. Charakteristiky CMOS obvodů. Propojení TTL a CMOS obvodů.**
27. **Princip dekodérů, konstrukce dekodérů. Dekodér BIN na 1 ze 4, dekodér BCD na 1 z 10. Integrované verze dekodérů.**
28. **Kodéry a rekodéry. Kodér 1 z 10 na BCD, dekodér z 8421 na 2421. Rekodér pro sedmisegmentový displej, jeho režimy.**
29. **Multiplexery a demultiplexery, multiplexerová logika.**
30. **Elektronické komparátory, využití funkce XOR a XNOR pro konstrukci komparátorů.**
31. **Číslicové obvody pro aritmetické operace. Binární polosčítačka a úplná sčítačka, BCD sčítačka. Aritmeticko – logická jednotka.**
32. **Klopné obvody RS a D, jednotlivé typy.**
33. **Klopné obvody JK, využití klopných obvodů pro návrh sekvenčního obvodu.**
34. **Posuvné registry, statické a dynamické registry.**
35. **Asynchronní čítače, princip činnosti, integrované verze.**
36. **Synchronní čítače, princip činnosti, integrované verze.**
37. **Dělič frekvence, konstrukce pomocí čítačů.**
38. **Vzorkovače, princip činnosti, chyby vzorkovačů.**
39. **A/Č převodníky, princip činnosti, typy převodníků a jejich chyby.**
    - jde o analogovědigitální převodník
    - princip činnosti:
      - vzorkování – odběr vstupního signálu v definovaných okamžicích, daných vzorkovacími impulsy
      - kvantování – odebraný vzorek je zaokrouhlen na hodnotu odpovídající nejbližší kvantovací úrovni
      - kódování – kvantované hodnoty jsou vyjádřeny čísly v určitém kódu
    - chyby:
      - chyba zesílení – je dána odchylkou sklonu skutečné převodní charakteristiky A/D od ideální
      - chyba nuly – je dána posunem převodní charakteristiky ve směru osy N
      - chyba linearity převodu
      - Kvantizační šum - rozdíl kvantovaného a vstupního spojitého signálu
40. **Č/A převodníky, princip činnosti, typy převodníků a jejich chyby.**

# SKÚŠKA

Často sa opakuje <!-- Rark — 15/01/2024 13:47 -->

- napětí v obvodu s tranzistorem tam párkrát bylo - společný kolektor/emitor/báze a hodnoty napětí na operačních zesilovačích, viz tohle
- jinak 3 a 4 jsou nějaké karnaughovy mapy/zapojení/logické funkce
- předpokládám že to nějak vyloženě nemění ale idk

## Variany

### 1. Varianta

1. diody obrz
2. tranzistor obrz
3. tabulka, k. mapa a zapojení polosčítačky a poté nakreslit 4-bit sčítačku
4. zase k. mapa jako u toho testu předem
5. dvousetný usměrnovač
6. co je to diak, schematická značka a k čemu se používá
7. popis rozdíl mezi logickým a analogovým komparatorem
8. k čemu slouží multiplexer

   ![alt](imgs/skuska1-1.jpg)
   ![alt](imgs/skuska1-2.jpg)

### 2. Varianta

1. diody obrz
1. tranzistor obrz
1. tabulka, polosčítačka pomoci NAND hradel a poté nakreslit 4-bit sčítačku
1. zase k. mapa jako u toho testu předem
1. dvoucestný můstkový usměrňovač
1. co je to diak, schematická značka a k čemu se používá
1. popis rozdíl mezi logickým a analogovým komparatorem
1. k čemu slouží multiplexer

   ![alt](imgs/skuska2-1.jpg)
   ![alt](imgs/skuska2-2.jpg)

### 3. Varianta

5. parametry polovodicovych diod
6. neco s tyristorem a jake mame druhy
7. jake zname cislicove soustavy
8. co je to multiplexer a k cemu se pouziva

   ![alt](imgs/skuska3-1.jpg)
   ![alt](imgs/skuska3-2.jpg)

### 4. Varianta

.
![alt](imgs/skuska4-1.jpg)
![alt](imgs/skuska4-2.jpg)

### 5. Varianta

.
![alt](imgs/skuska5-1.jpg)
![alt](imgs/skuska5-2.jpg)

## Random

![alt](imgs/skuska-random-1.png)
