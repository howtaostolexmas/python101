def simple_return(buy, sell):
    return (sell - buy) / buy * 100

def future_value(pv, r, n):
    return pv * (1 + r) ** n

def position_size(portfolio, risk, stoploss):
    return (portfolio * risk) / stoploss

def main():
    print("=" * 40)
    print("     Finance Calculator")
    print("=" * 40)

    # Simple Return
    buy  = float(input("ราคาซื้อ: "))
    sell = float(input("ราคาขาย: "))
    print(f"ผลตอบแทน: {simple_return(buy, sell):.2f}%\n")

    # Future Value
    pv   = float(input("เงินต้น: "))
    rate = float(input("อัตราดอกเบี้ย (%): ")) / 100
    n    = int(input("จำนวนปี: "))
    print(f"มูลค่าอนาคต: {future_value(pv, rate, n):,.2f} บาท\n")

    # Position Size
    portfolio = float(input("มูลค่าพอร์ต: "))
    risk      = float(input("ความเสี่ยงที่รับได้ (%): ")) / 100
    stoploss  = float(input("Stop Loss (%): ")) / 100
    print(f"ขนาด Position: {position_size(portfolio, risk, stoploss):,.2f} บาท")

main()

#print(f"ผลตอบแทน: {simple_return(100, 150):.2f}%")
#print(f"มูลค่าในอนาคต: {fv(100, 0.05, 10):.2f}")
#print(f"ขนาดตำแหน่ง: {position_size(10000, 0.02, 0.05):.2f}")