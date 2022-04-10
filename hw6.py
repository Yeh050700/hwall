a= input("輸入值為:").split(",")
min = sorted(a)
max = sorted(a,reverse = True)

tmax = "".join([str(_) for _ in max])
tmin = "".join([str(_)for _ in min])

ans = int(tmax) - int(tmin)
print("最大值數列與最校值數列相差:",ans)

