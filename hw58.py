box=[]
for i in range(10):
    a = int(input(f"請輸入第{i+1}個數字"))
    box.append(a)

max = sorted(box,reverse = True)
min = sorted(box,reverse = False)
#print(min)
#print(max)
print(f"最大的三個數字為{max[0]},{max[1]},{max[2]}")
print(f"最小的三個數字為{min[0]},{min[1]},{min[2]}")