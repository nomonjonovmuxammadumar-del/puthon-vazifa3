jami = 0
miqdor = 0
while True:
    x = float(input())
    if x == 0:
        break
    jami += x
    miqdor += 1
print("Jami:", int(jami))
print("Kiritilgan xarajatlar soni:", miqdor)
if miqdor > 0:
    print(f"O'rtacha: {jami / miqdor:.2f}")
 