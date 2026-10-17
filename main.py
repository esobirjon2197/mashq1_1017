class Uy:
    eshik = "2x1"
    def __init__(self, egasi, elektr=False, gaz=False, suv=False):
        self.egasi = egasi
        self.elektr = elektr
        self.gaz = gaz
        self.suv = suv

    def malumot(self):
        print(f"Eagasi: {self.egasi}\tElektr: {self.elektr}\tGaz: {self.gaz}\tSuv: {self.suv}")


u1 = Uy("Azamat T.")
u2 = Uy("Jahongir O.",True)
u3 = Uy("Sarvar X.",True, True)


u1.malumot()
u2.malumot()
u3.malumot()
