
a = input("輸入月和日").split(" ") 
a = list(map(int,a))

if a[0] == 1 and a[1] >=21 :
    print("星座為:水瓶")
elif a[0] ==1 and a[1] <21:
    print("星座為:魔蠍")
elif a[0] ==2 and a[1] >=19:
    print("星座為:雙魚")
elif a[0] ==2 and a[1] <19:
    print("星座為:水瓶")
elif a[0] ==3 and a[1] >=21:
    print("星座為:牧羊")
elif a[0] ==3 and a[1] <21:
    print("星座為:雙魚")
elif a[0] ==4 and a[1] >=21:
    print("星座為:金牛")
elif a[0] ==4 and a[1] <21:
    print("星座為:牧羊")
elif a[0] ==5 and a[1] >=22:
    print("星座為:雙子")
elif a[0] ==5 and a[1] <22:
    print("星座為:金牛")
elif a[0] ==6 and a[1] >=22:
    print("星座為:巨蠍")
elif a[0] ==6 and a[1] <22:
    print("星座為:雙子")
elif a[0] ==7 and a[1] >=23:
    print("星座為:獅子")
elif a[0] ==7 and a[1] <23:
    print("星座為:巨蠍")
elif a[0] ==8 and a[1] >=24:
    print("星座為:觸女")
elif a[0] ==8 and a[1] <24:
    print("星座為:獅子")
elif a[0] ==9 and a[1] >=24:
    print("星座為:天平")
elif a[0] ==9 and a[1] <24:
    print("星座為:觸女")
elif a[0] ==10 and a[1] >=24:
    print("星座為:天蠍")
elif a[0] ==10 and a[1] <24:
    print("星座為:天平")
elif a[0] ==11 and a[1] >=23:
    print("星座為:射手")
elif a[0] ==11 and a[1] <23:
    print("星座為:天蠍")
elif a[0] ==12 and a[1] >=22:
    print("星座為:魔蠍")
elif a[0] ==12 and a[1] >=22:
    print("星座為:雙魚")


