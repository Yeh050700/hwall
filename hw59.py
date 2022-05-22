a = int(input("輸入$$:"))
tmp = 0 
while True:
    if a < 100 :
        break
    a = a - 100 
    tmp = tmp+1
while True:
    if a < 50 :
        break
    a = a - 50 
    tmp = tmp +1 
while True :
    if a < 10 :
        break
    a = a - 10 
    tmp = tmp +1 
while True:
    if a<5 :
        break
    a = a - 5 
    tmp = tmp +1 
while True:
    if a == 0 :
        break
    a = a - 1 
    tmp = tmp + 1

print(f"總共需要{tmp}種")