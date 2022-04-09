M = int(input("輸入乘階值M:"))
n=1
rag = 1
tatal=1

while True:
    rag =rag+1
    n=n+1
    tatal =tatal*n  
    if tatal>M:
        break
print("超過M為",M,"的最小階層為",rag)


""""
for i in range(1,8):
    n =  n*i
    if n>M: 
        print("超過M為",M,"的最小階層為",i)
"""