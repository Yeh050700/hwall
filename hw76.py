'''

num = str(input("請輸入一個數"))
 
if len(num) != 6 :
    print("密碼不符,重新輸入")
else:
    num1 = int(num)//100000
    num2 = int(num)%100000//10000
    num3 = int(num)%10000//1000
    num4 = int(num)%1000//100
    num5 = int(num)%100//10
    num6 = int(num)%10//1
    Nnum1 = num1*4%7
    Nnum2 = num2*4%7
    Nnum3 = num3*4%7
    Nnum4 = num4*4%7
    Nnum5 = num5*4%7
    Nnum6 = num6*4%7
    print("解密後的密碼為:",Nnum1,Nnum2,Nnum3,Nnum4,Nnum5,Nnum6)

'''


out=""
while True:
    password = input("請輸入傳送密碼(6位數):")
    if len(password)==6:
        break
pp=list(password)
for i in range(0,len(password)):
    for j in range(0,10):
        if j*4%7==int(pp[i]):
            out +=str(j)
            break
print("解密後密碼為:"+ out)