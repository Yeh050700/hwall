n = input("輸入查詢組數N為:")
for i in range(int(n)):
    user = input("帳號 密碼").split( )
    accunt = user[0]
    passwd = user[1]
    if accunt == "123" :
        if passwd == "456" :
            print("9000")
        else:
            print("error")
    elif accunt == "456" :
        if passwd == "789" :
            print("5000")
        else:
            print("error")
    elif accunt == "789" :
        if passwd == "888" :
            print("6000")
        else:
            print("error")
    elif accunt == "336" :
        if passwd == "558" :
            print("10000")
        else:
            print("error")
    elif accunt == "775" :
        if passwd == "666" :
            print("12000")
        else:
            print("error")
    elif accunt == "566" :
        if passwd == "221" :
            print("7000")
        else:
            print("error")
    else:
        print("error")