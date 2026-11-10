pul = int(input("Boshlang'ich pul: "))
haftalik = int(input("Haftalik qo'shimcha: "))
hafta = 0
while pul <= 500000:
    pul += haftalik
    hafta += 1
print("Kerakli hafta:", hafta)
 