
#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a legkisebb értéket ezek közül!
def feladat1():
    tomb =[]
    for i in range(3):
        tomb.append(int(input("Adj meg egy számot!")))
    #print(min(tomb))
    tomb.sort()
    print(tomb[0])
    #vagy  print(f"A legkisebb elem: {min(tomb)} ")

#feladat1()

#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a legnagyobb értéket ezek közül!

def feladat2():
    tomb =[]
    for i in range(3):
        tomb.append(int(input("Adj meg egy számot!")))
    print(max(tomb))
    #tomb.reverse()
    #print(tomb[0])

#feladat2()

#Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.
def feladat3():
    pontszam=int(input("Add meg a pontszámodat!"))
    if pontszam < 50: print("Egyes")
    if pontszam >= 50 and pontszam < 60: print("Kettes")
    if pontszam >= 60 and pontszam < 70: print("Hármas")
    if pontszam >= 70 and pontszam < 85: print("Négyes")
    if pontszam >= 85 and pontszam <100: print("Ötös")

"""
def feladat3():
    pontszam =-1
    while pontszam < 0 or pontszam >100:
        pontszam= int(input("Kérem a dolgozatod pontszámát: "))
    if pontszam < 50:
        print("Elégtelen")
    elif pontszam < 60:
        print("Elégséges")
    elif pontszam < 70:
        print("Közepes")
    elif pontszam < 85:
        print("Jó")
    else:
        print("Jeles")
"""
#feladat3()

#Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!

"""def feladat4():
    szam=int(input("Adj meg egy egész számot!"))
    if szam%3==0:
        print("A szám osztható 3-al.")
    if szam%5==0:
        print("A szám osztható 5-el.")
    if szam%3==0 and szam%5==0:
        print("A szám osztható 3-al és 5-el is.")
    if szam%3!=0 and szam%5!=0:
        print("A szám nem osztható 3-al és 5-el sem.")

feladat4()"""
"""def feladat4():
    oszthato = False

    szam = int(input("Kérek egy számot!"))

    if szam %3 == 0 or szam %5 == 0
        oszthato = True
       
    if oszthato ==True
        print("Igen")
    else:
        print("Nem")

feladat4()"""

#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!  

def feladat5():
    a=int(input("Kerem a értékét:"))
    b=int(input("Kerem b értékét:"))
    c=int(input("Kerem c értékét:"))

    van = False
    if (a+b) == c:
        van=True

    if (a+c) == b:
        van=True

    if (c+b) == a:
        van=True

    if van:
        print("van ilyen szám!")
    else:
        print("Nincs ilyen szám!")
#feladat5()

#Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a képernyőre, hogy mind a három páros szám-e (igen/nem)!

def feladat6():
    szamok =[]
    j=1
    db=0

    for i in range(3):
        szamok.append(int(input(f"Kérem a(z) {j} számot:")))
        j=j+1

    for i in szamok:
        if i %2 == 0:
            db=db+1
            
    if db ==3:
        print("Az összes páros!")
    else:
        print("Van köztük páratlan!")


    """a=int(input("Kerem a értékét:"))
    b=int(input("Kerem b értékét:"))
    c=int(input("Kerem c értékét:"))"""

feladat6()

        


