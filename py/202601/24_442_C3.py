n,m= map(int,input().split())
ans=""
counts=[]

for i in range(n):
    counts.append(n-1)

for i in range(m):
    a,b= map(int,input().split())
    a-=1
    b-=1
    counts[a]-=1
    counts[b]-=1

for i in range(n):
    count=counts[i]
    if(count<=2):
        ans+="0"
    else:
        ans+=str(int((count*(count-1)*(count-2))/6))
    ans+=" "

print(ans)