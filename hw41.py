tmp = int(input("搭幾次電梯"))
money = 0 
anow = 1  
for i in range(tmp):
    lv = int(input("樓層"))
    if anow < lv :
        money = money + (lv - anow)*20
    if anow > lv : 
        money = money + (anow - lv)*10
    anow = lv 
print(money,"元")