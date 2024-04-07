Testy webovej stránky obce [Krakovany](https://www.krakovany.sk)

<!--
# _ znamená test sada, eg. 001_001 je prvá sada prvej sady
# - znamená test case, eg. 001_001-001 je prvý test case prvej sady prvej sady
-->

- TS_001 - Hlavná stránka obce Krakovany
  - TS_001_001 - Navigační/hlavné menu
    - TC_001_001-001 - Kontrola tlačítek
    - TS_001_001_001 - Obec
      - TC_001_001_001-001 - Kontrola interakcie tláčítka `Základné údaje a kontakty`
      - TC_001_001_001-002 - Kontrola interakcie tláčítka `Geografická poloha`
      - TC_001_001_001-003 - Kontrola interakcie tláčítka `História obce Krakovany`
      - TC_001_001_001-004 - Kontrola interakcie tláčítka `Monografia obce`
      - TC_001_001_001-005 - Kontrola interakcie tláčítka `Erb obce`
      - TC_001_001_001-006 - Kontrola interakcie tláčítka `Územný plán obce`
      - TC_001_001_001-007 - Kontrola interakcie tláčítka `Program rozvoja obce`
      - TC_001_001_001-008 - Kontrola interakcie tláčítka `Prevádzkový poriadok Zberného dvora`
      - TC_001_001_001-009 - Kontrola interakcie tláčítka `Starosta obce`
      - TC_001_001_001-010 - Kontrola interakcie tláčítka `Obecné zastupiteľstvo`
      - TC_001_001_001-011 - Kontrola interakcie tláčítka `Obecná knižnica`
      - TC_001_001_001-012 - Kontrola interakcie tláčítka `Fotogaléria`
      - TC_001_001_001-013 - Kontrola interakcie tláčítka `Podnikateľské subjekty`
      - TC_001_001_001-014 - Kontrola interakcie tláčítka `Červ. kríž`
      - TC_001_001_001-015 - Kontrola interakcie tláčítka `Mikroregión`
      - TS_001_001_001_001 - Základné údaje a kontakty
        - TC_001_001_001_001-001 - Kontrola interakcie pola `Komentár`
        - TC_001_001_001_001-002 - Kontrola interakcie pola `Meno`
        - TC_001_001_001_001-003 - Kontrola interakcie pola `E-mail`
        - TC_001_001_001_001-004 - Kontrola interakcie pola `Adresa webu`
        - TC_001_001_001_001-005 - Kontrola interakcie tlačidla `Pridať komentár`
    - TS_001_001_002 - Občan
      - TC_001_001_002-001 - Elektronická úradná tabuľa
    - TS_001_001_013 - PRIHLÁSIŤ SA / REGISTRÁCIA
      - TC_001_001_013-001 - Kontrola interakcie `Prihlasovacie meno alebo e-mailová adresa`
      - TC_001_001_013-002 - Kontrola interakcie `Heslo`
      - TC_001_001_013-003 - Kontorla funkcie `Zapamätať`
  - TS_001_002 - Kontrola Vyhľadávania
    - TC_001_002-001 - Kontrola interakcie vstupu `Vyhľadávanie`
    - TC_001_002-002 - Kontrola funkčnosti vyhladávania
  - TS_001_003 - Testovanie zmeny zobrazenia
    - TC_001_003-001 - Kontorla interakcie s tlačítkom `+`
    - TC_001_003-002 - Kontorla interakcie s tlačítkom `-`
    - TC_001_003-003 - Kontorla interakcie s tlačítkom `100%`
  - TS_001_004 - Cookies
    - TC_001_004-001 - Kontrola obsahu cookies
  - TS_001_005 - Kontrola Generovania Elementov
  - TC_001_005-001 - Kontrola, či sú všetky očakávané `div` elementy prítomné
    - TC_001_005-002 - Kontrola, či sú všetky očakávané `img` elementy prítomné a či majú správne nastavené `src` a `alt` atribúty
    - TC_001_005-003 - Kontrola, či sú všetky očakávané `a` elementy prítomné a či majú správne nastavené `href` atribúty
    - TC_001_005-004 - Kontrola, či sú všetky očakávané `input` elementy prítomné a či majú správne nastavené `type`, `name` a `id` atribúty
    - TC_001_005-005 - Kontrola, či sú všetky očakávané `button` elementy prítomné a či majú správne nastavené `type` a `name` atribúty
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
