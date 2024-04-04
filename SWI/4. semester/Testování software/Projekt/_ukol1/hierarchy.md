Testy webovej stránky obce [Krakovany](https://www.krakovany.sk)

<!--
# _ znamená test sada, eg. 001_001 je prvá sada prvej sady
# - znamená test case, eg. 001_001-001 je prvý test case prvej sady prvej sady
-->

- TS_001 - Hlavná stránka obce Krakovany
  - TS_001_001 - Navigační/hlavné menu
    - TC_001_001-001 - Kontrola tlačítek
    - TS_001_001_001 - Obec
      - TS_001_001_001_001 - Základné údaje a kontakty
        - TC_001_001_001_001-001 - Kontrola interakcie pola "Komentár"
        - TC_001_001_001_001-002 - Kontrola interakcie pola "Meno"
        - TC_001_001_001_001-003 - Kontrola interakcie pola "E-mail"
        - TC_001_001_001_001-004 - Kontrola interakcie pola "Adresa webu"
        - TC_001_001_001_001-005 - Kontrola interakcie tlačidla "Pridať komentár"
      - TC_001_001_001-001 - Geografická poloha
    - TS_001_001_002 - Občan
      - TC_001_001_002-001 - Elektronická úradná tabuľa
    - TS_001_001_013 - PRIHLÁSIŤ SA / REGISTRÁCIA
      - TC_001_001_013-001 - Kontrola interakcie "Prihlasovacie meno alebo e-mailová adresa"
      - TC_001_001_013-002 - Kontrola interakcie "Heslo"
      - TC_001_001_013-003 - Kontorla funkcie "Zapamätať"
  - TS_001_002 - Kontrola Vyhľadávania
    - TC_001_002-001 - Kontrola interakcie vstupu "Vyhľadávanie"
    - TC_001_002-002 - Kontrola funkčnosti vyhladávania
  - TS_001_003 - Testovanie zmeny zobrazenie
    - TC_001_003-001 - Kontorla interakcie s tlačítkom "+"
    - TC_001_003-002 - Kontorla interakcie s tlačítkom "-"
    - TC_001_003-003 - Kontorla interakcie s tlačítkom "100%"
  - TS_001_004 - Cookies
    - TC_001_004-001 - Kontrola obsahu cookies
  - TS_001_100 - UI/UX
    - TC_001_100-001 - Konzistentnosť elementov
    - TC_001_100-002 - Čitelnosť a vizibilita textu
    - TC_001_100-003 - Schopnosť reagovať na iné veľkosti obrazovky
    - TC_001_100-004 - Zrozumitelnosť chybových hlásení
    - TC_001_100-005 - Rozloženie stránky a použitie medzier
    - TC_001_100-006 - Využitie obrázkov
    - TC_001_100-007 - Farby a kontrast
        <!-- 
            Možné ďalšie UI/UX:
            - Funkčnosť navigačného menu
            - Funkčnosť linkov a ich správnosť
            - Funkčnosť foriem
            - Načítacia doba a výkon
            - Funkcie na prispôsobenie (možnosť zväčšiť/zmenšiť text)
            - Kompatibilita s rôznymi prehliadačmi
            - Funkčnosť možnosti vyhľadávania
            - Aktualita obsahu
            - Plynulost elementov pri hover
            - Funkčnosť interaktívnych elementov (buttons, dopdowns)
            - Funkčnosť možnosti prihlásenia
            - Presnosť predpovedi počasia
            - Funkčnosť tláčítok socialnych médií
        -->
