birinchi = {"Ali", "Madina", "Jasur", "Aziza"}
ikkinchi = {"Jasur", "Sardor", "Aziza", "Bekzod"}
print("Faqat birinchi:", ", ".join(sorted(birinchi - ikkinchi)))
print("Faqat ikkinchi:", ", ".join(sorted(ikkinchi - birinchi)))
print("Ikkalasida:", ", ".join(sorted(birinchi & ikkinchi)))
 