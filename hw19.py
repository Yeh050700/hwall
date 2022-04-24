n = input("輸入資料量")

for i in range(int(n)) :
    home = input("輸入血型").split(" ")
    d = home[0]
    m = home[1]
    s = home[2]

    if d == "O" and m =="O" :
        if s == "O" :
            print("YES")
        else:
            print("Impossible")
    elif d=="O" and m == "A":
        if s == "A" or s == "O":
            print("YES")
        else:
            print("Impossible")
    elif d=="O" and m == "B":
        if s == "B" or s== "O":
            print("YES")
        else:
            print("Impossible")
    elif d=="O" and m == "AB":
        if s == "A" or s == "B":
            print("YES")
        else:
            print("Impossible")
    elif d=="A" and m == "A":
        if s == "A" or s=="O":
            print("YES")
        else:
            print("Impossible")
    elif d=="A" and m == "B":
        if s == "A" or s=="B" or s=="O" or s=="AB":
            print("YES")
        else:
            print("Impossible")
    elif d=="A" and m == "AB":
        if s == "A" or s=="B" or s=="AB":
            print("YES")
        else:
            print("Impossible")
    elif d=="B" and m == "B":
        if s == "B" or s=="O":
            print("YES")
        else:
            print("Impossible")
    elif d=="B" and m == "AB":
        if s == "A" or s=="B" or s=="AB":
            print("YES")
        else:
            print("Impossible")
    elif d=="AB" and m == "AB":
        if s == "A" or s=="B" or s=="AB":
            print("YES")
        else:
            print("Impossible")