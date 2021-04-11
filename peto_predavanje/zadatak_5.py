# Oktagon duzine n koju unosi korisnik

n = int(input("Unesite broj n: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        if j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    for j in range(n):
        if i == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    for j in range(i + 1):
        if j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n):
    for j in range(3 * n):
        if j == 0 or j == 3 * n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()

for i in range(n):
    if i == 0:
        continue

    for j in range(i):
        print(" ", end=" ")
    
    for j in range(n - i):
        if j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    for j in range(n):
        if i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    for j in range(n - i):
        if j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()