a = int(input("請輸入處理方式(1)字典(2)串列:"))
if a == 1 :
    dict1={"金":4,"銀":5,"銅":9,"優":7}
    list1=zip(dict1.keys(),dict1.values())
    for key,values in list1:
        print("%s牌得到%d面"%(key,values)) 
else:
    dict2={"金":3,"銀":1,"銅":2,"優":1}
    item1=list(dict2.items())
    for name,s in item1:
        print("%s牌得到%d面"%(name,s))