
s=input()
sum=0
for i in range(1,len(s)+1):
    #print("new"+str(i))
    #偶数文字数のみ
    if(i%2==0):
        for j in range(len(s)-i+1):
            fill=True
            #print(s[j:j+i])
            num=s[j:j+i]
            #前半分のチェック
            print("前半")
            for k in range(1,int(i/2)):
                if(num[0]!=num[k]):
                    fill=False
                    break
            if(not(fill)):
                continue
            #後ろ半分のチェック
            print("後半")
            for k in range(int(i/2),i):
                if(num[int(i/2)]!=num[k]):
                    fill=False
                    break
            if(not(fill)):
                continue
            print("最初と最後")
            #最初+1と最後が同じか
            if(int(num[0])+1!=int(num[-1])):
                fill=False
            if(fill):
                #print(num)
                sum+=1
print(sum)
        