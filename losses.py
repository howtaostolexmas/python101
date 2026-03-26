portfolio = 100000
losses = [3000, 5000, 2000, 8000, 6000, 4000]

for loss in losses:
    portfolio -= loss
    drawdown = ((100000 - portfolio) / 100000) * 100
    print(f"พอร์ตเหลือ {portfolio:.2f} | Drawdown {drawdown:.2f}%")
    
    if drawdown >= 20:
        print("หยุดเทรด! พอร์ตหายเกิน 20%")
        break