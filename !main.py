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
sorok = []
lefut = False

print("Átlagszámító program\nKészítette: Ábrahám Dávid és Détári Leon")

while lefut == False:
    try:
        tantargyszam = int(input("Hány tantárgy átlagát szeretnéd kiszámítani? "))
        lefut = True
    except:
        print("nem jo :(") #LEON

for t in range(tantargyszam):
    print("Írja be a(z) ", t + 1, ". tantárgy nevét!") 
    tantargy = input()
    tantargyak.append(tantargy)


ido = asctime(localtime(time()))
with open("atlag.txt", "a", encoding="utf8()") as file:
    file.write(str(ido))

for i in range(tantargyszam):
    sorok = []
    print("A(z) ", tantargyak[i], " átlaga")
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
            else:
                print("A szém legyen 1 és öt kozott") #leon
            db = db + 1 
    db = db - 1
    print()
    sorok.append("\n")
    print("A(z) ", tantargyak[i], " eredménye:")
    sorok.append(f"A(z) {tantargyak[i]} eredménye:\n")
    print("----------------------------------------------")
    sorok.append("----------------------------------------------\n")
    print("Jelesek száma: ", jelesdb, "db")
    sorok.append(f"Jelesek száma: {jelesdb} db\n")
    print("Jók száma: ", jodb, "db")
    sorok.append(f"Jók száma: {jodb} db\n")
    print("Közepesek száma: ", kozepesdb, "db")
    sorok.append(f"Közepesek száma: {kozepesdb} db\n")
    print("Elégsegesek száma: ", elegsegesdb, "db")
    sorok.append(f"Elégsegesek száma: {elegsegesdb} db\n")
    print("Elégtelenek száma: ", elegtelen, "db") 
    sorok.append(f"Elégtelenek száma: {elegtelen}\n")
    print("----------------------------------------------") #ez sor2
    print("Jegyeid száma: ", db)
    sorok.append(f"Jegyeid száma: {db}\n")
    atlag = (jeles + jo + kozepes + elegseges + elegtelen) / db
    atlagok.append(atlag)
    print("Az átlagod: ", atlag, "\n")
    sorok.append(f"Az átlagod: {atlag} \n\n")

    with open("atlag.txt", "a", encoding="utf8()") as file:
        file.write("\n")
        file.writelines(sorok)
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

for b in range(len(atlagok)):
    teljesatlag = teljesatlag + atlagok[b]
teljesatlag = teljesatlag / len(atlagok)

with open("atlag.txt", "a", encoding="utf8()") as file:
    sor1 = f"Az összes tantárgyad teljes átlaga: {teljesatlag}"
    szoveg = str(sor1)
    file.write(szoveg)
    file.write("----------------------------------------------")

print("Az összes tantárgyad teljes átlaga: ", teljesatlag)  
print("Az összes eredményt mentsük egy .txt-be")  
input("A kilépéshez nyomjon egy [ENTER]-t")