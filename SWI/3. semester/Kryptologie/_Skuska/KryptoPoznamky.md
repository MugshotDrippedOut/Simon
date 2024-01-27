
<span style="color: red">**Kryptologie**</span> ​- technický obor zabývající se ochranou přenosu informace 

<span style="color: red">**Kryptografie**</span>  ​- zabývá se konstrukcí šifrovacích klíčů, tedy nástrojů napomáhající k šifrování zpráv 

<span style="color: red">**Steganografie​**</span>  - hlavním úkolem je zakrýt existenci zprávy 

<span style="color: red">**Kryptoanalýza**</span> ​- dala by se označit za protiklad kryptografie. Zkoumá vlastnosti otevřeného textu, šifrovaného textu 
 
<span style="color: red">**Symetrické šifry**</span> ​(k zašifrování se používá klíč, který je nutná sdílet s příjemcem, který ho díky tomuto klíči dešifruje) 
- Jeden klíč (symetrický, konvenční) je použit pro obě operace – šifrování i dešifrování 
- Nutnost sdílet klíč 
- Blokové šifry​ - pro šifrování datových souborů​ (AES, DES) 
    ​-​ Režimy činnosti ​- způsoby řetězení dat z výstupu na vstup, aby se nešifrovali stejné 
bloky (CBC, ECB) 
- Proudové šifry​ - (bit po bitu) aplikace pro přenos telekomunikací/datastream. ​(RC4) 
 
S-Box​ ​(substituční) a P-Box (permutační)​ - Základním stavebním blokem algoritmu ​DES ​je jednoduchá kombinace těchto technik (tj. substituce, následovaná permutací), která je modifikována hodnotou klíče 
 
<span style="color: red">**Asymetrické šifry**</span> (RSA, Diffie-H., DSA) ​(odesílatel si vyžádá příjemcův ​public key ​a tím zprávu zašifruje, jediný, kdo může potom zprávu dešifrovat je příjemce s jeho​ private key​. Kdyby to udělal někdo jiný, dešifruje se nesmysl). 
- Asymetrický klíčový pár (privátní, veřejný) 
- Odpadá nutnost sdílení klíče před inicializací komunikace 
- Vysoké výpočetní nároky 
- Nutnost dobře zabezpečit a kontrolovat veřejný klíč 
 
<span style="color: red">**Jednocestné funkce​**</span> - Jednocestné funkce - operace, které lze snadno provést pouze v jednom směru (ze vstupu lze snadno spočítat výstup, z výstupu je však velmi obtížné nalézt vstup.) (Poštovní schránka, míchání barev) 
 
<span style="color: red">**Hybridní šifry​**</span>  - data se šifrují symetricky, klíč se pošle pomocí asymetrických klíčů 
 
<span style="color: red">**Substituce**​</span> - znaky jsou nahrazeny za jiné, pořadí znaků zůstane zachované

<span style="color: red">**Transpozice**</span> ​- přeskupení znaků 
 
 
 
 
 
 
<span style="color: red">**Diffie-Hellman**  </span>
- Cílem je přes nezabezpečený kanál vytvořit mezi stranami šifrované spojení, bez předchozího dohodnutí šifrovacího klíč 
- Cílem je sestavit sdílený symetrický klíč pro hlavní datový provoz 
- je nutné aplikovat digitální podpisy a certifikáty pro autorizaci údajů (​kvůli man in the middle​) 
 
<span style="color: red">**Man-in-the-middle**</span> - ​funguje na principu prostředníka v komunikaci, který přeposílá a zároveň má možnost číst tok obou stran (jakoby se vydává za jednoho z nich) 
- Ochrana ​- digitální podpisy a certifikáty pro autorizaci údajů 
 
<span style="color: red">**Hash Algoritmy (ideálně 160 bitů) -  bCrypt knihovna**</span>
- Uložení hesel systému (aby nebyly uloženy v plain textu) 
- Systém nemusí znát heslo uživatele, stačí znát hash 
- Při změně jen jednoho bitu se mění i hodnota hashe 
- **MD5 (prolomen), SHA, SHA-2 algoritmy** 
 
<span style="color: red">**Útoky na šifry**</span> 
- Brute force (zkouším dokud to nevyjde), musím znát co hledám 
- Pokus omyl 
- Lineární  
- Dictionary útok (nejčastější kombinace, slova...) 

<span style="color: red">**Ciphertext-only**</span> attack ​- Odvodit co nejvíce otevřených textů nebo úplně nejlépe klíč použitý k zašifrování. 
 
<span style="color: red">**Known-plaintext**</span> attack ​- Je k dispozici zašifrovaný text, ale i odpovídající otevřený text - hledám klíč 
 
<span style="color: red">**Chosen-plaintext**</span> attack​ - Je k dispozici zašifrovaný text  i odpovídající otevřený text, útočník si vybírá bloky, které šifruje - hledá klíč 
 
<span style="color: red">**Brute force**</span>  attack ​- musím znát to, co hledám a kdy mám ten algoritmus zastavit 
 
<span style="color: red">**Útok postranními**</span> kanály ​- útok na fyzickou realizaci (analýza možných úniků informací při elektromagnetickém vyzařování...) 
 
Velké množství útoků pomocí sociálního inženýrství ​(**phishing, pharming**) ​nebo i fyzické napadnutí. 
 
 
 
<span style="color: red">**Kryptoanalýza monoalfabetických substitučních šifer**</span> ​- založena na vlastnostech jazyka 
- Analýza četnosti výskytu jednotlivých znaků (frekvenční analýza) 
- Vyhledávání typických shluků (poslední znaků slov, poměr souhlásek, samohlásek) 
 
<span style="color: red">**Kryptoanalýza polyalfabetických substitučních šifer​**</span> - určí se počet použitých substitucí, dále dokument rozdělíme na části, šifrované stejnou substitucí a na tyto části použijeme postupy analýzy monoalfabetických šifer.  
 
<span style="color: red">**Index koincidence​**</span> - dá se díky němu odhadnout, jak moc velké je klíčové slovo 
 
<span style="color: red">**Kasického metoda​**</span> - odhadování pomocí společného dělitele nějakých shluků, které se vyskytují od sebe v textu 
 
<span style="color: red">**RSA**</span> 
- Založen na předpokladu obtížnosti rozložit velké číslo na součin prvočísel – **​faktorizace** 
- **Posílání dat** - ​Šifruje se veřejným a dešifruje privátním 
- Vypočítá se jejich součin​ **n = p * q.**
- Vypočte se hodnota​ **Eulerovy funkce: φ(n) = (p − 1)(q − 1).** 
- **Veřejný klíč** složen z (n - ​modul​, e - ​veřejný exponent​)  
- **Soukromý klíč** složen z (n - ​modul​, d - ​dešifrovací, soukromý exponent​) 
- Šifrování ​- **c = m $^e$ mod n** 
- Dešifrování ​- **m = c $^d$ mod n (m** - ​zpráva​, c - ​šifra​) 
 
<span style="color: red">**DSA** </span>
- Založen na výpočtu **​diskrétního logaritmu** 
- **Podepisování** ​- Šifruje se privátním a dešifruje veřejným 
 
<span style="color: red">**Vernamova šifra​**</span> - nerozluštitelnost - nelze použít brute-force (klíč je dlouhý jako zpráva sama, je náhodný a nelze ho použít opakovaně) 
 
<span style="color: red">**Polyalfabetická šifra**</span>  
- **Vigenérova šifra** ​- Založena na 26 monoalfabetických substitucích a využívá klíčové slovo 
- V podstatě tabulka, kde je první řádek abeceda v plain textu a postupně se posune začátek o jednu 
- Hledá se průsečík s klíčem 
 
<span style="color: red">**Monoalfabetická šifra**</span>  
- Pevný posun ​(**caesarova šifra**) 
- Reversní abeceda 
- Lineární posun ​(**afinní šifra**) 
- Substituce klíčovým slovem 
**Frekvenční analýza** 
- Pomocí frekvenční analýzy lze rozhodnout zda se jedná o transpoziční či substituční systém 
- U transpoziční se pozná posun a u substituční s změní četnost jiných znaků 
- Počítá frekvenci znaků 
 
<span style="color: red">**Statistická analýza** </span> 
- Souvisí se zpracováním přirozeného jazyka (poměry souhlásek, samohlásek) 
- Jaká je pravděpodobnost, který znak je na začátku slova... 
 
<span style="color: red">**Substituční šifry**</span>  ​- Caesarova šifra, Vernamova, Playfair šifra 

<span style="color: red">**Transpoziční šifry**</span> ​- Zubatka, Transpozice v tabulce... 

<span style="color: red">**Hybridní**</span> ​-  RSA, DSA ...
 
<span style="color: red">**Steganografie**</span>  
- Snaha o ukrytí zprávy - nepřitahuje pozornost 
- Fyzická​ - skrytí zprávy uvnitř voskových tabulek, neviditelné inkousty 
- Digitální ​- ukrývání do obrázků, zvukových stop, a mm souborů 
- Lingvistická ​- modifikace nosného textu, aby ukryl tajný text (každé druhé písmeno ve slově) 
 
<span style="color: red">**Least Significant Bit​**</span>  - nejméně významný bit - spočívá v neschopnosti lidského oka poznat rozdíl mezi dvěma barvami, které se liší právě v LSB 
 
<span style="color: red">**Nulové šifry (nezašifrované zprávy)**</span> ​ - skutečná zpráva je obsažena v textu jiné, neškodně vypadající zprávy 
 
<span style="color: red">**Digitální vodoznak​**</span>  - vložení informace do digit. dokumentu tak, že je obtížné ji najít nebo odstranit. Vodoznak nelze odstranit jednoduchou úpravou. 
 
<span style="color: red">**Stegoanalýza**</span>  - ​opakem​ steganografie​ - odhaluje a detekuje skryté informace 
 
<span style="color: red">**Kvantová kryptologie** </span> 
- Jev neurčitosti​ - měření způsobuje změnu vlastností v kvantovém stavu - detekce narušitele 
- Hlavní komunikační je symetrický na základě klíče, který se domluví kvantovýma principama 
- Optický jev - (BB84) ​polarizace 
 
 
 
 
 
<span style="color: red">**Šifrování deterministickým chaosem** </span> 
- Modulace (práce se signály) 
- Chaotické maskování 
- Chaotické klíčování 
- CML Systémy  
 
<span style="color: red">**CML Systémy**</span>  ​-​ ​Zalozený na motylím effektu (citlivost na počáteční podmínky)  
- synchronizace chaotického systému na obou stranách 
 
<span style="color: red">**Eliptické křivky**</span>  
- Výhoda -​ kratší klíče​ - efektivnější výpočty certifikátů a podpisů 
 
<span style="color: red">**Délka klíče (délka klíčového prostoru)**</span>   
- Substituční - permutace ​k! 
- Klasický systém​ - n^k (n - abeceda, k - délka klíče) ​třeba abeceda 26 znaků a délka klíče 8 >​ 26^8 

Počty možných klíčů pro moderní symetrické šifry (DES, 3DES, AES...) - binární reprezentace klíče - tedy abecedu 2 počet bitů:
- 56 bitů (DES): 2 $^{56}$=  7.21*10 $^{16}$
- 128 bitů (AES): 2 $^{128}$ =  3.4*10 $^{38}$
- 168 bitů (3DES): 2 $^{168}$ =  3.74*10 $^{50}$
- 192 bitů (AES): 2 $^{192}$ =  6.28*10 $^{57}$
- 256 bitů (AES): 2 $^{256}$ =  1.16*10 $^{77}$
- 512 bitů (AES): 2 $^{512}$ =  1.34*10 $^{154}$