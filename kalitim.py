class Canli():
    def __init__(self,tur,beslenme,cins):
        self.tur = tur
        self.beslenme=beslenme
        self.cins=cins
    def bilgileriGoster(self):
        print(f"Tür: {self.tur}\nBeslenme: {self.beslenme}\nCins: {self.cins}")

class Kedi(Canli):
    def __init__(self,tur,beslenme,cins,ad,renk,cinsiyet):
        super().__init__(tur,beslenme,cins)
        self.ad=ad
        self.renk=renk
        self.cinsiyet=cinsiyet
    def bilgileriGoster(self):
        super().bilgileriGoster()
        print(f"Ad: {self.ad}\nRenk: {self.renk}\nCinsiyet: {self.cinsiyet}")
        
cat=Kedi("Kedigiller","Hepçil","Ankara Kedisi","Wadu","Beyaz","Erkek")
cat.bilgileriGoster()
