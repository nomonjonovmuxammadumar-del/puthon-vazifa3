ali = {"komediya", "sarguzasht", "fantastika"}
vali = {"fantastika", "drama", "komediya"}
print("Umumiy janrlar:", ", ".join(sorted(ali & vali)))
print("Faqat bittasiga yoqadi:", ", ".join(sorted(ali ^ vali)))
 