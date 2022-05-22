main = input("請選擇主餐與升級的套餐:").split(" ")
up1 = input("升級大杯飲料")
up2 = input("升級大薯")

money = 0 

if main[0]   == "1" :
    money = money + 72
elif main[0] == "2" :
    money = money + 62
elif main[0] == "3" :
    money = money + 82
elif main[0] == "4" :
    money = money + 44
elif main[0] == "5" :
    money = money + 50


if main[1] == "A" :
    money = money + 55
elif main[1] == "B":
    money = money + 68

if up1 == "是" :
    money = money + 7 

if up2 == "是" :
    money = money + 13

print(f"總共為{money}元")