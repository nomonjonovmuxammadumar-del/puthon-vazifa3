baholar = {"Ali": 85, "Vali": 72, "Madina": 96, "Jasur": 68}
for ism, ball in baholar.items():
    if ball >= 90:
        print(f"Yuqori ball olganlar: {ism} — {ball}")
print("O'rtacha ball:", sum(baholar.values()) / len(baholar))
