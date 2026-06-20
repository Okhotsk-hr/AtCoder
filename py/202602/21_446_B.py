n,m= map(int,input().split())
d=[True]*m
print(d)
for i in range(n):
    l=int(input())
    x=list(map(int, input().split()))
    get=True
    for j in range(l):
        if(d[x[j]-1] and get):
            print(x[j])
            d[x[j]-1]=False
            get=False
    if(get):
        print(0)
