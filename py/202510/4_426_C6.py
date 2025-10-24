
n,q= map(int,input().split())
pc=[1]*(n+1)
low=0
count=[]

for i in range(q):
    x,y=map(int,input().split())
    count.append(sum(pc[low:x]))
    pc[y-1]+=count[i]
    pc=[0]*(x)+pc[x:]
    #print(count)
    if(low<x):
        low=x

for i in range(len(count)):
    print(count[i])