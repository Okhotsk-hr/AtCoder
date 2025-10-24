x,y = map(int,input().split())

a=[]
a.append(x)
a.append(y)

for i in range(3,11):
    a.append(a[i-2]+a[i-3])
    if(a[i-1]>=10):
        s=str(a[i-1])
        a[i-1]=int(s[::-1])
print(a[9])