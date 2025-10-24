t=int(input())
ans=[]
for i in range(t):
    tc1,tc2,tc3=map(int,input().split())
    minnum=min(tc1,tc2,tc3)
    ans.append(minnum)
    tc1-=1*minnum
    tc2-=1*minnum
    tc3-=1*minnum
    # if(tc1>=1 and tc3>=2 and tc1<=tc3):
    #     minnum=min(tc1,tc3/2)
    #     ans[i]+=minnum
    #     tc1-=1*minnum
    #     tc3-=2*minnum
    # if(tc1>=2 and tc3>=1):
    #     minnum=min(tc1/2,tc3)
    #     ans[i]+=minnum
    maxnum=0
    for j in range(int(min(tc1,tc3))):
        for k in range(int(min(tc1,tc3))):
            if(tc1>=i*2+j and tc3>=i+j*2):
                if(maxnum<i+j):
                    maxnum=i+j
    ans[i]+=maxnum
            

for i in range(t):
    print(int(ans[i]))


