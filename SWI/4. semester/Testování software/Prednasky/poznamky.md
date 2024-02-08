# 8.2.

- Proč je duležité testovat?

  - prevence - aby chyby nevznikli
  - aby sa našli chyby

- Software

  - je nedílnou součástí života a softwarové defekty a zejména pak selhání mohou mít závažný dopad
  - Software, kteŕy nepracuje správne muže vést ke
  - ztráte peňez, času
  - ztráte obchodní reputace
  - atď.

- Therac-25 (1985-87)

  - Dva zpusoby ozařování: elektronový nebo x-ray paprsek
  - 6 známych případu predávkování, 4 osoby zemřely
  - hlavní príčiny:
    - žádna nezávislá softwarová revize
    - Testování probíhalo až na místě sestavení

- Mars Climate Orbiter (1999)

  - Určená pro sledovýní podnebí na Marsu
  - Shořela v atmosféře
  - dodavatel pouzival imperialni jednotky

- USA Blackout (2003)

  - severo-východ USA
  - 55 mil postižených na nekolik dnú
  - ztráta 6 miliard dolaru
  - Příčina: bug v Unixu, který vypnul vizuální i zvukové alarmy, následné nezpracované události byly převedeny na záložní systém, který po čase zkolaboval

- Corrupted Blood (2005)

  - Wow, pouze 1 lokace
  - Nákaza šířící se z postavy na postavu, ale tato postava se mohla teleppo

- Rozdíl medzi verifikaci a validaci
  - verifikace
    - Dle požadavku
      - modely
      - normy
      - specifikace
    - Před zákazníkem
    - Stavame spravny produkt?
  - Validace
    - Dle potřeby uživatelu
    - Akceptace
    - Postavili sme spravny produkt?
- Omyl
  - produkují defekty (chyby, bugy) v programu
  - Pokud je defekt v kódu proveden, systém muže selhat
    - Omyl (lidský faktor)=> defekt (chyba, bug)=> |incident| =>selhání
  - Príčiny softwarových defektu
    - Lidé sú omylní
    - Software a infrastruktura jsou složité
    - Časová tíseň
    - Menící se technologie
    - Mnoho systémových interakcí
    - Selhání zaviněné okolími podmínkami
