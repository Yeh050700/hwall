from itertools import count


t = int(input("輸入第一行正整數為:"))
while True :
    a = input("第二行中數列中的數字為:").split(" ")
    if len(a) == t:
        break
    print("格式不符,重新輸入")
a = list(map(int,a))

amax=(sorted(a,reverse = True))
s = int(amax[0])

bignum = 0
tm = 0
check = 0
for i in range(0,s):   
    if a.count(i) > bignum :
       tm = i
       bignum = a.count(i)
       check = check + 1
if check <= 1  :
    print("每個數字剛好出現一次")
else:
    print("最大出現次數的數字為:",tm,"出現次數:",bignum) 

