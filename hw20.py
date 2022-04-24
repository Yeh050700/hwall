n = input("組數為:")
for i in range(int(n)):
    pe = input(f"第{i+1}組").split(" ")
    b = pe[0]
    s = pe[1]
    bmoney = 250
    smoney = 175
    total = int(b)*bmoney + int(s)*smoney
    print("第",i+1,"組應該收費:",total)