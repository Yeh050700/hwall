from itertools import count


t = 8 
while True :
    a = input("輸入數字串").split(" ")
    """print(type(a[0]))"""
    """a=[4,4,6,2,3,5,8,7]"""
    if len(a) == t:
        break

a = list(map(int,a))

amax=(sorted(a,reverse = True))
s = int(amax[0])
print(s)

bignum = 0
tm = 0
check = 0
for i in range(0,s):   
    if a.count(i) > bignum :
       tm = i
       check + 1
       bignum = a.count(i)

if check > 0:
    print("每個數字剛好出現一次")
else:
    print("出現最多次的數字為:",tm,"出現次數:",bignum) 

