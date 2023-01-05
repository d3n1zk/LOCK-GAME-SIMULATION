def oyun_alanini_ciz(satir,sutun,taslar,sutun_harfleri):
    print("        ", end="")
    print("       ".join(sutun_harfleri[0:sutun]))
    print("    ",end="")
    print("--------"*satir,end="")
    print("-")
    for satir_no in range(1,len(taslar)+1):
        print(satir_no, "  |", end="")
        for sutun_no in range(1,len(taslar)+1):
            print("  ",taslar[satir_no-1][sutun_no-1],"  |",end="")
        print("  ", satir_no)
        print("    ", end="")
        print("--------" * sutun, end="")
        print("-")
    print("        ", end="")
    print("       ".join(sutun_harfleri[0:sutun]))
def hareket_ettirme(sira,oyuncu2char,oyuncu1char,taslar,sutun_harfleri,satir,durum):
    hareket_konum=""
    if sira==1:
        hareket_konum = input(f"Oyuncu {sira} lütfen kendi taşınızın konumunu ve hedef konumu giriniz:")
        while taslar[int(hareket_konum[0])-1][sutun_harfleri.index(hareket_konum[1])]==oyuncu2char:
            print("Rakibinizin taşını hareket ettiremezsiniz!!")
            hareket_konum = input(f"Oyuncu {sira} lütfen kendi taşınızın konumunu ve hedef konumu giriniz:")
    if sira==2:
        hareket_konum=input(f"Oyuncu {sira} lütfen kendi taşınızın konumunu ve hedef konumu giriniz:")
        while taslar[int(hareket_konum[0])-1][sutun_harfleri.index(hareket_konum[1])] == oyuncu1char:
            print("Rakibinizin taşını hareket ettiremezsiniz!!")
            hareket_konum=input(f"Oyuncu {sira} lütfen kendi taşınızın konumunu ve hedef konumu giriniz:")
    while int(hareket_konum[0]) > satir or int(hareket_konum[0]) <= 0 or int(hareket_konum[3]) > satir or int(
            hareket_konum[3]) <= 0:
        print("Oyun alanının dışında olan bir koordinat girişi yapmayınız!")
        hareket_konum = input(f"Oyuncu {sira} lütfen kendi taşınızın konumunu ve hedef konumu giriniz:")
    while taslar[int(hareket_konum[0])-1][sutun_harfleri.index(hareket_konum[1])]!="X" and taslar[int(hareket_konum[0])-1][sutun_harfleri.index(hareket_konum[1])]!="Y":
        print("Hatalı veri girişi! Girdiğiniz koordinatta herhangi bir taş bulunmamaktadır.")
        hareket_konum=input(f"Oyuncu {sira} lütfen kendi taşınızın konumunu ve hedef konumu giriniz:")
    while hareket_konum[0]!=hareket_konum[3] and hareket_konum[1]!=hareket_konum[4]:
        print("Hareketleriniz sadece dikey veya yatay eksende olmak zorundadır!")
        hareket_konum=input(f"Oyuncu {sira} lütfen kendi taşınızın konumunu ve hedef konumu giriniz:")
    while hareket_konum[1] not in sutun_harfleri or hareket_konum[4] not in sutun_harfleri:
        print("Hatalı veri girişi! Girdiğiniz sütün koordinatı oyun alanının içinde bulunmamaktadır.")
        hareket_konum = input(f"Oyuncu {sira} lütfen kendi taşınızın konumunu ve hedef konumu giriniz:")
    while taslar[int(hareket_konum[3])-1][sutun_harfleri.index(hareket_konum[4])] in ["X","Y"]:
        hareket_konum=input(f"Oyuncu {sira} başka bir taşın olduğu konuma hareket edemezsiniz lütfen güncel konumunuzu ve hareket etmek istediğiniz konumu yeniden giriniz:")
    while int(hareket_konum[0])!=int(hareket_konum[3]) and hareket_konum[1]==hareket_konum[4] and durum==True:#Dikeyde taşın üstünden atlama kontrolü
        if (int(hareket_konum[0])-1==int(hareket_konum[3]) or int(hareket_konum[0])==int(hareket_konum[3])-1):
            durum=False
            break
        else:
            if int(hareket_konum[0]) > int(hareket_konum[3]) and int(hareket_konum[0]) - 1 != int(
                    hareket_konum[3]):  # yukarı doğru gidiyorsa
                for satir_no in range(int(hareket_konum[3]), int(hareket_konum[0]) - 1):
                    while taslar[satir_no][sutun_harfleri.index(hareket_konum[1])] == oyuncu2char or taslar[satir_no][sutun_harfleri.index(hareket_konum[1])] == oyuncu1char:
                        print("Başka bir taşın üstünden atlama hareketi yapılamaz!")
                        hareket_konum = input(f"Oyuncu {sira} lütfen güncel konumunuzu ve hareket etmek istediğiniz yeni konumu girin:")
                    else:
                        durum = False
            elif int(hareket_konum[3]) > int(hareket_konum[0]) and int(hareket_konum[3]) - 1 != int(
                    hareket_konum[0]):  # aşağı doğru gidiyorsa
                for satir_no in range(int(hareket_konum[0]), int(hareket_konum[3]) - 1):
                    while taslar[satir_no][sutun_harfleri.index(hareket_konum[1])] == oyuncu2char or taslar[satir_no][sutun_harfleri.index(hareket_konum[1])] == oyuncu1char:
                        print("Başka bir taşın üstünden atlama hareketi yapılamaz!")
                        hareket_konum = input(f"Oyuncu {sira} lütfen güncel konumunuzu ve hareket etmek istediğiniz yeni konumu girin:")
                    else:
                        durum = False
            else:
                durum = False
    while (int(hareket_konum[0])==int(hareket_konum[3])) and (hareket_konum[1]!=hareket_konum[4]) and durum==True: #Yatayda taşın üstünden atlama kontrolü
        if (sutun_harfleri.index(hareket_konum[1])-1==sutun_harfleri.index(hareket_konum[4]) or sutun_harfleri.index(hareket_konum[1])==sutun_harfleri.index(hareket_konum[4])-1):
            break
        else:
            if sutun_harfleri.index(hareket_konum[1])>sutun_harfleri.index(hareket_konum[4]): #sola doğru gidiyorsa
              for sutun_no in range(sutun_harfleri.index(hareket_konum[4])+1,sutun_harfleri.index(hareket_konum[1])):
                while taslar[int(hareket_konum[0])-1][sutun_no]==oyuncu2char or taslar[int(hareket_konum[0])-1][sutun_no]==oyuncu1char:
                    print("Başka bir taşın üstünden atlama hareketi yapılamaz!")
                    hareket_konum = input(f"Oyuncu {sira} lütfen güncel konumunuzu ve hareket etmek istediğiniz yeni konumu girin:")
                else:
                    durum = False
            elif sutun_harfleri.index(hareket_konum[4])>sutun_harfleri.index(hareket_konum[1]): #sağa doğru gidiyorsa
               for sutun_no in range(sutun_harfleri.index(hareket_konum[1])+1,sutun_harfleri.index(hareket_konum[4])):
                  while taslar[int(hareket_konum[0])-1][sutun_no]==oyuncu2char or taslar[int(hareket_konum[0])-1][sutun_no]==oyuncu1char:
                     print("Başka bir taşın üstünden atlama hareketi yapılamaz!")
                     hareket_konum = input(f"Oyuncu {sira} lütfen güncel konumunuzu ve hareket etmek istediğiniz yeni konumu girin:")
                  else:
                    durum = False
            else:
              durum=False
    konumlar=hareket_konum.split()
    guncel_konum = konumlar[0]
    gidilecek_konum = konumlar[1]
    temp=taslar[int(guncel_konum[0])-1][sutun_harfleri.index(guncel_konum[1])]
    taslar[int(guncel_konum[0])-1].pop(sutun_harfleri.index(guncel_konum[1]))
    taslar[int(guncel_konum[0])-1].insert(sutun_harfleri.index(guncel_konum[1])," ")
    taslar[int(gidilecek_konum[0])-1].pop(sutun_harfleri.index(gidilecek_konum[1]))
    taslar[int(gidilecek_konum[0])-1].insert(sutun_harfleri.index(gidilecek_konum[1]),temp)
def patlama_durumlari(sutun_harfleri,oyuncu1char,oyuncu2char,oyuncu1tas,oyuncu2tas,taslar,sira):
    #4 KÖŞEDE KALANLARI KONTROL ETME DURUMU
    if taslar[0][0]==oyuncu1char or taslar[0][0]==oyuncu2char:
        if taslar[0][0]==oyuncu1char:
            if taslar[0][1]==oyuncu2char and taslar[1][0]==oyuncu2char:
                oyuncu1tas-=1
                print(f"{1,sutun_harfleri[0]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                taslar[0].pop(0)
                taslar[0].insert(0," ")
        elif taslar[0][0]==oyuncu2char:
            if taslar[0][1]==oyuncu1char and taslar[1][0]==oyuncu1char:
                print(f"{1, sutun_harfleri[0]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                oyuncu2tas-=1
                taslar[0].pop(0)
                taslar[0].insert(0," ")
    if taslar[0][len(taslar)-1]==oyuncu1char or taslar[0][len(taslar)-1]==oyuncu2char:
        if taslar[0][len(taslar)-1]==oyuncu1char:
            if taslar[0][len(taslar)-2]==oyuncu2char and taslar[1][len(taslar)-1]==oyuncu2char:
                oyuncu1tas-=1
                print(f"{1,sutun_harfleri[len(taslar)-1]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                taslar[0].pop(len(taslar)-1)
                taslar[0].insert(len(taslar)-1," ")
        elif taslar[0][len(taslar)-1]==oyuncu2char:
            if taslar[0][len(taslar)-2]==oyuncu1char and taslar[1][len(taslar)-1]==oyuncu1char:
                oyuncu2tas-=1
                print(f"{1, sutun_harfleri[len(taslar) - 1]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                taslar[0].pop(len(taslar)-1)
                taslar[0].insert(len(taslar)-1," ")
    if taslar[len(taslar)-1][0]==oyuncu1char or taslar[len(taslar)-1][0]==oyuncu2char:
        if taslar[len(taslar)-1][0]==oyuncu1char:
            if taslar[len(taslar)-2][0]==oyuncu2char and taslar[len(taslar)-1][1]==oyuncu2char:
                oyuncu1tas-=1
                print(f"{len(taslar),sutun_harfleri[0]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                taslar[len(taslar)-1].pop(0)
                taslar[len(taslar)-1].insert(0," ")
        elif taslar[len(taslar)-1][0]==oyuncu2char:
            if taslar[len(taslar)-2][0]==oyuncu1char and taslar[len(taslar)-1][1]==oyuncu1char:
                oyuncu2tas-=1
                print(f"{len(taslar), sutun_harfleri[0]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                taslar[len(taslar)-1].pop(0)
                taslar[len(taslar)-1].insert(0," ")
    if taslar[len(taslar)-1][len(taslar)-1]==oyuncu1char or taslar[len(taslar)-1][len(taslar)-1]==oyuncu2char:
        if taslar[len(taslar)-1][len(taslar)-1]==oyuncu1char:
            if taslar[len(taslar)-1][len(taslar)-2]==oyuncu2char and taslar[len(taslar)-2][len(taslar)-1]==oyuncu2char:
                oyuncu1tas-=1
                print(f"{len(taslar),sutun_harfleri[len(taslar)-1]} konumundaki taş kilitlendi ve oyundan çıkarıldı")
                taslar[len(taslar)-1].pop(len(taslar)-1)
                taslar[len(taslar)-1].insert(len(taslar)-1," ")
        elif taslar[len(taslar)-1][len(taslar)-1]==oyuncu2char:
            if taslar[len(taslar)-1][len(taslar)-2]==oyuncu1char and taslar[len(taslar)-2][len(taslar)-1]==oyuncu1char:
                oyuncu2tas-=1
                print(f"{len(taslar), sutun_harfleri[len(taslar) - 1]} konumundaki taş kilitlendi ve oyundan çıkarıldı")
                taslar[len(taslar)-1].pop(len(taslar)-1)
                taslar[len(taslar)-1].insert(len(taslar)-1," ")
    #SATIR VE SUTUN ARALARINI VE ORTADA KALANLARI KONTROL ETME KISMI
    if sira==1:
        for satir_no in range(1,len(taslar)-1):
            if taslar[satir_no][0]==oyuncu2char:
                if taslar[satir_no-1][0]==oyuncu1char and taslar[satir_no+1][0]==oyuncu1char:
                    oyuncu2tas-=1
                    print(f"{satir_no,sutun_harfleri[0]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                    taslar[satir_no].pop(0)
                    taslar[satir_no].insert(0," ")
        for satir_no in range(1,len(taslar)-1):
            if taslar[satir_no][len(taslar)-1]==oyuncu2char:
                if taslar[satir_no-1][len(taslar)-1]==oyuncu1char and taslar[satir_no+1][len(taslar)-1]==oyuncu1char:
                    oyuncu2tas-=1
                    print(f"{satir_no, sutun_harfleri[len(taslar)-1]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                    taslar[satir_no].pop(len(taslar)-1)
                    taslar[satir_no].insert(len(taslar)-1," ")
        for sutun_no in range(1,len(taslar)-1):
            if taslar[0][sutun_no]==oyuncu2char:
                if taslar[0][sutun_no-1]==oyuncu1char and taslar[0][sutun_no+1]==oyuncu1char:
                    oyuncu2tas-=1
                    print(f"{1,sutun_harfleri[sutun_no]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                    taslar[0].pop(sutun_no)
                    taslar[0].insert(sutun_no," ")

        for sutun_no in range(1,len(taslar)-1):
            if taslar[len(taslar)-1][sutun_no]==oyuncu2char:
                if taslar[len(taslar)-1][sutun_no-1]==oyuncu1char and taslar[len(taslar)-1][sutun_no+1]==oyuncu1char:
                    oyuncu2tas-=1
                    print(f"{len(taslar), sutun_harfleri[sutun_no]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                    taslar[len(taslar)-1].pop(sutun_no)
                    taslar[len(taslar)-1].insert(sutun_no," ")
        for satir_no in range(1,len(taslar)-1):
            for sutun_no in range(1,len(taslar)-1):
                if taslar[satir_no][sutun_no]==oyuncu2char:
                    if (taslar[satir_no][sutun_no-1]==oyuncu1char and taslar[satir_no][sutun_no+1]==oyuncu1char) or (taslar[satir_no-1][sutun_no]==oyuncu1char and taslar[satir_no+1][sutun_no]==oyuncu1char):
                        oyuncu2tas-=1
                        print(f"{satir_no,sutun_harfleri[sutun_no]} konumundaki taş kiltilendi ve oyundan çıkarıldı.")
                        taslar[satir_no].pop(sutun_no)
                        taslar[satir_no].insert(sutun_no," ")
    if sira==2:
        for satir_no in range(1,len(taslar)-1):
            if taslar[satir_no][0]==oyuncu1char:
                if taslar[satir_no-1][0]==oyuncu2char and taslar[satir_no+1][0]==oyuncu2char:
                    oyuncu1tas-=1
                    print(f"{satir_no, sutun_harfleri[0]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                    taslar[satir_no].pop(0)
                    taslar[satir_no].insert(0," ")
        for satir_no in range(1,len(taslar)-1):
            if taslar[satir_no][len(taslar)-1]==oyuncu1char:
                if taslar[satir_no-1][len(taslar)-1]==oyuncu2char and taslar[satir_no+1][len(taslar)-1]==oyuncu2char:
                    oyuncu1tas-=1
                    print(f"{satir_no, sutun_harfleri[len(taslar) - 1]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                    taslar[satir_no].pop(len(taslar)-1)
                    taslar[satir_no].insert(len(taslar)-1," ")
        for sutun_no in range(1,len(taslar)-1):
            if taslar[0][sutun_no]==oyuncu1char:
                if taslar[0][sutun_no-1]==oyuncu2char and taslar[0][sutun_no+1]==oyuncu2char:
                    oyuncu1tas-=1
                    print(f"{1, sutun_harfleri[sutun_no]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                    taslar[0].pop(sutun_no)
                    taslar[0].insert(sutun_no," ")

        for sutun_no in range(1,len(taslar)-1):
            if taslar[len(taslar)-1][sutun_no]==oyuncu1char:
                if taslar[len(taslar)-1][sutun_no-1]==oyuncu2char and taslar[len(taslar)-1][sutun_no+1]==oyuncu2char:
                    oyuncu1tas-=1
                    print(f"{len(taslar), sutun_harfleri[sutun_no]} konumundaki taş kilitlendi ve oyundan çıkarıldı.")
                    taslar[len(taslar)-1].pop(sutun_no)
                    taslar[len(taslar)-1].insert(sutun_no," ")
        for satir_no in range(1, len(taslar) - 1):
            for sutun_no in range(1, len(taslar) - 1):
                if taslar[satir_no][sutun_no] == oyuncu1char:
                    if (taslar[satir_no][sutun_no - 1] == oyuncu2char and taslar[satir_no][sutun_no + 1] == oyuncu2char) or (taslar[satir_no - 1][sutun_no] == oyuncu2char and taslar[satir_no + 1][sutun_no] == oyuncu2char):
                        oyuncu1tas -= 1
                        print(f"{satir_no, sutun_harfleri[sutun_no]} konumundaki taş kiltilendi ve oyundan çıkarıldı.")
                        taslar[satir_no].pop(sutun_no)
                        taslar[satir_no].insert(sutun_no, " ")
    return oyuncu1tas,oyuncu2tas
def main():
    sutun_harfleri = ["A", "B", "C", "D", "E", "F", "G", "H"]
    oyuncu1char=input("1. Oyuncuyu temsil etmek için bir karakter giriniz:")
    oyuncu2char=input("2. Oyuncuyu temsil etmek için bir karakter giriniz:")
    while True:
        try:
          satir = int(float(input("Oyun alanının satır/sütun sayısını giriniz(4-8):")))
          sutun=satir
        except ValueError:
          print("Bir sayı girmelisiniz ve lütfen 4 ila 8 arasında bir sayı giriniz!:")
        else:
            break
    while satir>8 or satir <4:
        print("Hatalı veri girişi!! Lütfen satır sütün sayısını 4 ile 8 arasında giriniz!")
        satir=int(input("Oyun alanının satır/sütun sayısını giriniz(4-8):"))
        sutun=satir
    taslar = [[oyuncu2char] * satir, [oyuncu1char] * satir]
    for satir_no in range(1, satir-1):  # satir burada ilk başlangıçta boş olan satırların listelerini oluşturmmak için yapıldı
        taslar.insert(satir_no, [" "] * sutun)
    oyuncu1tas=satir
    oyuncu2tas=satir
    oyun_alanini_ciz(satir,sutun,taslar,sutun_harfleri)
    sira=1
    durum=True
    while oyuncu1tas!=1 and oyuncu2tas!=1:
        hareket_ettirme(sira,oyuncu2char, oyuncu1char, taslar, sutun_harfleri,satir,durum)
        oyuncu1tas,oyuncu2tas=patlama_durumlari(sutun_harfleri,oyuncu1char,oyuncu2char,oyuncu1tas,oyuncu2tas,taslar,sira)
        oyun_alanini_ciz(satir, sutun, taslar, sutun_harfleri)
        print(oyuncu1tas,oyuncu2tas)
        durum=True
        sira+=1
        if sira%2==1:
            sira=1
        else:
            sira=2
    if oyuncu1tas == 1:
        return oyuncu2char
    if oyuncu2tas == 1:
        return oyuncu1char
devam="E"
while devam=="E":
    kazananoyuncu=main()
    print(f"Oyunu Oyuncu {kazananoyuncu} kazandı.")
    devam=input("Tekrar oynamak ister misiniz(E/H):")
    while devam not in ["E","H"]:
        print("Hatalı veri girişi!")
        devam=input("Lütfen devam edip etmeyeceğinizi E veya H olarak giriniz:")
