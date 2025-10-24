#ソート利用

n,q= map(int,input().split())
pc=[]
for i in range(n):
    pc.append(i+1)


for i in range(q):
    x,y=map(int,input().split())
    pc.sort()
    # print(pc)
    i=0

    while pc[i]<=x:
        pc[i]=y
        i+=1
    # for i in range(x):
    #     if(pc[i]<=x):
    #         pc[i]=y
    #         count+=1
    print(i)