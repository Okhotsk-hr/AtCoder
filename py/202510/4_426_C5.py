#バージョンごとに管理2
n,q= map(int,input().split())
pc=[1]*(n+1)
low=0

for i in range(q):
    x,y=map(int,input().split())
    count=sum(pc[low:x])
    pc[y-1]+=count
    pc=[0]*(x)+pc[x:]
    print(count)
    if(low<x):
        low=x