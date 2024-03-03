# class Araba():
#     def __init__(self,marka,model,hp,yil):
#         self.marka=marka
#         self.model=model
#         self.hp=hp
#         self.yil=yil
#     def bilgileriGoster(self):
#         print(f"Marka: {self.marka}\nModel: {self.model}\nHp: {self.hp}\nYıl: {self.yil}")
#     def __str__(self):
#         return self.marka
    

# car1=Araba("BMW","5.20i","125 HP","2020")
# car2=Araba("Mercedes-benz","S Class","348 HP","2020")
# car3=Araba("Toyota","Corolla","96 HP","2020")
# print("-------------------")
# car1.bilgileriGoster()
# print("-------------------")
# car2.bilgileriGoster()
# print("-------------------")
# car3.bilgileriGoster()
# print("-------------------")
# liste=[car1,car2,car3]
# for i in liste:
#     print(i)

# # Bir canlı clası oluşturun ve bu canlının özelliklerini kutucu  methot ile alın ve bu canlının cinsiyetine göre sonuna kızım ya da oğlum diye ekleme yapı

# class Canlı():
#     def __init__(self,tur,yasamAlanı,cinsiyet):
#         self.tur=tur
#         self.yasamAlani=yasamAlanı
#         self.cinsiyet=cinsiyet
#     def bilgileriGoster(self):
#         print(f"Tür: {self.tur}\nYaşam Alanı: {self.yasamAlani}\nCinsiyeti: {self.cinsiyet}")
#         if self.cinsiyet=="Kız":
#             print("Kızım")
#         else:
#             print("Oğlum")
#     def __str__(self):
#         return self.cinsiyet
    
# canli1=Canlı("Sürüngen","Afrika","Kız")
# canli2=Canlı("Memeli","Asya","Erkek")
# canli3=Canlı("Kuşlar","Avrupa","Kız")

# canli1.bilgileriGoster()
# canli2.bilgileriGoster()
# canli3.bilgileriGoster()


# class Canlı():
#     def __init__(self,ad,cinsiyet):
#         self.ad=ad
#         self.cinsiyet=cinsiyet
#     def bilgileriGoster(self):
#         metin=self.ad
#         # if self.cinsiyet=="Kadın" or self.cinsiyet=="kadın":
#         #     return metin+" Kızım"
#         # else:
#         #     return metin+" Oğlum"
#         return metin+(" kızım" if self.cinsiyet=="Kadın" or self.cinsiyet=="kadın" else " Oğlum")
    

# canli1=Canlı("Abdül Rezak","Erkek")
# canli2=Canlı("Şazimet","Kadın")
# canli3=Canlı("Berkay","Erkek")

# print(canli1.bilgileriGoster())
# print(canli2.bilgileriGoster())
# print(canli3.bilgileriGoster())


# Bir klas oluşturun ve içerisinde dört işlem bulunsun ve bu işlemleri bize değer olarak geri döndürsün

# class dortIslem():
#     def __init__(self,a,b,islem):
#         self.a=a
#         self.b=b
#         self.islem=islem
#     def dortIslemGoster(self):
#         if self.islem=="+":
#             return f"{self.a}+{self.b}={self.a+self.b}: Bu bir toplama!"
#         elif self.islem=="-":
#             return f"{self.a}-{self.b}={self.a-self.b}: Bu bir çıkarma!"
#         elif self.islem=="*":
#             return f"{self.a}*{self.b}={self.a*self.b}: Bu bir çarpma!"
#         elif self.islem=="/":
#             return f"{self.a}/{self.b}={self.a/self.b}: Bu bir bölme!"
#         else:
#             return "Geçersiz işlem seçimi!"

# olay1=dortIslem(10,5,"+")
# olay2=dortIslem(10,5,"-")
# olay3=dortIslem(10,5,"*")
# olay4=dortIslem(10,5,"/")
# print(olay1.dortIslemGoster())
# print("----------------------")
# print(olay2.dortIslemGoster())
# print("----------------------")
# print(olay3.dortIslemGoster())
# print("----------------------")
# print(olay4.dortIslemGoster())


        
