a = int(input("輸入一正整數"))
if a<11 or a>1000:
    print("error")
else :
    if a % 11 == 0 and a % 2 == 0 and a % 5 != 0 and a % 7 != 0 :
        print ("yes")
    else : 
        print("no")
