from datetime import datetime, timedelta
class klienta_informacija():
    def __init__(self, vards,uzvards,vecums,garums,dzimums):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums
        self.garums = garums
        self.dzimums = dzimums
    def izvade(self):
        print("***")
        print(f"Vārds: {self.vards}\nUzvārds: {self.uzvards}\nVecums: {self.vecums}\nGarums: {self.garums}\nDzimums: {self.dzimums}")
        print("***")
    def abonesana(self):
        abonesanas_laiks = datetime.now()
        self.abonesanas_laiks = abonesanas_laiks
        print("Abonamenta izveides laiks", self.abonesanas_laiks.strftime("%Y-%m-%d"))
        abonesanas_veids = int(input("Izvēlaties abonamentu: "))
        while True:
            if abonesanas_veids == 1:
                self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=1)
                print("Abonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
                break
            if abonesanas_veids == 2:
                self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=7)
                print("Abonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
                break
            if abonesanas_veids == 3:
                self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=30)
                print("Abonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
                break
            if abonesanas_veids == 4:
                self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=365)
                print("Abonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
                break
            
            else:
                print("Ievadiet pareizu skaitli! (1-4)!")
                abonesanas_veids = int(input("Izvēlaties abonamentu: "))
        print("***")
        print("Klienta fails ir izveidots!")
    def failu_izveide(self):
        faila_nosaukums = self.vards+"_"+self.uzvards+".txt"
        with open(faila_nosaukums,"a", encoding = "utf-8") as file:
            file.write(f"Vārds: {self.vards}\nUzvārds: {self.uzvards}\nVecums: {self.vecums}\nGarums: {self.garums}\nDzimums: {self.dzimums}\n")
            file.write(f"Abonamenta izveides datums: {self.abonesanas_laiks}\nAbonamenta beigšanās datums: {self.abonesanas_beigsanas}")
        



vards = input("Ievadiet klienta vārdu: ")
uzvards = input("Ievadiet klienta uzvārdu: ")
vecums = input("Ievadiet klienta vecumu: ")
garums = input("Ievadiet klienta garumu: ")
dzimums = input("Ievadiet klienta dzimumu: ")
klients = klienta_informacija(vards,uzvards,vecums,garums,dzimums)

klients.izvade()
klients.abonesana()
klients.failu_izveide()