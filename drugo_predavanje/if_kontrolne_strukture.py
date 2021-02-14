
""" Konvertovanje prosjek ocjena
5 -> A
4 -> B
3 -> C
2 -> D
1 -> F
"""

prosjek_ocjena = int(input("Unesite vas prosjek ocjena: "))

print("Vas prosjek ocjena je:", prosjek_ocjena)

konvertovani_prosjek_ocjena = None # tip None

if prosjek_ocjena == 5:
    konvertovani_prosjek_ocjena = "A"

elif prosjek_ocjena == 4:
    konvertovani_prosjek_ocjena = "B"

elif prosjek_ocjena == 3:
    konvertovani_prosjek_ocjena = "C"

elif prosjek_ocjena == 2:
    konvertovani_prosjek_ocjena = "D"

elif prosjek_ocjena == 1:
    konvertovani_prosjek_ocjena = "F"

else:
    print("Nije validan prosjek ocjena")


if konvertovani_prosjek_ocjena != None:
    print("Vas konvertovani prosjek ocjena je:", konvertovani_prosjek_ocjena)