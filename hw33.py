chi = 73
eng = 89
mat = 55
move = 70
pyyy = 95
bb = {"國文":chi,"英文":eng,"微積分":mat,"體育":move,"程式設計":pyyy}
bbkeys = bb.keys
bbvalue = bb.values
avg = (int(chi) + int(eng) + int(mat) + int(move) + int(pyyy) )/ 5
tl =[]
tl.append(chi)
tl.append(eng)
tl.append(mat)
tl.append(move)
tl.append(pyyy)
max = (sorted(tl,reverse = True))
print(max)
print("平均分數:",avg)
print("最高科目:","分數:",max[0])
print("最低科目:","分數:",max[4])
