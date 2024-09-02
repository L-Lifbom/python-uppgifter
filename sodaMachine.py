import random
import os


huvudmeny = ['Köp enstaka läskburkar', 'Köp ett/flera läskflak', 'Se utbudet', 'Avsluta']
meddelande = "\nSkriv in numret för det val du vill fortsätta med: "
enter = "\nTryck enter"
läsk = [['Coca Cola', 100], ['Pepsi', 100], ['Sprite', 100], ['Fanta', 100], ['Trocadero', 100], 'Backa']
pris = 8
flak_pris = 96


def enstaka():
#Köp av enstaka läskburkar
    while True:

        os.system('cls')
        print("Nedan visas alla olika läskdrycker i vårat utbud")
        for i in range(len(läsk)-1):
            print(i+1, läsk[i][0])

        print (len(läsk), läsk[len(läsk)-1])
        svar = int(input(meddelande))

        if svar < len(läsk):
            os.system('cls')
            svar_2 = int(input("Hur många {} vill du köpa? Köp av 12 eller mer görs i flak/backar: ".format(läsk[svar-1][0])))

            if svar_2 > läsk[svar-1][1]:
                print("\nDet finns bara {} kvar, Du kan inte köpa mer än det.".format(läsk[svar-1][1]))
                input(enter)
            elif svar_2 < 12:
                os.system('cls')
                print("Priset för köpet blir totalt {} kr.".format(pris*svar_2))
                svar_3 = input("\nForsätt med köpet Y/N: ").lower()

                if svar_3 == "y":
                    os.system('cls')
                    print("---Godkänt köp---")
                    input(enter)
                    läsk[svar-1][1] = läsk[svar-1][1]-svar_2
                    if läsk[svar-1][1] <= 0:
                        del läsk[svar-1] 
                elif svar_3 == "n":
                    os.system('cls')
                    print("---Avbrutet köp---")
                    input(enter)
                    main()

            elif svar_2 > 11:
                os.system('cls')
                print ("Välj endast mellan 1-11. Köp av större mängd görs i hela flak.")
                input(enter)

        elif svar == len(läsk):
            main()


def backar():
#Köp av flak/backar med läsk. Både välja själv och random val
    os.system('cls')
    print("Ett flak består av 12 läskburkar.")
    antal_flak = 0
    for i in range(len(läsk)-1):
        antal_flak += läsk[i][1]
    svar = int(input("Hur många flak vill du köpa? Svara med ett nummer 0-{}: ".format(int(antal_flak/12))))
    print("{} flak kostar {} kr".format(svar, flak_pris*svar))
    input(enter)
    os.system('cls')
    svar_2 = input("Välj läsk själv (V)\nRandom läsk (R)\nSvar: ").lower()

    #Välja vilka sorters läskdrycker själv
    if svar_2 == "v":
        os.system('cls')
        print("Du valde att köpa {} flak med läsk. Det blir totalt {} burkar".format(svar, svar*12))
        print("Skriv in hur många läskburkar från varje sort du vill köpa. Välj mellan 0 till {} läskburkar".format(svar*12))
        antal_köpta = []
        summa = 0
        
        for i in range(len(läsk)-1):
            print(f"{läsk[i][0]}: ", end="")
            antal = int(input())
            antal_köpta.append(antal)
            summa += antal

        if summa == svar*12:
            os.system('cls')
            print("Okej totalt har du valt:")
            for i in range(len(läsk)-1):
                print(f"{antal_köpta[i]} st {läsk[i][0]}")
            print("Totalt kostar det {} kr".format(flak_pris*svar))
            betala = input("Forsätt med köp Y/N?: ").lower()

            if betala == "y":
                os.system('cls')
                print("---Godkänt köp---")
                input(enter)
                for i in range(len(läsk)-1):
                    läsk[i][1] = läsk[i][1]- antal_köpta[i]
            elif betala == "n":
                os.system('cls')
                print("---Avbrutet köp---")
                input(enter)
                main()
        else:
            os.system('cls')
            print("---FEL---\nDu måste skriva in rätt mängd burkar!")
            input(enter)
            backar()

    #Ge random läskdrycker
    elif svar_2 == "r":
        antal_kvar = svar*12
        drickor = [0, 0, 0, 0, 0]

        while antal_kvar > 0:
            slump = random.randint(0, len(läsk)-2)
            antal = random.randint(0, min(antal_kvar, läsk[slump][1]-drickor[slump], 10))
            antal_kvar -= antal
            drickor[slump] += antal
        print(f"Ditt flak innehåller: ")

        for i in range(len(läsk)-1):
            print(f"{drickor[i]} st {läsk[i][0]}")

        print("Priset för köpet blir totalt {} kr.".format(flak_pris*svar))
        svar_3 = input("\nForsätt med köpet Y/N: ").lower()

        if svar_3 == "y":
            os.system('cls')
            print("---Godkänt köp---")
            input(enter)
            for i in range(len(läsk)-1):
                läsk[i][1] = läsk[i][1]-drickor[i]
        elif svar_3 == "n":
            os.system('cls')
            print("---Avbrutet köp---")
            input(enter)
            main()
    
    elif svar_2 != "v" or "r":
        os.system('cls')
        print("Svara endast (V) eller (R)")
        input(enter)
        backar()


def utbud():
#Visar aktuellt utbud av alla drycker
    os.system('cls')
    print("Mängden läskburkar i lager just nu\n")
    for i in range(len(läsk)-1):
        print(i+1, läsk[i])
    input(enter)


def main():
#Huvudmenyn för programmet
    while True:
        try:
            os.system('cls')
            print("Läskmaskin\n")
            for i in range(len(huvudmeny)):
                print(i+1, huvudmeny[i])
            svar = int(input(meddelande))
            match svar:
                case 1:
                    enstaka()
                case 2:
                    backar()
                case 3:
                    utbud()
                case 4:
                    exit()
                case _:
                    os.system('cls')
                    print("Svara endast 1-4")
                    input(enter)
        #Felhantering
        except ValueError:
            os.system('cls')
            print("Svara endast med ett nummer!")
            input(enter)
        except Exception:
            os.system('cls')
            print("Något gick fel!")
            input(enter)


if __name__ == '__main__':
    main()