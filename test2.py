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
szoveg = ""
tszoveg = []
sor = "\n"
sor1 = ""   #leon fel
sor2 = ""
sor3 = ""
sor4 = ""
sor5 = ""
sor6 = ""
sor7 = ""
sor8 = ""
sor9 = ""
sor10 = ""

print("Átlagszámító program\nKészítette: Ábrahám Dávid és Détári Leon")
tantargyszam = int(input("Hány tantárgy átlagát szeretnéd kiszámítani? "))

for t in range(tantargyszam):
    print("Írja be a(z) ", t + 1, ". tantárgy nevét!")
    tantargy = input()
    tantargyak.append(tantargy)


ido = asctime(localtime(time()))
with open("atlag.txt", "a", encoding="utf8()") as file:
    file.write(str(ido))

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
    sor1 = ""
    print("A(z) ", tantargyak[a], " eredménye:")
    sor2 = f"A(z) {tantargyak[a]} eredménye:"
    print("----------------------------------------------")
    sor3 = "----------------------------------------------"
    print("Jelesek száma: ", jelesdb, "db")
    sor4 = f"Jelesek száma: {jelesdb} db"
    print("Jó-k száma: ", jodb, "db")
    sor5 = f"Jó-k száma: {jodb} db"
    print("Közepesek száma: ", kozepesdb, "db")
    sor6 = f"Közepesek száma: {kozepesdb} db"
    print("Elégseges száma: ", elegsegesdb, "db")
    sor7 = f"Elégseges száma: {elegsegesdb} db"
    print("Elégtelen száma: ", elegtelen, "db")
    sor8 = f"Elégtelen száma: {elegtelen}"
    print("----------------------------------------------") #ez sor2
    print("Jegyeid száma: ", db)
    sor9 = f"Jegyeid száma: {db}"
    atlag = (jeles + jo + kozepes + elegseges + elegtelen) / db
    atlagok.append(atlag)
    print("Az átlagod: ", atlag, "\n")
    sor10 = f"Az átlagod: {atlag} \n"
    szoveg = str(sor1) + sor + str(sor2) + sor + str(sor3) + sor + str(sor4) + sor + str(sor5) + sor + str(sor6) + sor + str(sor7) + sor + str(sor8) + sor + str(sor2) + sor + str(sor9) + sor + str(sor10) + sor
    
    with open("atlag.txt", "a", encoding="utf8()") as file:
        file.write("\n")
        file.write(str(szoveg))
        file.write("")

        
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
    sor1 = ""   
    sor2 = ""
    sor3 = ""
    sor4 = ""
    sor5 = ""
    sor6 = ""
    sor7 = ""
    sor8 = ""
    sor9 = ""
    sor10 = ""






for b in range(len(atlagok)):
    teljesatlag = teljesatlag + atlagok[b]
teljesatlag = teljesatlag / len(atlagok)



with open("atlag.txt", "a", encoding="utf8()") as file:
    sor1 = f"Az összes tantárgyad teljes átlaga: {teljesatlag}"
    szoveg = str(sor1)
    file.write(szoveg)
    file.write("\n")



print("Az összes tantárgyad teljes átlaga: ", teljesatlag)  
print("Az összes eredményt mentsük egy .txt-be")  
input("A kilépéshez nyomjon egy [ENTER]-t")