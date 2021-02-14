"""
Osnovni kalkulator
-------------------------

1. Sabiranje
2. Oduzimanje
3. Mnozenje
4. Dijeljenje
5. Eksponenciranje
6. Korjenovanje
7. Postotak
8. Povrsina i obim kvadrata
9. Povrsina i obim pravougaonika
10. Testiranje da li tri broja mogu formirati trougao
"""

print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("Dobrodosli u osnovni kalkulator. Imate sljedece mogucnosti: ")
print("1. Sabiranje")
print("2. Oduzimanje")
print("3. Mnozenje")
print("4. Dijeljenje")
print("5. Eksponenciranje")
print("6. Korjenovanje")
print("7. Postotak")
print("8. Povrsina i obim kvadrata")
print("9. Povrsina i obim pravougaonika")
print("10. Testiranje da li tri broja mogu formirati trougao")

menu_item = int(input("Odaberite operaciju: "))

if menu_item == 1:
    a = float(input("Unesite prvi broj: "))
    b = float(input("Unesite drugi broj: "))
    print(a, "+", b, "=", a + b)
elif menu_item == 2:
    a = float(input("Unesite prvi broj: "))
    b = float(input("Unesite drugi broj: "))
    print(a, "-", b, "=", a - b)
elif menu_item == 3:
    a = float(input("Unesite prvi broj: "))
    b = float(input("Unesite drugi broj: "))
    print(a, "*", b, "=", a * b)
elif menu_item == 4:
    a = float(input("Unesite brojnik: "))
    b = float(input("Unesite nazivnik: "))
    print(a, "/", b, "=", a / b)
elif menu_item == 5:
    a = float(input("Unesite vrijednost: "))
    b = float(input("Unesite eksponent: "))
    print(a, "**", b, "=", a ** b)
elif menu_item == 6:
    # korijen iz a -> a ** (1 / 2)
    # treci korijen iz a -> a ** (1 / 3)
    # 5.7 korijen iz a -> a ** (1 / 5.7)
    a = float(input("Unesite vrijednost: "))
    b = float(input("Unesite korijen: "))
    print("sqrt(", a, "," , b, ") =", a ** (1 / b))
elif menu_item == 7:
    # a = 100, b = 95.3 => 100 * 0.953
    # % -> modulo operator, ostatak pri dijeljenju
    a = float(input("Unesite vrijednost: "))
    b = float(input("Unesite postotak: "))
    print(b, "%", "od", a, "=", a * b / 100)
elif menu_item == 8:
    a = float(input("Unesite stranicu kvadrata: "))

    povrsina_kvadrata = a ** 2
    obim_kvadrata = 4 * a
    dijagonala_kvadrata = a * (2 ** (1 / 2))

    print("Povrsina kvadrata:", povrsina_kvadrata)
    print("Obim kvadrata:", obim_kvadrata)
    print("Dijagonala kvadrata:", dijagonala_kvadrata)
elif menu_item == 9:
    a = float(input("Unesite duzinu pravougaonika: "))
    b = float(input("Unesite sirinu pravougaonika: "))

    povrsina_pravougaonika = a * b
    obim_pravougaonika = 2 * a + 2 * b
    dijagonala_pravougaonika = (a ** 2 + b ** 2) ** (1 / 2)

    print("Povrsina kvadrata:", povrsina_pravougaonika)
    print("Obim kvadrata:", obim_pravougaonika)
    print("Dijagonala kvadrata:", dijagonala_pravougaonika)
elif menu_item == 10:
    a = float(input("Unesite prvi broj: "))
    b = float(input("Unesite drugi broj: "))
    c = float(input("Unesite treci broj: "))

    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            print("Ova tri broja mogu formirati trougao.")
        else:
            print("Ova tri broja ne mogu formirati trougao.")
    else:
        print("Nisu ispravno uneseni brojevi, jer moraju biti pozitivni.")
else:
    print("Niste odabrali ispravan podmeni, molimo Vas, probajte ponovo.")
print("+++++++++++++++++++++++++++++++++++++++++++++++")