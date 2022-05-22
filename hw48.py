from re import X


tmp = int(input("輸入筆數:"))
box={}
for i in range(tmp): 
    an = str(input("輸入字典內容:")).split(" ")
    box[an[0]]= an[1]
want = str(input("請輸入想查詢的單字"))

print(f"{want}在字典中意思為{box[want]}")