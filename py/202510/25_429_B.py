n,m= map(int,input().split())
a = list(map(int, input().split()))

tf=False
for i in range(len(a)-1):
    b=a[:i]+a[i+1:]
    if(sum(b)==m):
        tf=True
        break

if(tf):
    print("Yes")
else:
    print("No")
