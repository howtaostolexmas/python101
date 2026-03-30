def safe_float(value):
    try:
        return float(value)
    except ValueError:
        print("กรุณาใส่ตัวเลขที่ถูกต้อง")
        return None
    
def safe_divide(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        print("ไม่สามารถหารด้วยศูนย์ได้")
        return None
    except ValueError:
        print("กรุณาใส่ตัวเลขที่ถูกต้อง")
        return None
    
def get_input(prompt):
    while True:
        value = safe_float(input(prompt))
        if value is not None and value > 0:
            return value
        print("กรุณาใส่ตัวเลขที่มากกว่า 0")

def main():
    print("=== Position Size Calculator ===")
    portfolio = get_input("มูลค่าพอร์ต: ")
    risk      = get_input("ความเสี่ยง (%): ") / 100
    stoploss  = get_input("Stop Loss (%): ") / 100

    position = safe_divide(portfolio * risk, stoploss)
    if position is not None:
        print(f"Position: {position:,.2f} บาท")

main()