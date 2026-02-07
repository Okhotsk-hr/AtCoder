n,k= map(int,input().split())
ans=0

for i in range(n+1):
    i2=str(i)
    sum=0
    for j in range(len(i2)):
        sum+=int(i2[j])
    if(sum==k):
        ans+=1

print(ans)