s,a,b,x= map(int,input().split())
d=0
while(x>0):
    if(x>=a):
        d+=s*a
        x-=a+b
    else:
        d+=s*(x)
        break
        

print(d)