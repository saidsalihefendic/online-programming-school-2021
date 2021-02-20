# Ispitivanje da li je broj prost
# Definicija prostog broja:
# Prirodan broj veci od 1 koji je striktno djeljiv sa 1 i sa samim sobom
# Primjere prostih brojeva:
# 3, 5, 7, 13, 11, 2, 17, 19, 23

# Proba 1 -> for petlja
# Zadatak: Za dati uneseni prirodan broj n treba da 
#          ispita da li je broj prost

# Ukoliko direktno iz definicije primijenimo logiku
# Necemo dobiti ocekivane rezultate
# Naivan pristup
# if n % 1 == 0 and n % n == 0:
#     print("Broj je prost")

# Rjesenje: Ispitati da li postoji ijedan drugi djelioc tog
#           broja, to znaci ako nadjemo taj drugi djelioc
#           onda kazemo da je broj slozen

# break komanda

n = int(input("Unesite prirodan broj n: "))
je_prost = True
for i in range(2, n): # 2 -> n -1 je raspon 
    if n % i == 0:
        je_prost = False
        break

if je_prost and n > 1:
    print("Broj je prost")
else:
    print("Broj je slozen")
