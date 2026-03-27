#FV = PV * (1 + r) ** n
PV = float(input("เงินต้น: "))
r = float(input("อัตราดอกเบี้ย (ร้อยละ): ")) / 100
n = int(input("จำนวนปี: "))

for year in range(1,n+1):
    FV = PV * (1 + r) ** year
    print(f"ปีที่ {year}: {FV:.2f} บาท")