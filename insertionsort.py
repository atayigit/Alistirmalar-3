def insertionsort():
    liste=[]
    a=int(input("liste uzunluğu girin:"))
    for i in range(0,a):
        l=int(input("listeye eleman girin:"))
        liste.append(l)
    #kullanıcadan alınacak bilgilerle liste oluşturdum
    # şimdi sıralıyorum
    print(liste)
    k=0
    while (k<=a):
        if k==0:
            k+=1
        for m in range(0,k):
            while m>0 and liste[m-1]>liste[m]:
                temp = liste[m-1]#temp kullanarak elemanların yerini değiştirdim
                liste[m-1]=liste[m]
                liste[m]=temp
                m-=1
        k+=1
                
    print(liste)




print(insertionsort())
    





        
