km = float(input("請輸入公里數"))
money = 75
if km <= 1.5 : 
    print("所需車資為",money)
elif km > 1.5:
    km = km - 1.5
    while True:
        km = km - 0.25
        money = money + 5
        if km <= 0 :
            break
    print("所需車資為:",money)
    