N = int(input("Unesite n: "))

suma = 0
for brojac in range(1, N + 1):
    # suma = suma + N # N = 4 -> 4 + 4 + 4 + 4
                    # N = 5 -> 5 + 5 + 5 + 5 + 5
    suma = suma + brojac

print("Suma od 1 do", N, "je:", suma)