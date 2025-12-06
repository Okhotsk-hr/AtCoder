n=int(input())
a = list(map(int, input().split()))
ans=0
for i in range(n):
    for j in range(i+1,n):
        #print(str(i)+":"+str(j))
        sum=0
        b=True
        for k in range(i,j+1):
            sum+=a[k]
        #print(sum)
        for k in range(i,j+1):
            if(sum%a[k]==0):
                b=False
        if(b):
            ans+=1
print(ans)