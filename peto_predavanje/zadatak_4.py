# Korisnik unosi prirodan broj n.
# Program treba da iscrta romb sa njegovim dijagonalama
# Primjer za n = 7


n = int(input("Unesite n: "))


for i in range(n):
    for j in range(i):
        print(" ", end="")

    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i == n - j - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()