# Korisnik unosi broj k, pri cemu je k broj glava ukupno u bacanju
# Program treba da ispise ocekivani broj bacanja novcica
# da se dobije k glava

# Las Vegas pristup

import random

k = int(input("Unesite ukupan broj glava: "))

# ocekivanje = ukupan_broj_bacanja / N

ukupan_broj_bacanja = 0
N = 10 ** 4

for i in range(N):
    broj_glava = 0

    while broj_glava != k:
        novcic = random.randint(0, 1) # 1 -> glava

        if novcic == 1:
            broj_glava += 1
        else:
            broj_glava = 0
        
        ukupan_broj_bacanja += 1

print("Ocekivan broj bacanja: {}".format(ukupan_broj_bacanja / N))