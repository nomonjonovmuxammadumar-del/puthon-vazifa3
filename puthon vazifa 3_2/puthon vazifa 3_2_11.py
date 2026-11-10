matematika = {"Ali", "Vali", "Madina", "Jasur", "Aziza"}
ingliz = {"Madina", "Jasur", "Sardor", "Aziza", "Malika"}
print("Ikkala kursda:", ", ".join(sorted(matematika & ingliz)))
print("Faqat bitta kursda:", ", ".join(sorted(matematika ^ ingliz)))
 