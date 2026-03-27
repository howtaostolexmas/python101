def simple_return(buy, sell):
    return (sell - buy) / buy * 100

def fv(pv, r, n):
    return pv * (1 + r) ** n

def position_size(portfolio, risk, stoploss):
    return (portfolio * risk) / stoploss

print(f"ผลตอบแทน: {simple_return(100, 150):.2f}%")
print(f"มูลค่าในอนาคต: {fv(100, 0.05, 10):.2f}")
print(f"ขนาดตำแหน่ง: {position_size(10000, 0.02, 0.05):.2f}")