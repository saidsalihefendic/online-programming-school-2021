# Ponavljanje gradiva

# Korisnik unosi prirodan broj n. Program trazi od korisnika da unese
# n realnih brojeva. Treba program da izbaci sljedece rezultate
# 1. aritmeticka sredina unesenih n brojeva 
# 2. geometrijska sredina unesenih n brojeva
# 3. harmonijska sredina unesenih n brojeva

n = int(input("Unesite broj n: "))

aritmeticka_sredina = 0
geometrijska_sredina = 1
harmonijska_sredina = 0

for i in range(n):
    broj = float(input("Unesite {}. broj: ".format(i + 1)))

    aritmeticka_sredina += broj
    geometrijska_sredina *= broj
    harmonijska_sredina += (1 / broj)

# Formula za aritmeticku sredinu = 1/n * (a_1 + a_2 + ... + a_n)
aritmeticka_sredina = aritmeticka_sredina / n

# Formula za geometrijsku sredinu = (a_1 * a_2 * ... * a_n) ** (1 / n)
geometrijska_sredina = geometrijska_sredina ** (1 / n)

# Formula za harmonijsku sredinu
# nazivnik = 1 / a_1 + 1 / a_2 + ... + 1 / a_n
# harmonijska sredina = n / nazivnik
harmonijska_sredina = n / harmonijska_sredina

print("Aritmeticka sredina: {}".format(aritmeticka_sredina))
print("Geometrijska sredina: {}".format(geometrijska_sredina))
print("Harmonijska sredina: {}".format(harmonijska_sredina))

