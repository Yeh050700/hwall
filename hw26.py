while True:
    need = input("檢測的字串(end結束)")
    if need == "end" :
        print("測驗結束")
        break
    else:
        ch = input("檢測的單一字元") 
        print("字元",ch,"出現次數為",need.count(ch))