from datetime import datetime, timedelta
class klienta_informacija():
    def __init__(self, vards,uzvards,vecums,garums,dzimums):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums
        self.garums = garums
        self.dzimums = dzimums
    def izvade(self):
        print(self.vards,self.uzvards,self.vecums,self.garums,self.dzimums)
    def abonesana(self):
        abonesanas_laiks = datetime.now()
        self.abonesanas_laiks = abonesanas_laiks
        print("Abonamenta izveides laiks", self.abonesanas_laiks.strftime("%Y-%m-%d"))
        abonesanas_veids = int(input("Izvēlaties abonamentu: "))
        if abonesanas_veids == 1:
            self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=1)
            print("Abonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
        if abonesanas_veids == 2:
            self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=7)
            print("Abonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
        if abonesanas_veids == 3:
            self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=30)
            print("Abonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
        if abonesanas_veids == 4:
            self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=365)
            print("Abonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))


vards = input("Ievadiet klienta vārdu: ")
uzvards = input("Ievadiet klienta uzvārdu: ")
vecums = input("Ievadiet klienta vecumu: ")
garums = input("Ievadiet klienta garumu: ")
dzimums = input("Ievadiet klienta dzimumu: ")
klients = klienta_informacija(vards,uzvards,vecums,garums,dzimums)

klients.izvade()
klients.abonesana()