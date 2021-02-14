# Osobine kruga

PI = 3.1415 # konstanta -> varijabla koja se neće više mijenjati i naznačimo sa velikim slovima
# casting variables
r = float(input("Molimo Vas, unesite vrijednost poluprecnika r: ")) # = je operator dodjeljivanja, duck typing, inicijalizacija varijable

# Python imena varijabli su case-sensitive
R = 2 * r # precnik
print(type(r))
print("r:", r)
print("R:", R)

# imenovanje varijable mora poceti sa slovom ili _, a kasnije moze sadrzavati slovo, broj ili _


# print(type(float("88.984"))) # parsiranje ili type casting


povrsina_kruga = r ** 2 * PI
obim_kruga = 2 * r * PI

print("Povrsina kruga za dato r =", r, "je:", povrsina_kruga)
print("Obim kruga za dato r =", r, "je:", obim_kruga)


"""
neko_ime_varijable = 12.77
print(neko_ime_varijable)
neko_ime_varijable = "Neko ime"
print(neko_ime_varijable)
neko_ime_varijable = True
print(neko_ime_varijable)
"""