n,m= map(int,input().split())
c=list(map(int, input().split()))
need=[0]*m
use=0

for i in range(n):
    a,b=map(int,input().split())
    need[a-1]+=b

for i in range(m):
    if(need[i]>=c[i]):
        use+=c[i]
    else:
        use+=need[i]

print(use)
