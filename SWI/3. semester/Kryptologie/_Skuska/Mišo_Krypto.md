
## 1. Úvod
<span style="color: red">**Kryptologie**</span>
​- technický obor zabývající se ochranou přenosu informace 
- **Kryptologie** = Kryptografie + Kryptoanalýza + Steganografie. 

<span style="color: red">**Kryptografie**</span> 
​- zabývá se vývojem, inovacemi a standardy šifrovacích algoritmů

<span style="color: red">**Kryptoanalýza**</span>
- zabývá se testováním šifrovacích algoritmů, jejích penetrací a možnostmi prolomení šifer
- Možné útoky na šifru:
  - Brute force (zkouším dokud to nevyjde), musím znát co hledám 
  - Pokus omyl 
  - Lineární  
  - Dictionary útok (nejčastější kombinace, slova...) 

<span style="color: red">**Steganografie​**</span>
- Reprezentace informací uvnitř zpráv, fotek a fyzických objektů tak, aby nebyly zřejmé 
- Ukrytí zprávy -> nepřitahuje pozornost
- Typy:
  - Fyzická​ -> skrytí zprávy uvnitř fyzických objektů -> voskových tabulek, neviditelné inkousty 
  - Digitální ​-> ukrývání do obrázků, zvukových stop, a video souborů 
  - Lingvistická ​-> modifikace nosného textu, aby ukryl tajný text (každé druhé písmeno ve slově)
  
<span style="color: red">**Stegoanalýza**</span>
- ​Opak steganografie​ -> snaha najít ukryté informace z fotek, .mp3, .mp4, OT... -> velmi náročné něco najít 

<span style="color: red">**KÓD/ŠIFRA**</span>
- KÓD
  - Příprava na přěnos a zabezpečení dat proti poruchám datového toku
  - Kodová slova -> AB28 = Útok na Čeňka dnes v 20:00. Chybí zde algoritmus
- ŠIFRA
  - Zabezpečuje obsah dat pomocí šifrovacích algoritmů

| |KRYPROGRAFICKÉ PRAVIDLA|
| ---: | --- |
| 1 | různé klíče |
| 2 | dostatečná délka hesla |
| 3 | co nejméně uhodnutelný |
| 4 | klíč by neměl jít odvodit od jiných klíčů|

<span style="color: red">**Klíčový prostor**</span>
- Pro *Substituční* platí P(n)=n! -> Permutace
  - Počet možných substitucí pro anglickou abecedu (26 znaků): 26!... stačí
- Pro *Většinu* ostatních platí Vk(n)= $n^{k}$ -> variace
  - 56 bitů (DES): 2 $^{56}$... stači 
  - 512 bitů (AES): 2 $^{512}$ ... stačí

## 2. Rozdělení šifer
<span style="color: red">**Symetrické šifry**</span> ​
- Stejný klíč využitý při šifrování i dešifrování, tento klíč je nutný poslat, předat... příjemci
- *Blokové šifry​*
  - Data jsou rozdělena do více bloků a následně transformována šifrovacím klíčem​ | AES, DES
    - *S-Box​ ​(substituční)* -> nahrazuje malý blok bit jiným blokem bitů
    - *P-Box (permutační)* -> všechny bity vstupního slova
  - Jejich spojením dostaneme **ideální mix** 
- *Proudové šifry*​ - využití funkce XOR a keystremu, bit po bitu, aplikace pro přenos telekomunikací/datastream. | ​RC4, Vernamova šifra

|VÝHODY|NEVÝHODY|
| --- | --- |
| jednoduchost | nutnost sdílení klíče nebo jeho přenos |
| rychlost šifrování i dešifrování | více účastníků -> mnoho klíčů |
| rychlost 100+ Mbit/s | pokud je klíč kompromitován, můžou být všechny texty odšifrovány -> **kryptografické pravidla** |
| pokud je správná implementace jsou velmi bezpečné | náchylnost k útokům |
 
<span style="color: red">**Asymetrické šifry**</span> 
- (RSA, Diffie-H., DSA) ​(odesílatel si vyžádá příjemcův ​public key ​a tím zprávu zašifruje, jediný, kdo může potom zprávu dešifrovat je příjemce s jeho​ private key​. Kdyby to udělal někdo jiný, dešifruje se nesmysl). 
- Klíčový pár (privátní, veřejný) 
 - Veřejný -> šifrování (n, e)
 - Privátní -> dešifrování (n, d) 

|VÝHODY|NEVÝHODY|
| --- | --- |
| není potřeba sdílet klíč | vysoká výpočetní náročnost |
| skupina uživatelů může využívat stejný klíč | pomalá a nepraktická -> 100x pomalejší než *symetrická* |
|  | potřeba zabezpečit veřejný klíč |
| faktorizace | X |

<span style="color: red">**Hybridní šifry​**</span>  
- data využívají *symetrickou šifru*, kvůli její rychlosti. symetrický klíč je potom zašifrován *asymetrickou šifrou* -> odeslaní *(zašifrované data, zašifrovaný klíč)*
- standard HTTPS, FTPS, SSH, SSL protokolů + TLS

<span style="color: red">**Rozdělení šifer​**</span>  
- ŠIFRY -> metody pro zabezpečení dat tak, aby byly přistupné jen určeným přijemcům
  - Klasické (konvenční) 
    - Kód -> kodová slova -> AB28 = Útok na Čeňka dnes v 20:00. Chybí zde algoritmus
    - Šifra -> Jednoznačný postup, algoritmická struktura a logika
      - Transpoziční -> Přeskupení znaků, reshuffle.
      - Substituční -> OT abeceda je nahrazena za jinou ŠT abecedu <- může jich být více
        - Monoalfabetická -> každé písmeno je nahrazeno jiným pismeném 
          - Pevný posun -> Posun o zvolený počet míst | ROT3, ROT13
          - Reverzní abeceda -> Šifrovací tabulkou je reverze abecedy | ATBASH
          - Nahodná abeceda -> Náhodná permutace abecedy |
          - Lineární posun -> Vztah *ax+b mod 26*, (a,b) jsou klíče, x = char | Afinní šifra
          - Substituce s klíčovým slovem -> Klíč je insertnut na začátek abecedy, potom pokračování abecedy | PLAYFAIR
        - Polyalfabetická -> je využito více sad substitucí | Vigenerova šifra
        - Polygrafická -> nahrazuje skupiny písmen za jiné skupiny písmen | PLAYFAIR, HILL, Vigenerova šifra
        - Homofonní -> jedno pismeno je nahrazeno více než jedním symbolem | ADFG(V)X
  - Mechanické
    - Enigma -> mechanická šifrovací mašina, spjato s Alanem Turingem
    - Lorenz -> další typ využíváný během WW2
  - Moderní -> založena na složitých matematických operacích
    - Symetrická -> využití stejného klíče pro šifrování i dešifrování; nutnost předat, poslat klíč
      - Blokové -> šifrují data v pevně stanovených blocích, šifrování datových souborů | AES, DES
      - Prodouvé -> bit po bitu, operace XOR a pseudonáhodná sekvence klíče, přenos telekomunikace/datastreamů. | RC4, Vernamova šifra
    - Asymetrická -> využití .pub (n,e) klíče pro *šifrování* a .priv (n, d) klíče pro *dešifrování*. | RSA
    - Hybridní -> zašifrování dat symetrickou šifrou, kvůli její rychlosti -> zašifrování *symetrického klíče* asymetrickou šifrou | PGP

## 3. Klasická kryptografie: Substituční šifry
<span style="color: red">**Substituce**​</span>
- znaky jsou nahrazeny za jiné, pořadí znaků zůstane zachované
- **Rozdělení v tabulce.**
​  - Monoalfabetické -> Caesarova šifra (ROT3), ROT13, Vernamova, Playfair šifra, Afinní
  - Polyalfabetické šifry -> Vigenerova šifra 
    - | A | B | ... | Y | Z |
      | --- | --- | --- | --- | --- |
      | B | C | ... | Z | A |
      | ... | ... | ... | ... | ... | 
      | Y | Z | ... | W | X |
      | Z | A | ... | X | Y |
  - **Homofonní substituc**e -> ADFGX & ADFGVX -> Jedno písmeno může být nahrazeno více různýmí písmeny
  - **Klamače** -> podobné jako hieroglyfy nebo nějaké asijské jazyky -> určitý znak = určitý význam
  - **Polygrafická substituce** -> PLAYFAIR, HILL, BIFID/TRIFID, AUTOKLÁV -> Pracuje se s většími skupinami písmen místo jednotlivých znaků.
    
## 4. Klasické kryptografie: Transpoziční šifry
<span style="color: red">**Transpozice**</span>
​- Snažíme se najít způsob jak zapsat text a jiný způsob jak text přečíst
- Pomocí seřazení(transpozice) klíče PETRKLIC -> CEIKLPRT 
​- Zubatka, Transpozice v tabulce -> jen transpozice
- ADFG(V)X -> Využivá substituci i transpozici, polní šifra

## 5. Úvod do Moderní kryptografie
- Přechod z klasické na moderní:
  - 1917 -> Vernamova šifra
  - 1948 -> Shannonuv teorém
- Je postavena na extrémní algoritmické složitosti -> Aritmetika, fermatovy věty, diskrétní logaritmy, euler...
- **Vernamova šifra**
  - One-time pad byl prvni patentovaný koncept proudové šifry
  - Výhodou bylo využití klíče na šifrování i dešifrování
  - Musí platit:
      | X | Pravidla Vermanova šifra |
      | :--- | ---|
      | 1 | Délka klíče = délka přenášené zprávy|
      | 2 | Dokonale náhodný klíč|
      | 3 | One-time klíč| 
  - **Upgrade**
    - symetrických -> vždy různý klíč;
    - proudové -> zajištění různého výstupu pro stejný klíč a vstupní data;
    - blokové -> způsoby šifrovaní a práce s inicializačním vektorem

## 6. Moderní kryptologie: Symetrické blokové šifry
- DES -> Data Encryption Standard
  - V dnešní době není spolehlivá, klič pouze o délce 56 bitů -> prolomení za méně než 24 hodin
  - Bloková šifra, bloky o velikost 64 bitů, klíč 56 bitů; pomocí S-BOX -> substituce, pomocí P-BOX -> permutace
- 3DES -> Triple Data Encryption Standard
  - 3x se využije šifra DES na OT -> 3*56bitů = 168bit
  - Bezpečnost záleží na *S-BOXU*, Lavinový efekt -> změna 1 bitu vede ke změně 1/2 vystupních dat
- AES -> Advanced Data Encryption Standard
  - V blocích s pevnou délkou -> (128, 192, 256)bitů
  - Vysoká rychlost šifrování -> stovky MB/s
- IDEA -> International Data Encryption Algorithm
  - Založena na PGP, 64 bitové bloky, 128 bitový klíč
    
## 7. Moderní kryptologie: Protokoly výměny klíčů, základy asymetrické šifry
- Skupina šifer, kde se pro *šifrovaní* a *dešifrování* používají jiné klíče, nevhodné pro velký objem dat
  - Veřejný klíč -> přístupný všem, využívá se na *šifrování*
  - Privátní klíč -> dustupný jen těm co vybereme, využívá se na *dešifrování*
  - Vyžádání si veřejného klíče -> zašifrování zprávy -> **příjemce**
  - **příjemce** -> znalost obou klíčů -> dešifrování zprávy
  - Jednocestné funkce **|HASH|**
    - operace, které lze snadno provést pouze v jednom směru (ze vstupu lze snadno spočítat výstup, z výstupu je však velmi obtížné nalézt vstup.) (Poštovní schránka,              míchání barev) 

## 8. Moderní kryptologie: Algoritmy asymetrické kryptografie
- RSA
  - Rivest, Shamir, Adleman
  - Algoritmus založen na faktorizaci, zatím nelze v Polynomiální čase rozložit klíče -> SAFE
  - Útoky -> Rostoucí výpočetní výkon -> dělší klíče -> klesá efektivita šifry! proto byly odvozeny další asymetrické šifry
  - Postup:
    - Prvočísla p a q -> podle standardů (3072,4096,8192)bitů
    - **Součin n = p * q**
    - Faktorizace φ(n) = (p − 1)(q − 1).
    - Podmínka -> e < φ(n) && nesoudělná e a φ(n).
  - **Veřejný klíč** složen z (n - ​modul​, e - ​veřejný exponent​) -> Šifrování
  - **Privátní klíč** složen z (n - ​modul​, d - ​privátní exponent​) -> Dešifrování
  - Šifrování ​-> c = m $^e$ mod n
  - Dešifrování ​-> m = c $^d$ mod n
    - (m** - ​zpráva​, c - ​šifra​) 
- DSA
  - Výpočet diskrétního logaritmu
  - Využití hash a modulární aritmetika
  - Bezpečnost (bity)
  - **Podepisování** ​- U dsa je postup obrácený, šifruje se klíčem privátním klíčem a dešifruje se klíčem veřejným 
    - | Minimální délka klíče v bitech |
      | Bezpečnost (bity) | RSA | DSA | ECC |
      | :---: | :---: | :---: | :---: |
      | 80 | 1024 | 1024 | 160 |
      | 112 | 2048 | 2048 | 224 |
      | 128 | 3072 | 3072 | 256 |
      | 192 | 7680 | 7680 | 384 |
      | 256 | 15360 | 15360 | 512 |
      
## 9. Moderní kryptologie: Asymetrická kryptografie 
- Elyptické křivky
  - Bezpečnější oproti RSA či Diffie-Hellman
  - Místo modulární aritmetiky -> operace nad eliptickou křivkou
  - Kratší klíče, kratší certifikáty -> větší výpočetní efektivnost
  - Potom nějaké rovnice a čáry máry, nerozumím tomu moc
    
## 10. Netradiční moderní kryptologie: Kvantová kryptografie a Teorie chaosu
- Kvantová kryptografie
  - Kvantová fyzika
    - Heisenbergův princip neurčitosti
    - Optický jev -> Polarizace 
    - QKD -> Quantum key distribution, hlavní distribuční kanál využití 3DES, AES
    - Tvorba Shared Random bit stringu -> **Klíč**
    - Má možnost detekovat narušení přenosu
    - Náhodný klíč pomocí *kvantového* principu; data pomocí volitelné *symetrické* šifry -> AES256, IDEA
    - **Nástupce** asymetrické kryptografie ve chvíli, kdy bude dostupný velmi rychlý kvantový počítač
  - Teorie chaosu
    - **CHAOS** -> Lze najít nejaká rovnice jak popsat chaos
      - Polarizace fotonů
      - Pokud je kanál kompromitován -> 50% na obrdžení špatných hodnot
      - **Rozdělení**:
        - Diskrétní systémy ----->
        - Podivné Atractory ---------> různé 3D klikyháky
        - Časoprostorový chaos ----->
        - Buttefly effect
      - V reálném světě -> Počasí, burza, turbuletní proudění, EkG
      - **CML Systémy** ->​ ​Časoprostorový chaos 
    - **NÁHODA** -> Při dokonalé náhodě by němělo být možné ji popsat
  - Fraktální kryptografie -> teorie Fraktálů a základní substituční šifry
  - Kognitivní kryptografie -> Neuronové sítě a modely...
 ## 11. STEGANOGRAFIE
 - Umění zakrýt kontext zprávy, či celou zprávu, tak aby nebyla viditelná -> NEJDE O ŠIFROVÁNÍ!!
  - **Rozdělení:**
   - Fyzická -> neviditelný inkoust(výroba bankovek), mikropunkty
   - Digitální -> skrytí v obrázky, audio či video souboru -> digitální vodoznak -> samostatné bity vodoznaku je težké          najít přesné data
   - Lingvisticka -> kodové slova, akronymy...
- Stegoanalýza
  - Detekování a odhálování skrytých informací
    
 ## 12. Kryptoanalýza a základní útoky na šifry
 - Metoda pokus<->omyl
 - Klasické šifry ->
   - Frekvenční analýza -> Substituční
   - Přeskupování bloků, hledání bigramů/digramů -> Transpoziční
 - Polyalfabetycké ->
    - Určí se počet použitých substitucí, dále dokument rozdělíme na části, šifrované stejnou substitucí a na tyto části        použijeme postupy analýzy monoalfabetických šifer.
   - **Index koincidence**
     - Dá se díky němu odhadnout, jak moc velké je klíčové slovo
     - Možnost určení či je šifra mono/polyalfabetická
   - **Kasického metoda​** - hledání podobných shluků ve vícekrát šifrovaném textu 
  - Monoalfabetycké ->
    - Založena na vlastnostech jazyka 
      - Analýza četnosti výskytu jednotlivých znaků (frekvenční analýza) 
      - Vyhledávání typických shluků (poslední znaků slov, poměr souhlásek, samohlásek)   
- Techniky:
  - Brute Force -> útok hrubou silou, zkoušení všech varint klíče -> musím znát to, co hledám a kdy mám ten algoritmus                       zastavit -> vždy je jedná o **KNOWN-PLAINTEXT ATTACK**
  - Lineární kryptoanalýza -> Bloková + Proudová šifra
  - Diferenciální kryptoanalýza -> Bloková + HASH
- Detailní rozdělení:
  - Ciphertext-only attack ​-> Nejčastější, nějtěžší -> k dispozici CT několika zprav -> odvozování OT
  - Known-plaintext attack ​-> K dispozici CT + OT -> úkolem je odvodit klíč + algoritmus -> lze použít jen při hrubém                                   porušení KRYPTO PRAVIDEL!!
  - Chosen-plaintext attack​ -> K dispozici CT + OT, kryptoanalytik si vybírá bloky, které umí převést -> odvodit klíč
  - Chosen-key attack -> objevuje se málo
  - Útok postranními kanály -> založeno za účelem získání OT nebo klíče -> úniky fyzických veličin -> elektromagnetické                                  záření, měření spotřeby energie, času, senzory, kamery...
  - Agenturní, korupční kryptoanalýza -> účelem je získání klíče či využitého algoritmu
    - Velké množství útoků pomocí sociálního inženýrství ​(**phishing, pharming**), krádež, ofocení
  - Pendreková analýza -> Nejstarší, nejúčinnější -> hrubá síla i fyzická
    - I s útoky na fyzickou infrastrukturu -> napadění osob, blackmailing...
- Kryptografické zajímavosti
  - Steganografie je často zastoupena v praxi
  - Steganofiltry -> email komunikace -> pracuje se na superpozici šifer
  - V dnešní době klíče o velikost 128 bitů považujeme za bezpečné
  - Potřeba energie slunce vyřezené za rok aby bylo možné rozlušit 187 bitový klíč -> nelze v polynomialním čase
  
## Další pojmy 
<span style="color: red">**Diffie-Hellman**  </span>
- Standard pro výměnu klíčů -> bez předchozí znalosti -> vytvoření tajného klíče přes nezabezpečený kanál
- Nejstarší veřejně známá práce s myšlenkou veřejného a privátního klíče
- Není dostatečný pro provoz -> není možno dopustit kompromitace hlavně ve vládní a vojenské sféře
  
<span style="color: red">**Hash Algoritmy**</span>
- Uložení hesel a dat v systému tak, aby nebyly uloženy v plain textu, ale byly *zahashované*.
- Hash je v podstatě náhodné vzorkování dat, které je velmi velmi velmi obtížné dostat zpět -> možná někdy v budoucnu 
- Systém nemusí znát heslo uživatele, stačí znát hash -> oveření hashe
- Při změně jen jednoho bitu -> se mění celá hodnota hashe 
- **MD5 (prolomen), SHA, SHA-2, SHA-3 algoritmy**  
 
<span style="color: red">**Statistická analýza** </span> 
- Hledání souvislostí, statistické hypotézy + modely, sumarizace dat 
 
<span style="color: red">**Least Significant Bit​**</span>  
- nejméně významný bit -> využívá little-endian -> spočívá v neschopnosti lidského oka poznat rozdíl mezi dvěma barvami, které se liší právě v LSB 
 
<span style="color: red">**Nulové šifry (nezašifrované zprávy)**</span> ​- skutečná zpráva je obsažena v textu jiné, neškodně vypadající zprávy 
 
