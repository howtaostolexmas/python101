#Portfolio_start = float(input("มูลค่าพอร์ตเริ่มต้น: "))
#Max_Drawdown = float(input("Max Drawdown ที่รับได้ (ร้อยละ): "))
#Portfolio_current = Portfolio_start

#while True:
#    Trade_Result = float(input("ผลการเทรด (กำไรเป็นบวก ขาดทุนเป็นลบ): "))
#    Portfolio_current += Trade_Result
#    Drawdown = (Portfolio_start - Portfolio_current) * 100 / Portfolio_start
#    print(f"มูลค่าพอร์ตปัจจุบัน: {Portfolio_current:.2f} บาท | Drawdown: {Drawdown:.2f}%")

#    if Drawdown >= Max_Drawdown:
#        print("หยุดเทรดเนื่องจาก Drawdown เกินกว่าที่รับได้")
#        break

# ============================================
# Portfolio Risk Monitor
# ============================================

# --- Setup ---
portfolio_start  = float(input("มูลค่าพอร์ตเริ่มต้น (บาท): "))
max_drawdown     = float(input("Max Drawdown ที่รับได้ (%): "))
portfolio        = portfolio_start
trade_count      = 0

print(f"\n{'='*45}")
print(f"{'เทรด':^5} | {'ผลเทรด':^12} | {'พอร์ต':^14} | {'Drawdown':^10}")
print(f"{'='*45}")

# --- Main Loop ---
while True:
    result = float(input("\nผลการเทรด (กำไรบวก ขาดทุนลบ): "))
    portfolio   += result
    trade_count += 1
    drawdown     = (portfolio_start - portfolio) / portfolio_start * 100

    print(f"{trade_count:^5} | {result:^+12.2f} | {portfolio:^14.2f} | {drawdown:^9.2f}%")

    # --- Risk Check ---
    if portfolio <= 0:
        print("\n⚠️  พอร์ตหมดแล้ว หยุดเทรด!")
        break

    if drawdown >= max_drawdown:
        print(f"\n⚠️  Drawdown {drawdown:.2f}% เกิน {max_drawdown:.2f}% หยุดเทรด!")
        break

# --- Summary ---
print(f"\n{'='*45}")
print(f"สรุป: เทรดทั้งหมด {trade_count} ครั้ง")
print(f"พอร์ตเริ่มต้น : {portfolio_start:,.2f} บาท")
print(f"พอร์ตสุดท้าย : {portfolio:,.2f} บาท")
print(f"กำไร/ขาดทุน  : {portfolio - portfolio_start:+,.2f} บาท")
print(f"Max Drawdown  : {drawdown:.2f}%")