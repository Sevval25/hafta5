class hesap:

    def __init__(self,say1,say2):
     self.say1 = say1
     self.say2 = say2

    def carp(self):
        sonuc = self.say1*self.say2
        return sonuc

    def böl(self):
        sonuc1 = self.say1/self.say2
        return sonuc1

    def çıkar(self):
        sonuc2 = self.say1 - self.say2
        return sonuc2

    def topla(self):
        sonuc3 = self.say1 + self.say2
        return sonuc3

    def yazdır(self):
        toplam=self.topla()
        carpma=self.carp()
        print('sayıların toplamı :',toplam)
        print('sayıların carpımı :', carpma)

A=hesap(5,3)
print(A.yazdır())
print(A.carpma())










