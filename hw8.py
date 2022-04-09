t = 8 
while True :
    a = [1,4,6,1,3,5,8,7]
    if len(a) == t:
        break

print (a.count(1))

for i in range(0,t):
    for j in range(0,10):
        print(a.count(j))
        
