date = input("輸入考試次數與學生數:").split(" ")
stunum = date[1]
#examnum = date[0]
exampar = input("每次考試所占百分比").split(" ")
eexapar = list(map(float,exampar))              #轉型態
#stu1 = [70,80,90,80,100,80]
#stu2 = [60,70,80,70,40,70]
#stu3 = [30,50,40,60,50,40]
#stunum = 3 
allnum = 0

for i in range(int(stunum)):
    stu = input("輸入學生成績").split(" ")       #輸入學生成績
    sstu = list(map(int,stu))                   #轉型態
    #exampar = [0.1,0.1,0.3,0.1,0.1,0.3]
    num = [x*y for x,y in zip(sstu,eexapar)]    #算單位同學各個成績
    allnum = allnum + int(sum(num))             #把同學成績存放起來
    
print("全班平均:",round((allnum/int(stunum)),2))
    
