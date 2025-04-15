import os
from datetime import datetime, timedelta

class klienta_informacija():
    def __init__(self, vards, uzvards, vecums, garums, dzimums):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums
        self.garums = garums
        self.dzimums = dzimums

    def izvade(self):
        print(self.vards, self.uzvards, self.vecums, self.garums, self.dzimums)
        print("***")
        print(f"Vārds: {self.vards}\nUzvārds: {self.uzvards}\nVecums: {self.vecums}\nGarums: {self.garums}\nDzimums: {self.dzimums}")
        print("***")

    def abonesana(self):
        abonesanas_laiks = datetime.now()
        self.abonesanas_laiks = abonesanas_laiks
        print("Abonamenta izveides datums", self.abonesanas_laiks.strftime("%Y-%m-%d"))
        izveleties_abonamentu()
        abonesanas_veids = int(input("Jūsu izvēle: "))

        while True:
            if abonesanas_veids == 1:
                self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=1)
                print("\nAbonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
                break
            if abonesanas_veids == 2:
                self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=7)
                print("\nAbonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
                break
            if abonesanas_veids == 3:
                self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=30)
                print("\nAbonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
                break
            if abonesanas_veids == 4:
                self.abonesanas_beigsanas = abonesanas_laiks + timedelta(days=365)
                print("\nAbonamenta beigu datums: ", self.abonesanas_beigsanas.strftime("%Y-%m-%d"))
                break
            
            else:
                print("Ievadiet pareizu skaitli! (1-4)!")
                abonesanas_veids = int(input("Jūsu izvēle: "))
        self.abonesanas_beigsanas = self.abonesanas_beigsanas.strftime("%Y-%m-%d") #Pārviedo lai izvada tikai gadu, mēnesi un dienu
        self.abonesanas_laiks = self.abonesanas_laiks.strftime("%Y-%m-%d")
        print("***")
        print("Klienta fails ir izveidots!")

    def failu_izveide(self):
        faila_nosaukums = self.vards+"_"+self.uzvards+".txt"
        with open(faila_nosaukums,"w", encoding = "utf-8") as file:
            file.write(f"Vārds: {self.vards}\nUzvārds: {self.uzvards}\nVecums: {self.vecums}\nGarums: {self.garums}\nDzimums: {self.dzimums}\n")
            file.write(f"\nAbonamenta izveides datums: {self.abonesanas_laiks}\nAbonamenta beigšanās datums: {self.abonesanas_beigsanas}")
        

def izveleties_abonamentu():
    print("\nIzvēlaties abonamenta veidu: \n1- dienas abonaments \n2- nedēļas abonaments \n3- mēneša abonaments \n4- gada abonaments")
    


def atcelt_abonamentu():
    filename = input("Ievadiet faila nosaukumu, no kura vēlaties dzēst abonamentu: ")
    if not os.path.exists(filename):
        print(f"Fails {filename} neeksistē!")
        return
    os.remove(filename)
    print("Abonaments ir dzēsts.") 

def galvena():
    while True:
        print("Ko jūs vēlaties darīt? (1- izveidot jaunu profilu, 2- dzēst abonamentu, 3- iziet):")
        izvele = input()
        if izvele == '1':
            vards = input("Ievadiet vārdu: ")
            uzvards = input("Ievadiet uzvārdu: ")
            vecums = input("Ievadiet vecumu: ")
            garums = input("Ievadiet garumu: ")
            dzimums = input("Ievadiet dzimumu: ")
            klients = klienta_informacija(vards, uzvards, vecums, garums, dzimums)
            klients.izvade()
            klients.abonesana()
            klients.failu_izveide()
        elif izvele == '2':
            atcelt_abonamentu()          
        elif izvele == '3':
            print("Uzredzēšanos!")
            break
        else:
            print("Nepareiza ievade, lūdzu ievadiet skaitli (1-3).")

galvena()