n,m=map(int,input().split())
f=list(map(int, input().split()))
c=[0]*m
for i in range(n):
    c[f[i]-1]+=1

q1="Yes"
q2="Yes"

for i in range(m):
    if(c[i]>1):
        q1="No"
    if(c[i]==0):
        q2="No"

print(q1)
print(q2)