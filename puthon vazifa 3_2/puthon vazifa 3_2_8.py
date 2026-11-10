harorat = (18, 20, 17, 23, 25, 21, 19)
issiq = [t for t in harorat if t > 20]
print("Haroratlar:", ", ".join(map(str, issiq)))
print("Kunlar soni:", len(issiq))
 