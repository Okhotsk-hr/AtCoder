
x,y = map(int,input().split())
sum=(x+y)%12
if(sum==0):
    print(12)
else:
    print(sum)