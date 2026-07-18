n=int(input())
hm=10000
am=10000
for i in range(n):
    a,b,s=map(str,input().split())
    am-=int(a)
    if(s=="keep"):
        hm-=int(b)
    else:
        hm-=int(a)
print(am-hm)