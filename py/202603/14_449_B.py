h,w,q= map(int,input().split())
for i in range(q):
    t,n= map(int,input().split())
    if(t==1):
        print(n*w)
        h-=n
    else:
        print(n*h)
        w-=n