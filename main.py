# opakovaniIT2python
import random

# 1. Proměnná pro jméno
krestni_jmeno = "Alex"

# 2. Proměnná pro příjmení
prijmeni = "Chyba"

# 3. Výpis jména a příjmení do konzole
print(krestni_jmeno + " " + prijmeni)

# 4. Vstup pro uživatele, který zadá věk (pouze číslo)
vek_uzivatele = int(input("Zadejte svůj věk (celé číslo): "))

#5. Vypište v konzoli délku první proměnné a druhé proměnné.
print (len(krestni_jmeno)) + len(prijmeni)

# 6. Proměnná s počáteční hodnotou 6
cislo = 6

# 7. Cyklus, který 5x přičte 3
for i in range(5):
    cislo += 3

# 8. Výpis výsledku po 5 opakováních cyklu
print("Konečná hodnota je:", cislo)

# 9. Cyklus pro kontrolu, zda uživatel zadal celé číslo jako věk
while True:
    try:
        vek_uzivatele = int(input("Znovu zadejte svůj věk: "))
        print("Děkuji, zadali jste správně.")
        break
    except ValueError:
        print("Zadejte prosím celé číslo.")

# 10. Generování náhodné hodnoty mezi 1 a 10
nahodne_cislo = random.randint(1, 10)
print("Náhodné číslo mezi 1 a 10:", nahodne_cislo)