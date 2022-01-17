tantargy = ()
tantargyok = []
tantargyszam = ()


tantargyszam = int(input("Hány tantárgy átlagát szeretéd kiszámítani? "))

for t in range(tantargyszam):
    print("Írja be az ", t + 1, ". tantárgy nevét!")
    tantargy = input()
    tantargyok.append(tantargy)

print(tantargyszam)
print(tantargyok)