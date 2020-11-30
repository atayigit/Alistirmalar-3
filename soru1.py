dizi=[]
#Dizi uzunluğu belirleyelim
dizi_uzunluğu=int(input("DİZİ UZUNLUĞUNU GİRİN"))
while len(dizi)!=(dizi_uzunluğu ):
    #diziye bir takım elemanlar ekleyelim
    değer=int(input("listeye eklenecek bir sayı girin"))
    dizi.append(değer)
    
#istenen dizi uzunluğuna ulaştık şimdi de listeden LİFO yöntemi ile veri çekelim
veriçek=int(input("kaç eleman çekmek istediğinizi girin"))
sayaç=0
while sayaç<=veriçek:
    print(dizi)
    print(dizi.pop())
    sayaç+=1
    
#kullanıcıdan bilgiler alarak dizi oluşturdum ve oluşturduğum diziden lifo(yığın)yöntemi ile bilgi çektim.
