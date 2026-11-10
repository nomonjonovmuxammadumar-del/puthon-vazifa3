zaxira = 12
while zaxira > 0:
    sotildi = int(input("Sotildi: "))
    if sotildi > zaxira:
        print("Zaxiradan ko'p sotib bo'lmaydi")
        continue
    zaxira -= sotildi
    print("Qoldi:", zaxira)
print("Ombor bo'sh")
 