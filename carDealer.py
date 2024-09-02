import random

#Personal ansvariga för bilfirman
personal = ['Lars', 'Johan', 'Emilie', 'Alice']
personal_1 = personal[random.randint(0,len(personal))]

meddelande = "\nSkriv in numret för det val du vill fortsätta med: "
ogiltigt = "\n------------Inget giltigt svar! Svara endast de listade alternativen------------."
ogiltigt_2 = "\n------------Ogiltigt svar, skriv endast Y eller N------------"
meny_1 = ['Köpa', 'Sälja', 'Service', 'Register', 'Avsluta Programmet', '(Backa)']
bilar = ['BMW iX', 'Tesla Model-3', 'Volvo V90', 'Toyota Corolla', 'Mercedes-Benz A-Klass']
service_1 = ['Service', 'Reparationer', 'Garantiärenden']
garanti_längd = ['(1-3 år)', '(3-8 år)', '(8+ år)']

#Menyn för att köpa en bil
def köpa():
    svar = 1
    while svar != (len(bilar)+1):
        print ("\nOkej, så du ska köpa en bil. Vi har ett stort utbud. Välj ett alternativ 1-6.")
        for i in range(len(bilar)):
            print (i+1, bilar[i])
        print (f"{len(bilar)+1} (Backa)")
        pris = random.randint(100000,500000)
        svar = int(input(meddelande))
        if svar < (len(bilar)+1):
            print (f"\nOkej, så vi har en {bilar[svar-1]}, jag kan sälja den för {pris} kr")
            svar_2 = input("Vill du köpa eller inte Y/N?: ").lower()
            if svar_2 == "y":
                print ("\n------------Grattis, på köpet för din nya bil, då tar vi bort den ur försäljning!------------")
                input("Tryck enter för att gå tillbaka")
                del bilar[svar-1]
            elif svar_2 == "n":
                print ("\n------------Vad synd att bilen inte passade dig!------------")
                input("Tryck enter för att gå tillbaka")
            else:
                print(ogiltigt_2)

#Menyn för att sälja en bil
def sälja():
    pris = random.randint(20000,60000)
    print ("\nOkej så du vill sälja din bil. Vad har du för sorts bilmärke?")
    svar = input ("Svara på frågan eller tryck 1 för att backa: ")
    if svar != "1":
        svar_2 = input("Vad är det för modell?: ")
        print("Okej så du har en {} {}, jag kan köpa den av dig för {} kr.".format(svar, svar_2, pris))
        svar_3 = input ("Vill du sälja bilen Y/N?: ").lower()
        if svar_3 == "y":
            print("\nTack för en bra affär! Din bil är tillagd i vårt lager och möjligt för kunder att köpa.")
            input("Tryck enter för att gå tillbaka")
            såld_bil = svar + " " + svar_2
            bilar.append(såld_bil)
        elif svar_3 == "n":
            print("\n------------Okej, vi förstår att priset inte passade dig------------")
            input("Tryck enter för att gå tillbaka")
        elif svar_3 != "y" or "n":
            print(ogiltigt_2)

#Menyn för service på en bil
def service():
    svar = 1
    while svar != 4:
        print ("\nPå den här avdelningen kan du välja mellan följande:")
        for i in range(len(service_1)):
            print (i+1, service_1[i])
        print ("4 Backa")
        svar = int(input(meddelande))
        pris = random.randint(10000,20000)
        if svar == 1:
            print(f"\nOkej, du har valt service på din bil. Det kommer kosta dig totalt {pris} kr.")
            svar_2 = input("Vill du fortsätta Y/N?: ").lower()
            if svar_2 == "y":
                print ("\nOkej, då börjar vi nu och ringer dig när du kan hämta upp bilen.")
            elif svar_2 == "n":
                print ("\n------------Okej, du skickas tillbaka till menyn------------")
            elif svar_2 != "y" or "n":
                print(ogiltigt_2)
        elif svar == 2:
            print("Vad är det som behöver repareras?")
            reparera = input("Svar: ")
            print ("Det kommer kosta {} för att reparera {} på din bil.".format(pris, reparera))
            svar_3 = input("Vill du fortsätta Y/N?: ").lower()
            if svar_3 == "y":
                print ("\nOkej, då börjar vi nu och ringer dig när du kan hämta upp bilen.")
            elif svar_3 == "n":
                print ("\n------------Okej, du skickas tillbaka till menyn------------")
            elif svar_3 != "y" or "n":
                print(ogiltigt_2)
        elif svar == 3:
            print("\nOkej beskriv ditt garantiärende för oss.")
            garanti = input("Svar: ")
            print("\nHur länge sedan köpte du bilen från oss?")
            for i in range(len(garanti_längd)):
                print (i+1, garanti_längd[i])
            svar_4 = input(meddelande)
            if svar_4 == "1":
                print(f"Problem:", garanti)
                print("Bilålder: 1-3 år")
                print("\nUtifrån informationen du lämnat ska du få en utbetalning på 10000 kr.")
                input("Tryck enter för att gå tillbaka")
            elif svar_4 == "2":
                print(f"Problem:", garanti)
                print("Bilålder: 3-8 år")
                print("\nUtifrån informationen du lämnat ska du få en utbetalning på 2000 kr.")
                input("Tryck enter för att gå tillbaka")     
            elif svar_4 == "3":
                print(f"Problem:", garanti)
                print("Bilålder: 8+ år")
                print("\nUtifrån informationen du lämnat har din garanti gått ut.")
                input("Tryck enter för att gå tillbaka")
        elif svar != 4:
            print(ogiltigt)

#Visar alla registrerade namn
def register(användarnamn):
    svar = "svar"
    while svar != "y":
        print("\nHär sparas alla köpare")
        print (användarnamn)
        svar = input("Backa: Y/N?: ").lower()

#Start menyn
def meny(användare, användarnamn):
    svar = 1
    while svar != 6:
        print("\nHej {}, välkommen till Bilarnas Värld, Jag heter {} och kommer att hjälpa dig idag!\n".format(användare, personal_1))
        for i in range(len(meny_1)):
            print (i+1, meny_1[i])
        svar = int(input(meddelande))
        if svar == 1:
            köpa()
        elif svar == 2:
            sälja()
        elif svar == 3:
            service()
        elif svar == 4:
            register(användarnamn)
        elif svar == 5:
            exit()
        elif svar != 6:
            print (ogiltigt)

#Lägger till och sparar namn
def main():
    användarnamn = []
    while True:
        svar = input("\nÄr du en ny användare Y/N?: " ).lower()
        if svar == "y":
            användarnamn.append(input("Skriv ett nytt användarnamn: "))
            meny(användarnamn[len(användarnamn)-1], användarnamn)
        elif svar == "n":
            användare = input("Vad är ditt användarnamn?: ")
            finns_användare = False
            for i in användarnamn:
                if användare == i:
                    finns_användare = True
                    meny(användare, användarnamn)
            if not finns_användare:
                print ("Ditt användarnamn finns inte! Skapa ett användarnamn.")
        else:
            print("Ogiltigt svar, skriv endast Y eller N")

if __name__ == '__main__':
    main()