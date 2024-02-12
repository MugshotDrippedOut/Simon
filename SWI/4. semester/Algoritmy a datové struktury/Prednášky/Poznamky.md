# Prednáška 5.2.

- Treba Gitlab
- projekty budú robené v C
- Bodové hodnocení
  | | |
  | ---------------------------------- | :-------: |
  | Příklady ve cvičeních | 40 bodů |
  | Půlsemestrální test | 10 bodů |
  | Semestrální test | 50 bodů |
  | Prémiový projekt (včetně obhajoby) | 20 bodů |
  | Celkem | 120 bodů |
- Program přednášek
  - Přednáška: Algoritmus. Metoda návrhu algoritmu shora dolů. Popis algoritmu - vývojové diagramy, stavové automaty...Časová a paměťová složitost.
    - Cvičení: Organizační záležitosti, úvod do programování v Pascalu/C.
  - Přednáška: Datové struktury: Základní struktury. Seznam, strom
    - Cvičení: Lineární seznam - implementace
  - Přednáška: AVL stromy. Délka cesty v binárním vyhledávacím stromu. Halda, B-strom, fronta, zásobník, tabulka.
    - Cvičení: Binární vyhledávací strom - implementace
  - Přednáška: Množina, asociativní pole, graf, zásobník.
    - Cvičení: AVL strom - implementace
  - Přednáška: Použití zásobníku. Metody návrhu algoritmu: Rozděl a panuj, hladový algoritmus, dynamické programování.
    - Cvičení: AVL strom - dokončení implementace. Euklidův algoritmus. Hanojské věž
  - Přednáška: Backtracking, obecné metody prohledávání stavového stromu. Některé další metody. Rekurze.
    - Cvičení: jako přednáška
  - Přednáška: Třídění haldou, quicksort, třídění souborů.
    - Cvičení:Hanojské věže. Třídění seznamu, topologické třídění
  - Přednáška: Hledání mediánu. Přihrádkové třídění, lexikografické třídění, abecední řazení.
    - Cvičení: Lexikografické třídění, optimální strom.
  - Přednáška: Optimální binární vyhledávací strom. Seminumerické algoritmy.
    - Cvičení: Důsledky zobrazení čísel v počítači.
  - Přednáška: Algoritmy pro zpracování problémů z oblasti umělé inteligence - neuronové sítě, genetické programování
    - Cvičení: jako přednáška
  - Přednáška: Programování komplexních informačních systémů - relační databáze, ERD, SQL...
    - Cvičení: Návrh jednoduché databázové aplikace
  - Přednáška: Objektové programování. Metody návrhu komplexních informačních systémů - UML.
    - Cvičení: Návrh složité distribuované aplikace v UML

## Algoritmus

- Algoritmus je postup řešení určité úlohy. Ne každý postup je ale algoritmem!
- Algoritmus musí splňovatt n=asledujíci vlastnosti:
  - je konečný = musí skončit po provedení konečného počtu kroku
  - je elementární = je specifikován jako posloupnost elementárn=ich, pro daný provádecí stroj jednoznačne definovyných operací
  - je rezultativní = vede ke správnému výsledku
  - je determinovaný = po každém kroku lze zjistit, zda již algoritmus skončil, a pokud neskončil, jak má dále pokračovat
- Možnosti zápisu
  - Data-flow diagramy
  - Petriho síte
  - Vývojové diagramy
  - ERD diagramy

## Abstraktí datové typy

- snaha o vytvoření zapouzdření
- každý objekt je len c-čková struktura

## Základní ADT a časové složitosti jejich operací

|                 | Vkládání                               | Mazání              | Vyhledávání         | Řazení                          |
| --------------- | -------------------------------------- | ------------------- | ------------------- | ------------------------------- |
| Dynaické pole   | Pokud je buňka volná: O(1) Jinak: O(N) | O(1)                | O(N)                | O(N\*log<sub>2</sub>N)          |
| Lineární seznam | O(1)                                   | O(1)                | O(N)                | O(N\*log<sub>2</sub>N)          |
| Binárni strom   | O(log<sub>2</sub>N)                    | O(log<sub>2</sub>N) | O(log<sub>2</sub>N) | Vždy seřazen                    |
| Hash tabulka    | O(1)                                   | O(1)až O(K)         | O(1) až O(K)        | Lze jen v kombinaci s jiným ADS |

# Prednáška 12.2.

- Je dobré si nakreslit obrázek
- Je taktické používat enum - kompatibilný int

### Príklad enum

```C
#include <stdio.h>

typedef enum {SUDA,LICHA, TRETI=3, CTVRTA, PATA} t_Stavy;

int main() {

  t_Stavy stav= TRETI;
  printf("stav=%d\n",stav);
  for (int i=0;i<10; i++)
    printf("i=%d\n",i);
  return 0;
}

```

### Príklad konečný automat

Spracovanie dvoch stavov

![alt](Images/SudaLicha.png)

```C
#include <stdio.h>

typedef enum {SUDA,LICHA} t_Stavy;

int main() {

  t_Stavy stav= SUDA;
  int znak;
  znak=getchar();
  while (znak!EOF){ /*EOF = -1 | preddefinovaná premenná*/
    znak=getchar();
  }
  return 0
}

```

Využite swich case

```C
#include <stdio.h>
#include <ctype.h>

typedef enum {SUDA,LICHA} t_Stavy;

int main() {

  t_Stavy stav= SUDA;
  int znak;
  znak=getchar();
  while((znak=getchar())!=EOF)
    printf("stav=%d, znak=%c, ASCII=%d\n ",stav,znak,znak)
    swich (stav) {
      case SUDA:
        if (znak==’1’) {putchar(’L’); stav=LICHA;}
        else if (znak==’0’) putchar(’S’);
        else if (!isspace(znak)){puts("Error, neocakavane pismeno")}

        break;
      case LICHA:
        if (znak==’1’) {putchar(’S’); stav=SUDA;}
        else if (znak==’0’) putchar(’L’);
        else if (!isspace(znak)){puts("Error, neocakavane pismeno")}
        break;
  }
  return 0
}

```
