# Zadatak
# Korisnik unosi prirodne brojeve m i n
# pri cemu m < n
# Program ispisuje sve proste brojeve u rasponu (m, n)
# te ispisuje njihovu sumu i njihov proizvod

m = int(input("Unesite broj m: "))
n = int(input("Unesite broj n: "))

if m >= n:
    print("Nisu ispravno uneseni podaci.")
else:
    suma_prostih = 0
    proizvod_prostih = 1
    for i in range(m, n + 1):
        # Testiranje da li je brojac i prost broj
        je_prost = True
        for j in range(2, i): # 2 -> i - 1 je raspon 
            if i % j == 0:
                je_prost = False
                break

        if je_prost and i > 1:
            suma_prostih = suma_prostih + i
            proizvod_prostih = proizvod_prostih * i
            print(i)
    
    print("Suma prostih:", suma_prostih)
    print("Proizvod prostih:", proizvod_prostih)