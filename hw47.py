tmp = int(input("輸入筆數"))
box = []
for i in range(tmp):
    s = str(input("輸入獎牌與數量")).split(" ")
    box.append(s) 

for i in range(tmp):
    print(box[i][0],"牌得到",box[i][1],"面")