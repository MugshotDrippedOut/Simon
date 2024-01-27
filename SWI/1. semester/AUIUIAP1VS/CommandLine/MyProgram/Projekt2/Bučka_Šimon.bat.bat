@ECHO OFF

REM příkaz pro vyčištění obrazovky od předchozích příkazů
CLS

REM Pozdravenie uzivatela
Echo Ahoj Pouzivatel, aktualni cas je:

REM Vypis casu
TIME/T

REM Medzera aby bol prehlad
ECHO

REM Vytvorenie zlozky MyProgram
MKDIR MyProgram

REM Otvorenie zlozky MyProgram
CD MyProgram

REM Vytvorenie zloziek scr a info
MKDIR scr
MKDIR info

REM Vyzvanie uzivatela na zadanie premennej
SET /P prom="Zadejte promennou: "

REM Vypisanie premennej
ECHO (Promnenna je:) 
ECHO %prom%



REM vytvorenie novej zlozky
MKDIR %prom%



REM premiestnenie do zlozky info
cd info

REM otestovanie pripojenia na server utb
PING utb.cz > ping.log
REM Spravenie suboru dir.log
mkdir dir.log
ping.log

EXIT /B 0

