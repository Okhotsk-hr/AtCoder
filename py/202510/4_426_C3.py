#バージョンごとに管理
n,q= map(int,input().split())
pc=[]
for i in range(n):
    pc.append(1)


for i in range(q):
    x,y=map(int,input().split())
    count=0
    for i in range(x):
        count+=pc[i]
        pc[y-1]+=pc[i]
        pc[i]=0
    # for i in range(x):
    #     if(pc[i]<=x):
    #         pc[i]=y
    #         count+=1
    print(count)