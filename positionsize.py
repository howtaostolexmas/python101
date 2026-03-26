portfolio = float(input("มูลค่าพอร์ต: "))
risk = float(input("ความเสี่ยงที่รับได้(ร้อยละ): ")) / 100
stoploss = float(input("ระยะ stoploss(ร้อยละ): ")) /100
Position_Size = (portfolio * risk) / stoploss

print(f"Position ของคุณ: {Position_Size:.2f} บาท")
#position = (portfolio * risk)/stoploss


