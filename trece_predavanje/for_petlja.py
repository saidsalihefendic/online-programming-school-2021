# prvih 50 brojeva

suma = 0

suma = suma + 1
print(suma)

suma = suma + 2
print(suma)


suma = suma + 3
print(suma)

# for petlja, to jeste, for komanda
# obratiti paznju da range(m, n) ide od m do n - 1
# primjer: (0, 10) -> 0 - 9
for i in range(0, 10):
    print("Iteracija", i)

# sumiranje prvih N brojeva

N = 5
suma = 0
for i in range(1, N + 1):
    suma = suma + i
    
print("Suma prvih", N, "brojeva je:", suma)