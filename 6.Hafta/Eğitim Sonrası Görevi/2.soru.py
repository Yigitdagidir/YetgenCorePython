# 2.Problemin Çözümünü Buraya Yazınız
import random
import time
time.sleep(1)
liste=[i for i in range(1,101)]
asil=random.choice(liste)
kul=int(input("ilk sayi:"))
print("1. sayınız:",kul)

for lap in range(1,5):
    
    if asil==kul:
        print("tebrikler")
        break
    else:
        if asil>kul:
            print("tahmininizi yükseltin")
            kul=int(input("tahmini yükselt:"))
            print(f"{lap+1}. sayı:",kul)

            continue
        elif asil<kul:

            print("tahmini düşürün")
            kul=int(input("tahmini düşür:"))
            print(f"{lap+1}. sayı:",kul)


            continue
    
    if lap==4:
        print(f"sayi:{asil}")



