import random
from os import system, name 
from time import sleep


def clear():#terminali temizlemek için oluşturduğumuz bir fonksiyon
    
        #  windows için
        if name == 'nt':
            _ = system('cls')
    
        #  mac ve linux için (burada, os.name 'posix' olarak geçer ama else diyerek bunu zaten kapsıyoruz)
        else:
            _ = system('clear')
    


def blackjack(x):
    oyuncununEli=[]
    krupiyeninEli=[]
    clear()
    deste = ["♥A","♥2","♥3","♥4","♥5","♥6","♥7","♥8","♥9","♥10","♥J","♥Q","♥K","♤A","♤2","♤3","♤4","♤5","♤6","♤7","♤8","♤9","♤10","♤J","♤Q","♤K","♦A","♦2","♦3","♦4","♦5","♦6","♦7","♦8","♦9","♦10","♦J","♦Q","♦K","♧A","♧2","♧3","♧4","♧5","♧6","♧7","♧8","♧9","♧10","♧J","♧Q","♧K"]
    
    def oyuncuyaKartAc(deste):
        oyuncununEli.append(deste.pop())
        print("Oyuncuya çekilen kart: " + oyuncununEli[-1])
        

    def krupiyeyeKartAc(deste):
        krupiyeninEli.append(deste.pop())
        if(len(krupiyeninEli)==2):
            print("Krupiyeye çekilen kart: #")
        else:
            print("Krupiyeye çekilen kart: " + krupiyeninEli[-1])


    deste = x * deste
    random.shuffle(deste)
    print(len(deste))

    def eliHesapla(el):
        toplam = 0
        duzenlenmisEl=[]
        for i in el:
            duzenlenmisEl.append(i[1:])#kartlardaki sembolleri puan hesaplaması için çıkarıyoruz
        duzenlenmisEl=sorted([i for i in duzenlenmisEl if not str(i).isdigit()]) + sorted([i for i in duzenlenmisEl if str(i).isdigit()])#kart değerlerini hesaplama yapmak için doğru şekilde sıralyoruz
        duzenlenmisEl.reverse()#kart değerlerini hesaplayabilmek için A kartını destenin sonuna koyuyoruz
        for i in el:
            if(i[1]=="K" or i[1]=="Q" or i[1]=="J"):
                toplam+=10
            elif(i[1]=="A"):
                if(toplam>10):
                    toplam+=1
                else:
                    toplam+=11
            else:
                toplam+=(int(i[1:]))
        return toplam


    def eliGoster(x):
        oyuncuElDegeri=eliHesapla(oyuncununEli)
        krupiyeElDegeri=eliHesapla(krupiyeninEli)

        if (x ==1):
            oyuncununEliString=""
            for i in oyuncununEli:
                oyuncununEliString+=" " + i
            print("\nKrupiyenin elindeki kartlar: "+  krupiyeninEli[0] + " # \n\n\nOyuncunun elindeki kartlar: " + oyuncununEliString+"\tDeğer: "+ str(oyuncuElDegeri)  +"\n" )
        elif(x==2):
            krupiyeninEliString=""
            for i in krupiyeninEli:
                krupiyeninEliString+=" " + i
            oyuncununEliString=""
            for i in oyuncununEli:
                oyuncununEliString+=" " + i
            
            print("\nKrupiyenin elindeki kartlar: "+  krupiyeninEliString  + "\tDeğer: "+str(krupiyeElDegeri)+ "\n\n\nOyuncunun elindeki kartlar: " + oyuncununEliString +"\tDeğer: "+ str(oyuncuElDegeri) +"\n" )
        else:
            print("Erol dörtyüzdört hll")

    def oyunuBaslat(deste):
        oyuncuyaKartAc(deste)
        sleep(0.5)
        krupiyeyeKartAc(deste)
        sleep(0.5)
        oyuncuyaKartAc(deste)
        sleep(0.5)
        krupiyeyeKartAc(deste)
        sleep(0.5)
        clear()
        eliIlerlet()


    def eliDegerlendir():
        krupiyeElDegeri=eliHesapla(krupiyeninEli)
        oyuncuElDegeri=eliHesapla(oyuncununEli)
        if(krupiyeElDegeri == oyuncuElDegeri or (krupiyeElDegeri>21 and oyuncuElDegeri>21)):#21'in altındaki eşitlik ve iki tarafın da 21'i geçmesi durumu
            print("Berabere bitti!")
        elif(oyuncuElDegeri==21):#eşitlik olmadığı durumda oyuncunun 21 değerini bulması
            print("Oyunu kazandınız!")
        elif((oyuncuElDegeri>krupiyeElDegeri) and not oyuncuElDegeri>21 ):#oyuncunun 21'i geçmediği fakat krupiyeyi geçtiği durum
            print("Oyunu kazandınız!")
        elif(krupiyeElDegeri>21 and (not oyuncuElDegeri>21)):#oyuncunun 21 değerini geçmediği fakat krupiyenin 21 değerini aştığı durum
            print("Oyunu kazandınız!")
        else:
            print("Oyunu kaybettiniz!")




    def eliSonlandir():
        clear()
        eliGoster(2)
        sleep(1)
        krupiyeElDegeri=eliHesapla(krupiyeninEli)
        if(krupiyeElDegeri<=16):
            clear()
            krupiyeyeKartAc(deste)
            eliGoster(2)
            eliSonlandir()
        else:
            eliDegerlendir()



    def eliIlerlet():
        clear()
        eliGoster(1)
        oyuncununPuani=eliHesapla(oyuncununEli)
        if(not(oyuncununPuani >= 21)):
            karar = input("\nKart çekmek için Y/y sıranı bitirmek için N/n tuşlarını kullanınız: \n")
            if(karar == "n" or karar == "N"):
                eliSonlandir()
            elif(karar == "y" or karar == "Y"):
                oyuncuyaKartAc(deste)
                eliIlerlet()
            else:
                print("\nGeçersiz bir girdi yaptınız lütfen gösterilen girdilerden biriniz seçiniz!")
                sleep(2)
                eliIlerlet()
        else:
            input("\nArtık hamle yapamazsınız. Eli ilerletmek için herhangi bir tuşa basınız:\n")
            eliSonlandir()
    
    #print(deste[0] +"-  -" + deste[52]+"-  -" +deste[104]+"-  -" +deste[156])#küçük bir kontrol
    '''

    for k in deste:
        print(k)
        sleep(0.5)
        clear()

    '''
    oyunuBaslat(deste)
clear()

oyunlar=["Blackjack : B","Poker : P (Hazır değil)"]
i = max(s.index(":") for s in oyunlar)
cols = [s.split(":") for s in oyunlar]
aligned = [f"{c[0].ljust(i)}:{c[1]}" for c in cols]
print("Hangi oyunu oynamak istersiniz?")
for s in aligned:
    print(s)

secilenOyun=input()
if (secilenOyun == "b" or secilenOyun == "B"):
    desteSayisi=int(input("4-8 aralığında deste sayısını giriniz: "))
    blackjack(desteSayisi)

