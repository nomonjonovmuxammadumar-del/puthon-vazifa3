ruxsat = {"matematika", "ingliz", "informatika", "fizika"}
tanlangan = {"ingliz", "informatika", "tarix"}
print("Ruxsat etilgan:", ", ".join(sorted(tanlangan & ruxsat)))
print("Ruxsat etilmagan:", ", ".join(sorted(tanlangan - ruxsat)))
 