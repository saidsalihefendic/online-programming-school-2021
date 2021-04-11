# y = f(x) = x^2 + 4x + 5
# Primjer:
# f(3) = 26
# f(2) = 17
# f(1) = 10
# y = 3x + 5

def f(x):
    y = x ** 2 + 4 * x + 5
    return y

def je_prost(n):
    """
    Ova funkcija vraca True ukoliko je broj n prost broj, u svakom slucaju False,
    koji oznacava da je broj n slozen.

    Prima prirodan broj n tipa int i vraca bool vrijednost True ili False
    """

    if n == 1:
        return False
    
    # pronalazak djelioca
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def nzd(m, n):
    """
    Funkcija vraca najveci zajednicki djelioc brojeva m i n.
    Prima m i n parametre tipa int i vraca NZD tih brojeva tipa int
    """

    nzd = 1
    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            nzd = i
    
    return nzd

def relativno_prosti(m, n):
    """
    Funkcija vraca True ukoliko je NZD(m, n) = 1, jer smatramo da su oni relativno
    prosti, a ako je NZD(m, n) > 1, tada nisu relativno prosti
    """
    return nzd(m, n) == 1

def euler(n):
    """
    Vraca broj brojeva manji ili jednak od n koji su relativno prosti sa tim brojem
    Primjer:
    euler(10) -> #{1, 3, 7, 9} -> 4

    Prima n tipa int i vraca broj relativno prostih brojeva sa n koji su manji od
    n i tipa je int
    """

    broj_relativno_prostih = 0

    for i in range(1, n + 1):
        if relativno_prosti(i, n):
            broj_relativno_prostih += 1

    return broj_relativno_prostih

def prosti_faktori_to_string(n):
    """
    Funkcija vraca u tekstnom formatu proste faktore sa njihovim stepenima
    Funckija prima n tipa int i vraca tipa string
    """

    tekst_faktori = ""
    for i in range(1, n + 1):
        if n == 1:
            break
        
        if je_prost(i) and n % i == 0:
            tekst_faktori = tekst_faktori + str(i)

            stepen = 0
            while n > 1 and n % i == 0:
                stepen += 1
                n = n // i
            
            # ispisivanje stepena
            if stepen > 1:
                tekst_faktori = tekst_faktori + "^{}".format(stepen)
            
            if n > 1:
                tekst_faktori += " * "

    return tekst_faktori


# primjer funkcije koja vraca vrijednost bez ulaza
def pi():
    return 3.1415

# primjer funkcija koja prima ulaz, ali ne vraca nista
# defaultna vrijednost

# poslije parametra sa defaultnom vrijednoscu, svaki naredni parametar mora imati
# defaultnu vrijednost
def print_auto(boja, tip, marka, model, snaga=0):
    auto = "Auto\n"
    auto += "Boja: {}\n".format(boja)
    auto += "Tip: {}\n".format(tip)
    auto += "Marka: {}\n".format(marka)
    auto += "Model: {}\n".format(model)
    auto += "Snaga: {}KS\n".format(snaga)

    print(auto)

print_auto(
    "Plava",
    "Limuzina",
    "Opel",
    "Insignia",
    80
)

print_auto(
    "Crvena",
    "Limuzina",
    "Volkswagen",
    "Golf V",
    75
)

print_auto(
    "Zuta",
    "Limuzina",
    "Alfa Romeo",
    "Juliette",
    65
)