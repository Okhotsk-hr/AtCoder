n,q= map(int,input().split())
oa=list(map(int, input().split()))
for i in range(q):
    a=oa[:]
    k=int(input())
    b=list(map(int,input().split()))
    for j in range(k):
        a[b[j]-1]=10**9
    print(min(a))