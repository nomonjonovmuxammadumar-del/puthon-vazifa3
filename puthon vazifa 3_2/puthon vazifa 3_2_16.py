ombor = {"olma": 12, "banan": 8, "anor": 15, "uzum": 6}
kop = max(ombor, key=ombor.get)
kam = min(ombor, key=ombor.get)
print(f"Eng ko'p: {kop} ({ombor[kop]} ta)")
print(f"Eng kam: {kam} ({ombor[kam]} ta)")
print("Jami mahsulot:", sum(ombor.values()), "ta")
 