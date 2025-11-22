
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
            for k in range(int(i/2)):
                if(int(num[k])+1!=int(num[int(i/2)+k])):
                    fill=False
                    break
                if(int(num[k])+1!=int(num[len(num)-1-k])):
                    fill=False
                    break
            if(fill):
                #print(num)
                sum+=1
print(sum)
        