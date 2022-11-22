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
        
feladat2()

