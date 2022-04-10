a = input("輸入月租費及通話時間為:").split(",")
if int(a[0]) == 186:
    if int(a[1]) <= 186 :
        print("通話費為:",a[1]*0.09)
    elif int(a[1]) < int(a[0])*2:
        print("通話費為:",int(a[1])*0.09*0.9) 
    elif int(a[1]) > int(a[0])*2:
        print("通話費為:",int(a[1])*0.09*0.8)
elif int(a[0]) == 386:
    if int(a[1]) <= 386 :
        print("通話費為:",int(a[1])*0.08)
    elif int(a[1]) < int(a[0])*2:
        print("通話費為:",int(a[1])*0.08*0.8)
    elif int(a[1]) > int(a[0])*2:
        print("通話費為:",int(a[1])*0.08*0.7)
elif int(a[0]) == 586:
    if int(a[1]) <= 586 :
        print("通話費為:",int(a[1])*0.07)
    elif int(a[1]) < int(a[0])*2:
        print("通話費為:",int(a[1])*0.07*0.7)
    elif int(a[1]) > int(a[0])*2:
        print("通話費為:",int(a[1])*0.07*0.6)
elif int(a[0]) == 986:
    if int(a[1]) <= 986 :
        print("通話費為:",int(a[1])*0.06)
    elif int(a[1]) < int(a[0])*2:
        print("通話費為:",int(a[1])*0.06*0.6)
    elif int(a[1]) > int(a[0])*2:
        print("通話費為:",int(a[1])*0.06*0.5)
