import random

def feladat1():
    text=(input("Jó napod van?"))

    if text=="Igen":
        print("Örülök neki!")
    elif text=="Nem":
        print("Nem örülök neki!")
    else:
        print("Sajnos nem értem a válaszodat!")

#feladat1()

def feladat2():
    
    try:
        number=int(input("Kérem a számot!"))

        if number%2==0:
            print("Aszám páros.")
        else:
            print("A szám páratlan.")
    except:
        print("nem jó értéket adtál meg.")
        
#feladat2()
def feladat3():
    try:
        rnd=random.randrange(1,6)
        print(rnd)
        number=0
        

        while  number<1 or number>5:
            
            number=int(input("Kérem a számot 1 és 5 között!"))
        if rnd>number:
            print("Nagyobb a generált szám!")
        elif rnd<number:
            print("Kisebb a generált szám!")
        else:
            print("Eltaláltad")
    except:
        print("Nem jó formátum.")


#feladat3()

def ciklus1():
    for i in range(1,11):
        if(i%2==0):
            print(i)

#ciklus1()

def ciklus2():
    for i in reversed(range(1,11)):
        print(i)

#ciklus2()

def ciklus3():
    for i in range(10,0,-1):
        if i%2!=0:
            print(i)
#ciklus3()
        
