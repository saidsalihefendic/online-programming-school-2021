# Zadatak
# Korisnik unosi prirodan broj n.
# Program treba da ispise sumu prvih n parnih brojeva

n = int(input("Unesite prirodan broj n: "))

suma_parnih = 0
for i in range(2, n * 2 + 1):
    if i % 2 == 0:
        # suma_parnih = suma_parnih + i
        print(i)
        suma_parnih += i

suma_parnih_2 = 0
for i in range(1, n + 1):
    suma_parnih_2 += i * 2

print("Suma parnih:", suma_parnih)
print("Suma parnih 2:", suma_parnih_2)