# Více možností

- Která fáze nespadá do TDD ? A která fáze je z uvedených první ?

  - Spouštění testů
  - **<u>Formální reportování incidentů vyššímu stakeholdingu</u>**
  - Refactoring kódu und
  - Opětovné spuštění testů
  - **<u>Tvorba testů</u>**
  - Přidávání testůu

- Vyberte možnosti a pádné důvody, které souvisí s tím, kdy začít s testováním údržby.

  - Archivace dat
  - **<u>Odebrání stávající funkcionality</u>**
  - Rozkaz nadřízeného
  - **<u>Změna HW na kterém aplikace běží</u>**
  - **<u>Změna formátu dat, které aplikace odesílá</u>**
  - Názor kolegy vývojáře
  - **<u>Změna v legislativě</u>**
  - Názor věštce
  - **<u>Přidání nové funkcionality</u>**
  - **<u>Patchování</u>**
  - **<u>Update OS na kterém aplikace běží</u>**

- Co jsou faktory, co odlišují testovací úroveň. Vyberte všechny správně možnosti.

  - **<u>Nástroje</u>**
  - Odpovědnost za bugy
  - **<u>Role a kdo testování provádí</u>**
  - Odměna za nalezený bug
  - Jestli se bude jednat o incident či bug
  - **<u>Typické defekty</u>**
  - **<u>Přístupy</u>**
  - **<u>Cíle testování</u>**
  - **<u>Testovací báze</u>**
  - **<u>Testované objekty</u>**
  - **<u>UI/UX</u>**

- Kolik mezer lze použít na oddělení Keywords a lokátorů v rámci Robot frameworku ?

  - 1
  - 3
  - 2
  - 5
  - 0
  - 4
  - **<u>libovolný počet</u>**

- Vyberte typy a druhy testů, které jsme si uváděli. (prej bonusová otázka)
  - **<u>End-to-end testování</u>**
  - **<u>Nefunkcionální testy</u>**
  - testování odvozené od kritérií rozhodování
  - Red-box
  - Omega testování
  - **<u>V-Model testování</u>**
  - **<u>Alfa testování</u>**
  - Testování založené na hodu mincí
  - Testování založené na čase
  - **<u>Black-box</u>**
  - **<u>Beta testování</u>**
  - Random testování
  - Big-box
  - Green-box
  - **<u>White-box</u>**
  - **<u>Funkcionální testy</u>**
  - **<u>Systémově integrační testování</u>**
  - Pink-box
  - **<u>Glass-box</u>**
  - **<u>Grey-box</u>**

# Otevřená odpověď

- S jakým principem nejvíce souvisí "Shift-left" princip ? (Uveďte číslici na intervalu 0-1111)

  - 3

- Které slovo je zásadní pro Keywords, které používáme pro kontrolu očekávaných výsledků?

  - Assert

- Doplňte slovo. White-box testování je založené na . (Jedno slovo, bez diakritiky)

  - strukture

- Doplňte slovo. Black-box testování je založené na . (Jedno slovo, bez diakritiky)

  - specifikaci

- Napište XPath, která vyhledá všechny elementy na stránce dle následujících pravidel. Jedná se o HTML tag typu odkaz na URL a zahrnuje text "klikni". (Pro zápis stringu využijte uvozovek)
  - //a[contains(text(),"klikni")]

- Jak by měl vypadat první řádek skriptu .robot, který slouží pro objektový repozitář
  - *** Variables ***

- Napište XPath, která vyhledá a určí 155 prvek na stránce s HTML tagem div.
  - (//div)[155]
- Napište XPath, která lokalizuje 155 element na webové stránce.
  - (//*)[155]
- Napište XPath, která lokalizuje element na stránce, pokud víme, že má atribut TestID roven Tlacitko1. (Pro zápis stringu využijte uvozovky")
    - //*[@TestID="Tlacitko1"]