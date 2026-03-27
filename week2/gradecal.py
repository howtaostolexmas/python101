score = float(input("คะแนนที่ได้: "))

while score < 0 or score > 100:
    print("กรุณาใส่คะแนนระหว่าง 0 ถึง 100")
    score = float(input("คะแนนที่ได้: "))
if score >= 90:
    print("เกรด A")
elif score >= 80:
    print("เกรด B")
elif score >= 70:
    print("เกรด C")
elif score >= 60:
    print("เกรด D")
else:
    print("เกรด F")