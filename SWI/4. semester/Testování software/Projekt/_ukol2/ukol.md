# 1. Zadanie

Na základě následující specifikace určete ekvivalenční třídy a navrhněte testovací případy, tak abyste otestovali že aplikace dělá, co dělat má. Aplikace má na vstupu string maximální délky 20 znaků ASCII. (1 bod)

- Jestli se jedná o datum formátu – DD-MM-YYYY.
- Jestli se jedná o datum formátu – DD/MM/YYYY.
- Jestli se jedná o datum formátu – DD.MM.YYYY.
- Jestli se nejedná o datum, ale string obsahující pouze malá písmena.
- Jestli se nejedná o datum, ale string obsahující pouze velká písmena.

## Odpoveď ⬇️

5 testovacích sad a případú

1.  datum formátu – DD-MM-YYYY
    - "07-04-2003"
2.  datum formátu – DD/MM/YYYY
    - "07/04/2003"
3.  datum formátu – DD.MM.YYYY
    - "07.04.2003"
4.  string obsahující pouze malá písmena
    - "malepismena"
5.  string obsahující pouze velká písmena
    - "VELKAPISMENA"

# 2. Zadanie

Na základě následující specifikace určete ekvivalenční třídy a navrhněte testovací případy, tak abyste otestovali že aplikace dělá, co dělat má. Aplikace slouží k otestování a určení, zda-li se jedná o číslo a jaké. Aplikace dokáže rozlišit. (1 bod)

- Jestli se jedná o číslo, které je liché.
- Jestli se jedná o číslo, které je sudé a záporné.
- Jestli se jedná o číslo, které je prvočíslo.
- Jestli se jedná o komplexní číslo.
- Jestli se jedná o číslo, které je vyjádřeno slovně.
- Nebo aplikace řekne, že neví.

## Odpoveď ⬇️

6 testovacích sad a případů

1.  číslo, které je liché
    - 7
2.  číslo, které je sudé a záporné
    - -786289632896218962489624896896
3.  číslo, které je prvočíslo
    - 13
4.  komplexní číslo
    - 3 + 4i
5.  číslo, které je vyjádřeno slovně
    - "deset"
6.  aplikace neví

    - "aplikace nevi"

# 3. Zadanie

Na základě následující specifikace otestujte aplikaci pomocí techniky analýzy hraničních hodnot a navrhněte testovací případy. Aplikace slouží pro objednání zboží v rámci e-shopu. Uživatel si může zakoupit jedno ze tří zboží -> Auta, zábavní pyrotechnika nebo plyšáci. (2 body)

- Pokud si bude chtít koupit automobily, tak si musí koupit minimálně 3. Pokud jich koupí více jak 6, tak dostane slevu 2 procenta. Maximální počet vozů k zakoupení je 100.
- Pokud by si chtěl koupit zábavní pyrotechniku, tak minimum není stanovené, ale nelze objednat 0. V případě, že si bude chtít koupit více jak 1000 kusů, tak je příplatek za služby 100%. Maximálně máme na skladě 10000 kusů.
- Pokud by si chtěl koupit plyšáky, tak to lze pouze od počtu 100 kusů, kdy za každých deset dalších je 10 % sleva. Sleva může být maximálně 30 procent. Nelze koupit více jak 8888 plyšáků.
- Testujeme pouze situaci, kdy si uživatel nakoupí.

## Odpoveď ⬇️

### Auta

Testovacie sady: 3

Testovacie připady: 6

|  Testovacia sada  |     |     |
| :---------------: | :-- | :-- |
|     Neplatné      | 1   | 2   |
| Platné, bez zlavy | 3   | 6   |
| Platné, so zlavou | 7   | 100 |

### Zábavní pyrotechnika

Testovacie sady: 2

Testovacie připady: 4

| Testovacia sada |      |       |
| :-------------: | :--- | :---- |
|  Bez příplatku  | 1    | 1000  |
| Příplatek 100%  | 1001 | 10000 |

### Plyšáci

Testovacie sady: 5

Testovacie připady: 10

| Testovacia sada |     |      |
| :-------------: | :-- | :--- |
|    Neplatné     | 1   | 99   |
|    Bez slevy    | 100 | 109  |
|    Sleva 10%    | 110 | 119  |
|    Sleva 20%    | 120 | 129  |
|    Sleva 30%    | 130 | 8888 |
