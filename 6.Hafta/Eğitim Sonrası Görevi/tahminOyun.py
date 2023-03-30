import random 
import time
rastgele=random.randint(1,100)
tahminHakki=5
print("************************SAYI TAHMİN OYUNUNA HOŞ GELDİN...************************")

while True:
    tahmin=int(input("tahmin ettiğiniz sayı:"))

    print(f"{-tahminHakki+6}.Tahmin: {tahmin}")
    print("değer kontrol ediliyor...")
    time.sleep(1)

    if tahmin==rastgele:
        print("TEBRİKLERRR :DDD",rastgele)
        break

    elif (tahmin<rastgele):           
        print("daha YÜKSEK bir sayı tahmininde bulunun")
        tahminHakki-=1
    
    elif (tahmin>rastgele):
        print("daha DÜŞÜK bir sayı tahmininde bulunun")
        tahminHakki-=1

    if tahminHakki==0:
        print("Hakkın bitti. KAYBETTİN ://    SAYI:",rastgele)
        
        break


