
scoretype = ["國文","英文","微積分","體育","程式設計"]
scorebox =[]
total = 0 
maxscore= 0
minscore=100

for i in range(5):
    score = int(input(scoretype[i]+":"))
    if score > 100 or score < 0 :
        print("error")
    else:
         total = total + score
         if score > maxscore :
             maxscore = score
             maxl = scoretype[i]
         if score < minscore :
             minscore = score
             minl = scoretype[i]

print("平均分數:",total/5)
print("最高科目為:",maxl,"分數為",maxscore)
print("最低科目為",minl,"分數為",minscore)





