dizi=[]
#Dizi uzunluğu belirleyelim
dizi_uzunluğu=int(input("DİZİ UZUNLUĞUNU GİRİN:"))
while len(dizi)!=(dizi_uzunluğu ):
    #diziye bir takım elemanlar ekleyelim
    değer=(input("listeye eklenecek bir değer girin:"))
    dizi.append(değer)
#soruda dizide bulunan bilgilerin sayı yada string olup olmadığı belirtilmemiş
#python da liste içinde sayı ve karakter olabildiği için kolaylık sağlaması amacıyla string bıraktım
#istenen dizi uzunluğuna ulaştık şimdi de listeden LİFO yöntemi ile veri çekelim
veriçek=int(input("kaç eleman çekmek istediğinizi girin"))
if veriçek>len(dizi):
    print("dizide çekmek istediğiniz kadar eleman yok")
    veriçek=int(input("kaç eleman çekmek istediğinizi girin"))

sayaç=0
while sayaç<=veriçek:
    print(dizi)
    print(dizi.pop())
    sayaç+=1
    
#kullanıcıdan bilgiler alarak dizi oluşturdum ve oluşturduğum diziden lifo(yığın)yöntemi ile bilgi çektim.
