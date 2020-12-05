def stupidsort():
    liste=[]
    a=int(input("liste uzunluğu girin:"))
    for i in range(0,a):
        l=int(input("listeye eleman girin:"))
        liste.append(l)
    #kullanıcadan alınacak bilgilerle liste oluşturdum
    # şimdi sıralıyorum
    print(liste)
    k=0
    #bir değişken tanımlayarak liste istenen çevrim kadar dönmesini sağladım.
    while (k<(a-1)):# bir çıkardım çünkü indis 0 dan başlar 
        if (liste[k+1]< liste[k]):
            temp = liste[k+1]#temp kullanarak elemanların yerini değiştirdim
            liste[k+1]=liste[k]
            liste[k]=temp
            k=0
        else:
            k+=1
        

                    
    print(liste)
     
        
                        
                     
                     

                    
