#a = [23,34,34,5,5,34,34]
a = input("輸入一整數序列:").split(" ")

a = list(map(int,a))

amax=(sorted(a,reverse = True))
s = int(amax[0])


over = 0 

for i in range(0,s+1):   
    # if a.count(i) > 0 :
        if a.count(i) >= len(a)/2:
            over = over + i    
if over > 0 :
    print("過半元素是:",over)
else:
    print("過半元素:NO")
        