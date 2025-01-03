## Test 1

1. (3 B) Nakreslete blokové schéma jednočipového mikropočitače a stručně popište jednotlivé části a jejich účel.

   - ![alt](/Imgs/jednocipovy.excalidraw.png)
   - CPU - mikroprocesor
   - Paměť - RAM + ROM
   - I/O - vstupy a výstupy
   - CLK - hodinový signál
   - Čítač - čítač pro časovač
   - ADC - A/D převodník

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

   - Nepravda

7. Paměti typu FLASH uchovávají informaci i po odpojení napájení.

   - Pravda

8. Indexové adresování znamená, že operand instrukce je index do nějakého pole.

   - Nepravda

9. Zásobník je u mikropočítačů umístěn v paměti RAM.

   - Pravda

10. Při paralelní komunikaci se přenáší více bitů současně. Při sériové komunikaci se přenášejí jednotlivé bity za sebou.

    - Pravda

11. Přerušovací systém je implementován pouze u starších CPU, moderní mikropočítače jej nevyužívají, protože je pro ně vzhledem k výpočetnímu výkonu zbytečný.

    - Nepravda

12. Procesor mikropočítače ukládá při příchodu přerušení na zásobník operační kód instrukce, jejíž vykonávání bylo přerušeno.

    - Nepravda

13. A/D převodník může být přímo součástí mikropočítače.

    - Pravda

14. Výstupem A/D převodníku s rozlišením 8 bitů je číselná hodnota v rozsahu 0 až 7.

    - Nepravda

15. Základní odlišností mezi operačním systémem reálného času (RTOS) a běžným operačním systémem je doba odezvy. Ta je u RTOS několikanásobně kratší (řádově milisekundy).

    - Pravda

16. Proces, který je připraven k vykonávání, ale není právě vykonáván procesorem, např. proto, že se právě provádí proces s vyšší prioritou, se označuje jako připravený (ready).

    - Pravda

17. Plánovač systému FreeRTOS umožňuje pouze kooperativní plánování.

    - Nepravda

18. Zkratka ARM znamená Advanced Register Model.

    - Nepravda

19. Mechanizmus pipeline znamená, že instrukce jsou do procesoru přenášeny z paměti přes tzv. rouru (pipe) a nikoliv přes sběrnice.

    - Nepravda

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
