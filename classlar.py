class Hesapla():
    a=0
    b=0
    def topla(self,a,b):
        return a+b
    def carp(self,a,b):
        return self.a*b
    
class Hesapla2():
    a=0
    b=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "Hesapla 2 class'ı"
    def topla(self,a,b):
        return a+b
    def carp(self,a,b):
        return self.a*b
    
class Hesapla3():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "Hesapla 3 class'ı"
    def topla(self):
        return self.a+self.b
    def carp(self):
        return self.a*self.b

islem=Hesapla()
islem2=Hesapla2(10,10)
islem2.a=5
islem2.b=5
islem3=Hesapla3(5,10)
a="asd"
print(type(a),type(islem))
print(islem.topla(5,10))
print(islem.carp(3,4))
islem.a=8
print(islem.carp(3,4))
print(islem2.carp(5,5))
print(islem2.topla(5,5))
print(islem)
print(islem2)
print(islem3.topla())
print(islem3.carp())
islem3.a=2
islem3.b=3
print(islem3.topla())
print(islem3.carp())
