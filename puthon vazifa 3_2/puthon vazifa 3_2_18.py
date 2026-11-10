shaharlar = {"Toshkent": 3000000, "Farg'ona": 300000, "Samarqand": 600000}
katta = [sh for sh, a in shaharlar.items() if a > 500000]
print("500 000 dan ko'p:", ", ".join(katta))
print("Eng ko'p aholi:", max(shaharlar, key=shaharlar.get))
 