print("Hello") # literal - doslovna vrijednost, primjer tipa string

print(type("Hello")) # primjer stringa, prikaze kao 'str'
print(1234)
print(type(1234)) # primjer integera, to jeste, cijeli broj, prikazuje kao 'int'
print(12.34)
print(type(12.34)) # primjer floata, to jeste, realni broj, prikazuje kao 'float'
print(True)
print(type(True)) # primjer boolean-a, to jeste, istinitosne vrijednosti, prikazuje kao bool
print(False)
print(type(False)) # primjer boolean-a

print("----------------------")

print("Cijeli brojevi i njihovi operatori")
# operator sabiranja: +
print("Sabiranje cijelih brojeva (zbir): ", 2 + 3)

# operator mnozenja: *
print("Mnozenje cijelih brojeva (proizvod):", 5 * 5)

# operator dijeljenja: /
print("Dijeljenje cijelih brojeva (rezultat dijeljenja): ", 35 / 4)

# operator cjelobrojnog dijeljenja: //
print("Cjelobrojno dijeljenje cijelih brojeva (rezultat dijeljenja): ", 35 // 4)

# operator modulo: %
print("Ostatak dijeljenja sa cijelim brojem: ", 35 % 4)

# operator oduzimanja: -
print("Oduzimanje cijelih brojeva: ", 5 - 3)

# Unarni operator: negacija
print("Negacija broja: ", -5 + 3)

# Operator eksponenciranja: **
print("Eksponenciranje cijelih brojeva: ", 2 ** 3)

print("----------------------")

print("Operatori podrzani od strane tipa string")

# Ovo nije operator sabiranja, ovo je operator konkatenacije
print("Ovo je tekst 1" + "Ovo je tekst 2" + "Ovo je tekst 3")

# print("Ovo" - "je") # -, /, //, %, * nije podrzan za stringove

# Operator * - operator ponavljanja za stringove, podrzava samo str i int
print("Jedan" * 10)
print(10 * "Jedan")

print("--------------------------------")
print("Uvod u matematičke izraze")
print("Netacna evaluacija razlomka: ", 1 + 4 / 3) # 2.3333333
print("Evaluacija razlomka: ", (1 + 4) / 3) # zaista zelimo, 1.66666667

print("Mini zadatak: ", ((2 + 4) * (2 + 4) * (2 + 4) + 5 * 5) / (3 - 5))
print("Mini zadatak (laksi nacin): ", ((2 + 4) ** 3 + 5 ** 2) / (3 - 5))

print("--------------------------------")
print("Logički operatori")

print("Manje od")
print("2 < 5:", 2 < 5)
print("2 < 2:", 2 < 2)
print("2 < 1:", 2 < 1)

print("Manje ili jednako od")
print("2 <= 5:", 2 <= 5)
print("2 <= 2:", 2 <= 2)
print("2 <= 1:", 2 <= 1)

print("Vece od")
print("2 > 1:", 2 > 1)
print("2 > 2:", 2 > 2)
print("2 > 5:", 2 > 5)

print("Vece ili jednako od")
print("2 >= 1:", 2 >= 1)
print("2 >= 2:", 2 >= 2)
print("2 >= 5:", 2 >= 5)

print("Jednakost")
print("2 == 2:", 2 == 2)
print("2 == 5:", 2 == 5)

print("Nejednakost")
print("2 != 2:", 2 != 2)
print("2 != 5:", 2 != 5)

print("Negacija")
print(not 2 == 2)
print(not 2 == 5)

print("and operacija") # operacija and daje True ako i samo ako su oba izraza True
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("or operacija") # operacija or daje True ukoliko bar jedan uslov je zadovoljen, to jeste True
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("Primjer 1:", False or False or True or False)

print("------------------------------")

print("Logicki izrazi")
print(not True or True and False)
print((False or False or False) and (False or False or True))

# osnovni kalkulator
# sistem ocjenjivanja učenika na osnovu unesenih ocjena za sve predmete

# Pitanja

print("Dvojni razlomak primjer")
print(((2 + 3) / (3 + 4)) / ((4 + 5) / (5 + 6)))

# Navodni znaci u stringu

print("Neki tekst: \"Ovo je pod navodnim znacima\"")
print('Neki tekst: "Ovo je pod navodnim znacima"')