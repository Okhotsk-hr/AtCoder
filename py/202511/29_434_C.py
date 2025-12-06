tt=int(input())
for i in range(tt):
    n,h= map(int,input().split())
    t0=0
    for j in range(n):
        t,l,u=map(int,input().split())
        if(abs(h-l)>abs(h-u)):
            d=abs(h-u)
            h1=u
        else:
            d=abs(h-l)
            h1=u
        #d=min(abs(h-l),abs(h-u))
        if(d/(t-t0)<=1):
            print("高度更新")
            h=h1
            print(h)

print(h)