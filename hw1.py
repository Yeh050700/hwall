
n = int(input('輸入一個正整數:'))
c = 2

while c < n:
    if n % c == 0:
                print(c)  
    c += 1
        
if c == n:
    print('是質數')