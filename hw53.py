import email


tmp = int(input("n:"))
box ={}
for i in range(tmp) :
    name = input("姓名:") 
    Email = input("Email:")
    box[name]=[Email]

want = input("輸入想查詢的人")
print(f"{want}的電子郵件帳號為{box[want]}")

    