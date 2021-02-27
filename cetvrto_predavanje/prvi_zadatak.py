# prirodan broj izrazen u svoje proste faktore

# 21 = 3 * 7
# 25 = 5 * 5 = 5 ^ 2

n = int(input("Unesite prirodan broj n: "))

broj = n
for i in range(2, n):
    je_prost = True
    for j in range(2, i):
        if i % j == 0:
            je_prost = False
            break

    if je_prost and i > 1:
        eksponent = 0

        while broj > 0 and broj % i == 0:
            eksponent += 1
            broj = broj // i
        
        if eksponent == 1:
            print(i, end=" ")
            if broj > 1:
                print("*", end=" ")
        elif eksponent > 1:
            print(i, "^", eksponent, end=" ")
            if broj > 1:
                print("*", end=" ")

        if broj == 1:
            break   