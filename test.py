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
tantargyok = []
tantargy = ()
tantargyszam = ()
teljesatlag = 0

print("Átlag kiszámító program\n Készítette: Ábrahám Dávid és Détári Leon")
tantargyszam = int(input("Hány tantárgy átlagát szeretéd kiszámítani? "))

for t in range(tantargyszam):
    print("Írja be az ", t + 1, ". tantárgy nevét!")
    tantargy = input()
    tantargyok.append(tantargy)



for a in range(tantargyszam):
    print("A(z) ", tantargyok[a], " átlaga")
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
    print("A(z) ", tantargyok[a], " eredménye:")
    print("----------------------------------------------")
    print("Jelesek száma: ", jelesdb, "db")
    print("Jó-k száma: ", jodb, "db")
    print("Közepesek száma: ", kozepesdb, "db")
    print("Elegseges db: ", elegsegesdb, "db")
    print("Elegtelen db: ", elegtelen, "db")
    print("----------------------------------------------")
    print("Jegyeid száma: ", db)
    atlag = (jeles + jo + kozepes + elegseges + elegtelen) / db
    print("Az átlagod: ", atlag, "\n")
    teljesatlag = teljesatlag + atlag
    
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



if tantargyszam > 1:
    print("Az összes tantárgy átlaga8: ", teljesatlag / tantargyszam) 




   
input("A kilépéshez nyomjon [ENTER]")