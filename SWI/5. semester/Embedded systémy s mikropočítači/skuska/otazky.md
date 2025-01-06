## Test 1

1. (3 B) Nakreslete blokové schéma jednočipového mikropočitače a stručně popište jednotlivé části a jejich účel.

   - ![alt](/Imgs/jednocipovy1.png)
   - CPU - mikroprocesor
   - Paměť - RAM + ROM
   - I/O - vstupy a výstupy
   - ADC - A/D převodník
   - Časovač - generování časových signálů
   - Hodinový generátor - generování hodinového signálu
   - Komunikační rozhraní - SCI, SPI... - komunikace s periferiemi
   - Vnitřní sběrnice - propojení jednotlivých bloků

2. (3 B) Co znamená zkratka CISC? Čím jsou charakteristické procesory využívajíci instrukční sadu typu CISC?

   - CISC - Complex Instruction Set Computer
   - Procesory mohou obsahovat velké množství instrukcí, které mohou být velmi složité a mohou pracovat s pamětí přímo.

3. (3 B) Vysvětlete, jak funguje cyklické plánování u operačního systému. Uvěďte také příklad chování systému např. se třemi procesy (úlohami).

   - Proces se přideluje v časových kvantech po skončení kvanta na konec té fronty tech procesů
   - 1. Proces A začíná a běží po dobu určitého času (napr 20ms)
   - 2. Proces A je přesunut na konec fronty a proces B začíná běžet (20ms)
   - 3. Proces B je přesunut na konec fronty a proces C začíná běžet (20ms)
   - 4. Proces C je přesunut na konec fronty a proces A začíná běžet (20ms)

4. (2 B) Napište masku pro nastavení bitu 4 v registru REG pro použití v náslédujícím kódu:

   - REG |= MASKA;
   - MASKA = 1 << 4;

5. (2 B) Napište v jazyku C podmínku, která bude splněna, když bit 2 v registru REG bude nastaven na 1

   - if (REG & (1 << 2)) {}

6. Mikropočítač vždy obsahuje displej a klávesnici nebo tlačítka.

   - Nepravda <!-- Mikropočítač nemusí obsahovat displej a klávesnici, může být pouze procesor s pamětí a periferiemi. -->

7. Paměti typu FLASH uchovávají informaci i po odpojení napájení.

   - Pravda

8. Indexové adresování znamená, že operand instrukce je index do nějakého pole.

   - Nepravda <!-- Indexové adresování znamená, že operand instrukce je index do nějakého pole, ale ne nutně pole. -->

9. Zásobník je u mikropočítačů umístěn v paměti RAM.

   - Pravda

10. Při paralelní komunikaci se přenáší více bitů současně. Při sériové komunikaci se přenášejí jednotlivé bity za sebou.

    - Pravda

11. Přerušovací systém je implementován pouze u starších CPU, moderní mikropočítače jej nevyužívají, protože je pro ně vzhledem k výpočetnímu výkonu zbytečný.

    - Nepravda <!-- Přerušovací systém je důležitou součástí moderních mikropočítačů a umožňuje efektivní správu přerušení a událostí. -->

12. Procesor mikropočítače ukládá při příchodu přerušení na zásobník operační kód instrukce, jejíž vykonávání bylo přerušeno.

    - Nepravda <!-- Procesor ukládá na zásobník program counter a někdy stavový registr, nikoliv operační kód instrukce -->

13. A/D převodník může být přímo součástí mikropočítače.

    - Pravda

14. Výstupem A/D převodníku s rozlišením 8 bitů je číselná hodnota v rozsahu 0 až 7.

    - Nepravda <!-- Výstupem A/D převodníku s rozlišením 8 bitů je číselná hodnota v rozsahu 0 až 255. -->

15. Základní odlišností mezi operačním systémem reálného času (RTOS) a běžným operačním systémem je doba odezvy. Ta je u RTOS několikanásobně kratší (řádově milisekundy).

    - Pravda

16. Proces, který je připraven k vykonávání, ale není právě vykonáván procesorem, např. proto, že se právě provádí proces s vyšší prioritou, se označuje jako připravený (ready).

    - Pravda

17. Plánovač systému FreeRTOS umožňuje pouze kooperativní plánování.

    - Nepravda <!-- FreeRTOS umožňuje jak kooperativní, tak preemptivní plánování. -->

18. Zkratka ARM znamená Advanced Register Model.

    - Nepravda <!-- ARM znamená Acorn RISC Machine. -->

19. Mechanizmus pipeline znamená, že instrukce jsou do procesoru přenášeny z paměti přes tzv. rouru (pipe) a nikoliv přes sběrnice.

    - Nepravda <!-- Mechanizmus pipeline znamená, že instrukce jsou zpracovávány paralelně, tj. několik instrukcí je zpracováno současně. -->

## Test 2

1. (3 B) Uveďte 3 typy polovodičových paměti běžně použivaných u současných mikropočitačů. U každého typu paměti uveďte jeho základní vlastnosti (např. možnosti přepisu a mazání, uchování dat bez napájení).

   - RAM - Random Access Memory - rychlá, náhodný přístup, nestálá paměť
   - ROM - Read Only Memory - neměnná paměť, obsahuje firmware
   - FLASH - programovatelná paměť, uchovává data i bez napájení

2. (3 B) Jaký je rozdil mezi instrukční sadou typu RISC a CISC? Popište vlastností obou sad.

   - RISC - Reduced Instruction Set Computer - jednoduché instrukce, rychlejší zpracování, je potřeba více instrukcí v programu
   - CISC - Complex Instruction Set Computer - složité instrukce, méně instrukcí

3. (3 B) Uveďte tři základni stavy, ve kterých se může nacházet proces (task) u operačního systému reálného času. Každý stav stručně charakterizujte.

   - Active - Proces je běžící, má přidělený procesor a běží s vysokou prioritou
   - Waiting - Proces čeká na nějakou událost, např. dokončení I/O operace
   - Blocked - Proces je blokován, např. kvůli synchronizaci s jinými procesy

4. (2 B) Napište masku pro vynulování (clear) bitu 2 v registru REG pro použití v následujícím kódu:

   - REG &= ~MASKA;

   - MASKA = 1 << 2;

5. (2 B) Napište v jazyku C podmínku, která bude splněna, když bit 1 v registru REG bude nulový

   - if (!(REG & (1 << 1))) {}

6. (1 B) Adresová sběrnice osmibitového mikropočítače HCS08 má šířku 8 bitů.

   - Nepravda <!-- Adresová sběrnice HCS08 je obvykle větší než 8 bitů, aby mohla adresovat dostatečné množství paměti.  -->

7. (1 B) Mezi základní typy paměti používaných v současných mikropočitačich patří paměť RAM a FLASH.

   - Pravda

8. (1 B) Instrukční soubor obsahuje u současných mikropočítačů obvykle několik desítek až několik stovek instrukcl.

   - Pravda

9. (1 B) Zásobník je u mikropočítačů umístěn v paměti RAM.

   - Pravda

10. (1 B) Při paralelní komunikaci se přenáší více bitů současně. Při sériové komunikaci se přenášejí jednotlivé bity za sebou.

    - Pravda

11. (1 B) Misto přerušení je možno zjišťovat stav periferie opakovaným testováním (tzv. polling), ale nevýhodou je vytížení procesoru touto činností.

    - Pravda

12. (1 B) Procesor mikropočítače ukládá při příchodu přerušení na zásobník všechny lokální proměnné, se kterými přerušený program pracoval.

    - Nepravda <!-- Procesor ukládá na zásobník pouze některé registry a některé informace o stavu procesoru. -->

13. (1 B) Pro konfiguraci A/D převodníku u mikropočítače KL25Z se používají speciální funkce obsažené v paměti ROM mikropočítače přímo z výroby a vyvolávané z uživatelského programu pomocí instrukce CALL

    - Nepravda <!-- Konfigurace A/D převod níku se obvykle provádí zápisem do speciálních registrů, které ovlivňují chování A/D převodníku. -->

14. (1 B) Výstupem A/D převodníku s rozlišením 10 bitů je číselná hodnota v rozsahu 0 až 255.

    - Nepravda <!-- Výstupem A/D převodníku s rozlišením 10 bitů je číselná hodnota v rozsahu 0 až 1023. -->

15. (1 B) Popisovač procesu (deskriptor tasku) slouži programátorovi k popsání vlastností procesu. Obvykle se zapisuje přimo do zdrojového kódu jako komentář.

    - Nepravda <!-- Deskriptor tasku je struktura v OS, která uchovává informace o procesu, nikoliv komentář v kódu.-->

16. (1 B) Proces, který je právě prováděn procesorem se označuje jako běžící nebo aktivní.

    - Pravda

17. (1 B) FreeRTOS je možno použít pro aplikace pracující v reálném čase pouze se speciálním ovladačem jádra dodávaným výrobcem daného mikropočítače.

    - Nepravda <!-- FreeRTOS je univerzální operační systém reálného času, který lze použít na mnoha různých mikropočítačích. -->

18. (1 B) Instrukční sada používaná u procesorů ARM Cortex-M se nazývá SIS (Super Instruction Set).

    - Nepravda <!-- Instrukční sada používaná u procesorů ARM Cortex-M se nazývá Thumb. -->

19. (1 B) Mechanizmus pipeline znamená, že instrukce jsou ze zásobníku programu vybírány postupně jedna za druhou. Není možno vybrat instrukci, která není na vrcholu zásobníku.

    - Nepravda <!-- Mechanizmus pipeline znamená, že instrukce jsou zpracovávány paralelně, tj. několik instrukcí je zpracováváno současně. -->

## Test 3

1. (3 B) Vysvětlete účel tří základních sběrnic, které se používají u současných mikropočítačů pro propojení internich komponent (adresová, datová a řídicí). Uveďte také příklad šířky adresové a datové sběrnice u 8 bitového nebo 32 bitového mikropočítače.

   - Adresová sběrnice - slouží k adresování paměti a periferií
   - Datová sběrnice - slouží k přenosu dat mezi pamětí a periferiemi
   - Řídicí sběrnice - slouží k řízení komunikace mezi komponentami
   - Příklad: 8 bitový mikropočítač
     - Adresová sběrnice: 8 bitů (256 adres)
     - Datová sběrnice: 8 bitů (přenos 8 bitů dat najednou)
   - Příklad: 32 bitový mikropočítač
     - Adresová sběrnice: 32 bitů (2^32 adres)
     - Datová sběrnice: 32 bitů (přenos 32 bitů dat najednou)

2. (3 B) Vysvětlete pojem instrukce procesoru. Uveďte příklad konkrétní instrukce nebo činnosti, kterou může instrukce vykonávat.

   - Instrukce procesoru je základní operace, kterou procesor může vykonávat
   - Příklad: ADD - sčítání dvou čísel, MOV - přesun dat z jednoho místa do druhého

3. (3 B) Vysvětlete pojem preemptivní multitasking.

   - Preemptivní multitasking je způsob plánování procesů, kdy je procesor schopen přerušit běžící proces a přepnout na jiný proces s vyšší prioritou

4. (2 B) Napište kód v jazyku C pro nastavení bitu 3 v registru REG na log. 1.

   - REG |= (1 << 3);

5. (2 B) Napište v jazyku C podmínku, která bude splněna, když bit 5 v registru REG bude nulový

   - if (!(REG & (1 << 5))) {}

6. (1 B) Mikropočítač a mikroprocesor jsou synonyma (slova se stejným významem).

   - Nepravda

7. (1 B) Paměť RAM je typicky u mikropočítačů využívána pro uložení dat, se kterými program pracuje, např. globálních proměnných.

   - Pravda

8. (1 B) Základní (elementární) operace, kterou daný procesor umí vykonat, se označuje jako instrukce.

   - Pravda

9. (1 B) Odkaz na následující volnou pozici na zásobníku je uložen v registru procesoru označovaném jako PC (program counter).

   - Nepravda <!-- Odkaz na následující volnou pozici na zásobníku je uložen v registru SP (stack pointer). -->

10. (1 B) Rozhraní SPI se využívá typicky pro připojení externích periferních obvodů jako např. A/D nebo D/A převodníky.

    - Pravda

11. (1 B) Přerušení může být vyvoláno pouze vnějším periferním obvodem, tj. pouze obvodem, který není přímo součástí mikropočítače. Vyvolání přerušení některým z vnitřních obvodů mikropočítače není možné a bylo by také zbytečné, protože tyto obvody mohou přímo přistupovat k paměti mikropočítače (tzv. DMA přístup).

    - Nepravda <!-- Přerušení může být vyvoláno jak vnějším, tak vnitřním periferním obvodem mikropočítače. -->

12. (1 B) Procesor mikropočítače ukládá při příchodu přerušení na zásobník všechny lokální proměnné, se kterými přerušený program pracoval.

    - Nepravda <!-- Procesor ukládá na zásobník pouze některé registry a některé informace o stavu procesoru. -->

13. (1 B) Pro konfiguraci A/D převodníku u mikropočítače KL25Z se používají speciální funkce obsažené v paměti ROM mikropočítače přímo z výroby a vyvolávané z uživatelského programu pomocí instrukce CALL.

    - Nepravda <!-- Konfigurace A/D převodníku se obvykle provádí zápisem do speciálních registrů, které ovlivňují chování A/D převodníku. -->

14. (1 B) Výstupem A/D převodníku s rozlišením 8 bitů je číselná hodnota v rozsahu 0 až 255.

    - Pravda

15. (1 B) Jestliže operačním systém podporuje multitasking, znamená to, že může vykonávat několik úloh (procesů) "současně". Slovem současně je zde míněno, že z pohledu uživatele úlohy běží souběžně; ve skutečnosti se na procesoru rychle střídají.

    - Pravda

16. (1 B) Popisovač procesu (deskriptor tasku) je interní název procesu přidělený procesu operačním systémem

    - Nepravda <!-- Deskriptor tasku je struktura v OS, která uchovává informace o procesu, nikoliv interní název procesu. -->

17. (1 B) FreeRTOS je možno použít pro aplikace pracující v reálném čase pouze se speciálním ovladačem jádra dodávaným výrobcem daného mikropočítače.

    - Nepravda <!-- FreeRTOS je univerzální operační systém reálného času, který lze použít na mnoha různých mikropočítačích. -->

18. (1 B) Instrukce instrukční sady Thumb mají délku 64 bitů.

    - Nepravda <!-- Instrukce instrukční sady Thumb mají délku 16 nebo 32 bitů. -->

19. (1 B) Procesory Cortex-MO (použité u mikropočítače Kinetis KL25Z) mají 13 registrů pro všeobecné použití (general purpose) označených jako RO až R12.

    - Nepravda <!-- Procesory Cortex-M0 mají 16 registrů pro všeobecné použití označených jako R0 až R15. -->

## Test 4

1. (3 B) Co jsou registry procesoru a k čemu slouži? Uveďte příklady základních registrů a vysvětlete jejich účel

   - Jedná se o logické obvody pro dočasné uložení informace. Jsou velmi rychlé, ale mají velmi malou kapacitu.
   - Příklady registrů:
     - PC (Program Counter) - uchovává adresu následující instrukce, která se má vykonat
     - SP (Stack Pointer) - ukazatel na vrchol zásobníku
     - R0, R1, R2, ... - registry pro ukládání dat a mezivýsledků

2. (3 B) Co je to ukazatel zásobníku? Vysvětlete, k čemu slouží.

   - Ukazatel zásobníku (stack pointer) je registr procesoru, který ukazuje na vrchol zásobníku. Slouží k ukládání lokálních proměnných a návratových adres funkcí.

3. (3 B) Uveďte tři základní stavy, ve kterých se může nacházet proces (task) u operačního systému reálného času. Každý stav stručně charakterizujte.

   - Active - Proces je běžící, má přidělený procesor a běží s vysokou prioritou
   - Waiting - Proces čeká na nějakou událost, např. dokončení I/O operace
   - Blocked - Proces je blokován, např. kvůli synchronizaci s jinými procesy

4. (2 B) Napište masku pro vynulování (clear) bitu 3 v registru REG pro použití v následujícím kódu:

   - REG &= ~MASKA;

   - MASKA = 1 << 3;

5. (2 B) Napište v jazyku C podmínku, která bude splněna, když bit 0 v registru REG bude nastaven na 1

   - if (REG & (1 << 0)) {}

6. (1 B) CPU mikropočítače s architekturou ARM Cortex- M neobsahuje žádné registry. Místo registrů se využívá vysokorychlostní zásobník typu LIFO uloženy v paměti X-FLASH.

   - Nepravda <!-- CPU mikropočítače obsahuje registry pro ukládání dat a mezivýsledků. -->

7. (1 B) Paměť EEPROM je možno přepisovat po jednotlivých bytech.

   - Pravda

8. (1 B) Přímé adresování znamená, že operand instrukce je uveden přímo v instrukčním slově. V assembleru pro HCS08 se zapisuje pomoci #, např. LDA #5 ..

   - Nepravda <!-- Přímé adresování znamená, že operand instrukce je přímo v instrukčním slově, ale v assembleru pro HCS08 se zapisuje bez #, např. LDA 5. -->

9. (1 B) Zásobník je u mikropočítačů umístěn v paměti RAM.

   - Pravda

10. (1 B) SPI je asynchronní sériová komunikace.

    - Nepravda <!-- SPI je synchronní sériová komunikace. -->

11. (1 B) Přerušení může být vyvoláno pouze vnějším periferním obvodem, tj. pouze obvodem, který není přímo součástí mikropočítače. Vyvolání přerušení některým z vnitřních obvodů mikropočítače není možné a bylo by také zbytečné, protože tyto obvody mohou přímo přistupovat k paměti mikropočítače (tzv. DMA přístup).

    - Nepravda <!-- Přerušení může být vyvoláno jak vnějším, tak vnitřním periferním obvodem mikropočítače. -->

12. (1 B) Procesor mikropočítače ukládá při příchodu přerušení na zásobník operační kód instrukce, jejíž vykonávání bylo přerušeno.

    - Nepravda <!-- Procesor ukládá na zásobník program counter a někdy stavový registr, nikoliv operační kód instrukce -->

13. (1 B) Doba převodu u A/D převodníku u mikropočítače KL25Z se pohybuje v řádu desetin sekundy.

    - Nepravda <!-- Doba převodu u A/D převodníku se pohybuje v řádu mikrosekund. -->

14. (1 B) Výstupem A/D převodníku s rozlišením 10 bitů je číselná hodnota v rozsahu 0 až 1023.

    - Pravda

15. (1 B) Na jednom fyzickém procesoru (resp. na jednom jádře u vícejádrových procesorů) se může v daném okamžiku vykonávat jen jedna úloha.

    - Pravda

16. (1 B) Prioritní plánovací strategie se vyznačuje tím, že procesy mají přiděleny priority a operační systém vybírá ze seznamu připravených procesů ten, který má nejvyšší prioritu.

    - Pravda

17. (1 B) FreeRTOS je operační systém reálného času (RTOS).

    - Pravda

18. (1 B) Zkratka ARM znamená Advanced Register Model.

    - Nepravda <!-- ARM znamená Acorn RISC Machine. -->

19. (1 B) Procesory Cortex-MO (použité u mikropočítače Kinetis KL25Z) mají registr ukazatel zásobníku (SP) o velikosti 8 bitů.

    - Nepravda <!-- Procesory Cortex-M0 mají registr ukazatel zásobníku (SP) o velikosti 32 bitů. -->

## Test 5

1.  (3 B) Co jsou registry procesoru a k čemu slouží? Uveďte příklady základních registrů a vysvětlete jejich účel.

    - Jedná se o logické obvody pro dočasné uložení informace. Jsou velmi rychlé, ale mají velmi malou kapacitu.
    - Příklady registrů:
      - PC (Program Counter) - uchovává adresu následující instrukce, která se má vykonat
      - SP (Stack Pointer) - ukazatel na vrchol zásobníku
      - R0, R1, R2, ... - registry pro ukládání dat a mezivýsledků

2.  (3 B) Co znamená zkratka CISC? Čím jsou charakteristické procesory využívající instrukční sadu typu CISC?

    - CISC - Complex Instruction Set Computer
    - Procesory mohou obsahovat velké množství instrukcí, které mohou být velmi složité a mohou pracovat s pamětí přímo.

3.  (3 B) Vysvětlete, jak funguje cyklické plánování u operačního systému. Uvěďte také příklad chování systému např. se třemi procesy (úlohami).

    - Proces se přideluje v časových kvantech po skončení kvanta na konec té fronty tech procesů
    - 1. Proces A začíná a běží po dobu určitého času (napr 20ms)
    - 2. Proces A je přesunut na konec fronty a proces B začíná běžet (20ms)
    - 3. Proces B je přesunut na konec fronty a proces C začíná běžet (20ms)
    - 4. Proces C je přesunut na konec fronty a proces A začíná běžet (20ms)

4.  (2 B) Napište masku pro vynulování (clear) bitu 6 v registru REG pro použití v následujícim kódu:

    - REG & =~ MASKA;
    - MASKA = 1 << 6;

5.  (2 B) Napište v jazyku C podmínku, která bude splněna, když bit 0 v registru REG bude nulový

    - if (!(REG & (1 << 0))) {}

6.  (1 B) Mikropočitač obsahuje procesor, paměti a dalši obvody, např. časovače.

    - Pravda

7.  (1 B) Mezi základní typy pamětí používaných v současných mikropočítačích patři paměť RAM a FLASH.

    - Pravda

8.  (1 B) Instrukční soubor obsahuje u současných mikropočítačů obvykle několik desítek až několik stovek instrukcl.

    - Pravda

9.  (1 B) Zásobník u mikropočítače HCS08 funguje na principu FIFO (první dovnitř - první ven).

    - Nepravda <!-- Zásobník u mikropočítače HCS08 funguje na principu LIFO (poslední dovnitř - první ven). -->

10. (1 B) Při paralelní komunikaci se přenáší více bitů současně. Při sériové komunikaci se přenášejí jednotlivé bity za sebou.

    - Pravda

11. (1 B) Při příchodu přerušení procesor okamžitě začne vykonávat obsluhu přerušení, aniž by dokončil právě prováděnou instrukci. Rozpracovaná instrukce je uložena na zásobník.

    - Nepravda <!-- Procesor dokončí právě prováděnou instrukci a teprve poté začne vykonávat obsluhu přerušení. -->

12. (1 B) Procesor mikropočítače ukládá při příchodu přerušení na zásobník všechny lokální proměnné, se kterými přerušený program pracoval.

    - Nepravda <!-- Procesor ukládá na zásobník pouze některé registry a některé informace o stavu procesoru. -->

13. (1 B) Pro konfiguraci A/D převodníku u mikropočítače KL25Z se používají speciální funkce obsažené v paměti ROM mikropočítače přímo z výroby a vyvolávané z uživatelského programu pomocí instrukce CALL.

    - Nepravda <!-- Konfigurace A/D převodníku se obvykle provádí zápisem do speciálních registrů, které ovlivňují chování A/D převodníku. -->

14. (1 B) Rozlišení A/D převodníku u mikropočítačů bývá obvykle v rozsahu 8 až 16 bitů.

    - Pravda

15. (1 B) Základní odlišností mezi operačním systémem reálného času (RTOS) a běžným operačním systémem je doba odezvy. Ta je u RTOS několikanásobně kratší (řádově milisekundy).

    - Pravda

16. (1 B) Proces, který je připraven k vykonávání, ale není právě vykonáván procesorem, např. proto, že se právě provádí proces s vyšší prioritou, se označuje jako připravený (ready).

    - Pravda

17. (1 B) FreeRTOS je operační systém reálného času (RTOS).

    - Pravda

18. (1 B) Instrukční sada používaná u procesorů ARM Cortex-M se nazývá SIS (Super Instruction Set).

    - Nepravda <!-- Instrukční sada používaná u procesorů ARM Cortex-M se nazývá Thumb. -->

19. (1 B) Mechanizmus pipeline znamená, že instrukce jsou do procesoru přenášeny z paměti přes tzv. rouru (pipe) a nikoliv přes sběrnice.

    - Nepravda <!-- Mechanizmus pipeline znamená, že instrukce jsou zpracovávány paralelně, tj. několik instrukcí je zpracováváno současně. -->

## TABULKA

| Otázka                                                                                                                                                                                                                                                                                                                                                        | Odpověď (Správně/Nesprávně) | Vysvětlení                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mikropočítač a mikroprocesor jsou synonyma.Mikropočítač a mikroprocesor jsou synonyma (slova se stejným významem).                                                                                                                                                                                                                                            | Nesprávně                   | Mikroprocesor je pouze procesor, zatímco mikropočítač zahrnuje procesor a další komponenty jako paměť a vstupy/výstupy.                               |
| Registry CPU není dovoleno ukládat na zásobník, protože by tím mohlo dojít ke zpomalení výpočetních operací.                                                                                                                                                                                                                                                  | Nesprávně                   | Registry CPU lze ukládat na zásobník, např. při volání funkce nebo přerušení, aby se zachoval jejich stav.                                            |
| Statická paměť RAM (SRAM) se od dynamické RAM liší tím, že při odpojení napájení uchovává uložené informace, kdežto u dynamické RAM se informace ztratí.                                                                                                                                                                                                      | Nesprávně                   | SRAM i DRAM ztrácí informace při odpojení napájení. Rozdíl je v tom, že SRAM je rychlejší a dražší, zatímco DRAM potřebuje pravidelně obnovovat data. |
| Vstupní parametry podprogramu nelze předávat na zásobníku. Zásobník se při vstupu do podprogramu maže, aby měl podprogram k dispozici čistý zásobník.                                                                                                                                                                                                         | Nesprávně                   | Parametry lze předávat na zásobníku a je to běžná praxe. Zásobník se při vstupu do podprogramu obvykle nečistí.                                       |
| Instrukční soubor je sada instrukcí v programu.                                                                                                                                                                                                                                                                                                               | Nesprávně                   | Instrukční soubor (instruction set) je sada instrukcí, které procesor rozumí a umí vykonávat, nikoliv instrukce v konkrétním programu.                |
| Mikropočítače s jádrem HCS08 nemají indexový registr.                                                                                                                                                                                                                                                                                                         | Nesprávně                   | Jádra jako HCS08 obvykle mají indexové registry pro efektivní práci s pamětí a adresování.                                                            |
| Zásobník je u mikropočítačů umístěn v paměti RAM.                                                                                                                                                                                                                                                                                                             | Správně                     | Zásobník je typicky částí RAM, kde se ukládají dočasné hodnoty a informace o voláních funkcí.                                                         |
| Rozhraní SPI se používá pro propojení na krátké vzdálenosti, typicky v rámci plošného spoje.                                                                                                                                                                                                                                                                  | Správně                     | SPI je vhodné pro rychlou komunikaci na krátké vzdálenosti, např. na jednom plošném spoji.                                                            |
| Paralelní komunikace vyžaduje více vodičů než sériová.                                                                                                                                                                                                                                                                                                        | Správně                     | Paralelní přenos posílá několik bitů najednou po samostatných vodičích, zatímco sériová posílá bity postupně.                                         |
| Procesor mikropočítače ukládá při příchodu přerušení na zásobník operační kód instrukce, jejíž vykonávání bylo přerušeno.                                                                                                                                                                                                                                     | Nesprávně                   | Procesor ukládá na zásobník program counter a někdy stavový registr, nikoliv operační kód instrukce.                                                  |
| Přerušení slouží k tomu, aby se procesor nemusel opakovaně dotazovat na stav nějakého zařízení, ale toto zařízení se mohlo samo ohlásit.                                                                                                                                                                                                                      | Správně                     | Přerušení umožňuje zařízením signalizovat procesoru, že vyžadují pozornost, což šetří výpočetní výkon.                                                |
| Rozlišení A/D převodníku u 32-bitového KL25Z je 24 bitů.                                                                                                                                                                                                                                                                                                      | Nesprávně                   | KL25Z má obvykle 16-bitový A/D převodník, nikoliv 24-bitový.                                                                                          |
| Jednoúlohový operační systém je charakterizován tím, že provádí pouze jednu úlohu tak dlouho, dokud nepřijde požadavek na spuštění úlohy s vyšší prioritou.                                                                                                                                                                                                   | Nesprávně                   | Jednoúlohový systém zpracovává jednu úlohu najednou, ale neznamená to, že čeká na požadavek s vyšší prioritou.                                        |
| Preemptivní multitasking je charakteristický tím, že operační systém může kdykoliv přerušit běh kteréhokoliv procesu a přepnout na jiný proces.                                                                                                                                                                                                               | Správně                     | Preemptivní multitasking umožňuje systému přerušit a přepnout procesy podle potřeby pro efektivní využití zdrojů.                                     |
| Firma ARM nevyrábí mikroprocesory, pouze je navrhuje.                                                                                                                                                                                                                                                                                                         | Správně                     | ARM navrhuje mikroprocesorové architektury a licencuje je výrobcům, kteří je fyzicky vyrábějí.                                                        |
| Adresová sběrnice HCS08 má šířku 8 bitů.                                                                                                                                                                                                                                                                                                                      | Nesprávně                   | Adresová sběrnice HCS08 je obvykle větší než 8 bitů, aby mohla adresovat dostatečné množství paměti.                                                  |
| Instrukce Thumb mají délku od 8 do 64 bitů.                                                                                                                                                                                                                                                                                                                   | Nesprávně                   | Thumb instrukce mají buď 16 nebo 32 bitů, nikoliv 8 až 64 bitů.                                                                                       |
| Procesory ARM jsou vždy založeny na architektuře typu Harvard.                                                                                                                                                                                                                                                                                                | Nesprávně                   | ARM architektury mohou být založeny na Harvardu nebo von Neumannově modelu, závisí na konkrétním návrhu.                                              |
| Paměť FLASH je typicky u mikropočítačů vyuřívána pro uložení dat, se kterými program pracuje.                                                                                                                                                                                                                                                                 | Nesprávně                   | Flash paměť se typicky využívá pro uložení programu nebo firmware, nikoliv pro data, se kterými program pracuje (to je obvykle v RAM).                |
| Výhodou použití registrů pro předání parametrů do podprogramu je, že volající proces nemusí před zavoláním podprogramu žádat OS o uložení registrů CPU.                                                                                                                                                                                                       | Nesprávně                   | Volající proces obvykle musí uložit stav registrů, aby se zabránilo jejich přepsání podprogramem.                                                     |
| Plánovač systému FreeRTOS umožňuje pouze kooperativní plánování.                                                                                                                                                                                                                                                                                              | Nesprávně                   | FreeRTOS umožňuje jak kooperativní, tak preemptivní plánování.                                                                                        |
| Jako čekající se označuje proces, který neusiluje o své vykonávání na procesoru, protože čeká na nějakou událost nebo prostředek, např. na uvolnění schránky.                                                                                                                                                                                                 | Správně                     | Čekající proces je ve stavu, kdy nelze pokračovat v provádění, dokud není dostupná potřebná událost nebo prostředek.                                  |
| U operačního systému podporujícího multitasking mají procesy vždy přidělenu prioritu, bez ohledu na to, jakou plánovací strategii operační systém využívá.                                                                                                                                                                                                    | Nesprávně                   | Některé plánovací strategie nemusí využívat priority, ale jiné kritéria.                                                                              |
| Víceúlohový operační systém je charakterizován tím, že v daném okamžiku se v něm může nacházet několik úloh v různém stupni rozpracování. Operační systém mezi úlohami přepíná a vyvolává tak dojem jejich současného běhu.                                                                                                                                   | Správně                     | To je základní charakteristika víceúlohových systémů, které mezi úlohami přepínají a vytvářejí iluzi současného běhu.                                 |
| Doba převodu u A/D převodníku KL25Z se pohybuje v řádu desetin sekundy.                                                                                                                                                                                                                                                                                       | Nesprávně                   | Převodník v mikropočítači KL25Z obvykle pracuje mnohem rychleji, v řádu mikro nebo milisekund.                                                        |
| Přerušení slouží k tomu, aby se přerušil proces s velkou prioritou, který by jinak zabránil procesům s nižší prioritou v přístupu na procesor.                                                                                                                                                                                                                | Nesprávně                   | Přerušení může přerušit jakýkoliv proces, ne jen ty s velkou prioritou, aby zpracovalo důležitější úlohy.                                             |
| Procesor ukládá při příchodu přerušení na zásobník instrukci RTI (návrat z obsluhy přerušení).                                                                                                                                                                                                                                                                | Nesprávně                   | Ukládá se stav procesoru a adresa pro návrat, nikoliv instrukce RTI.                                                                                  |
| Synchronní komunikace znamená, že data jsou přenášena po jednotlivých bitech, zatímco při asynchronní jsou data přenášena po více bitech najednou, typicky po osmi tj. po bytech.                                                                                                                                                                             | Nesprávně                   | Synchronní znamená, že přenos je synchronizován hodinovým signálem, asynchronní, že každý rámec začíná start bitem a končí stop bitem.                |
| Bezprostřední adresování znamená, že operand je uveden přímo v instrukčním slově zapisuje pomocí #, např. LDA #5                                                                                                                                                                                                                                              | Správně                     | Bezprostřední adresování znamená, že data jsou součástí instrukce, často označená #.                                                                  |
| Instrukce je elementární operace, kterou daný procesor umí vykonat.                                                                                                                                                                                                                                                                                           | Správně                     | Instrukce je základní jednotka práce, kterou procesor rozumí a umí provést.                                                                           |
| CPU mikropočítače s architekturou ARM Cortex-M neobsahuje žádné registry.                                                                                                                                                                                                                                                                                     | Nesprávně                   | ARM Cortex-M má soubor registrů; nevyužívá zásobník v paměti X-FLASH pro běžné operace.                                                               |
| Paměť EPROM je možno vymazat UV zářením.                                                                                                                                                                                                                                                                                                                      | Správně                     | EPROM (Erasable Programmable Read-Only Memory) se skutečně vymazává pomocí UV záření.                                                                 |
| LDA je příkladem instrukce pro logické operace pro mikropočítač HCS08.                                                                                                                                                                                                                                                                                        | Nesprávně                   | LDA (Load Accumulator) je instrukce pro načtení hodnoty do akumulátoru, nikoliv pro logické operace.                                                  |
| Zásobník u mikropočítače HCS08 funguje na principu FIFO.                                                                                                                                                                                                                                                                                                      | Nesprávně                   | Zásobník pracuje na principu LIFO (Last In, First Out), nikoliv FIFO.                                                                                 |
| Přenosová rychlost pro rozhraní SCI je 9600 b/s.                                                                                                                                                                                                                                                                                                              | Správně                     | 9600 baudů/s je běžná přenosová rychlost pro sériovou komunikaci.                                                                                     |
| Přerušení může být vyvoláno pouze vnějším periferním obvodem, tj. pouze obvodem, který není přímo součástí mikropočítače.                                                                                                                                                                                                                                     | Nesprávně                   | Přerušení mohou být vyvolána jak vnějšími, tak vnitřními zdroji, včetně časovačů a dalších interních periferií.                                       |
| Paměť typu RAM ztrácí svůj obsah při odpojení napájení.                                                                                                                                                                                                                                                                                                       | Správně                     | RAM (Random Access Memory) je volatilní a ztrácí informace bez napájení.                                                                              |
| Podprogram je vymezený úsek kódu, který lze opakovaně použít (volat) z různých míst programu.                                                                                                                                                                                                                                                                 | Správně                     | Podprogram je definovaná sekce kódu, která může být volána z různých míst programu k opakovanému využití.                                             |
| Pokud proces uvázne v nekonečné smyčce (kód procesu obsahuje chybu), bude v případě operačního systému s preemptivním multitaskingem narušena správná činnost celého systému, protože problémový proces spotřebuje pro sebe celý čas procesoru a nepustí na něj žádný jiný proces včetně těch s vyšší prioritou.                                              | Nesprávně                   | V systému s preemptivním multitaskingem může plánovač přerušit uváznutý proces a umožnit spuštění jiných procesů.                                     |
| Priorita procesu je většinou uložena jako bitová maska, kde jednotlivé bity mají význam určitých oprávnění procesu, např. k přepsání paměti jiného procesu nebo k volání privilegovaných služeb operačního systému.                                                                                                                                           | Nesprávně                   | Priorita procesu je obvykle uložena jako jednoduchá numerická hodnota, nikoliv jako bitová maska s oprávněními.                                       |
| Popisovač procesu (deskriptor tasku) slouží programátorovi k popsání vlastností procesu.                                                                                                                                                                                                                                                                      | Nesprávně                   | Deskriptor tasku je struktura v OS, která uchovává informace o procesu, nikoliv komentář v kódu.                                                      |
| Ve FreeRTOS jsou implementovány semafory.                                                                                                                                                                                                                                                                                                                     | Správně                     | FreeRTOS podporuje semafory jako součást svých synchronizačních mechanismů.                                                                           |
| Doba převodu u A/D převodníku KL25Z se pohybuje v řádu desetin sekundy.                                                                                                                                                                                                                                                                                       | Nesprávně                   | Doba převodu je obvykle mnohem kratší, v řádu mikro nebo milisekund.                                                                                  |
| Mechanizmus pipeline znamená, že instrukce jsou ze zásobníku programu vybírány postupně jedna za druhou. Není možno vybrat instrukci, která není na vrcholu zásobníku.                                                                                                                                                                                        | Nesprávně                   | Pipelining je technika, kde se různé fáze instrukcí provádějí současně, ale nejsou omezeny pouze na zásobník.                                         |
| Při paralelní komunikaci se přenáší více bitů současně. Při sériové komunikaci se přenášejí jednotlivé bity za sebou.                                                                                                                                                                                                                                         | Správně                     | To je základní princip paralelní komunikace oproti sériové, kde se bity přenáší postupně.                                                             |
| Mezi základní typy paměti v mikropočítačích patří RAM a FLASH.                                                                                                                                                                                                                                                                                                | Správně                     | To jsou běžné typy pamětí v mikropočítačích.                                                                                                          |
| Paměť, která ztrácí obsah při odpojení napájení, se nazývá redundantní.                                                                                                                                                                                                                                                                                       | Nesprávně                   | Taková paměť se nazývá volatilní, nikoliv redundantní.                                                                                                |
| Z hlediska velikosti výsledného kódu je výhodnější, jestliže použijeme pro realizaci často používaného algoritmu v našem programu podprogram. Kód podprogramu se totiž ve výsledném programu bude nacházet pouze jednou. Při použití makroinstrukce by se stejný kód v programu nacházel v tolika kopiích, kolikrát bychom v programu makroinstrukci použili. | Správně                     | Použití podprogramu vede k menší velikosti kódu, protože se kód neopakuje.                                                                            |
| Instrukční soubor je soubor uložený na disku s instrukcemi pro procesor.                                                                                                                                                                                                                                                                                      | Nesprávně                   | Instrukční soubor (instruction set) je sada instrukcí, které procesor může vykonávat, ne soubor na disku.                                             |
| Mikropočítače s jádrem HCS08 nemají indexový registr.                                                                                                                                                                                                                                                                                                         | Nesprávně                   | HCS08 obvykle obsahuje jeden nebo více indexových registrů pro efektivní adresování.                                                                  |
| Zásobník je u mikropočítačů umístěn v paměti FLASH.                                                                                                                                                                                                                                                                                                           | Nesprávně                   | Zásobník je obvykle umístěn v paměti RAM.                                                                                                             |
| SPI je asynchronní sériová komunikace.                                                                                                                                                                                                                                                                                                                        | Správně                     | SPI je skutečně asynchronní sériový protokol.                                                                                                         |
| Procesor ukládá při příchodu přerušení na zásobník všechny globální proměnné, se kterými přerušený program pracoval.                                                                                                                                                                                                                                          | Nesprávně                   | Ukládá se obvykle stav procesoru a adresa návratu, nikoliv všechny proměnné.                                                                          |
| Rozlišení A/D převodníku u mikropočítačů je obvykle 8 nebo 10 bitů.                                                                                                                                                                                                                                                                                           | Správně                     | Tyto hodnoty jsou běžné pro rozlišení A/D převodníků.                                                                                                 |
| Jednoúlohový operační systém je charakterizován tím, že v daném okamžiku může být prováděna pouze jedna úloha. Další úloha může být spuštěna teprve po ukončení předchozí úlohy.                                                                                                                                                                              | Správně                     | To je definice jednoúlohového systému.                                                                                                                |
| Prioritní plánovací strategie se vyznačuje tím, že procesy mají přiděleny priority a operační systém vybírá ze seznamu připravených procesů ten, který má nejvyšší prioritu.                                                                                                                                                                                  | Správně                     | To je základ prioritního plánování.                                                                                                                   |
| Proces, který je připraven k vykonávání, ale není právě vykonáván procesorem, např. proto, že se právě provádí proces s vyšší prioritou, se označuje jako připravený (ready).                                                                                                                                                                                 | Správně                     | Takto se definuje stav připravený (ready) v mnoha systémech.                                                                                          |
| Operační systém FreeRTOS je dostupný zdarma (open source).                                                                                                                                                                                                                                                                                                    | Správně                     | FreeRTOS je skutečně open source.                                                                                                                     |
| Firma ARM je největším výrobcem mikroprocesorů.                                                                                                                                                                                                                                                                                                               | Nesprávně                   | ARM navrhuje architektury, které pak licencuje výrobcům, sama je nevyrábí.                                                                            |
| Sběrnice slouží k propojení jednotlivých částí mikropočítače.                                                                                                                                                                                                                                                                                                 | Správně                     | To je základní funkce sběrnice.                                                                                                                       |
| Paměť typu PROM je programovatelná uživatelem.                                                                                                                                                                                                                                                                                                                | Správně                     | PROM (Programmable Read-Only Memory) lze programovat, obvykle jednou.                                                                                 |
| Mikropočítače s jádrem HCS08 nemají indexový registr.                                                                                                                                                                                                                                                                                                         | Nesprávně                   | HCS08 obvykle obsahuje jeden nebo více indexových registrů pro efektivní adresování.                                                                  |
| Zásobník u mikropočítače HCS08 funguje na principu FIFO (první dovnitř — první ven).                                                                                                                                                                                                                                                                          | Nesprávně                   | Zásobník v mikropočítačích typicky funguje na principu LIFO (Last In, First Out), nikoliv FIFO.                                                       |
| Pro propojení dvou zařízení pomocí rozhraní SPI postačují 2 vodiče: data a zem.                                                                                                                                                                                                                                                                               | Nesprávně                   | SPI obvykle vyžaduje 4 vodiče: MISO, MOSI, SCK, a SS (Slave Select), kromě země.                                                                      |
| Přerušení je možno vyvolat z programu pomocí speciální instrukce.                                                                                                                                                                                                                                                                                             | Správně                     | Software může vyvolat softwarové přerušení speciální instrukcí.                                                                                       |
| Procesor mikropočítače ukládá při příchodu přerušení na zásobník adresu obsluhy přerušení, která bude provedena jako odezva na příchod přerušení.                                                                                                                                                                                                             | Nesprávně                   | Ukládá se adresa následující instrukce, která má být provedena po obsluze přerušení.                                                                  |
| Pro konfiguraci A/D převodníku u mikropočítače KL25Z se používají speciální funkce obsažené v paměti ROM mikropočítače přimo z výroby a vyvolávané z uživatelského programu pomocí instrukce.                                                                                                                                                                 | Nesprávně                   | Konfigurace A/D převodníku obvykle vyžaduje zápis do speciálních konfiguračních registrů, nikoliv volání funkcí z ROM.                                |
| Rozlišení A/D převodníku u mikropočítačů bývá v rozsahu 8 až 16 bitů.                                                                                                                                                                                                                                                                                         | Správně                     | To je běžný rozsah rozlišení pro A/D převodníky v mikropočítačích.                                                                                    |
| Pokud proces uvázne v nekonečné smyčce (kód procesu obsahuje chybu), bude v případě operačního systému s preemptivním multitaskingem narušena správná činnost celého systému, protože problémový proces spotřebuje pro sebe celý čas procesoru a nepustí na něj žádný jiný proces.                                                                            | Nesprávně                   | V systému s preemptivním multitaskingem může plánovač přerušit jakýkoliv proces, včetně toho, který uvázl v nekonečné smyčce.                         |
