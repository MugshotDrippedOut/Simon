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

   - Ready - připravený k běhu
   - Running - běžící
   - Blocked - blokovaný

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
