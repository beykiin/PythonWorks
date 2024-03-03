
def fakt(a):
    finish=1
    for i in range(1,a+1):
        finish*=i
    return finish
# print(fakt(a))

def tekSayi(a):
    if a%2!=0:
        return "Sayınız Tek Sayıdır."
    else:
        return "Bu Sayı Çift Kör müsün?"
    
def ciftSayi(a):
    if a%2==0:
        return "Sayınız Çift Sayıdır."
    else:
        return "Bu Sayı Tek Yarak Kafa."
    
def ustAl(a,b):
    return a**b
def kokAl(a,b):
    return a*(1/b)
def menu1(corbalar,fiyat):
    return f"Çorba: {corbalar}\nFiyat: {fiyat} TL"
def calisanlar(isim,yas,cinsiyet,meslek):
    pass
def motorlar(marka,model,hp,yil):
    pass
def eksiUstAl(a,b):
    return a**(-b)
def harfSil(cumle,silinen):
    cumle=cumle.lower().replace(silinen.lower(),"")
    return cumle



            
        
