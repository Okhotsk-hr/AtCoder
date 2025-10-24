n,q= map(int,input().split())
pc=[]
for i in range(n):
    pc.append(i+1)


for i in range(q):
    x,y=map(int,input().split())
    count=0
    for i in range(n):
        if(pc[i]<=x):
            pc[i]=y
            count+=1
    print(count)