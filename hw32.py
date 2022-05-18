bal = input("Money") 
memu = input("有幾種飲料")
tmp = 0 
for i in range(int(memu)):
    sel = input("商品售價")
    if sel <= bal:
        tmp = tmp + 1
print("小明可以買",tmp,"種飲料") 
