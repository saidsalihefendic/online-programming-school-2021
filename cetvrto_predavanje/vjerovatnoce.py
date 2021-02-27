# X, X, X
# 2 * 2 * 2 = 8
"""
{
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1), X
    (1, 0, 0),
    (1, 0, 1), X
    (1, 1, 0), X
    (1, 1, 1)
}

To znaci da imamo ukupno 3 događaja koji su korektni za nas, a ukupno imamo 8
dogadjaja, sto znaci da je vjerovatnoca P je jednaka broj događaja koji nama
odgovara kroz ukupan broj događaja
To jeste, 3 / 8 = 0.375 -> 37.5%
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
    
    if prvo_bacanje == 1:
        broj_glava += 1
    
    if drugo_bacanje == 1:
        broj_glava += 1
    
    if trece_bacanje == 1:
        broj_glava += 1

    # na kraju ispitujemo
    if broj_glava == 2:
        broj_uspjesnih_eksperimenata += 1

print("Približna vjerovatnoca:", broj_uspjesnih_eksperimenata / N)