ovozlar = {"Ali": "Python", "Vali": "JavaScript", "Madina": "Python",
           "Jasur": "C++", "Aziza": "Python", "Sardor": "JavaScript"}
sanoq = {}
for til in ovozlar.values():
    sanoq[til] = sanoq.get(til, 0) + 1
for til, s in sanoq.items():
    print(f"{til}: {s} ta ovoz")
print("G'olib:", max(sanoq, key=sanoq.get))
 