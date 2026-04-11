t,x=map(int,input().split())
a=list(map(int, input().split()))
lt=0
la=a[0]
print(str(0)+" "+str(a[0]))

for i in range(1,t+1):
    if(abs(a[i]-la)>=x):
        lt=i
        la=a[i]
        print(str(i)+" "+str(a[i]))
