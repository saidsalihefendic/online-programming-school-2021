# 16, 2
# 16 -> 8 -> 4 -> 2 -> 1 = 4
# 12, 2
# 12 -> 6 -> 3

broj = int(input("Unesite prirodan broj: "))
djelioc = int(input("Unesite prirodan djelioc: "))

broj_dijeljenja = 0


# kao u if-u imamo logički izraz za pokretanje bloka koda
while broj > 0 and broj % djelioc == 0:
    broj_dijeljenja += 1
    broj = broj // djelioc

print("Broj dijeljenja:", broj_dijeljenja)