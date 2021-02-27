# X, X, X
# 2 * 2 * 2 = 8
"""
Bacamo 4 novcica uzastopno. Kolika je vjerovatnoca da ćemo dobiti bar tri glave?

Ukupan broj dogadjaja = 2 * 2 * 2 * 2 = 16

(1, 1, 1, 1),
(0, 1, 1, 1),
(1, 0, 1, 1),
(1, 1, 0, 1),
(1, 1, 1, 0)

Vjerovatnoca -> 5 / 16 = 0.3125 -> 31.25%
"""

import random

N = 10 ** 6 # broj eksperimenata

broj_uspjesnih_eksperimenata = 0
# randint
# 0 -> pismo, 1 -> glava
for i in range(N):
    broj_glava = 0

    prvo_bacanje = random.randint(0, 1)
    drugo_bacanje = random.randint(0, 1)
    trece_bacanje = random.randint(0, 1)
    cetvrto_bacanje = random.randint(0, 1)
    
    if prvo_bacanje == 1:
        broj_glava += 1
    
    if drugo_bacanje == 1:
        broj_glava += 1
    
    if trece_bacanje == 1:
        broj_glava += 1

    if cetvrto_bacanje == 1:
        broj_glava += 1

    # na kraju ispitujemo
    if broj_glava >= 3:
        broj_uspjesnih_eksperimenata += 1

print("Približna vjerovatnoca:", broj_uspjesnih_eksperimenata / N)