from time import * 

atlag = "a"
jeles = 0
jo = 0
kozepes = 0
elegseges = 0
elegtelen = 0
jelesdb = 0
jodb = 0
kozepesdb = 0
elegsegesdb = 0
elegtelendb = 0
db = 0
tantargyak = []
tantargy = 0
tantargyszam = 0
atlagok = []
teljesatlag = 0

print("Átlag kiszámító program\n Készítette: Ábrahám Dávid és Détári Leon")
tantargyszam = int(input("Hány tantárgy átlagát szeretéd kiszámítani? "))

for t in range(tantargyszam):
    print("Írja be az ", t + 1, ". tantárgy nevét!")
    tantargy = input()
    tantargyak.append(tantargy)



for a in range(tantargyszam):
    print("A(z) ", tantargyak[a], " átlaga")
    while atlag != 0:
        if atlag == 0:
            break
        else:
            atlag = int(input("Írd egymás után a jegyeidet: "))
            if atlag == 1:
                elegtelen = elegtelen + 1
                elegtelendb = elegtelendb + 1
            elif atlag == 2:
                elegseges = elegseges + 2
                elegsegesdb = elegsegesdb + 1
            elif atlag == 3:
                kozepes = kozepes + 3
                kozepesdb = kozepesdb + 1 
            elif atlag == 4:
                jo = jo + 4
                jodb = jodb + 1
            elif atlag == 5:
                jeles = jeles + 5
                jelesdb = jelesdb + 1
            db = db + 1 
    db = db - 1
    print()
    print("A(z) ", tantargyak[a], " eredménye:")
    print("----------------------------------------------")
    print("Jelesek száma: ", jelesdb, "db")
    print("Jó-k száma: ", jodb, "db")
    print("Közepesek száma: ", kozepesdb, "db")
    print("Elegseges db: ", elegsegesdb, "db")
    print("Elegtelen db: ", elegtelen, "db")
    print("----------------------------------------------")
    print("Jegyeid száma: ", db)
    atlag = (jeles + jo + kozepes + elegseges + elegtelen) / db
    atlagok.append(atlag)
    print("Az átlagod: ", atlag, "\n")
    
    #valtozo reset
    atlag = "a"
    jeles = 0
    jo = 0
    kozepes = 0
    elegseges = 0
    elegtelen = 0
    jelesdb = 0
    jodb = 0
    kozepesdb = 0
    elegsegesdb = 0
    elegtelendb = 0
    db = 0
    atlag = ()

print(atlagok)

for b in range(len(atlagok)):
    teljesatlag = teljesatlag + atlagok[b]
teljesatlag = teljesatlag / len(atlagok)

print(teljesatlag) 




print("Az összes tantárgy teljes átlaga: ", teljesatlag)    
input("A kilépéshez nyomjon [ENTER]")