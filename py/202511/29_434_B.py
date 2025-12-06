n,m= map(int,input().split())
size=[]
count=[]
for i in range(m):
    size.append(0)
    count.append(0)
for i in range(n):
    a,b=map(int,input().split())
    size[a-1]+=b
    count[a-1]+=1
for i in range(m):
    print(size[i]/count[i])