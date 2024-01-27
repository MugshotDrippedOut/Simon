
<!-- Otázky z dicordu -->
1. Připojte do systému IDE disk o velikosti 6GB. V linuxu hho poré rozdelte na jden primární a dva logické disky každý o velikosti 2GB. Popište postup, co musíte udelat, aby primární a druhý logický disk byly připojeny při každém spuštení systému a první logický se připojoval manuálne, ale systém už o něm věděl. Všechny oddíly už budou prípraveny na použivání. Na primárním disku poté vytvořte soubor info.txt, který bude obsahovat kopie souboru, ve kterém jsou nadefinováni uživatelé systému.

2. Vytvořte skript, který bude zjišťovat, který ze dvou souboru je novější. Tyto soubory se budou zadávat až po spuštění skriptu, bude se testovat, jestli existují. Po zadání souboru vypíše, který ze souboru je starší a poté se zeptá, jakým zpusobem chceme soubor zabalit s možnostmi bzip2 nebo gzip. Na závěr se zeptá na název složky, zkontroluje její existenci a poté vypíše její obsah.
#!/bin/bash
echo "Zadejte nazev prvniho souboru"
read soubor1
echo "Zadejte nazev druheho souboru"
read soubor2

Kontrola existence souborů
if [ ! -e "$file1" ]; then
    echo "Soubor $file1 neexistuje."
    exit 1
fi

if [ ! -e "$file2" ]; then
    echo "Soubor $file2 neexistuje."
    exit 1
fi

Porovnání data a času poslední úpravy souborů
if [ "$file1" -nt "$file2" ]; then
    echo "Soubor $file1 je novější než $file2."
else
    echo "Soubor $file2 je novější než $file1."
fi

Získání volby komprese od uživatele
echo "Chcete soubor zabalit pomocí bzip2 nebo gzip?"
read compression

if [ "$compression" = "bzip2" ]; then
    tar -cjf "$file1.tar.bz2" "$file1"
    tar -cjf "$file2.tar.bz2" "$file2"
elif [ "$compression" = "gzip" ]; then
    tar -czf "$file1.tar.gz" "$file1"
    tar -czf "$file2.tar.gz" "$file2"
else
    echo "Neznámá volba komprese: $compression"
    exit 1
fi

Získání názvu složky od uživatele
echo "Zadejte název složky:"
read directory

Kontrola existence složky a výpis jejího obsahu
if [ -d "$directory" ]; then
    echo "Obsah složky $directory:"
    ls "$directory"
else
    echo "Složka $directory neexistuje."
fi

4. Vytvořte soubor soubory.txt, ve kterém budou vypsány soubory začinající písmenem d ze složky /bin a nakonec souboru složky a soubory začínajíci písmenem p ze složky /etc.
-ls /bin/d* & ls /bin/s* >> soubory.txt
5. Nastavte systém tak aby každou sobotu v poledne vypsal seznam všech běžících procesu všech uživatelu do souboru ~/proc.txt a poté restartoval počítač.
crontab -e
00 12 * * 6 ps aux >> ~/proc.txt; reboot
7. Co znamená, když má položka ve výpisu atributy d (rwx)-vlastnik (rw-)-skupina vlastnika (r--)-ostatni?
- d = directory r - cist w - zapis e - execute
6. Jste přihlásen jako root a ve skupině root. Jakým příkazem získate dočasně práva skupiny users, jejiž jste také členem?
- newgrp users
- groups
7. Ve své domovské složce vytvořte tvrdý a symbolický odkaz na soubor /etc/fstab
- ln /etc/fstab tvrdak -> jen soubory
- ln -s /etc/fstab mekous -> soubory i složky 


<!--  -->
1. Přidejte do sys´temu nového uživatele s uživatelským jménem marek. V domovské složce tohoto uživatele vytvořte složku zalohy, kde bude textový soubor zalogovani.log ve kterém se bude každou hodinu přidávat aktuálni datum a čas a seznam Príhlasených uživatelu. Poté změňte práva k tomuto souboru tak, aby ho mohl číst a editovat jen vlastník souboru. Dále v domovské složce uživatele marek vytvořte soubor procesy.txt obsahující výpis aktuálně běžícich procesu všech uživatelu. Na závěr se přihásite v druhé konzoli jako rot a překopírujte výše uvedený soubor procesy.txt do své domovské složky a změňte vlastníka a skupinu na root:root.

2. Vytvořte skript, který bude zjišťovat, který ze dvou souboru je novější tyto soubory se budou zadávat až po spuštění skriptu, bude se testovat, jestli existují. Po zadání souboru vypíše, který ze souboru je starší a poté se zeptá, jakým zpusobem chceme soubor zabalit s možnostmi bzip2 nebo gzip. Na závěr se zeptá na název složky, zkontrolujte jeji existenci a poté vypíše její obsah.

#!/bin/bash
echo zadejte soubor 1. soubor
read prvy
until [ -e $prvy ]
do
    echo znova
    read prvy
done

echo zadejte soubor 2. soubor
read druhy
until [ -e $prvy ]
do
    echo znova
    read druhy
done 
if [ $prvy -ot $druhy ]
then 
    echo the older file is 



3. Vytvořte soubor uzivatele.txt v domovské složce uživatele student. Tento soubor bude obsahovat výpis domovského adresáře uživatele root a student a na konec tohoto souboru vložte výpis aktuálně přihlášených uživatelu s detailním výpisem.

(ls /root && ls /home/student && who) >/home/student/uzivatele.txt

4. Nastavte systém tak, aby každý desátý den v měsíci v 11:45 večer vypsal na konec souboru ~/soubory.txt počet souboru v domovské složce uživatele student

crontab -e
45 23 10 * * find /date/student -type f -print | wc -1 >>~/soubory.txt



5. Co znamená, když má položka ve výpisu atributy -rwxr--r--

user môže čítať písať a spustit
group a other môžu iba čítať


6. Spusťte proces cpuls na 50s již při spuštění na pozadí a poté ho přesuňte na popředí

cpuls 50 &
ctr+Z
fg % ${cislo ukolu}$
jobs - vypsani úkolúc




7. Jakým přikazem provedete aktualizaci systému a nainstalováni interaktivního kreslíciho programu gnuplot z internetu?

apt-get update
apt-get install gnuplot






## <center>Plánování úlohy</center>

1. Opakované
    - crontab
    - crontab -l vypise nastavene planovane ulohy
    - crontab -e editace textovevéhosouboru a pak otevře skript ve kterém je každá naplánována úloha
        -   | Min | Hod |Den|Mes|Dvt|Příkaz|
            | --- | --- |--- |--- |--- |--- |
            | 30 | 16 | * | * | 3 | .....
            - *- Každý 
            - dvt -> 0(ne)-6(so)


Rozdeleni disku

Fyzicke pripoeni

vytvoreni oddilu

sformatovani
- cfdisk

formatovani
- mkfs
- ms mount

vytvorim novy oddil, nastavim velskost a zvolim ci bude primarny alebo rozsireny

ulozim

mkfs -t ext4 /sdb1
mkfs -t ext4 /sdb2
mkfs -t ext4 /sdb5

df - zisti ci su oddily pripojene

pristupuju adresařově

mkdir /media/disk1
mkdir /media/disk2
mkdir /media/disk3

mount -t ext4 /dev/sdb1 /media/disk1
mount -t ext4 /dev/sdb2 /media/disk2
mount -t ext4 /dev/sdb3 /media/disk3

nano /etc/fstab
- pridanie pri spustení

## parametre
existuje slozka 

existuje soubor

ktere je novjejsi
