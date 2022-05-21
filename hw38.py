tmp = int(input("小狗可能會去幾個點:"))
maptotal =[]
for i in range(tmp):
    map =  int(input()) 
    maptotal.append(map)
print("第2個點:",maptotal[1])
print("第5個點:",maptotal[4])