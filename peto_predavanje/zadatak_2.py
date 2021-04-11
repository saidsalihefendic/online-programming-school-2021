# Korisnik unosi sljedece brojeve:
# k -> broj bacanja novcica
# l -> broj uzastopnih glava
# Program da kalkulise kolika je vjerovatnoca da se pojavi l uzastopnih glava
# u k bacanja

# Dogadjaj -> k bacanja novcica
# Vjerovatnoca ovog problema
# uspjesan_broj_dogadjaja / ukupan_broj_dogadjaja <= 1
# [0, 1]

# Monte Carlo pristup

import random

N = 10 ** 5
broj_uspjesnih = 0

k = int(input("Unesite broj bacanja novcica: "))
l = int(input("Unesite broj uzastopnih glava: "))

for i in range(N):
    novcic = None
    broj_uzastopnih_glava = 0

    uspjesan_dogadjaj = False
    
    for j in range(k):
        # 1 -> glava
        if broj_uzastopnih_glava == l:
            uspjesan_dogadjaj = True
            break
        
        novcic = random.randint(0, 1)

        if novcic == 1:
            broj_uzastopnih_glava += 1
        else:
            broj_uzastopnih_glava = 0

    if broj_uzastopnih_glava == l:
        uspjesan_dogadjaj = True

    if uspjesan_dogadjaj:
        broj_uspjesnih += 1

print("Vjerovatnoca: {}".format(broj_uspjesnih / N))

