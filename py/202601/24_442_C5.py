#AI
n,m= map(int,input().split())
counts=[n-1]*n

for _ in range(m):
    a,b= map(int,input().split())
    counts[a-1]-=1
    counts[b-1]-=1
    
ans=[]
for i in range(n):
    count=counts[i]
    if(count<=2):
        ans.append("0")
    else:
        ans.append(str(count*(count-1)*(count-2)//6))

print(" ".join(ans))