n,m=map(int,input().split())
item=[0]*n
item[0]=1
change=[[False]*n]*n

for i in range(m):
    a,b=map(int,input().split())
    change[a-1][b-1]=True
    item[b-1]+=1

ans=0
for i in range(n):
    if(item[i]>=1):
        ans+=1

print(ans)