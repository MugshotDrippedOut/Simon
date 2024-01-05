# 1. otázky z dc

- Frekvenční analýza, co jsme pomocí ní schopni zjistit.
  - Jestli se jedná o substituci, písmená budú zachovávať frekvenčné rozloženie, čiže najčastejšie vyskytujúce písmeno bude pravdepodobne to písmeno ktoré sa najčastejšie vyskytuje v pôvodnej abecede.
- Co kdyby byl vytvořený kvantový Pc, jak by to ovlivnilo symetrickou a asymetrickou šifru.
  - Zanikne asymetrická a symetrická kryptografie(faktorizace a eliptické křivky budou řešeny v řádech milisekund), její nástupce bude kvantová kryptografie
- Máš 24 bitový obrázek BPM asi 20x50 pixelů použiješ poslední dva bity+něco se složkou R, kolik se tam vleze bitů dat do obrázku.
  - 20x50 = 1000 pixelov
  - posledné 2 pixely R (red) složky 2x1000=2000 pixelov
  - do obrázku se vleze 2000bit dat
- Popiš jak funguje AES šifra.
  - v blocích s pevnou délkou
  - 10 nebo 14 rund a každá z techto rund se skládá
    - ByteSub Transformation
    - ShiftRow Transformation
    - MixColumn Tranfromation
    - AddRoundKey
- kolik bitů používá klíč šifer AES, ECC, SHA-384.
  - AES - 128, 192, 256
  - ECC - 256, 384
  - SHA-384 -384
- rozdíl mezi RSA a ECC rozepiš.
  - ECC použivá operace nad eliptickou křivkou (Diskrétní logaritmus eliptických křivek) namiesto modulárnej aritmetiky (Faktorizace součinu prvočísel)
    - taky kratšie klíče čiže väčšia výpočetná efektivita a bezpečnosť na pomer délky klíče
- něco o Moderní kryptografii, její výhody.
  - Moderní kryptologie je postavena zejména na externí algoritmické složitosti výpočtu a analýty klíčového prostoru.
  - výhody u vernamovej šifry : Stejný algoritmus je možné použít pro zašifrování i dešifrování
- Zašifruj svoje jmeno pomocí vegenarovy šifry.
  - abeceda zacina podla klucoveho slova a index je +1
  - B..C..D....A
  - U..V..W....T
  - B = D
  - U = P
  - C = F
  - K = V
  - A = B
- kolik ruznych hodnot a, b můžeme použít v affiní šifře a proč ?
  - počet hodnôt pre parameter "a" závisí na velkosti abecedy "m"( všetky prvočísla po hodnotu m)
  - počet hodnôt pre parameter "b" nemá obmedzenie
  - celkový počet kombinácii zavisí na počtu možných hodnôt pre "a" a pre "b"

# 2. otázky z testu ktorý som mal ja

- Výhody a nevýhody symetrické šifry
  - Výhody: rýchlost až 100Mbit/s, jednoduchost
  - Nevýhody: Nutnosť zdielať kľúč, viacej účastníkov = mnoho kľúčov
- rozdíl mezi RSA a ECC rozepiš.
  - ECC použivá operace nad eliptickou křivkou namiesto modulárnej aritmetiky
    - taky kratšie klíče čiže väčšia výpočetná efektivita a bezpečnosť na pomer délky klíče
- Jde ze sifrovaného textu zjistit jestli byla pouzita substituce nebo transpozice
  - Áno
  - Transpozice se muze po blocich opakovat
  - Substituce je náhodná
- proč je vernamova šifra neprolomitelná
  - neuspěje ani útok hrubou silou
  - Protože dodržuje pravidla kryptografie:
    - Klíč je dokonale náhodný
    - Vždy iný klíč
    - Klíč má rovnakou délku jako zpráva
- vysvetli pojmy P-box, S-box a rundový klíč
  - P-box : premutační blok, nahrádza poradie bitú podla danej permutaňej tabulky
  - S-box : substituční blok, nahrádza bity za iné podla danej substitučnej tabulky
  - rundový klíč je klíč který ktérý se využíva opakovane pri blocích v blokových šifrách (Rundách)
    - rundový klíč se odvádzí z pôvodného klíče

# 3. otázky 
- K čemu všemu lze využit frekvenční analýzu? Vysvětlete.
  - Ke zistení jestli byla použita substituce na základe toho že najčastejšei opakovaný znak bude pravdepodobne najviac frekventovaný znak v pôvodnej abecede.
- Který klíč lze považovat za nejméné bezpečný? A proč?

      Délka klíče pro AES 128 bitu
      Déllka klíče je 128 místné hexadecimální číislo
      Klíč je odvozen z 10 místného hesla pomocí SHA3-512.
      Klíč je odvozen z 89 místného hesla pomocí SHA3-256
      Klíč je odvozen z 111 místného hesla pomocí SHA-256
  - AES 128 -> 128 bitov
  - hex 128 -> 32 bitov
  - Sha3-512 -> 128 bitov
  - Sha3-256 -> 64 bitov
  -Sha-256 -> 64bitov
- Stručne popište šifru AES
  - Advanced data enctryption standart
  - 128, 192, 256
  - bloková, 10 nebo 14 rund, používaf rundový klíč
  - každá runda používa:
    - ByteSub
    - ShiftRow
    - MixColumn
    - AddRoundKey
- Popište pravidla, které vymezují "nejsilnejší" klíč použitý pro Vigenérovu šifru
- Co je to Vernamova šifra a proč ji považujeme za neprelomitelnou
- Rozepište rozdíl mezi proudovými a blokovými šiframi
  - Proudové šifry postupujú bit po bitu, operace XOR
    - Vernamova šifra  
  - blokové po blokoch (rundách)
    - AES
- Popište, co znamená pojem "moderní hybridní kryptografie". K čemu slouží a jaké má výhody?
  - zašifrovanie dat symetricky pre jej rychlost a zašifrovanie symetrického klíče asymetricky
- Zašifrujte své příjmení pomocí ADFGVX 6x6. Jako klíč použijte "RASPUTIN"
  - DAFAXAAAFAA
- Kolik lze vložit dat do obrázku 24-bitového .bmp který má 20x50 pixelu pomocí steganografické techniky LSB při využití barevné složky R a G a dvou posledních bitu?
  - 20x50 = 1000
  - R a G = 4 dostupné bity 
  - 1000x4 = 4000 dostupných bitov
- Lze získat z HASHE zpátky vstupní data? Za předpokladu, že použijeme hashovací algoritmus SHA3-512? Vysvětlete.
  - iba ak použijeme brute-force ináč nie