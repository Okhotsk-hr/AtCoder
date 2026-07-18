n,m=map(int,input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
count=0
for i in range(n-1):
    if((a[i]+i+a[i+1])%m==b[i]):
        count+=1
        print(count)