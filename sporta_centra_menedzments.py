def izveleties_abonamentu():
    print("Izvēlaties abonamenta veidu: (1- dienas abonaments, 2- nedēļas abonaments, 3- mēneša abonaments, 4- gada abonaments):")
    izvele1 = input()
    veidi = {
        '1': 'dienas',
        '2': 'nedēļas',
        '3': 'mēneša',
        '4': 'gada'
    }
    return 


def izveleties_abonamentu():
    print("Izvēlaties abonamenta veidu: (1- dienas abonaments, 2- nedēļas abonaments, 3- mēneša abonaments, 4- gada abonaments):")
    izvele1 = input()
    veidi = {
        '1': 'dienas',
        '2': 'nedēļas',
        '3': 'mēneša',
        '4': 'gada'
    }
    return 




def galvena():
    while True:
        print("Ko jūs vēlaties darīt? (1- izviedot jaunu profilu, 2- dzēst abonamentu, 3- iziet):")
        izvele = input()
        if izvele == '1':
            klienta_informacija()
        elif izvele == '2':
            atcelt_abonamentu()          
        elif izvele == '3':
            print("Uzredzēšanos!")
            break
        else:
            print("Nepareiza izvēle, lūdzu mēģiniet vēlreiz.")

