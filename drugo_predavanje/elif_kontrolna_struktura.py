number = int(input("Unesite cijeli broj: "))

print("Uslovna kontrolna struktura sa elifom")
# Jedna komponenta
# elif -> else if
if number > 0:
    print("Broj je pozitivan")

elif number >= 0:
    print("Broj je nenegativan")
else:
    print("Broj je negativan")


print("Uslovna kontrolna struktura bez elifa")
# Jedna komponenta
if number > 0:
    print("Broj je pozitivan")

# Druga komponenta
if number >= 0:
    print("Broj je nenegativan")
else:
    print("Broj je negativan")