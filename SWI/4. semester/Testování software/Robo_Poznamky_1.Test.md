# Software a chyby
- Chyby v softwaru můžou vést k
	- Ztrátě peněz
	- Ztrátě času
	- Ztátě reputace
	- Někdy i ztrátě na životě nebo zranění

- Příklady
	- [Therac-25](https://www.youtube.com/watch?v=Ap0orGCiou8)
	- [Mars Climate Orbiter](https://youtu.be/IWHTyibmB7U?feature=shared)
	- [USA Blackout](https://youtu.be/KciAzYfXNwU?feature=shared)
	- [Corrupted Blood WoW](https://youtu.be/YNhP5b9YafM?feature=shared)

## Testování
- Testování je
	- Provádění testů
	- Plánování a řízení
	- Výběr testovacích podmínek
	- Tvorba testových specifikací
	- Reporting
	- Analýza rizik
	- Vyhodnocení kritérií
	- Statická analýza kódu
	- Revize dokumentace

**QA** = Quality Assurance je strategický postup zajištění a vyhodnocování kvality.

**QC** = Quality Control je proces testování.

- Role
	- Tester
	- Manažer Testování

- Norma ISO-29119
	- 5 částí
		- Part 5: Keyword-driven testing
		- Part 4: Test techniques
		- Part 3: Test documentation
		- Part 2: Test processes
		- Part 1: Concepts and definitions
	- Definuje role, procesy testování a pracovní produkty

Plánování $\to$ Analýza $\to$ Návrh testů $\to$ Implementace testů $\to$ Testování $\to$ Hotovo 🥳️

- Verifikace testování
	- Dle požadavků
		- Modely
		- Normy
		- Specifikace
	- Před zákazníkem

- Validace
	- Dle potřeb uživatelů
	- Akceptace

- Omyly produkují chyby v programu
	- Omyl $\to$ Defekt $\to$ (někdy Incident) $\to$ Selhání

- **Root cause** = Příčina vzniku chyby
	- Nesrozumitelnost, neúplná specifikace, komunikace
	- Myslel jsem $\dots$
	- Nezkušenost
	- Časový tlak

- **Testování nikdy nekončí**

- Rizika
	- Technická
	- Obchodní
	- Bezpečnostní

### Testování může být
- Statické
	- Modely, diagramy
	- Automatická statická analýza
	- Manuální revize
- Dynamické
	- Snažíme se docílit selhání (spouštění programu)

- **SDLC** = Software Development Lifecycle

**Quality Management** = Quality Assurance + Quality Control

**Ladění vs. Testování** - Ladění provozuje vývojář, testování je na testerovi.

## Principy testování
1. Testování odhaluje pouze přítomnost, nikoliv nepřítomnost chyb.
2. Nelze otestovat kompletně vše.
3. Testování za včasu šetří čas a peníze.
4. Shlukování chyb (Paretovo pravidlo 80:20)
5. Testy se opotřebovávají. Změny v SW znamená změny v testech.
6. Testování je závislé na kontextu. Každá věc se testuje jinak.
7. Nepřítomnost chyb je iluze. Nelze si být nikdy 100% jistý.

# Otázky z testu
- Kdo nejlépe hledá chyby?
	- Zákazník, Tester
- Co začít testovat jako první?
	- Základní funkce
- Rozdíl mezi **verifikací** a **validací**?
	- Verifikace = Ověření splnění požadavků.
	- Validace = Funguje správně pro koncové uživatele.
- Dokáže statické testování najít každou chybu?
	- Nedokáže, jen ty, které má test ověřovat.
- Na co je statické testování nejlepší?
	- (bug incident...)
- Kdo může nejvíc za defekty?
	- Vývojář.
- Co je incident?
	- Událost způsobená defektem.
- Cíl testování?
	- Prevence vzniku chyb. Nalezení existujících.
- Co znamená že se opotřebovávají testy?
	- Stejné testy neodhalí nové chyby.
- Doplnit pořadí rovnice: _+_=_
	- QA+QC=QM
- Co dělá vývojář a co tester?
	- Tester hledá bugy, oznamuje bugy
	- Vývojář opravuje kód
	- (chyba, incident, defekt, omyl,incident)
- Očíslovat pořadí:
	1. Root case
	2. Omyl
	3. Defekt
	4. Selhání
- Počet principů testování:
	- 7
- Co patří k testování?
	- Provádění testů
	- Plánování a řízení
	- Výběr testovacích podmínek
	- Tvorba testových specifikací
	- Reporting
	- Analýza rizik
	- Vyhodnocení kritérií
	- Statická analýza kódu
	- Revize dokumentace
- Je pravda, že nejhorší defekty ovlivní peníze a reputaci?
	- Ano
- Kdy rostou náklady na vyřešení defektů?
	- Když je nutné předělat začátek. Nedomyšleno při plánovací fázi.
- Co patří do statické analýzy?
	- text, modely, diagramy
- Co zahrnuje QA?
	- Preventivní přístup
		- Zavádění a zlepšování procesů
		- Procesy pro kompletní vývoj (včetně testování)
		- Celý tým
- Jak je testování závislé na kontextu?
	- Každý program testujeme jinak, jiným testem.
- Opravit bug
	- dražší před spuštěním aplikace
- Otestovat kód
	- levnější před spuštěním aplikace
				