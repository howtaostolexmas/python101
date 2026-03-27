Present_Value = float(input("เงินต้น: "))
Interest_Rate = float(input("อัตราดอกเบี้ย (ร้อยละ): ")) / 100
Number_of_Periods = int(input("จำนวนงวด: "))
Future_Value = Present_Value * (1 + Interest_Rate) ** Number_of_Periods
print(f"มูลค่าในอนาคต: {Future_Value:.2f} บาท")
#FV = PV * (1 + r) ** n