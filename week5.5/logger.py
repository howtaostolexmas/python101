while True:
    ticker = input("ใส่ ticker (หรือ done เพื่อจบ): ")
    if ticker == 'done':
        break
    
    while True:
        try:
            price = float(input("ใส่ราคา: "))
            break
        except ValueError:
            print("ใส่ตัวเลขเท่านั้น")
            
    while True:
        try:
            counts = int(input("ใส่จำนวนหุ้น: "))
            break
        except ValueError:
            print("ใส่ตัวเลขเท่านั้น")

    trade = (ticker, price, counts)
    with open("trades.txt", "a") as f:
        f.write(f"{trade[0]},{trade[1]},{trade[2]}\n")
    print("บันทึกแล้ว ✅")