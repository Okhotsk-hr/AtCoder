n=int(input())
a=list(map(int,input().split()))
s=-1
e=-1
max=0
for j in range(n):
    b=[a[j]]
    for i in range(j+1,n):
        if(b[len(b)-1]+1==a[i]):
            b.append(a[i])
    if(max<len(b)):
        max=len(b)

print(max)
