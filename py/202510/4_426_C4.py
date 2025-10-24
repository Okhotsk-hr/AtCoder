#バージョンごとに管理2
n,q= map(int,input().split())
pc=[1]*(n+1)
# for i in range(n):
#     pc.append(1)


#print(pc)
for i in range(q):
    x,y=map(int,input().split())
    count=sum(pc[0:x])
    pc[y-1]+=count
    # pc1=[0]*(x)
    # pc2=pc[x:]
    #print(pc2)
    pc=[0]*(x)+pc[x:]
    #print(pc)
    # for i in range(x):
    #     #count+=pc[i]
    #     #pc[y-1]+=pc[i]
    #     pc[i]=0
    #print(pc)
    # for i in range(x):
    #     if(pc[i]<=x):
    #         pc[i]=y
    #         count+=1
    print(count)